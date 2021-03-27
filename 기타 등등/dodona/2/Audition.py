# https://dodona.ugent.be/en/activities/122590180/

class Collection:
    def __init__(self, collection: list):
        self.collection = list()
        for ele in collection:
            if type(ele) in [list, tuple, set] and len(ele) > 1:    # type() : 요소의 타입(=자료형)을 반환
                self.collection.extend(range(ele[0], ele[1]+1))     # 리스트.extend(리스트) : 리스트 2개를 합칩(확장)
            else:
                self.collection.append(ele[0] if type(ele) in [list, tuple, set] else ele)
        self.collection = list(set(self.collection))    # set() : 집합 자료형으로 변환(중복 제거),
        self.collection.sort()      # 리스트.sort() : 요소 정렬

    def _to_normal_form(self):      # [1, 2, 3, 5]를 [[1, 3], 5] 형태와 같이 바꿔주는 함수 (실제 문제에선 쓰이진 않음)
        if len(self.collection) < 2:    # 리스트의 요소가 1개 이하면,
            return self.collection      # 걍 그대로 반환

        # 첫번째 인자(self.collection[0])를 형태에 맞게 결과 리스트에 저장
        result = ([[self.collection[0]]] if self.collection[0] + 1 is self.collection[1] else [self.collection[0]])

        # 두번째 ~ 마지막에서 두번째 인자를 형태에 맞게 결과 리스트에 저장
        for i in range(1, len(self.collection) - 1):
            if self.collection[i - 1] + 1 is not self.collection[i]:
                result.append([self.collection[i]] if self.collection[i] + 1 is self.collection[i + 1] else self.collection[i])
            elif self.collection[i] + 1 is not self.collection[i + 1]:
                result[-1].append(self.collection[i])

        # 마지막 인자(self.collection[-1])를 형태에 맞게 결과 리스트에 저장
        (result[-1] if self.collection[-2] + 1 is self.collection[-1] else result).append(self.collection[-1])

        return result

    def __len__(self): return len(self.collection)      # len(객체) 시, 이 함수 호출
    def numbers(self): return set(self.collection)
    def __str__(self): return str(self._to_normal_form())   # 객체를 print 등으로 출력시, 이 함수 호출
    def normalform(self): return self._to_normal_form()
    def __repr__(self): return f"Collection({self._to_normal_form()})"  # 파이썬에서 객체를 (print 없이) 출력시, 이 함수 호출

    def __sub__(self, other): return Collection([i for i in self.collection if i not in other.collection])  # 객체 - 객체 시, 이 함수 호출
    def __or__(self, other): return Collection(list(set(self.collection) | set(other.collection)))  # 객체 | 객체 시, 이 함수 호출
    def __and__(self, other): return Collection(list(set(self.collection) & set(other.collection))) # 객체 & 객체 시, 이 함수 호출
    def __xor__(self, other): return Collection(list(set(self.collection) ^ set(other.collection))) # 객체 ^ 객체 시, 이 함수 호출
    def __eq__(self, other): return self.collection == other.collection     # 객체 == 객체 시, 이 함수 호출
    def __ne__(self, other): return self.collection != other.collection     # 객체 != 객체 시, 이 함수 호출
    def __lt__(self, other): return (not self - other) and bool(other - self)       # 객체 > 객체 시, 이 함수 호출
    def __le__(self, other): return not self - other        # 객체 >= 객체 시, 이 함수 호출
    def __gt__(self, other): return (not other - self) and bool(self - other)       # 객체 < 객체 시, 이 함수 호출
    def __ge__(self, other): return not other - self        # 객체 <= 객체 시, 이 함수 호출


if __name__ == '__main__':

    A = Collection([33, [27, 30], 32, 25, [20, 24], 31, 19])
    print(A.numbers())
    print(len(A))
    print(A.normalform())
    print(A)
    print(A.__repr__())

    B = Collection([22, 26, 30])
    print(A - B)
    print(B - A)
    print(A | B)
    print(A & B)
    print(A ^ B)

    C = Collection([[1, 5], [7, 7]])
    D = Collection([[1, 5], [7, 8]])
    print(C == Collection([1, 2, 3, 4, 5, 7]))
    print(C == D)
    print(C != D)
    print(C < D)
    print(C <= D)
    print(C > D)
    print(C >= D)
    print(D > C)
    print(D >= C)

    # list 말고도 다른 시퀀스 자료형까지
    F1 = Collection([(17, 20), 4, [1, 4], [8, 11]])
    print(F1)
    F2 = Collection([9, [14, 15], 10, (5, 6), [7, 12]])
    print(F2)
    FF = Collection({(12, 14), (4, 6), (13, 15), (9, 10), (3, 8), 19})
    print(FF)
    FF2 = Collection([1, 1, 2, 3])
    print(FF2)
    FFF = Collection([[10]])
    print(FFF)
    FFF2 = Collection([1])
    print(FFF2)
