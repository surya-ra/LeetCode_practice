class Solution:
    def isValid(self, s: str) -> bool:
        ref = {'(': ')', '{': '}', '[': ']'}
        stack = []
        if len(s) == 0:
            return True

        for elem in s:
            if elem in ref.keys():
                stack.append(elem)
            else:
                try:
                    n = stack.pop()
                    if elem != ref[n]:
                        return False
                except IndexError:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
            
if __name__ == '__main__':
    a = Solution()
    sts = '['
    print(a.isValid(sts))