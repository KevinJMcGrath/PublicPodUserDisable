import csv

from pathlib import Path

def import_csv_users(csv_path: str):

    id_list = []
    with open(csv_path, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            id_list.append(row['userId'])

    return id_list