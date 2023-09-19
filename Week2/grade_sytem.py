
def get_grade(grade):
    if grade >= 0.9:
        return 'A'
    elif grade >= 0.8:
        return 'B'
    elif grade >= 0.7:
        return 'C'
    elif grade >= 0.6:
        return 'D'
    else:
        return 'F'



if __name__ == "__main__":
    while True:
        try:
            grade = float(input("Please, enter a grade: "))
            print(f"Your grade is {get_grade(grade=grade)}")
            break
        except ValueError:
            print("You cannot enter strings,try again")
