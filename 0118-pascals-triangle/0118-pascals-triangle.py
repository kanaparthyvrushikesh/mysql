class Solution:
    def generate(self, numRows):
        v = []

        for i in range(numRows):
            temp = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    elem = 1
                else:
                    elem = v[i - 1][j - 1] + v[i - 1][j]

                temp.append(elem)

            v.append(temp)

        return v