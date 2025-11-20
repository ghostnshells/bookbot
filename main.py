import sys
from stats import number_of_words, number_of_chars, sorted_dictionary

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = ""
    len_of_sys = len(sys.argv)
    if len_of_sys < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    word_count = number_of_words(path)
    print("===============BOOKBOT===============")
    print(f"Analyzing book found at {path}")
    print("-------------WORD COUNT-------------")
    print(f"Found {word_count} total words")
    dict_chars = number_of_chars(get_book_text(path))
    #print(dict_chars)
    print("----------CHARACTER COUNT----------")
    sorted_chars = sorted_dictionary(dict_chars)
    for ch in sorted_chars:
        if ch["char"].isalpha():
            print(f"{ch['char']}: {ch['num']}")

main()
