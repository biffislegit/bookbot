def main()-> None:
    file_path = "./books/frankenstein.txt"
    file_contents = read_file(file_path)
    words_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    final_report(words_count, letter_count)
    print("ok")
def final_report(words, letters):
    print(f"\nBegin report of ./books/frankensetein\n\n"
    print(words_count)
    print(letter_count)


def read_file(file_path: str):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(file):
    words = file.split()
    return len(words)


def count_letters(file_contents):
    lower_letters = file_contents.lower()
    letters = []
    for letter in lower_letters:
        if letter.isalpha() and letter not in letters:
            letters.append(letter)
    letter_count = {letter: lower_letters.count(letter) for letter in letters}
    return letter_count

if __name__ == "__main__":
    main()
