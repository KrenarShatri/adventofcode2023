class Solution:
    def read_input(self, file_path: str = "./input.txt"):
        with open(file_path) as file:
            lines = [line.rstrip() for line in file]
            return lines

    def result(self):
        total_sum = 0
        lines = self.read_input()

        for line in lines:
            i, j = 0, len(line) - 1
            left = ""
            right = ""
            while i <= j:
                if line[i] >= "0" and line[i] <= "9":
                    left = line[i]
                    break
                i += 1

            while i <= j:
                if line[j] >= "0" and line[j] <= "9":
                    right = line[j]
                    break
                j -= 1
            num = int((left + right))
            total_sum += num
        return total_sum

print(Solution().result())

