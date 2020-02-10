#!/usr/bin/env python

# Read secrets from .env file
import requests
import csv
import json
import os
from dotenv import load_dotenv
load_dotenv()

BOARD_ID = os.getenv("TRELLO_BOARD_ID")
TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')

output_filename = f'output-{BOARD_ID}.csv'

keep_fetching = True
BASE_URL = "https://api.trello.com/1/boards/{board_id}/actions/?key={api_key}&token={token}&limit=1000".format(
    board_id=BOARD_ID,
    api_key=TRELLO_API_KEY,
    token=TRELLO_TOKEN)

url = BASE_URL

with open(output_filename, mode='w') as csv_file:
    # , quoting=csv.QUOTE_MINIMAL)
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')
    # headers
    csv_writer.writerow(['timestamp', 'type', 'card_id', 'card_name', 'card_shortLink',
                         'listAfter_id', 'listAfter_name', 'listBefore_id', 'listBefore_name', 'text',
                         'member_fullName', 'member_username'])

    while(keep_fetching):
        print(url)
        print("fetching...")
        response = requests.get(url)
        print("done.")

        # json_data = json.load(json_file)
        # for action in json_data.get('actions'):
        for action in response.json():
            row = []

            data = action.get('data')
            card = data.get('card', {})
            # type

            row.append(action.get('date'))
            row.append(action.get('type'))

            # data.card.id
            # data.card.name
            # data.card.shortLink
            row.append(card.get('id', ''))
            row.append(card.get('name', ''))
            row.append(card.get('shortLink', ''))

            listAfter = data.get('listAfter', {})

            # data.listAfter.id
            # data.listAfter.name
            row.append(listAfter.get('id', ''))
            row.append(listAfter.get('name', ''))

            listBefore = data.get('listBefore', {})
            # data.listBefore.id
            # data.listBefore.name
            row.append(listBefore.get('id', ''))
            row.append(listBefore.get('name', ''))

            # data.text
            row.append(data.get('text', ''))

            memberCreator = action.get('memberCreator', {})

            # memberCreator.fullName
            # memberCreator.username
            row.append(memberCreator.get('fullName', ''))
            row.append(memberCreator.get('username', ''))

            # Write to the CSV file
            csv_writer.writerow(row)

        # if we got data, then keep going
        keep_fetching = len(response.json()) > 0
        if (keep_fetching):
            # last_action
            oldest_action = response.json()[-1]
            print(oldest_action.get('date'))
            url = "{base_url}&before={oldest_id}".format(
                base_url=BASE_URL, oldest_id=oldest_action.get('id'))
        else:
            print("No records")
        print("----------------------")
