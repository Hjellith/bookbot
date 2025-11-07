import sys
from stats import word_count
from stats import get_num_characters
from stats import sort_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    char_list = sort_counts(get_num_characters(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")
    print("--------- Character Count -------")
    
    for i in char_list: 
        print(i["char"] + ":", i["num"])
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
