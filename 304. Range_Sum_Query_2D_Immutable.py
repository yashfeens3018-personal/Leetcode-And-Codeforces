#304. Range Sum Query 2D - Immutable
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.rows=len(matrix)
        self.columns=len(matrix[0])
        self.new=[[0] for r in range(self.rows+1)]
        for i in range(self.rows+1):
            self.new[i]=[0 for c in range(self.columns+1)]
        for r in range(self.rows):
            for c in range(self.columns):
                self.new[r+1][c+1]=self.new[r][c+1]+self.new[r+1][c]+self.matrix[r][c]-self.new[r][c]
        print(self.new)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        A=self.new[row2+1][col2+1]
        B=self.new[row1][col2+1]
        C=self.new[row2+1][col1]
        D=self.new[row1][col1]
        return A-B-C+D
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
