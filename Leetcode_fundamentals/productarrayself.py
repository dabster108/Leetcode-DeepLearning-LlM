class Solution:
    def productExceptSelf(self, nums):
        result = []
        product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        for num in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // num)

        return result
