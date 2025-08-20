from stats import get_num_words
from stats import count_character_appear
from stats import sort_dict
import sys
import os

def get_book_text(path):
    text = None
    with open(path) as f:
        text = f.read()

    return text

def validate_inputs(args):
    if not len(args) == 2:
        print(f"Usage: python3 {os.path.basename(__file__)} <path_to_book>")
        sys.exit(1)

def main():
    
    # Check if the script has an arg. Exit if not.
    validate_inputs(sys.argv)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = get_num_words(book)
    char_count = count_character_appear(book)
    char_dict = sort_dict(char_count)
    char_list = None

    for item in char_dict:
        if item["char"].isalpha():
            if char_list is None:
                char_list = f"{item['char']}: {item['num']}"
            else:
                char_list = f"{char_list}\n{item['char']}: {item['num']}"

    report = f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{char_list}
============= END ===============
 """
    print(report)
main()
