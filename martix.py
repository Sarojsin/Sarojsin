#take an input from user to excess the number from the matrix
matrix=[[1,3,2],[4,5,2],[6,7,8]]
print(matrix)
position=int(input('Enter the position'))
#geting the digits or position
row_no=position/10
column_no=position%10
print(matrix[int(row_no) - 1][int(column_no) - 1])

matrix[int(row_no) - 1][int(column_no) - 1]="🫦"                    # this is string so  '' at output
print(matrix)