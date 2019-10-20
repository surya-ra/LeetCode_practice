class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = []
        temp = []
        if (rowIndex == 0):
            l = [1]
        for rows in range(1, rowIndex + 1):
            l = [None for _ in range(rows + 1)]
            l[0], l[-1] = 1, 1
            for x in range(1, rows):
                l[x] = temp[x] + temp[x - 1]
            temp = l
        return l