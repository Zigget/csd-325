"""
Samuel Sidzyik
Module 9.1
3/1/26

Create python code to run APIs
"""

""" import statements """
import requests
import json

response = requests.get("http://anapioficeandfire.com/api/houses")
print(response.status_code)
data = json.loads(response.text)
print(f"Filtered Houses: {len(data)}")
print(f"First House: {data[0]['name']}")

params = {
    'filter_by': 'region=The Riverlands',
    'limit': 4
    }

response = requests.get(
    "http://anapioficeandfire.com/api/houses",
    params = params)

print(response.status_code)
data = json.loads(response.text)

print(f"Filtered Houses: {len(data)}")
print(f"First House: {data[0]['name']}")