import csv

from src.constants import ID_STR


def get_locations():
    locations = []
    with open('resources/Locations.csv') as csv_file:
        read_csv = csv.reader(csv_file)

        headers = []

        for row in read_csv:
            if row[0] == ID_STR:
                headers = row
                continue
            location = {}
            for i in range(len(row)):
                location[headers[i]] = row[i]
            locations.append(location)
    return locations