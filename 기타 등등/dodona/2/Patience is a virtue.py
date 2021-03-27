# https://dodona.ugent.be/en/activities/2033201011/

class PatienceSorter:
    def __init__(self): self.stack = []
    def stacks(self): return [s[::-1] for s in self.stack]
    def stack_count(self): return len(self.stack)
    def item_count(self): return sum(len(s) for s in self.stack)

    def add_item(self, item):
        for s in self.stack:
            if s[-1] > item:
                s.append(item)
                return self
        self.stack.append([item])
        return self

    def remove_item(self):
        min_items = [s[-1] for s in self.stack]
        assert min_items, "no more items"
        target_index = min_items.index(min(min_items))
        pop_item = self.stack[target_index].pop()
        if not self.stack[target_index]:
            self.stack.pop(target_index)
        return pop_item

    def add_items(self, items):
        for item in items:
            self.add_item(item)
        return self

    def remove_items(self):
        return tuple(self.remove_item() for _ in range(self.item_count()))


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
