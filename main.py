import logging

import config
import package_logger

from symphony.bot_client import BotClient

package_logger.initialize_logging()

def run_main():
    sym_client = BotClient(config.bot_config)

    user_list = sym_client.Admin.list_users()

    users_for_update = {}

    for user in user_list:
        if user.type == 'NORMAL' and user.domain == 'symphony.com':
            payload = {
                "division": 'Symphony'
            }
            users_for_update[user.id] = payload

    for uid, payload in users_for_update.items():
        logging.info(f'Updating user Id: {uid} - setting Division to Symphony')
        sym_client.Admin.update_user(user_id=uid, payload=payload)

    logging.info('Done!')


if __name__ == '__main__':
    run_main()