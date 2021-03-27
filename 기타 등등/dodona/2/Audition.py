# https://dodona.ugent.be/en/activities/122590180/

class Collection:
    def __init__(self, collection: list):
        self.collection = list()
        for ele in collection:
            self.collection.extend(range(ele[0], ele[1]+1)) if type(ele) is list else self.collection.append(ele)
        self.collection.sort()

    def _to_normal_form(self):
        if len(self.collection) < 2:
            return [self.collection]

        result = ([[self.collection[0]]] if self.collection[0] + 1 is self.collection[1] else [self.collection[0]])
        for i in range(1, len(self.collection) - 1):
            if self.collection[i - 1] + 1 is not self.collection[i]:
                result.append(
                    [self.collection[i]] if self.collection[i] + 1 is self.collection[i + 1] else self.collection[i])
            elif self.collection[i] + 1 is not self.collection[i + 1]:
                result[-1].append(self.collection[i])
        (result[-1] if self.collection[-2] + 1 is self.collection[-1] else result).append(self.collection[-1])

        return result

    def __len__(self): return len(self.collection)
    def numbers(self): print("{" + str(self.collection)[1:-1] + "}", end="")
    def __str__(self): return str(self._to_normal_form())
    def normalform(self): print(self._to_normal_form(), end="")
    def __repr__(self): return f"Collection({self._to_normal_form()})"

    def __sub__(self, other): return Collection([i for i in self.collection if i not in other.collection])
    def __or__(self, other): return Collection(list(set(self.collection) | set(other.collection)))
    def __and__(self, other): return Collection(list(set(self.collection) & set(other.collection)))
    def __xor__(self, other): return Collection(list(set(self.collection) ^ set(other.collection)))
    def __eq__(self, other): return self.collection == other.collection
    def __ne__(self, other): return self.collection != other.collection
    def __lt__(self, other): return (not self - other) and bool(other - self)
    def __le__(self, other): return not self - other
    def __gt__(self, other): return (not other - self) and bool(self - other)
    def __ge__(self, other): return not other - self


if __name__ == '__main__':

    A = Collection([33, [27, 30], 32, 25, [20, 24], 31, 19])
    A.numbers()
    print(len(A))
    A.normalform()
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
