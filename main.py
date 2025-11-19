from stats import number_of_words, number_of_chars

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    word_count = number_of_words('books/frankenstein.txt')
    print(f"Found {word_count} total words")
    dict_chars = number_of_chars('books/frankenstein.txt')
    print(dict_chars)

main()
