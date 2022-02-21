def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename, word):
    """Count the approximate number of occurances of the given word."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents = contents.lower()
        word = word.lower()
        occur = contents.count(word)
        print(f"The word, {word}, occurred {occur} times in the {filename} file")

filenames = ['The Raven.txt', 'The Road Not Taken.txt', 'Jabberwocky.txt', 'Fire And Ice.txt']
for filename in filenames:
    count_words(filename)
searchWord = input("Enter a common word you would like to search: ")
for filename in filenames:
    find_words(filename, searchWord)