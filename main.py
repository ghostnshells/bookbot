from stats import number_of_words

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    word_count = number_of_words('books/frankenstein.txt')
    print(f"Found {word_count} total words")

main()
