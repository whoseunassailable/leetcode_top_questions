from typing import List
import ast

class Solution:
    def __init__(self,  nums: List[int], target: int):
        self.__nums = nums
        self.__target = target

    def two_sum(self) -> List[int]:
        for i in range(len(self.__nums)):
            for j in range(len(self.__nums)):
                if i != j and self.__nums[i] + self.__nums[j] == self.__target:
                    return [i, j]

def main():
    nums = ast.literal_eval(input("nums = "))
    target = int(input())
    solution = Solution(nums, target)
    result = solution.two_sum()
    print(f"Indices: {result}")

if __name__ == "__main__":
    main()
