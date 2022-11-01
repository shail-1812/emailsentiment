# Python program to read
# json file


import json

# Opening JSON file
f = open('test.json', "r")

# returns JSON object as
# a dictionary
data = f.read()
# data = json.dumps(data)

data = data.split("\"email\":")

print(data[1])

# Iterating through the json
# list
# for i in data['Emails']:
# 	print(i)

# # Closing file
# f.close()
