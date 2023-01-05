def matrics(rows, column):
    mat = []
    for i in range(rows):
        temp = []
        for j in range(column):
            element = int(input(f"Enter The [{i}][{j}] Element"))
            temp.append(element)
        mat.append(temp)
    return mat

m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))
mat1 = matrics(m, n)
mat2 = matrics(m, n)
