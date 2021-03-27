# https://dodona.ugent.be/en/activities/2033201011/

class PatienceSorter:       # class 클래스명 : 클래스 선언
    # 클래스에 속한 함수를 '메소드' 라고 합니다.
    # 메소드는 첫번째 인자로 항상 self 를 가집니다. (self : 객체 자기 자신을 의미합니다.)
    # 원래 함수는 '함수명()' 과 같이 호출 가능하지만, 메소드는 '객체명.함수명()' 과 같이 호출 가능합니다.
    def __init__(self):     # __init__(self) : 생성자 함수
        self.stack = []     # 생성자 함수 안에서는, 객체가 사용할 변수들을 선언해줄 수 있습니다.
    # 생성자 함수는 외부에서 '클래스명()' 과 같이 객체를 생성할 때 호출됩니다.
    def stacks(self): return [s[::-1] for s in self.stack]  # [요소 for 요소 in 리스트] : for in 문을 한줄로 넣은 것과 같습니다.
    # [i for i in [1, 2, 3]] 은 [1, 2, 3] 을 반환합니다.
    # [i+1 for i in [1, 2, 3]] 은 [2, 3, 4] 를 반환합니다.
    # 요소[::-1] 는 요소가 시퀀스 자료형(=리스트자료형, 집합자료형, 튜플자료형) 경우 리스트의 순서를 바꿔서 반환합니다.
    def stack_count(self): return len(self.stack)   # len() : 리스트의 길이를 반환 (ex> len([1, 2, 3]) -> 3)
    def item_count(self): return sum(len(s) for s in self.stack)    # sum() : 리스트의 모든 요소를 합한 값을 반환 (ex> sum([1, 2, 3]) -> 6)

    def add_item(self, item):   # 메소드에도 매개변수를 받을 수 있습니다. 위같이 두번째 인자부터 매개변수 이름을 적어주면 됩니다.
        for s in self.stack:
            if s[-1] >= item:   # 리스트[-1] : 맨 뒤(=맨 오른쪽)의 요소를 반환
                s.append(item)
                return self     # 객체 자기자신을 반환 (return 을 처리하면 밑의 코드를 실행하지 않고 함수는 종료됩니다.)
        self.stack.append([item])
        return self

    def remove_item(self):
        min_items = [s[-1] for s in self.stack]
        assert min_items, "no more items"       # assert 체크할값, "에러메시지" : 체크할 값이 없거나 비어있으면 에러를 반환
        target_index = min_items.index(min(min_items))      # min() : 리스트 중에서 가장 작은 값을 반환
        # 리스트.index(요소) : 리스트에 있는 요소의 인덱스를 반환
        pop_item = self.stack[target_index].pop()   # pop() : 리스트에서 맨 뒤(=맨 오른쪽)의 요소를 삭제 후 반환
        if not self.stack[target_index]:    # 리스트가 비어있으면(= not 리스트),
            self.stack.pop(target_index)    # 빈 리스트도 삭제
        return pop_item

    def add_items(self, items):
        for item in items:
            self.add_item(item)
        return self

    def remove_items(self):
        return tuple(self.remove_item() for _ in range(self.item_count()))
        # _ : for 문에서 리스트의 요소를 하나씩 빼낼 때, 빼낸 요소가 필요없을 경우(=변수에 담을 필요가 없는 경우), _으로 처리합니다.


if __name__ == '__main__':
    sorter = PatienceSorter()
    print(sorter.stacks())
    # []
    print(sorter.stack_count())
    # 0
    print(sorter.add_item(4).stacks())
    # [[4]]
    print(sorter.stack_count())
    # 1
    print(sorter.add_item(3).stacks())
    # [[3, 4]]
    print(sorter.add_item(9).stacks())
    # [[3, 4], [9]]
    print(sorter.stack_count())
    # 2
    print(sorter.add_item(1).stacks())
    # [[1, 3, 4], [9]]
    print(sorter.add_item(5).stacks())
    # [[1, 3, 4], [5, 9]]
    print(sorter.add_item(2).stacks())
    # [[1, 3, 4], [2, 5, 9]]
    print(sorter.add_item(7).stacks())
    # [[1, 3, 4], [2, 5, 9], [7]]
    print(sorter.stack_count())
    # 3
    print(sorter.add_item(8).stacks())
    # [[1, 3, 4], [2, 5, 9], [7], [8]]
    print(sorter.add_item(6).stacks())
    # [[1, 3, 4], [2, 5, 9], [6, 7], [8]]
    print(sorter.stack_count())
    # 4
    print(sorter.item_count())
    # 9
    print(sorter.remove_item())
    # 1
    print(sorter.stacks())
    # [[3, 4], [2, 5, 9], [6, 7], [8]]
    print(sorter.remove_item())
    # 2
    print(sorter.stacks())
    # [[3, 4], [5, 9], [6, 7], [8]]
    print(sorter.remove_item())
    # 3
    print(sorter.stacks())
    # [[4], [5, 9], [6, 7], [8]]
    print(sorter.remove_item())
    # 4
    print(sorter.stacks())
    # [[5, 9], [6, 7], [8]]
    print(sorter.stack_count())
    # 3
    print(sorter.remove_item())
    # 5
    print(sorter.stacks())
    # [[9], [6, 7], [8]]
    print(sorter.remove_item())
    # 6
    print(sorter.stacks())
    # [[9], [7], [8]]
    print(sorter.remove_item())
    # 7
    print(sorter.stacks())
    # [[9], [8]]
    print(sorter.remove_item())
    # 8
    print(sorter.stacks())
    # [[9]]
    print(sorter.remove_item())
    # 9
    print(sorter.stacks())
    # []
    # print(sorter.remove_item())
    # Traceback(most recent call last):
    # AssertionError: no more items

    sorter = PatienceSorter()
    print(sorter.add_items([7, 5, 2, 1, 8, 6, 3, 9, 4]).stacks())
    # [[1, 2, 5, 7], [3, 6, 8], [4, 9]]
    print(sorter.stack_count())
    # 3
    print(sorter.item_count())
    # 9
    print(sorter.remove_items())
    # (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(sorter.stacks())
    # []
    print(sorter.stack_count())
    # 0
    print(sorter.item_count())
    # 0
