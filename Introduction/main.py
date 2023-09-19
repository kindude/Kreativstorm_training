
def main():

    while True:
        try:
            hours = float(input("Please, enter the hours: "))
            rate = float(input("Please, enter the rate: "))
            print(f"Your gross pay is {hours * rate}")
            break
        except ValueError:
            print("You cannot enter strings,try again")


if __name__ == "__main__":
    main()
