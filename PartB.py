import sys
import PartA


def printCommonTokens(file1_path, file2_path):
    """
    print token in common
    Runtime Complexity:O(n^2)
    :param file1_path:
    :param file2_path:
    :return:
    """
    commonTokensCount = 0
    tokens1 = PartA.tokenize(file1_path)
    tokens2 = PartA.tokenize(file2_path)
    tokens1_set = set(tokens1)
    tokens2_set = set(tokens2)
    for token in tokens1_set:
        if token in tokens2_set:
            print(token)
            commonTokensCount += 1
    return commonTokensCount


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 3:
        print("Command parameters are wrong!")
        sys.exit(0)
    file1_path = argv[1]
    file2_path = argv[2]
    print("There is %d common tokens in '%s' and '%s'." % (
    printCommonTokens(file1_path, file2_path), file1_path, file2_path))
