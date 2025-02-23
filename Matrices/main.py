[
    [1, 2],
    [3, 4]
]
class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    
    def add_row(self,row,pos=False):
        if(not pos):
            self.matrix.append(row)
            print('Row successfully added!')
            return
        self.matrix.insert(pos,row)
        return print('Row successfully added!')
    def del_row(self,pos=False):
        if(not pos):
            self.matrix.pop()
            return print('Row delete was successful')
        self.matrix.pop(pos)
    
    def add_matrix(self,matrix):
        #Verify the both matrices are the same dimension
        A=self.matrix
        B=matrix.matrix
        [A_row_len,B_row_len]=[len(A),len(B)]
        [A_col_len,B_col_len]=[len(A[0]),len(B[0])]
        result=[]

        if((A_row_len!=B_row_len) or (B_col_len!=A_col_len)):
            raise ValueError('They have unmatching dimensions!')
        for i in range(A_row_len):
            row=[]
            for j in range(A_col_len):
                row.append(A[i][j]+B[i][j])
            result.append(row)
        self.matrix=result

        return self
    def subtract_matrix(self,matrix):
        #Verify the both matrices are the same dimension
        A=self.matrix
        B=matrix.matrix
        [A_row_len,B_row_len]=[len(A),len(B)]
        [A_col_len,B_col_len]=[len(A[0]),len(B[0])]
        result=[]

        if((A_row_len!=B_row_len) or (B_col_len!=A_col_len)):
            raise ValueError('They have unmatching dimensions!')
        for i in range(A_row_len):
            row=[]
            for j in range(A_col_len):
                row.append(A[i][j]-B[i][j])
            result.append(row)
        self.matrix=result

        return self
    def scalar_multiply(self, scalar):
        A=self.matrix
        result=[]
        for i in range(len(A)):
            row = []
            for j in range(len(A[i])):
                row.append(A[i][j]* scalar)
            result.append(row)
        self.matrix=result
        return self


testA=Matrix([
    [1,2],
    [3,4]
])

testB=Matrix(
    [
        [5,6],
        [7,8]
    ]
)


result=testB.scalar_multiply(2)
    
        
print(result.matrix)

    
        
