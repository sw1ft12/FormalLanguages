class RegExp:
    regexp = ""
    letter = ""
    k = 0

    def __init__(self, regexp, letter, k):
        self.regexp = regexp
        self.letter = letter
        self.k = k

    def star_operator(self, rem_set, stack):
        new_set = set(rem_set)
        old_set = set()
        while new_set != old_set:
            old_set = set(new_set)
            for el1 in old_set:
                for el2 in old_set:
                    new_set.add((el1 + el2) % self.k)

        stack.append(new_set)

    def or_operator(self, set1, set2, stack):
        stack.append(set1 | set2)

    def point_operator(self, rem1_set, rem2_set, stack):
        _set = set()
        for el1 in rem1_set:
            for el2 in rem2_set:
                _set.add((el1 + el2) % self.k)
        stack.append(_set)

    def parse(self):
        stack = []
        for symbol in self.regexp:
            if symbol == '1':
                stack.append({0})

            elif symbol in "abc":
                isLetter = int(symbol == self.letter)
                stack.append({isLetter})

            elif symbol == '*' and len(stack) > 0:
                    operand = stack.pop(len(stack) - 1)
                    self.star_operator(operand, stack)

            elif len(stack) > 1:
                    operand1 = stack.pop(len(stack) - 1)
                    operand2 = stack.pop(len(stack) - 1)
                    if symbol == '.':
                        self.point_operator(operand1, operand2, stack)
                    else:
                        self.or_operator(operand1, operand2, stack)
        return 0 in stack[0]

