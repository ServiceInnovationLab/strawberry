#!/usr/bin/env python

import json
import csv

INPUT_FILENAME = 'input.json'
OUTPUT_FILENAME = 'output.csv'

# Note: assumes crappy encoding produced on a windows Pc.
# If you're using a better OS, you can remove this `encoding=`

with open(INPUT_FILENAME, encoding = "ISO-8859-1") as json_file:
    with open(OUTPUT_FILENAME, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"') #, quoting=csv.QUOTE_MINIMAL)

        #headers
        csv_writer.writerow(['timestamp', 'type', 'card_id', 'card_name', 'card_shortLink',
            'listAfter_id', 'listAfter_name', 'listBefore_id', 'listBefore_name', 'text',
            'member_fullName', 'member_username'])

        json_data = json.load(json_file)
        for action in json_data.get('actions'):
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

