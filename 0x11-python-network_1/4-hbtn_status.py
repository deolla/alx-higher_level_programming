#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)

print("Body response:")
print(f"    - type: {type(response.text).__name__}")
print(f"    - content: {response.text}")
