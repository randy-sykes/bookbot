import string

def count_letters(data: str) -> dict:
    result = {}
    for i in data.lower():
        if not i.isalpha():
            continue
        if i not in result:
            result[i] = 0
        result[i] += 1
    return result


book_file = "books/frankenstein.txt"

with open(book_file) as f:
    book = f.read()
    words = book.split()
    letters = dict(sorted(count_letters(book).items(), key=lambda x: x[1], reverse=True))
    print()
    print(f"--- Begin report of {book_file} ---")
    print(f"{len(words)} words found in the document")
    print()
    print("\n".join([f"The '{letter}' character was found {letters[letter]} times" for letter in letters]))
    print("--- End report ---")

