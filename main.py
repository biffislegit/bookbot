def main()-> None:
    """create report about specified book"""
    file_path = "./books/frankenstein.txt"
    file_contents = read_file(file_path)
    words_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    summary = final_report(file_path, words_count, letter_count)
    for line in summary:
        print(line)


def final_report(book: str, words: int, letters: dict) -> list[str]:
    """generate report summary"""
    title = f"Begin report of {book}"
    report = [f"\n*** {title} ***", f"{words} found in the document\n"]
    for letter, counts in letters:
        report.append(f"The '{letter}' character was found {counts} times")
    report.append("--- End Report ---")
    return report


def read_file(file_path: str) -> str:
    """read and return contents of file"""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(file: str) -> int:
    """return total word count of file"""
    words = file.split()
    return len(words)


def count_letters(file_contents: str) -> dict:
    """generate dict of letter with corresponding count"""
    lower_letters = file_contents.lower()
    letters = []
    for letter in lower_letters:
        if letter.isalpha() and letter not in letters:
            letters.append(letter)
    letter_count = {letter: lower_letters.count(letter) for letter in letters}
    return sorted(letter_count.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    main()
