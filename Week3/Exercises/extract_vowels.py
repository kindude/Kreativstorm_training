

def main():
    vowels = "aeiou"
    sentence = "Hello World"
    extracted_vowels = [i for i in sentence if i in vowels]
    print(extracted_vowels)

if __name__ == "__main__":
    main()