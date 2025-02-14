class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix


    def add_row(self,row,position=False):
        if(not position):
            self.matrix.append(row)
        self.matrix.insert(position,row)

    def del_row(self,position=False):
        if(not position):
            self.matrix.pop()

    def add(self,matrix):
        [A_row_len,A_col_len]=[len(self.matrix),len(self.matrix[0])]
        [B_row_len,B_col_len]=[len(matrix),len(matrix[0])]
        A=self.matrix
        B=matrix
        result=[]

        if((A_row_len!=B_row_len) or (A_col_len!=B_col_len) ):
            raise ValueError('The Dimensions of the matrices are  not equal')
        for i in range(A_row_len):
            result.append([])
            for j in range(A_col_len):
                result[i].append(A[i][j]+B[i][j])
        
        self.matrix=result
        print("Addition Successful")
        return self
        



    


