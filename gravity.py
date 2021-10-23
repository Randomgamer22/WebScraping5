import csv
import re
import string

headers = []
all_star_data = []

with open("main.csv", "r") as f:
    csv_reader = csv.reader(f)

    for index, row in enumerate(csv_reader):
        if index == 0:
            headers.append(row)
            headers = headers[0]
        else:
            all_star_data.append(row)

# print(headers, all_star_data)

headers.append('Gravity')

gravity_list = []

def filter_data(data):
    non_numeric_chars = list(set(string.printable) - set(string.digits))
    for index, star_data in enumerate(data):
        for index, values in enumerate(star_data):
            if values == '?':
                del data[index]
            if index == 3 or index == 4 or index == 5:
                for char in non_numeric_chars:
                    if char in values:
                        del data [index]
    return data

all_star_data = filter_data(all_star_data)

for index, star_data in enumerate(all_star_data):
    all_star_data[index][3] = re.sub('[^0-9]', '', star_data[3])
    all_star_data[index][4] = re.sub('[^0-9]', '', star_data[4])

for index, star_data in enumerate(all_star_data):
    mass = float(star_data[3]) * 1.989e+30
    radius = float(star_data[4]) * 6.957e+8

    gravity = (6.67e-11) * mass / (radius**2)

    gravity_list.append(gravity)

for index, star_data in enumerate(all_star_data):
    all_star_data[index].append(gravity_list[index])
    all_star_data[index][0] = index + 1

with open("main1.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(all_star_data)

