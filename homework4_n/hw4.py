#2.1
n_list = list(range(21))
print (n_list)

#2.2
def SquareList(input_list):
    return [x**2 for x in input_list]
SquareNum = SquareList(n_list)
print(SquareNum)

#2.3
def first_fifteen_elements(input_list):
    return input_list[:15]
print(first_fifteen_elements(SquareNum))

#2.4
def every_fifth_element(input_list):
    return input_list[4::5]
print(every_fifth_element)

#2.5
def fancy_function(input_list):
    return input_list[-3::-3]
print(fancy_function(SquareNum))

#3.1
def create_2d_list():
    matrix = []
    count = 1
    for i in range(5):
        row = []
        for j in range (5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix
matrix = create_2d_list()
print(matrix)

#3.2
def modified_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix
new_matrix = modified_2d_list(matrix)
print(new_matrix)

#3.3
def sum_non_questionM_elements(matrix):
    total = 0
    for row in matrix:
        for element in row:
            if element != "?":
                total += element
    return total
print(sum_non_questionM_elements)