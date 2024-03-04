def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    render_number_count(count_letters(text))
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def render_number_count(list):
    for entry in list:
        k = entry.get("key")
        v = entry.get("value")
        print(f"The \'{k}\' character was found {v} times")


def count_letters(text):
    lowered = text.lower()
    letters = {}
    for letter in lowered:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    list = []
    for key, value in letters.items():
        if key.isalpha():
            list.append({"key": key, "value": value})

    list.sort(reverse=True, key=sort_on)
    return list


def sort_on(dict):
    return dict["value"]


main()
