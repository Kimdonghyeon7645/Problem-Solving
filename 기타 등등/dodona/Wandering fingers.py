# https://dodona.ugent.be/en/activities/574186898/

def outside(word: str) -> str: return word[0] + word[-1]
def inside(word: str) -> str: return word[1:-1]


def issubword(sub_word: str, word: str) -> bool:
    for ch in word:
        if ch in sub_word:
            sub_word = sub_word.lstrip(ch)
    return not sub_word


def iswandering(sub_word: str, word: str) -> bool:
    return outside(sub_word) == outside(word) and issubword(sub_word, word)


def read_dictionary(file: str) -> dict:
    result = dict()
    with open(file, "r") as f:
        for word in [line.rstrip("\n") for line in f.readlines()]:
            result[outside(word)] = result[outside(word)] | {inside(word)} if outside(word) in result.keys() else {inside(word)}

    return result


def wanderings(word: str, word_dict: dict) -> set:
    result = set()
    if outside(word) in word_dict.keys():
        result = set(ch for ch in word_dict[outside(word)] if issubword(ch, word))

    return result


if __name__ == '__main__':

    # outside
    print(outside('quick'))
    print(outside('queen'))
    print(outside('king'))
    print(outside('win'))

    # inside
    print(inside('quick'))
    print(inside('queen'))
    print(inside('king'))
    print(inside('win'))

    # issubword
    print(issubword('quick', 'qwertyuihgfcvbnhjk'))
    print(issubword('win', 'qwertyuytresdftyuiokn'))
    print(issubword('queen', 'qwertyuytresdftyuiokn'))
    print(issubword('quick', 'qwertyuytresdftyuiokn'))

    # iswandering
    print(iswandering('quick', 'qwertyuihgfcvbnhjk'))
    print(iswandering('win', 'qwertyuytresdftyuiokn'))
    print(iswandering('queen', 'qwertyuytresdftyuiokn'))
    print(iswandering('quick', 'qwertyuytresdftyuiokn'))

    # read_dictionary
    dictionary = read_dictionary("dictionary.txt")
    print(dictionary['qk'])
    print(dictionary['qn'])
    # print(dictionary['xx'])

    # wanderings
    print(wanderings('qwertyuihgfcvbnhjk', dictionary))
    print(wanderings('qwertyuytresdftyuiokn', dictionary))
    print(wanderings('ghijakjthoijerjidsdfnokg', dictionary))
    print(wanderings('xkzjunspebfgslddfksdrx', dictionary))
