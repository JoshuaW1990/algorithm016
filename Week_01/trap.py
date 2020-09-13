class Solution:
    # def trap(self, height: List[int]) -> int:
    def trap(self, height):
        if len(height) < 3:
            return 0
        result = 0
        stack = [0]
        index = 1
        while index < len(height):
            h = height[index]
            while len(stack) > 0 and h > height[stack[-1]]:
                topIndex = stack.pop()
                if len(stack) <= 0:
                    break
                minHeight = min(h, height[stack[-1]])
                distance = index - stack[-1] - 1
                volume = distance * (minHeight - height[topIndex])
                result += volume
            stack.append(index)
            index += 1
        return result

solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution.trap(height))
