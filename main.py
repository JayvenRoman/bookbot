import sys
from stats import word_counter, letter_counter, letter_sorter

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(f"./{sys.argv[1]}")
        num_words = word_counter(text)
        letters = letter_counter(text)
        letters_dict = letter_sorter(letters)
    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in letters_dict:
                if item["char"].isalpha():
                    print(f"{item['char']}: {item['num']}")
        print("============= END ===============")


main()