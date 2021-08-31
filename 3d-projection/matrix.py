def matrix_multiplication(a, b):

    # Defining columns
    columns_a = len(a[0])
    columns_b = len(b[0])

    # Defining rows
    rows_a = len(a)
    rows_b = len(b)

    # Calculates the resulting matrix after the two have been multiplied
    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]

    if columns_a == rows_b:

        # Goes through each row of
        # a and each column of b
        for x in range(rows_a):
            for y in range(columns_b):

                sum = 0  # Define sum variable

                # For each column in a
                # update the sum variable
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]

                # Updates matrix by x, y vals
                result_matrix[x][y] = sum

        return result_matrix

    else:  # Error handling
        print("Error.")
        return None
