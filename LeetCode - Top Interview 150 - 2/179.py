"""
I think the most important thing for this problem is to go through a few examples.

[7, 79, 70] => "79770"
[7,77,76,75,78] => "787777675"

The logic becomes much clearer only after listing them out. During the actual problem-solving process, I should always list as many examples as possible to identify the
underlying logic.

=====

This problem is honestly quite difficult. I feel like I need to memorize the solution approach to some extent. The numbers should be sorted in the order of "34" "3" and
"32". In other words based on string comparison the order should be "numbers where the second digit is greater than the first > numbers with no second digit > numbers
where the second digit is smaller than the first". To achieve this a trick like key=lambda x: x * (20 // len(x)) is necessary.  

For reference a standard sorted would result in the order of "3" "32" and "34".
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num == 0 for num in nums):
            return "0"

        sorted_nums = sorted(
            [str(num) for num in nums], reverse=True, key=lambda x: x * (20 // len(x))
        )

        result = ""

        for str_num in sorted_nums:
            result += str_num

        return result
