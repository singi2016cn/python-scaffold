"""常见单词"""

book_file = 'book.txt'


def count_word_in_book(book_file, count_word='the'):
    try:
        with open(book_file,encoding='utf-8') as f:
            book_content = f.read()
    except FileNotFoundError:
        return 0
    else:
        return book_content.lower().count(count_word)


print(count_word_in_book(book_file))

