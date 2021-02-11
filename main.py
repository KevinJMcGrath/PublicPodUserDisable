import logging

import config
import csv_import
import package_logger

from symphony.bot_client import BotClient

package_logger.initialize_logging()

def run_main():
    sym_client = BotClient(config.bot_config)

    user_list = sym_client.Admin.list_users()

    csv_path = 'C:/Users/Kevin/Downloads/public_pod_disable_users_2021-02-12.csv'
    userIds_from_csv = csv_import.loader.import_csv_users(csv_path)

    logging.info(f"Disabling {len(userIds_from_csv)} users.")

    index = 0
    for userId in userIds_from_csv:
        logging.info(f'{index} - Disabling userId {userId}')
        result = sym_client.Admin.update_user_status(user_id=userId)

        if result != 'OK':
            logging.error(f'Error updating {userId}: {result}')

        index += 1

    # for uid, payload in users_for_update.items():
    #     logging.info(f'Updating user Id: {uid} - setting Division to Symphony')
    #     sym_client.Admin.update_user(user_id=uid, payload=payload)

    logging.info('Done!')


if __name__ == '__main__':
    run_main()