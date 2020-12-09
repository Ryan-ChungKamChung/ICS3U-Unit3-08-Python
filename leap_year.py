#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program figures out if an inputted year is a leap year


def main():
    # Function figures out if an inputted year is a leap year

    print("Give me a year number and I will tell you if it is a leap year")

    # Input
    leap_year_string = input("Enter year: ")

    # Process
    try:
        leap_year = int(leap_year_string)

        if leap_year % 4 == 0:
            if leap_year % 100 != 0:
                # Output
                print("This is a leap year")
            else:
                if leap_year % 400 == 0:
                    # Output
                    print("This is a leap year")
                else:
                    # Output
                    print("This is not a leap year")
        else:
            # Output
            if leap_year % 4:
                print("This is a leap year")
            else:
                print("This is not a leap year")
    except Exception:
        # Output
        print("This isn't a valid year")


if __name__ == "__main__":
    main()
