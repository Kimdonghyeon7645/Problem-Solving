def card2symbols(file: str) -> dict:    # 파일이름을 전달받아, 카드번호(index)를 키로, 심볼들(symbols)을 값으로 하는 딕셔너리를 반환
    result = dict()
    with open(file, "r") as f:
        for index, symbols in enumerate(f.readlines()):     # enumerate(리스트) : 리스트의 인덱스와 값을 함께 반환 (-> 그래서 현재 for 문의 변수도 2개) (정확하게는 (인덱스, 값) 형태의 튜플로 반환 -> 언패킹 되어 두개의 변수에 대입)
            result[index+1] = set(symbols.rstrip("\n").split(","))      # 카드번호(index)를 키로, 심볼들(symbols)을 값으로 딕셔너리에 저장
    return result   # 해당 딕셔너리 반환


def common_symbols(indexA: int, indexB: int, card_dict: dict) -> set:   # 카드번호1(indexA)과 카드번호2(indexB) 둘 다 가지고있는 심볼들을 집합으로 반환
    return card_dict[indexA] & card_dict[indexB]    # 집합1 & 집합2 : 집합1, 집합2 두곳 모두에 있는 값들만 반환


def symbol2cards(card_dict: dict) -> dict:  # 카드번호(index)를 키로, 심볼들(symbols)을 값으로 하는 딕셔너리를 전달받아, 심볼(symbol)을 키로, 카드번호(index)들을 값으로 하는 딕셔너리
    result = dict()
    for index, symbols in card_dict.items():    # 딕셔너리의 하나의 키:값 쌍을 한개씩 꺼냄
        for symbol in symbols:      # 심볼들에서 하나의 심볼을 꺼냄
            result[symbol] = (result[symbol] | {index} if symbol in result.keys() else {index})     # 심볼(symbol)을 키로, 카드번호(index)들을 값으로 딕셔너리에 저장
    return result   # 해당 딕셔너리 반환


def common_cards(symbolA: str, symbolB: str, symbol_dict: dict) -> dict:    # 심볼1(symbolA)과 심볼2(symbolB) 둘 다 가지고있는 카드번호들을 집합으로 반환
    return symbol_dict[symbolA] & symbol_dict[symbolB]


def missing_card(file: str) -> set:     # 파일이름을 전달받아, 파일의 카드 덱에서 잃어버린 카드 1장을 반환 (카드 덱에서 모든 심볼은 모든 카드에서 일정한 개수만큼 존재해야 하는데, 모든 카드에서 존재하는 개수가 모자란 심볼들이 잃어버린 카드 구성이 되므로, 이 방식으로 잃어버린 카드를 찾아 반환)
    result = dict()
    for symbol, indexs in symbol2cards(card2symbols(file)).items():     # 파일이름으로, 심볼(symbol)을 키로, 카드번호(index)들을 값으로 하는 딕셔너리를 반환해, 반복문에 사용
        result[len(indexs)] = (result[len(indexs)] | {symbol} if len(indexs) in result.keys() else {symbol})    # 심볼이 있는 카드의 개수(len(indexs))를 키로, 심볼(symbol)들을 값으로 딕셔너리에 저장
    return result[min(result.keys())]   # 심볼이 있는 카드의 개수가 적은(min(result.keys())) 심볼들(result[min(result.keys())])을 하나의 집합으로 묶어 반한 


if __name__ == '__main__':
    
    # card2symbols
    c2s = card2symbols('기타 등등/dodona/cards.txt')
    print(c2s[1])
    print(c2s[2])
    print(c2s[3])1

    # common_symbols
    print(common_symbols(1, 2, c2s))
    print(common_symbols(1, 3, c2s))
    print(common_symbols(2, 3, c2s))

    # symbol2cards
    s2c = symbol2cards(c2s)
    print(s2c["snowman"])
    print(s2c["ice cube"])
    print(s2c["zebra"])

    # common_cards
    print(common_cards('snowman', 'ice cube', s2c))
    print(common_cards('ice cube', 'zebra', s2c))
    print(common_cards('zebra', 'snowman', s2c))

    # missing_card
    print(missing_card('기타 등등/dodona/missing.txt'))
