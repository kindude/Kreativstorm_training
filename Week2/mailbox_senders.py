

try:
    with open("mbox-short.txt", "r") as file:
        senders = 0
        lines = file.readlines()
        for l in lines:
            if l.startswith("From:"):
                print(f"Sender {(l.split())[1]}")
                senders += 1

    print(f"{senders} senders")

except FileNotFoundError as error:
    print(f"File not found {error}")
