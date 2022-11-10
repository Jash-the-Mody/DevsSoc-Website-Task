# Print result after every function to check
# Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value

filepaths = 'data.json'


# CHANGES: returned data
def read_data(filepaths):
    with open(filepaths) as json_file:
        data = json.load(json_file)
        return data
    # Read data from filepaths


data = read_data(filepaths)


def get_oldest(data):
    max = 0
    c = 0
    oldest = {}
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max = data["AVENGERS"][i]['age']
            oldest = data["AVENGERS"][i]

    for i in data["DC"]:
        if (data["DC"][i]['age'] > max):
            max = data["DC"][i]['age']
            oldest = data["DC"][i]

        if data["DC"][i]['age'] == max:
            oldest[c] = data["DC"][i]
            c += 1
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
    return oldest


# returns info: Thor and Wonder Woman

# CHANGES: removed j, there was no need for it
def get_oldest_avenger(data):
    max = 0
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max = data["AVENGERS"][i]['age']
            oldest_avenger = data["AVENGERS"][i]
    # Return all info of the oldest avenger
    return oldest_avenger


# returns info: Thor

# CHANGES: "DCU" -> "DC" as that is the correct key
def get_total_points(data):
    total_points = {}
    for i in data["AVENGERS"]:
        key = data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
            total_points[key] += data["AVENGERS"][i]['points'][j]
    for i in data["DC"]:
        key = data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
            total_points[key] += data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points


# returns info: Dict of superhero name and total points


# CHANGES:
# made changes such that two different lists are created, one each for MCU and DCU
# (as question wanted two different lists).append function used to prevent it going out of index
def get_more_than_average(data):
    more_than_average_mcu = []
    more_than_average_dc = []
    avg_mcu = 0
    avg_dc = 0
    for i in data["AVENGERS"]:
        avg_mcu += data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu = avg_mcu / len(data["AVENGERS"])
    c = 0
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['points']['stealth'] > avg_mcu):
            more_than_average_mcu.append(0)
            more_than_average_mcu[c] = data["AVENGERS"][i]['name']
            c += 1

    for i in data["DC"]:
        avg_dc += data["DC"][i]['points']['strength']
    avg_dc = avg_dc / len(data["DC"])
    c = 0
    for i in data["DC"]:
        if (data["DC"][i]['points']['strength'] > avg_dc):
            more_than_average_dc.append(0)
            more_than_average_dc[c] = data["DC"][i]['name']
            c += 1

    more_than_average = [more_than_average_mcu, more_than_average_dc]
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCEU
    '''
    return more_than_average


# returns info: Steve Rogers and Superman

# CHANGES:
# used append function rather than insert since we dont need to insert at a specific point
# corrected argument of append function to remove the name
def get_names(data):
    names = []
    for i in data["AVENGERS"]:
        names.append(data["AVENGERS"][i]['name'])
    for j in data["DC"]:
        names.append(data["DC"][j]['name'])
    # Return a list of superhero names
    return names

# returns a list
