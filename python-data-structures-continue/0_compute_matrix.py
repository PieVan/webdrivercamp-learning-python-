#!/usr/bin/python3

# was first version
# additional_matrix=[]
# def compute_matrix(matrix=[]):
#     for row in matrix:
#         new_row=[]
#         for element in row:
#             new_element= element ** 2
#             new_row.append(new_element)
#         additional_matrix.append(new_row)
#     return additional_matrix

def compute_matrix(matrix=[]):
    temporary_matrix=[[element**2 for element in row]for row in matrix]
    return temporary_matrix


if __name__=="__main__":
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
