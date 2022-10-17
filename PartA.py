import sys
import re
import builtins
import string


def tokenize(file_path):
    """
    Get token list
    Runtime Complexity:O(n)
    :param file_path:
    :return:
    """
    tokens = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                words = re.split("[^a-z^A-Z^0-9]", line)
                for word in words:
                    word = word.strip(string.punctuation).lower()
                    if word != "":
                        tokens.append(word)
    except FileNotFoundError:
        builtins.print("Can not open file: " + file_path)
        sys.exit(0)
    return tokens


def computeWordFrequencies(tokens):
    """
    Compute token Frequencies
    Runtime complexityO(n)
    :param tokens:
    :return:
    """
    frequencies = {}
    for token in tokens:
        token_count = frequencies.get(token, 0)
        frequencies[token] = token_count + 1
    return frequencies


def print(frequencies):
    """
    Print out Frequencies
    Since used sorted()，Runtime Complexity:O(nlogn)
    :param frequencies:
    :return:
    """
    frequencies_items = frequencies.items()
    frequencies_sorted_items = sorted(frequencies_items, key=lambda x: x[1], reverse=True)
    for token, count in frequencies_sorted_items:
        builtins.print(token + " - " + str(count))


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        builtins.print("Command parameters are wrong!")
        sys.exit(0)
    tokens = tokenize(argv[1])

    frequencies = computeWordFrequencies(tokens)
    print(frequencies)

