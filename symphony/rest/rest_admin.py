import symphony.rest.endpoints as sym_ep

from typing import List

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
        """

        ep = self.get_endpoint(sym_ep.update_user(user_id))
        return self.post(ep, payload)

    def list_users(self) -> List[user.User]:
        ep = self.get_endpoint(sym_ep.list_users())

        return [user.User(user_json=u) for u in self.get(ep)]
