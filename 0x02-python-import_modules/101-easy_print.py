#!/usr/bin/python3
import os
message = "#pythoniscool\n"
os.write(1, message.encode())
