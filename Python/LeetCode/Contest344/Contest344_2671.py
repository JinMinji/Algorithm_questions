#Contest344, Q2
from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.data = []
        self.cnt_dict = defaultdict(int)
        self.cnt = [0 for i in range(100001)]

    def add(self, number: int) -> None:
        self.data.append(number)
        self.cnt_dict[number] += 1
        self.cnt[self.cnt_dict[number]-1] -= 1
        self.cnt[self.cnt_dict[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.data:
            idx = self.data.index(number)
            self.data.pop(idx)
            self.cnt_dict[number] -= 1
            self.cnt[self.cnt_dict[number] + 1] -= 1
            self.cnt[self.cnt_dict[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.cnt[frequency]:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

def test_run(input, numbers):
    answer = []
    obj = FrequencyTracker()
    answer.append(None)
    for i in range(len(input)):
        if input[i] == 'add':
            answer.append(obj.add(numbers[i][0]))
        elif input[i] == 'deleteOne':
            answer.append(obj.deleteOne(numbers[i][0]))
        elif input[i] == 'hasFrequency':
            answer.append(obj.hasFrequency(numbers[i][0]))
        else:
            continue
    return answer


if __name__ == "__main__":
    print(test_run(["FrequencyTracker", "add", "add", "hasFrequency"], [[], [3], [3], [2]]))
    print(test_run(["FrequencyTracker", "add", "deleteOne", "hasFrequency"], [[], [1], [1], [1]]))
    print(test_run(["FrequencyTracker", "hasFrequency", "add", "hasFrequency"], [[], [2], [3], [1]]))


