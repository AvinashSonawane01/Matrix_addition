# Matrix_addition


def matAddition(mat1, mat2, r, c):
    addition = []
    for i in range(r):
        subList = []
        for j in range(c):
            sum = mat1[i][j]+mat2[i][j]
            subList.append(sum)
        addition.append(subList)
    return addition   


def cMatrix(mat, r, c):
    for i in range(r):
            row = []
            for j in range(c):
                element = int(input("Enter elements of matrix: "))
                row.append(element)
            mat.append(row)

mat1 = []
mat2 = []
decision = 0
loop = True

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))



while loop:
    if r== c:
        choice = input("*** Enter y to start ***")
    
        if choice == "y":
            cMatrix(mat1, r, c)
            print("Create another matrix")
            choice = "2"

        if choice == "2":
            cMatrix(mat2, r, c)
            print("Addition of matrix is given below: \n")
            choice = "3"

        if choice == "3":
            matrix = matAddition(mat1, mat2, r, c)
            for i in range(r):
                for j in range(c):
                    print(matrix[i][j],end="\t")
                print("\n")
            loop = False
    
    else:
        print("Addition not possible as rows and columns are not equal")
        loop = False
