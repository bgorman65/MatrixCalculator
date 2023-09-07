# Importing random library to generate random numbers
import random

# Function to create a random 5x6 matrix taking in the min and max values for the values
def randomM(min, max):
    # Creating an empty list to return the random matrix
    randomMatrix = []
    # Looping 5 times to create 5 rows
    for i in range(5):
        # Creating an empty list to hold each row generated
        row = []
        # Looping 6 times to create 6 columns
        for j in range(6):
            # Adding random integers from the designated min and max to the row
            row.append(random.randint(min, max))
        # Adding each row to the random matrix
        randomMatrix.append(row)
    # Returning the random matrix
    return randomMatrix

# Transpose List function taking in a matrix
def transpose(parentmatrix):
    # Creating an empty list to return with the transposed matrix
    B = []
    # Looping through all of the columns/elements in the matrix
    for i in range(len(parentmatrix[0])):
        # Creating another list to hold the new rows
        row = []
        # Looping for all the rows
        for item in parentmatrix:
            # Adding the indexed items to the new rows
            row.append(item[i])
        # Adding the new rows to the list which will hold the transposed list
        B.append(row)
    # Returning the transposed list
    return B

# Creating a product function ot find the product of two matrices passed in
def product(parentmatrix1, parentmatrix2):
    # Creating an empty list to return with the multiplied matrix
    productmatrix = []
    # Checking to see of the number of columns in the first matrix is not equal to the second matrix
    if len(parentmatrix1[0]) != len(parentmatrix2):
        # Ending the function then if the condition is passed
        return "Inconclusive"
    # Looping through all of the rows
    for i in range(len(parentmatrix1)):
        # Creating another list to hold the elements of the new rows
        row = []
        # Looping through all of the columns/elements in the second matrix
        for j in range(len(parentmatrix2[0])):
            # Creating a sum counter
            sumProd = 0
            # Looping through all of the columns/elements in the first matrix
            for k in range(len(parentmatrix1[0])):
                # Finding the product of each element corresponding to the columns
                sumProd += parentmatrix1[i][k] * parentmatrix2[k][j]
            # Adding the sum to the row list
            row.append(sumProd)
        # Adding the row with the sums to the product list
        productmatrix.append(row)
    # Returning the multiplied list
    return productmatrix

# Creating an addition function to find the sum of two matrices passed in
def addition(parentmatrix1, parentmatrix2):
    # Creating an empty list to return with the added matrix
    additionmatrix = []
    # Checking if the rows and columns of each matrix are the same
    if len(parentmatrix1) != len(parentmatrix2) or len(parentmatrix1[0]) != len(parentmatrix2[0]):
        # Ending the function if the condition is passed
        return "Inconclusive"
    # Looping through the rows
    for i in range(len(parentmatrix1)):
        # Creating another list to hold the elements of the new rows
        row = []
        # Looping through all of the columns/elements in the matrices
        for j in range(len(parentmatrix1[0])):
            # Appending the added elements to the new row
            row.append(parentmatrix1[i][j] + parentmatrix2[i][j])
        # Appending these rows to the addition matrix
        additionmatrix.append(row)
    # Returning the added list
    return additionmatrix

# Creating a sum function to find the sum of the even elements in a passed in matrix
def sumeven(parentmatrix):
    # Creating a sum counter
    sumeven = 0
    # Looping through the rows
    for i in range(len(parentmatrix)):
        # Looping through all of the columns/elements in the matrices
        for j in range(len(parentmatrix[0])):
            # Checking if the element of the matrix is even
            if parentmatrix[i][j] % 2 == 0:
                # Adding the value of the element to the counter if the condition is met
                sumeven += parentmatrix[i][j]
    # Returning the counter
    return sumeven

# Creating a subtraction matrix to find the difference of two matrices passed in
def subtraction(parentmatrix1, parentmatrix2):
    # Creating an empty list to return with the subtracted matrix
    subtractionmatrix = []
    # Checking if the rows and columns of each matrix are the same
    if len(parentmatrix1) != len(parentmatrix2) or len(parentmatrix1[0]) != len(parentmatrix2[0]):
        # Ending the function if the condition is passed
        return "Inconclusive"
    # Looping through the rows
    for i in range(len(parentmatrix1)):
        # Creating another list to hold the elements of the new rows
        row = []
        # Looping through all of the columns/elements in the matrices
        for j in range(len(parentmatrix1[0])):
            # Appending the added elements to the new row
            row.append(parentmatrix1[i][j] - parentmatrix2[i][j])
            # Appending these rows to the addition matrix
        subtractionmatrix.append(row)
    # Returning the subtracted list
    return subtractionmatrix

# Function to find the sum of odd elements from a passed in matrix
def sumodd(parentmatrix):
    # Creating a sum counter
    sumodd = 0
    # Looping through the rows
    for i in range(len(parentmatrix)):
        # Looping through all of the columns/elements in the matrices
        for j in range(len(parentmatrix[0])):
            # Checking if the element of the matrix is even
            if parentmatrix[i][j] % 2 != 0:
                # Adding the value of the element to the counter if the condition is met
                sumodd += parentmatrix[i][j]
    # Returning the counter
    return sumodd

# Test Cases
# (a)
A = randomM(0,10)
# (b)
B = transpose(A)
print("A: ", A)
print("B: ", B)
# (c)
print("AB: ", product(A, B))
# (d)
print("BA: ", product(B, A))
# (e)
A2 = randomM(0,10)
B2 = transpose(A2)
print("A2: ", A2)
print("B2: ", B2)
print("A2B2: ", product(A2, B2))
print("B2A2: ", product(B2, A2))
A3 = randomM(0,10)
B3 = transpose(A3)
print("A3: ", A3)
print("B3: ", B3)
print("A3B3: ", product(A3, B3))
print("B3A3: ", product(B3, A3))
# (g)
C = randomM(-10, 0)
print("C: ", C)
# (h)
AC = addition(A, C)
print("A + C: ", AC)
# (i)
print("Sum of Even in A + C: ", sumeven(AC))
# (j)
AC2 = subtraction(A, C)
print("A - C: ", AC2)
# (k)
print("Sum of Odd in A - C: ", sumodd(AC2))