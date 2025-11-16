# Build a Drink Water Reminder App in Python that notifies users to drink water at regular intervals. You can use libraries like time for timing and plyer for notifications. This app helps you practice basic logic, user interaction, and periodic reminders in Python.
import time
import os

while True:
    print("Please sip some water!")

    os.system("""
              osascript -e 'display notification "You need to drink some water" with title "Drink Water Reminder"'
              """)

    time.sleep(60*60)  # 1 hour