
def calculate_pay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_hours = 40
        over_hours = hours-40
        pay = (regular_hours * rate) + (over_hours * 1.5 * rate)
    return pay


def main():

    while True:
        try:
            hours = float(input("Please, enter the hours: "))
            rate = float(input("Please, enter the rate: "))
            if hours < 0 or rate < 0:
                raise ValueError("Hours and rate must be positive numbers.")
            print(f"Your gross pay is {calculate_pay(hours=hours, rate=rate)}")

            break
        except ValueError:
            print("You cannot enter strings,try again")


if __name__ == "__main__":
    main()
