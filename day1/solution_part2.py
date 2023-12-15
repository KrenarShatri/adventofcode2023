from collections import deque
from functools import lru_cache

class SolutionPart2:
    def __init__(self) -> None:
        self.nums_dict = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        self.reverse_nums_dict = self.reverse_nums_dict()

    def read_input(self, file_path: str = "./input.txt"):
        with open(file_path) as file:
            lines = [line.rstrip() for line in file]
            return lines

    @lru_cache(maxsize=None)
    def reverse_nums_dict(self):
        reversed_nums = {}

        for k, v in self.nums_dict.items():
            reversed_nums[k[::-1]] = v
        return reversed_nums

    def result(self):
        total_sum = 0
        left_num = ""
        right_num = ""
        lines = self.read_input()
        root = Trie().root
        reverse_trie_node = Trie(True).root
        stack = []

        for line in lines:
            current_node = root
            i, j = 0, len(line) - 1
            left_num = ""
            right_num = ""
            while i <= j:
                offset = 0
                stack = []
                current_node = root

                # if "0" < line[i] <= "9":
                #     left_num = line[i]
                #     print(f"left: {left_num}")
                #     break

                # if line[i] in current_node.children:
                #     current_node = current_node.children[line[i]]
                #     stack.append(line[i])
                # elif line[i] in root.children:
                #     stack = []
                #     current_node = root
                #     current_node = current_node.children[line[i]]
                #     stack.append(line[i])

                # if current_node.end_of_word:
                #     left_num = self.nums_dict["".join(stack)]
                #     stack = []
                #     print(f"left: {left_num}")
                #     break


                while i <= j and "0" > line[i] > "9" and line[i] not in current_node.children:
                    i += 1

                if i <= j and "0" <= line[i] <= "9":
                    left_num = line[i]
                    break

                while i + offset <= j and line[i + offset] in current_node.children:
                    stack.append(line[i + offset])
                    current_node = current_node.children[line[i + offset]]
                    offset += 1

                    if current_node.end_of_word:
                        left_num = self.nums_dict["".join(stack)]
                        stack = []
                        break

                if left_num != "":
                    break

                i += 1

            stack = []
            current_node = reverse_trie_node

            while i <= j:
                offset = 0
                stack = []
                current_node = reverse_trie_node

                while i <= j and "0" > line[j] > "9" and line[j] not in current_node.children:
                    j -= 1

                if i <= j and "0" <= line[j] <= "9":
                    right_num = line[j]
                    break

                while i + offset <= j and line[j - offset] in current_node.children:
                    current_node = current_node.children[line[j - offset]]
                    stack.append(line[j - offset])
                    offset += 1

                    if current_node.end_of_word:
                        right_num = self.reverse_nums_dict["".join(stack)]
                        break

                if right_num != "":
                    break
                j -= 1

            total_sum += int(left_num + right_num)

        return total_sum


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self, reverse: bool = False) -> None:
        nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        if reverse:
            for i in range(len(nums)):
                nums[i] = nums[i][::-1]

        self.root = TrieNode()
        current = self.root

        for num in nums:
            current = self.root
            for ch in num:
                if ch not in current.children:
                    current.children[ch] = TrieNode()

                current = current.children[ch]
            current.end_of_word = True

print(SolutionPart2().result())
