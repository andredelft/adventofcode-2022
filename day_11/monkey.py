from typing import Callable


class Monkey(object):
    def __init__(
        self,
        starting_items: list[int],
        operation: str,
        divisible_by: int,
        throw_true: int,
        throw_false: int,
    ):
        self.items = starting_items
        self.operation = operation
        self.divisible_by = divisible_by
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.num_inspections = 0

    def perform_operation(self, old: int):
        return eval(self.operation)

    def inspect(self):
        throw_dict = {self.throw_true: [], self.throw_false: []}

        for item in self.items:
            self.num_inspections += 1
            item = self.perform_operation(item)
            item //= 3
            if item % self.divisible_by == 0:
                throw_dict[self.throw_true].append(item)
            else:
                throw_dict[self.throw_false].append(item)

        self.items = []
        return throw_dict

    def catch(self, items: list[int]):
        self.items += items
