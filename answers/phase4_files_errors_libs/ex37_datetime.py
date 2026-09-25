"""
Exercise 37 — datetime Module

Task:
    Print:
        - Current date
        - Current time
        - Days until your next birthday
"""

from datetime import date, datetime

def days_until_birthday(month, day):
    today = date.today()
    birthday = date(today.year, month, day)
    if birthday < today:
        birthday = date(today.year + 1, month, day)
    return (birthday - today).days

def main():
    today = date.today()
    now = datetime.now()
    days = days_until_birthday(12, 25)  # example: Dec 25

    print("Today:", today)
    print("Time:", now.time())
    print("Days until birthday:", days)

if __name__ == "__main__":
    main()
