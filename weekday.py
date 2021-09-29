#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This program converts the number to its corresponding weekday


def main():
    # This program converts the number to its corresponding weekday

    # input
    user_weekday = input("Enter the number of the weekday (ex: 5 for Thursday) : ")

    try:
        user_weekday = int(user_weekday)
        # process and output
        if user_weekday == 1:
            print("Sunday")
        elif user_weekday == 2:
            print("Monday")
        elif user_weekday == 3:
            print("Tuesday")
        elif user_weekday == 4:
            print("Wednesday")
        elif user_weekday == 5:
            print("Thursday")
        elif user_weekday == 6:
            print("Friday")
        elif user_weekday == 7:
            print("Saturday")
        else:
            print("Invalid input.")
    except Exception:
        print("Not a valid input.")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
