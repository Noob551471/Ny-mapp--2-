import time
import random

number = 0

print("Starting count...")

while True:
    number += 1
    print(number, end="\r")
    time.sleep(0.5)