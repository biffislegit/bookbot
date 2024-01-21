def main()-> None:
    file_path = "./books/frankenstein.txt"
    file_contents = read_file(file_path)
    words_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    final_report(file_path, words_count, letter_count)


def final_report(book, words, letters):
    title = f"Begin report of {book}"
    print(f"\n*** {title} ***")
    print(f"{words} found in the document\n")
    for letter, counts in letters:
        print(f"The '{letter}' character was found {counts} times")
    print("--- End Report ---")


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
    return sorted(letter_count.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    main()
