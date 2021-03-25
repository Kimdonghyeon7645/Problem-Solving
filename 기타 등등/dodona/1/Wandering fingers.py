# https://dodona.ugent.be/en/activities/574186898/

def outside(word: str) -> str: return word[0] + word[-1]    # 문자열을 전달받아, 문자열의 처음(= 문자열[0])과 끝(= 문자열[-1])을 반환
def inside(word: str) -> str: return word[1:-1]     # 문자열을 전달받아, 문자열의 처음과 끝을 뺀 문자열(= 문자열[1:-1])을 반환


def issubword(sub_word: str, word: str) -> bool:    # 서브문자열(=sub_word)과 문자열(= word)을 전달받아, 서브문자열이 문자열에 속해있는지 판별(= 참 or 거짓으로 반환)
    for ch in word:     # 문자열(= word)을 한글자씩 가져와서,
        if ch in sub_word:      # 서브문자열(= sub_word) 중에 하나라도 같은 것이 있으면,
            sub_word = sub_word.lstrip(ch)      # 서브문자열(= sub_word)에서 해당 글자(= ch)를 뺀다. (문자열.lstrip(문자) : 문자열에서 왼쪽에있는 문자를 제거)
    return not sub_word     # 이렇게 하고난 후, 문자열(= word) 안의 글자들이, 서브문자열(= sub_word)에 모두 있었으면, 서브문자열의 모든 글자가 제거됬을 것이기에, 서브문자열이 비어있으면 참을 반환(= return not sub_word)


def iswandering(sub_word: str, word: str) -> bool:      # 서브문자열(=sub_word)과 문자열(= word)을 전달받아, 서브문자열이 문자열과 wander 관계인지 판별(= 참 or 거짓으로 반환)
    # wander 관계 = 서브문자열이 문자열에 속해있으면서(= issubword(sub_word, word)), 서브문자열의 첫글자와 끝글자(= outside(sub_word))가 문자열의 첫글자와 끝글자(= outside(sub_word))와 같아야 한다
    return outside(sub_word) == outside(word) and issubword(sub_word, word)


def read_dictionary(file: str) -> dict:     # 파일명을 전달받아, 첫글자+끝글자(= outside())를 키로, 첫글자와 끝글자를 뺀 나머지(= inside())를 값으로 하는 딕셔너리를 반환
    result = dict()
    with open(file, "r") as f:     
        for word in [line.rstrip("\n") for line in f.readlines()]:      # 파일을 한줄씩 끊은 리스트(= 파일.readlines())에서, 반복문으로 line 변수에 한개씩 불러와, 맨오른쪽의 개행문자를 제거(= line.rstrip("\n"))해 리스트로 반환, 이걸 반복문으로 해서 word 변수엔 단어가 하나씩 저장
            result[outside(word)] = result[outside(word)] | {inside(word)} if outside(word) in result.keys() else {inside(word)}    # result 딕셔너리에, 단어(= word)의 첫글자+끝글자(= outside())를 키로, 첫글자와 끝글자를 뺀 나머지(= inside())를 값으로 저장

    return result       # 해당 딕셔너리를 반환


def wanderings(word: str, word_dict: dict) -> set:      # 단어(=word)와 딕셔너리(=word_dict)를 전달받아, 단어와 wander 관계를 만족하는 딕셔너리의 단어를 집합(= set) 자료형에 담아 반환
    result = set()
    if outside(word) in word_dict.keys():   # 문자의 첫글자+끝글자가 딕셔너리의 키 리스트(= word_dict.keys() : 단어의 첫글자+끝글자가 딕셔너리의 키였던 딕셔너리임)안에서 일치하는 것이 있으면,
        result = set(outside(word)[0] + ch + outside(word)[-1] for ch in word_dict[outside(word)] if issubword(ch, word))       # 단어와 wander 관계를 만족하는 딕셔너리의 단어를 집합(=result)에 저장

    return result   # 해당 집합을 반환


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
