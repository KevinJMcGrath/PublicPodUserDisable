import jsonpickle

from typing import List

import symphony.rest.endpoints as sym_ep

from symphony.api_base import APIBase
from symphony.models import user


class Admin(APIBase):
    def __init__(self, session):
        super().__init__(session)

    def update_user_features(self, user_id, features: list):
        """
        :param user_id
            Symphony user Id
        :param features: list(dict)
            List of features to be actioned for the user. Each feature should be specified as follows:
            {
                "entitlement": "myEntitlementName",
                "enabled": True (False)
            }
        """

        ep = self.get_endpoint(sym_ep.update_user_features(user_id))

        return self.post(ep, features)

    def update_user(self, user_id, payload: dict):
        """
        :param user_id:
            Symphony user id either as a string or integer
        :param payload:
            Dict of attributes to update
        :return:
        """

        ep = self.get_endpoint(sym_ep.update_user(user_id))
        return self.post(ep, payload)

    def update_user_status(self, user_id, disable_user: bool) -> str:
        """
        :param user_id:
            Symphony user id either as a string or integer
        :param disable_user: bool
            Flag to set user to ENABLED or DISABLED
        :return:
            Update status result e.g. { "message": "OK" }
        """

        status_str = 'DISABLED' if disable_user else 'ENABLED'
        ep = self.get_endpoint(sym_ep.update_user_status(user_id))

        payload = {
            "status": status_str
        }

        result_status = jsonpickle.decode(self.post(ep, user_id), payload)

        if result_status:
            return result_status['message']




    def list_users(self) -> List[user.User]:
        ep = self.get_endpoint(sym_ep.list_users())

        return [user.User(user_json=u) for u in self.get(ep)]
