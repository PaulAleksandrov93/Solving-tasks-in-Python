

# row = int(input())
# col = int(input())

# a = row * col

# words = []
# matrix = []
# li = []

# for i in range(a):
#     word = input()
#     words.append(word)
# #print('words:', words)
# while words:
#     li = []
#     sl = words[:col]
#     matrix.append(sl)
#     del words[:col]
# #print(matrix)
# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j], end=' ')
#     print()

# matrix_t = np.transpose(matrix)
# # print('default:', matrix)
# #print('transpose:', matrix_t)

# for i in range(col):
#     for j in range(row):
#         print(matrix_t[i][j], end=' ')
#     print()


# n = int(input())

# matrix = []

# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)

# #print('matrix', matrix)
# elem = np.diagonal(matrix)
# #print('elem:', elem)
# res = sum(elem)
# print('res:', res)

# n = int(input())       

# matrix = []
# counter = []
# for i in range(n):
#     count = 0
#     s = input().split()
#     nums = [int(c) for c in s]
#     average = (sum(nums)) / n
#     for j in nums:
#         if j > average:
#             count += 1
#     counter.append(count)

# for i in counter:
#     print(i)     

# n = int(input())

# matrix = []
# diagonals = []
# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)
# # print('matrix', matrix)
# for i in range(n):
#     d = np.diagonal(matrix, offset=-i)
#     m = max(d)
#     diagonals.append(m)
#     res = max(diagonals)

# print(res)

# n = int(input())

# matrix = []
# diagonals = []
# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)
# # print('matrix', matrix)
# for i in range(n):
#     d = np.diagonal(matrix, offset=-i)
#     m = max(d)
#     diagonals.append(m)
#     res = max(diagonals)
# print(diagonals)
# print(res)




# n = int(input())

# matrix = []
# elem_l = []
# elem_r = []
# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)
# # print('matrix', matrix)
# for i in range(n):
#     for j in range(n):
#         if i >= j and i <= n - 1 - j:
#             elem_l.append(matrix[i][j])
#         if i <= j and i >= n - 1 - j:
#             elem_r.append(matrix[i][j])
            
    

# # print(elem_l)
# # print(elem_r)

# res = elem_r + elem_l
# print(max(res))
# #print(res)

# n = int(input())

# matrix = []
# elem_u = []
# elem_l = []
# elem_r = []
# elem_d = []

# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)
# #print('matrix', matrix)

# for i in range(n):
#     for j in range(n):
#         if i < j and i < n - 1 - j:
#             elem_u.append(matrix[i][j])
    
#         if i > j and i < n - 1 - j:
#             elem_l.append(matrix[i][j])
          
#         if i < j and i > n - 1 - j:
#             elem_r.append(matrix[i][j])
          
#         if i > j and i > n - 1 - j:
#             elem_d.append(matrix[i][j])

# # print('Верхняя четверь:', sum(elem_u))
# # print('Правая четверь:', sum(elem_r))
# # print('Нижняя четверь:', sum(elem_d))
# # print('Левая четверь:', sum(elem_l))

# print('Верхняя четверь: ' + str(sum(elem_u)))
# print('Правая четверь: ' + str(sum(elem_r)))
# print('Нижняя четверь: ' + str(sum(elem_d)))
# print('Левая четверь: ' + str(sum(elem_l)))
#--------------------------------------------------------
# n = int(input())
# m = int(input())


# for i in range(n):
#     mult = []
#     for j in range(m):
#         mult.append(str(i * j).ljust(3)) 

#     print(*mult)
#--------------------------------------------------------

# n = int(input())
# m = int(input())
# matrix = []
# nums = []
# res = []
# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)
    
# print('matrix', matrix)

       
# largest = np.amax(matrix)
# print(largest)
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == largest:
#             res.append(i)
#             res.append(j)
            
# res_s = [str(i) for i in res]    
# print(' '.join(res_s[:2]))

#---------------------------------------------------------------
# def print_matrix(matrix, r, n, width=1):
#     for r in range(r):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# row = int(input()) #количество строк
# col = int(input()) #количество столбцов
# matrix = []
# nums = []

# for i in range(row):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)
# ex = input().split()
# exchange = [int(c) for c in ex]
# e1 = exchange[0]
# e2 = exchange[1]

# for k in range(len(matrix)):
#     matrix[k][e1], matrix[k][e2] = matrix[k][e2], matrix[k][e1]  

# print_matrix(matrix, row, col)

#-----------------------------------------------------------------------------

# n = int(input())
# matrix = []
# l=[]
# r=[]

# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)

# for i in range(n):
#     a = np.diagonal(matrix, offset=-i)
#     a = a.tolist()
#     l.append(a)
# for i in range(n):
#     a = np.diagonal(matrix, offset=i)
#     a = a.tolist()
#     r.append(a)

# if l == r:
#     print('YES')
# else:
#     print('NO')

#-----------------------------------------------------------------------------
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
# n = int(input())
# matrix = []
# res = []

# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# for i in range(n):
#     for j in range(n):
#         matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
# print()
# print_matrix(matrix, n)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# k = np.flipud(matrix)
# for i in k:
#     i = i.tolist()
#     res.append(i)

# print_matrix(res, n)
#---------------------------------------------------------------------------------------------------

# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
# n = int(input())
# matrix = []
# res = []

# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)

# k = np.rot90(matrix, k = -1)

# for i in k:
#     i = i.tolist()
#     res.append(i)

# print_matrix(res, n)

#---------------------------------------------------------------------------------------------------
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# # n = int(input())
# matrix = []
# points = []
# res = []

# xy = input()
# y = '87654321'.index(xy[1])
# x = 'abcdefgh'.index(xy[0])


# for i in range(8):
#     #points.append()
#     matrix.append(['.']*8)

# # for i in range(8):
# #     for j in range(8):
# #         if i == x and j == y:
# matrix[x][y] = 'N'


# #print_matrix(matrix, 8)

# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if (x - i) ** 2 + (y - j) ** 2 == 5:
#             matrix[i][j] = '*'
# l = np.transpose(matrix)
# for c in l:
#     c.tolist()
#     res.append(c)
# print_matrix(res, 8)    

# #(x - i) ** 2 + (y - j) ** 2 == 5

#-----------------------------------------------------------------------------------

# import numpy as np

# n = int(input())
# matrix = []
# rows = []
# cols = []
# for i in range(n):
#     s = input().split()
#     nums = [int(c) for c in s]
#     matrix.append(nums)

# check = [i for i in range(1, n**2 + 1)]
# numbers = []
# for i in matrix:
#     for j in i:
#         numbers.append(j)
# # print('numbers:', numbers)
# # print('check:', check)    
# count_check = 0
# for i in numbers:
#     if i in check:
#         count_check += 1
#         check.remove(i)
# # print('check:', check)
# # print('count_check:', count_check)


# for row in range(n):
#     r = matrix[row]
#     rows.append(r)
# m = np.array(matrix)
# for col in range(n):
#     c = m[:,col]
#     cols.append(c)
# cols_res = [a.tolist() for a in cols]
# main_d = np.diagonal(matrix, offset=0)
# k = np.fliplr(matrix)
# side_d = np.diagonal(k)
# main = main_d.tolist()
# side = side_d.tolist()
# # print('rows:', rows)
# # print('cols_res:', cols_res)
# # print('main:', main)
# # print('side:',side)

# rows.append(main)
# cols_res.append(side)
# answers = []
# count_answ = 0
# res = rows + cols_res
# result = [sum(i) for i in res]
# # print(res)
# average = sum(result)/len(result)
# for i in range(len(result)):
#     if average == result[i]:
#         count_answ += 1 

# if len(result) == count_answ and count_check == n**2 and check == []:
#     print('YES')
# else:
#     print('NO')

#---------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# s = input().split()
# n = int(s[0])
# m = int(s[1])

# matrix = []

# for i in range(n):
#     matrix.append(['.']*m)
# #print_matrix(matrix, n, m)

# for i in range(n):
#     for j in range(m):
#         if i % 2 == 0 and j % 2 != 0:
#             matrix[i][j] = '*'
#         if i % 2 != 0 and j % 2 == 0:
#             matrix[i][j] = '*'
# print_matrix(matrix, n, m)

#----------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
# n = int(input())
# a = np.zeros((n, n), int)

# for i in range(n):
#     np.fill_diagonal(a[:,i:], 2)
# #np.fill_diagonal(np.fliplr(a), 1)
# np.flipud(a)
# np.fill_diagonal(a, 1)
# #print(np.flipud(a))
# k = np.flipud(a)
# res = k.tolist()
# print_matrix(res, n, n)

#----------------------------------------------------------------------------------------------------------

# def print_matrix(matrix, m, n, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# nums = input().split()
# n = int(nums[1])
# m = int(nums[0])
# mp = n * m

# a = np.arange(1, mp + 1)
# b = a.reshape((n, m))
# #print(b.transpose())
# c = b.transpose()
# result = c.tolist()
# #print(result)
# print_matrix(result, n, m, 3)

#------------------------------------------------------------------------------------------------------------

# def print_matrix(matrix, m, n, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# n = int(input())
# a = np.zeros((n, n), int)
# np.fill_diagonal(a, 1)
# b = np.fliplr(a)
# np.fill_diagonal(b, 1)
# res = b.tolist()
# print_matrix(res, n, n, 3)


#------------------------------------------------------------------------------------------------------------

# def print_matrix(matrix, m, n, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# n = int(input())
# a = np.zeros((n, n), int)

# b = a.tolist()

# for i in range(n):
#     for j in range(n):
#         if i <= j and i <= n - 1 - j:
#             b[i][j] = 1
#         if i >= j and i >= n - 1 - j:
#             b[i][j] = 1

# print_matrix(b, n, n, 3)

#-----------------------------------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# nums = input().split()

# n = int(nums[0])
# m = int(nums[1])
# a = np.zeros((n, m), int)
# matrix = a.tolist()

# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = (i + j) % m + 1

# print_matrix(matrix, n, m, 3)

#-----------------------------------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# nums = input().split()
# n = int(nums[0])
# m = int(nums[1])
# mp = n * m

# a = np.arange(1, mp + 1)
# b = a.reshape((n, m))

# matrix = b.tolist()

# for i in range(len(matrix)):
#     if i % 2 != 0:
#         matrix[i].reverse()
    
# print_matrix(matrix, n, m, 3)

#------------------------------------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# nums = input().split()
# n = int(nums[0])
# m = int(nums[1])
# mp = n * m

# a = np.arange(1, mp + 1)
# b = a.reshape((n, m))


# b = np.zeros((n,m), int) 
# num = 1       
# for j in range(m+n-1):
#     for i in range(n):
#         if j-i in range(m):
#             b[i][j-i] = num 
#             num += 1

# matrix = b.tolist()        
# print_matrix(matrix, n, m, 3)

#------------------------------------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# nums = input().split()
# n = int(nums[0])
# m = int(nums[1])
# b = np.zeros((n,m), int)
# matrix = b.tolist() 
# count = 1
# count_1 = 1
# i, j = 0, 0

# matrix[i][j] = str(count)
# while True: 
#     while j < m - count_1:
#         j += 1
#         count += 1
#         matrix[i][j] = str(count)
#         if count == m * n:
#             break
#     while i < n - count_1:
#         if count == m * n:
#             break
#         i += 1
#         count += 1
#         matrix[i][j] = str(count)
        
#     while j > count_1 - 1: 
#         if count == m * n:
#             break
#         j -= 1 
#         count += 1  
#         matrix[i][j] = str(count)
        
#     while i > count_1: 
#         if count == m * n:
#             break  
#         i -= 1 
#         count += 1  
#         matrix[i][j] = str(count)
             
    
#     if count == m * n:
#         break   
#     count_1 += 1
# print_matrix(matrix, n, m, 3)

#------------------------------------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# nums = input().split()
# n = int(nums[0])
# m = int(nums[1])


# matrix_1 = []
# matrix_2 = []
# #res = []
# res_matrix = []
# for i in range(n):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix_1.append(elem)
# input()
# for i in range(n):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix_2.append(elem)

# for i in range(n):
#     res = []
#     for j in range(m):
#         r = matrix_1[i][j] + matrix_2[i][j]
#         res.append(r)
#     res_matrix.append(res)
# print()
# print_matrix(res_matrix, n, m)

#--------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# nums = input().split()
# n = int(nums[0])
# m = int(nums[1])

# matrix_1 = []
# matrix_2 = []


# for i in range(n):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix_1.append(elem)
# input()
# nums_1 = input().split()
# m = int(nums_1[0])
# k = int(nums_1[1])

# for i in range(m):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix_2.append(elem)


# arr_1 = np.array(matrix_1) 
# arr_2 = np.array(matrix_2)

# res_arr = np.dot(arr_1, arr_2)
# res_matrix = res_arr.tolist()


# print_matrix(res_matrix, n, m)

#--------------------------------------------------------------------------------

# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# n = int(input())

# matrix = []
# for i in range(n):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix.append(elem)

# m = int(input())

# arr = np.array(matrix)

# arr_1 = np.linalg.matrix_power(arr, m)

# res = arr_1.tolist()
# print_matrix(res, n, n)

#---------------------------------------------------------------------------------
#Экзамен по вложеным спискам

# #1
# s = input().split()
# n = int(input())
# result = []

# for i in range(n):
#     result.append(s[i::n])

# print(result)

#2
# n = int(input())
# matrix = []
# res = []
# result = list()
# for i in range(n):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix.append(elem)

# a = np.array(matrix)

# for i in range(n):
#     d = np.diagonal(np.fliplr(a), offset=-i)
#     diag = d.tolist()
#     res.append(diag)
# for i in range(n):
#     mx = max(res[i])
#     result.append(mx)
# ans = max(result)
# print(ans)
#3
# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# n = int(input())
# matrix = []
# res = []
# result = list()
# for i in range(n):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix.append(elem)

# a = np.array(matrix)
# t = np.transpose(a)
# result = t.tolist()
# print_matrix(result, n, n)
#4
# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# n = int(input())

# matrix = []
# res = []
# d = n // 2 
# for i in range(n):
#     matrix.append(['.'] * n)
# a = np.array(matrix)
# np.fill_diagonal(a, '*')
# np.fill_diagonal(np.fliplr(a), '*')
# res = (a).tolist()
# for i in range(n):
#     for j in range(n):
#         if i == d:
#             res[i][j] = '*'
#         if j == d:
#             res[i][j] = '*'

# print_matrix(res, n, n)

#------------------------------------------------------------------------------
#5

# n = int(input())
# matrix = []
# res = []
# res_1 = []
# result = list()
# for i in range(n):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix.append(elem)

# a = np.array(matrix)

# for i in range(n):
#     d = np.diagonal(np.fliplr(a), offset=-i)
#     d_1 = np.diagonal(np.fliplr(a), offset=i)
#     diag = d.tolist()
#     diag_1 = d_1.tolist()
#     res.append(diag)
#     res_1.append(diag_1)
# res_count = 0
# for i in range(n):
#     if sum(res[i]) == sum(res_1[i]):
#         res_count += 1
# if res_count == n:
#     print('YES')
# else:
#     print('NO')

#-----------------------------------------------------------------------------

# import numpy as np
# #6
# n = int(input())
# matrix = []
# res = []
# res_1 = []
# result = list()
# for i in range(n):
#     el = input().split()
#     elem = [int(c) for c in el]
#     matrix.append(elem)


# count_r = 0
# count_c = 0
# a = np.array(matrix)

# for i in range(n):
#     c = a[:, i]
#     check = [i+1 for i in range(n)] 
#     for j in range(n):
#         if c[j] not in check:
#             break
#         if c[j] in check:
#             count_c += 1
#             check.remove(c[j])
      
# for i in range(n):
#     r = a[i, :]
#     check = [i+1 for i in range(n)] 
#     for j in range(n):
#         if r[j] not in check:
#             break
#         if r[j] in check:
#             count_r += 1
#             check.remove(r[j])
       
# res_count = count_r + count_c

# if res_count == n**2*2:
#     print('YES')
# else:
#     print('NO')

#-------------------------------------------------------

#7
# import numpy as np

# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# # n = int(input())
# matrix = []
# points = []
# res = []

# xy = input()
# y = '87654321'.index(xy[1])
# x = 'abcdefgh'.index(xy[0])


# for i in range(8):
#     matrix.append(['.']*8)


# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if i == y or j == x or abs(y - i) == abs(x - j):
#             matrix[i][j] = '*'

# matrix[y][x] = 'Q'
# print_matrix(matrix, 8)

#(x - i) ** 2 + (y - j) ** 2 == 5 - для коня
#i == y or j == x or abs(y - i) == abs(x - j) - для ферзя

#------------------------------------------------------------------------------
#8
# import numpy as np


# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# size = int(input())

# a = np.zeros((size,size), dtype=np.int16)
# for k in range(size):
#     x = np.arange(0,size-k)
#     y = x + k
#     a[x,y] = k

# for k in range(size):
#     x = np.arange(0,size-k)
#     y = x + k
#     a[y,x] = k

# matrix = a.tolist()    
# print_matrix(matrix, size)

#----------------------------------------------------------------------

#кортежи

# poets = [
#     ('Есенин', 13),
#     ('Тургенев', 14),
#     ('Маяковский', 28),
#     ('Лермонтов', 20),
#     ('Фет', 15)]

# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i][1] > poets[j][1]:
#             poets[i], poets[j] = poets[j], poets[i]

# print(poets[0])
# print(poets[-1])

# n = int(input())
# students = []
# res = []
# for i in range(n):
#     student = input().split()
#     std = tuple(student)
#     students.append(std)
# for i in range(len(students)):
#     if students[i][1] == '4' or students[i][1] == '5':
#         res.append(students[i])
# for i in students:
#     print(*i)
# print()
# for i in res:
#     print(*i)

# n = int(input())
# t1, t2, t3 = 1, 1, 1

# for i in range(n):
#     print(t1, end=' ')
    
#     t1, t2, t3 = t2, t3, t1+t2+t3

# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
# #     f1, f2 = f2, f1 + f2
# import math
# g = int(input())
# k1 = int(input())

# k2 = g**2 - k1**2
# print(math.sqrt(k2))
# check = '.,;:-?!'
# s = input()
# s1 = ''
# for c in s:
#     if c in check:
#         c = ''
#     s1 += c
# lst = s1.split()
# lst1 = [word.lower() for word in lst]
# print('lst', lst1)
# result = set(lst1)
# print(len(result))

# nums = input().split()
# numbers = [int(c) for c in nums]
# st = set()
# for num in numbers:
#     if num in st:
#         print('YES')
#     else:
#         print('NO')
#         st.add(num)        

# set1 = {'a', 'b', 'c', 'd', 'h'}
# set2 = {'b', 'd', 'f', 'h'}

# set3 = set1 - set2 & set1
# print(set3)

# nums1 = input().split()
# nums2 = input().split()

# numbers1 = [int(c) for c in nums1]
# numbers2 = [int(c) for c in nums2]

# set1 = set(numbers1)
# set2 = set(numbers2)
# set3 = set1.intersection(set2)
# res = sorted(set3)
# print(*res)

# nums1 = input().split()
# nums2 = input().split()

# numbers1 = [int(c) for c in nums1]
# numbers2 = [int(c) for c in nums2]

# set1 = set(numbers1)
# set2 = set(numbers2)
# set1.difference_update(set2)
# res = sorted(set1)
# print(*res)

# n = int(input())
# number = input()
# myset = set(number)
# for i in range(1, n):
#     num = input()
#     myset &= set(num)
# res = sorted(myset)
# result = [int(c) for c in  res]
# print(*result)

# num1 = input()
# num2 = input()
# n1 = set(num1)
# n2 = set(num2)

# res = n2.issubset(n1)
# if res:
#     print('YES')
# else:
#     print('NO')

# n1 = input().split()
# n2 = input().split()
# n3 = input().split()
# st1 = set(n1)
# st2 = set(n2)
# st3 = set(n3)
# res = st1.intersection(st2)
# res.difference_update(st3)
# result = sorted(res, reverse=True)
# result1 = [int(c) for c in result]
# result1.sort(reverse=True)

# print(*result1)

# n1 = input().split()
# n2 = input().split()
# n3 = input().split()
# st1 = set(n1)
# st2 = set(n2)
# st3 = set(n3)
# res = st1.intersection(st2, st3)
# u = st1.union(st2, st3)

# result = u.difference(res)
# result1 = [int(c) for c in result]
# result1.sort()
# print(*result1)

# n1 = input().split()
# n2 = input().split()
# n3 = input().split()
# st1 = set(n1)
# st2 = set(n2)
# st3 = set(n3)

# u = st1.union(st2)
# res = st3.difference(u)
# result = res.difference(u)
# result1 = [int(c) for c in result]
# result1.sort(reverse=True)
# print(*result1)

# n1 = input().split()
# n2 = input().split()
# n3 = input().split()
# st1 = set(n1)
# st2 = set(n2)
# st3 = set(n3)
# check = [str(i) for i in range(11)]
# checkst = set(check)
# u = st1.union(st2, st3)
# res = checkst.difference(u)
# result = res.difference(u)
# result1 = [int(c) for c in result]
# result1.sort()
# print(*result1)

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# myset = {int(i) for i in items }
# print(*sorted(myset))

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# myset = {w[0].lower() for w in words}
# print(*sorted(myset))

# sentence = 'My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'
# sent = ''
# check = '.,;:-?!()'
# for c in sentence:
#     if c in check:
#         c = ''
#         sent += c
#     sent += c
# lst = sent.split()
# myset = {w.lower() for w in lst if w not in check}
# print(*sorted(myset))

# sentence = 'My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'
# sent = ''
# check = '.,;:-?!()'
# for c in sentence:
#     if c in check:
#         c = ''
#         sent += c
#     sent += c
# lst = sent.split()
# myset = {w.lower() for w in lst if len(w) < 4}
# print(*sorted(myset))

# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# files1 = [w.lower() for w in files]
# check = '.png'
# myset = {f.lower() for f in files1 if check in f}
# print(*sorted(myset))

# set1 = {'p', 'a', 't', 'f'}
# set2 = {'a', 't', 'f'}

# print(set1 - set2)

# s = input().split()
# myset = {int(c) for c in s}
# res = len(s) - len(myset)
# print(res)

# n = int(input())
# cities = set()
# for i in range(n):
#     city = input()
#     cities.add(city)
# last = input()
# if last in cities:
#     print('REPEAT')
# else:
#     print('OK')

# m = int(input()) # library
# n = int(input()) # list of books
# mylib = [input() for j in range(m)]
# # mylist = {input() for i in range(n)}

# res = []
# for i in range(n):
#     if input() in mylib:
#         res.append('YES')
#     else:
#         res.append('NO')
# print(*res, sep='\n')

# s1 = input().split()
# s2 = input().split()

# st1 = {int(n) for n in s1}
# st2 = {int(n) for n in s2}

# if st1.isdisjoint(st2):
#     print('BAD DAY')
# else:
#     res = st1.intersection(st2)
#     print(*sorted(res, reverse=True))

# s1 = input().split()
# s2 = input().split()

# st1 = {int(n) for n in s1}
# st2 = {int(n) for n in s2}

# if st1.issubset(st2):
#     print('YES')
# else:
#     print('NO')

# m = int(input()) # изучают математику
# n = int(input()) # изучают информатику

# mat = {input() for w in range(m)}
# inf = {input() for b in range(n)}

# res = mat - inf
# print(len(res))

# m = int(input()) # изучают математику
# n = int(input()) # изучают информатику

# res = m - n

# if res == 0:
#     print('NO')
# else:
#     print(abs(res))

# myset1 = set(input().split())
# myset2 = set(input().split())
# res = myset1.union(myset2)
# print(*sorted(res))

# m = int(input())  # math
# n = int(input())  # info
# math = {input() for i in range(m)}
# info = {input() for j in range(n)}
# res = math.symmetric_difference(info)
# if math == info:
#     print('NO')
# else:
#     print(len(res))
#-----------------------------
# m = int(input())  # math
# n = int(input())  # info
# math = [input() for i in range(m)]
# info = [input() for j in range(n)]

# set_math = set(math)
# set_info = set(info)

# res = set_math.symmetric_difference(set_info)

# if set_math == set_info:
#     print('NO')
# else:
#     print(len(res))
#-----------------------------

# m = int(input())  # math
# n = int(input())  # info
# math = [input() for i in range(m)]
# info = [input() for j in range(n)]

# set_math = set(math)
# set_info = set(info)


# if set_math == set_info:
#     print('NO')
# else:
#     for i in math:
#         if math.count(i) > 1:
#             set_info.add(i)
#     res = set_math.symmetric_difference(set_info)
#     print(len(res))


# y_stud = []
# m = int(input())  
# ni = int(input())  
# f1 = {input() for i in range(ni)}  
# for i in range(m - 1):
#     ni = int(input())  
#     f = {input() for i in range(ni)}  
#     y_stud.append(f)
# for i in y_stud:
#     f1.intersection_update(i)   
# print(*sorted(f1), sep='\n')


#DICTIONARIES=====================================================================================
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# res = []
# for i in users:
#     p = i['phone']
#     if p[-1] == '8':
#         res.append(i['name'])
# res.sort()
# print(*res, sep=' ')


# res = []
# for i in users:
#     if 'email' not in i:
#         res.append(i['name'])
#     elif 'email' in i:
#         for k, v in i.items():
#             if k == 'email' and v == '':
#                 res.append(i['name'])

# res.sort()
# print(*res, sep=' ')

#=================================================================================
# nums = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
#         '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
# n = input()
# res = []

# for c in n:
#     d = nums[c]
#     res.append(d)
# print(*res, sep=' ')
#=================================================================================

# courses = {'CS101': ['3004', 'Хайнс', '8:00'],
#            'CS102': ['4501', 'Альварадо', '9:00'],
#            'CS103': ['6755', 'Рич', '10:00'],
#            'NT110': ['4501', 'Альварадо', '9:00'],
#            'CM241': ['1411', 'Ли', '13:00']}
# s = input()
# print(f'{s}' + ': ' + f'{courses[s][0]}' + ', ' + f'{courses[s][1]}' + ', ' + f'{courses[s][2]}')


#=================================================================================
# buttons = {'.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
#            'A': '2', 'B': '22', 'C': '222',
#            'D': '3', 'E': '33', 'F': '333',
#            'G': '4', 'H': '44', 'I': '444',
#            'J': '5', 'K': '55', 'L': '555',
#            'M': '6', 'N': '66', 'O': '666',
#            'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
#            'T': '8', 'U': '88', 'V': '888',
#            'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
#            ' ': '0'}
# s = input().upper()

# for c in s:
#     if c in buttons:
#         print(buttons[c], end='')
#=================================================================================

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

# s = input().upper()
# info = dict(zip(letters, morse))
# for c in s:
#     if c in info:
#         print(info[c], end=' ')

#=================================================================================

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

# result = {}

# for k in dict1:
#     if k in dict2:
#         if dict1.get(k) != dict2.get(k):
#             result[k] = dict1.get(k) + dict2.get(k)
#         elif dict1.get(k) == dict2.get(k):
#             result[k] = dict1.get(k) + dict2.get(k)
#     else:
#         result[k] = dict1.get(k)

# for k in dict2:
#     if k not in result:
#         result[k] = dict2.get(k)     

# print(result)

#=================================================================================

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

# result = {}

# for c in text:
#     result[c] = text.count(c)

# print(result)

#=================================================================================

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# lst = s.split()

# result = {}

# values = []
# keys = []
# for w in lst:
#     result[w] = s.count(w)

# for v in result.values():
#     values.append(v)
# max_v = max(values)

# for k, v in result.items():
#     if v == max_v:
#         keys.append(k)

# # print(result)
# print(min(keys))

#===========================================================================

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]

# result = {}

# for i in range(len(pets)):
#     result[pets[i][1:]] = []

# for k, v in result.items():
#     for p in pets:
#         if k[1] == p[2]:
#             v.append(p[0])

# print(result)  

#===========================================================================

# check = '.,!?:;-'
# s = input()
# p = ''
# result = {}
# values = []
# keys = []
# for c in s:
#     if c in check:
#         c = ''
#         p += c
#     p += c
# lst = p.lower().split()
# # print(lst)

# for w in lst:
#     result[w] = lst.count(w)
# # print(result)


# for v in result.values():
#     values.append(v)

# min_v = min(values)

# for k, v in result.items():
#     if v == min_v:
#         keys.append(k)

# print(min(keys))

#==========================================================================

# s = input().split()
# result = {}
# res = []
# keys = []
# for c in s:
#     if c not in result:
#         res.append(c)
#         result[c] = ''
#     elif c in result:
#         res.append(c)
#         result[c + '_' + str(res.count(c) - 1)] = ''

# for k in result.keys():
#     keys.append(k)
# print(*keys)

#==========================================================================

# n = int(input())
# values = []
# keys = []
# result = []
# for i in range(n):
#     value = ''
#     key = ''
#     s = input()
#     for c in s:
#         if c == ':':
#             break
#         key += c
#     keys.append(key.lower())
#     for i in range(len(s)):
#         if s[i] == ' ':
#             value = s[i + 1:]
#             break
#     values.append(value)
# # print(keys)
# # print(values)
# base = dict(zip(keys, values))
# # print(base)
# m = int(input())
# for j in range(m):
#     s1 = input().lower()
#     if s1 not in list(base.keys()):
#         nf = 'Не найдено'
#         result.append(nf)
#         continue
#     res = base[s1]
#     result.append(res)
    
# print(*result, sep='\n')
# for i in range(8):
#     s1 = input().lower()
#     s2 = input().lower()
#     n1 = 0
#     n2 = 0
#     check = '.,!?:;- '
#     s1_f = ''
#     s2_f = ''

#     for c in s1:
#         if c in check:
#             c = ''
#             s1_f += c
#         s1_f += c  
#     for c in s2:
#         if c in check:
#             c = ''
#             s2_f += c
#         s2_f += c       

#     if len(s1_f) == len(s2_f):
#         for i in range(len(s1_f)):
#             n1 += ord(s1_f[i])
#             n2 += ord(s2_f[i])
#         if n1 == n2:
#             print('YES')
#         else:
#             print('NO')
#     else:
#         print('NO')
# # print(n1, n2)

#==========================================================================

# n = int(input())
# keys = []
# values = []
# for i in range(n):
#     s = input().split()
#     keys.append(s[0])
#     values.append(s[1])
# base = dict(zip(keys, values))

# q = input()

# for k, v in base.items():
#     if k == q:
#         print(v)
#         break
#     if v == q:
#         print(k)
#         break

#=========================================================================

# n = int(input())
# keys = []
# values = []
# countries = []
# for i in range(n):
#     s = input().split()
#     keys.append(s[0])
#     values.append(s[1:])
# base = dict(zip(keys, values))
# m = int(input())
# for i in range(m):
#     s = input()
#     for k, v in base.items():
#         if s in v:
#             countries.append(k)
# print(*countries, sep='\n')

#===========================================================================

# n = int(input())
# contacts = {}
# result = []
# for i in range(n):
#     contact = input().lower().split()
#     if contact[1] not in contacts:
#         contacts[contact[1]] = [contact[0]]
#     else:
#         for k, v in contacts.items():
#             if k == contact[1]:
#                 v.append(contact[0])

# m = int(input())
# for i in range(m):
#     name = input().lower()
#     if name not in contacts:
#         result.append('абонент не найден')
#     if name in contacts:
#         phones = contacts[name]
#         result.append(phones)

# for i in range(len(result)):
#     if result[i] == 'абонент не найден':
#         print(result[i])
#     else:
#         print(' '.join(result[i]))

#==========================================================================================

# s = input()
# keys = []
# values = []
# # nums = []
# # result = []
# n = int(input())
# for i in range(n):
#     l = input()
#     keys.append(l[0])
#     values.append(int(l[3]))
# base = dict(zip(values, keys))

# # for c in s:
# #     count = s.count(c)
# #     nums.append(count)
# nums = [s.count(c) for c in s]
# # for i in range(len(nums)):
# #     res = base[nums[i]]
# #     result.append(res)
# result = [base[nums[i]] for i in range(len(nums))]
# print(''.join(result))

#=================================================================

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]

# result = {numbers.index(n): n**2 for n in numbers}
# result1 = {i: numbers[i]**2 for i in range(len(numbers))}
# print(result)
# print(result1)
#=======================================================================================

# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}

# result = {k: v for k, v in colors.items() if v != None}
# print(result)

#=======================================================================================

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# result = {k: v for k, v in favorite_numbers.items() if len(str(v)) == 2}
# print(result)
    
#=======================================================================================

# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

# result = {v: k for k, v in months.items()}
# print(result)

#=======================================================================================

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# result = {int(k.split(':')[0]): k.split(':')[1] for k in s.split()}
# print(result)

#==========================================================================================

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

# result = {k: [v for v in range(1, k + 1) if k % v == 0] for k in numbers }

# print(result)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

# result = {k: [ord(v) for v in k] for k in words}

# print(result)

#==============================================================================================

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]

# result = {k[0]: k[1:] for k in tuples}

# print(result)

#=============================================================================================

# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013'] 
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'] 
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

# result = [{k: {k1: v}} for k, k1, v in zip(student_ids, student_names, student_grades)]
# print(result)

#================================================================================================================

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

# for v in my_dict.values():
#     r = []
#     for i in v:
#         if i > 20:
#             r.append(i)    
#     for i in r:
#         if i in v:
#             v.remove(i)
# print(my_dict)

#===============================================================================================================

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# result = []
# for k, v in emails.items():
#     for i in range(len(v)):
#         result.append(v[i] + '@' + k)
# print(*sorted(result), sep='\n')

#==============================================================================================================

# s = input()

# base = {'G': 'C', 'C': 'G', 'T': 'A','A': 'U'}
# result = []
# for c in s:
#     result.append(base[c])
# print(''.join(result))

#==============================================================================================================

# s = input().split()
# res = []
# for w in range(len(s)):
#     r = s[:w+1].count(s[w]) 
#     res.append(r)
# print(*res)

#====================================================================================================

# s = input()
# res = 0
# base = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'D': 2, 'G': 2,
#         'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
#         'Q': 10, 'Z': 10} 
# for c in s:
#     d = base[c]
#     res += d
# print(res)

#========================================================================================================

# def build_query_string(dict):
#     result = []
#     for k, v in dict.items():
#         res = []
#         res.append(str(k))
#         res.append(str(v))
#         r = '='.join(res)
#         result.append(r)
#         result.sort()
#     a = '&'.join(result)
#     return a

# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))

#======================================================================================================

# def merge(values):      # values - это список словарей
#     result = {}
#     for d in values:
#         for k in d.keys():
#             result[k] = set()

#     for k, v in result.items():
#         for d in values:
#             for key, val in d.items():
#                 if k == key:
#                     v.add(val)
#     return result
            
# res = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])           
# print(res)        

#=====================================================================

# commands_base = {'write': 'W', 'read': 'R' , 'execute': 'X'}

# f = {}
# n = int(input())
# for w in range(n):
#     s = input().split()
#     f[s[0]] = s[1:]
# m = int(input())

# result = []

# for w in range(m):
#     g = {} 
#     s = input().split()
#     g[s[1]] = s[0] 
#     for k, v in g.items():
#         for key, val in f.items():
#             if k == key:
#                 if commands_base[v] in val:
#                     result.append('OK')
#                 else:
#                     result.append('Access denied')

# print(*result, sep='\n')

#==========================================================

# cart = {}
# buys = []
# n = int(input())
# for i in range(n):
#     s = input().split()
#     cart[s[0]] = []
#     buys.append(s)
# for b in range(len(buys)):
#     for k, v in cart.items():
#         name = buys[b][0]
#         if name == k and v == []:
#             v.append([buys[b][1], int(buys[b][2])])
#         elif name == k and v != []:
#             flag = False
#             for d in range(len(v)):
#                 if buys[b][1] == v[d][0]:
#                     v[d][1] += int(buys[b][2])
#                     flag =True
#                     break
#             if flag == False:
#                 v.append([buys[b][1], int(buys[b][2])])
#                 break
# for v in cart.values():
#     for i in v:
#         for d in range(len(i)):
#             i[d] = str(i[d])
# print(cart)
# for k,v in sorted(cart.items()):
#     print(k + ':')
#     for p in sorted(v):
#         print(' '.join(p))
    
#=======================================================

# import random

# n = int(input())    # количество попыток

# for i in range(n):
#     res = random.randint(0, 1)
#     if res == 1:
#         print('Орел')
#     else:
#         print('Решка')

#=========================================================

# import random

# n = int(input())
# password = ''
# for i in range(n):
#     choice = random.randint(0, 1)
#     if choice == 0:
#         c = random.randint(65, 90)
#         password += chr(c)
#     else:
#         c = random.randint(97, 122)
#         password += chr(c)

# print(password)

#=======================================================

# import random
# nums = {random.randint(1, 49) for _ in range(7)}
# print(*nums, sep=' ')

#======================================================

# import random

# def generate_ip():
#     ip = []
#     for i in range(4):
#         if i != 2:
#             num = random.randint(0, 255)
#             ip.append(str(num))
#         else:
#             num = random.randint(0, 9)
#             ip.append(str(num))
#     result = '.'.join(ip)
#     return result

# print(generate_ip())

#========================================================

# import random
# import string
# def generate_index():
#     index = []
#     for i in range(2):
#         s = ''
#         for j in range(2):
#             let = random.choice(string.ascii_uppercase)
#             s += let
#         num1 = random.randint(0, 99)
#         s += str(num1)
#         if i == 0:
#             index.append(s)
#         else:
#             index.append(s[::-1])
#     result = '_'.join(index)
#     return result
# print(generate_index())

#==========================================================

# import random

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]

# for l in matrix:
#     l = random.shuffle(l)

# print(matrix)
    
#=======================================================
# import random

# for i in range(100):
#     print(random.randint(1000000, 9999999))

#=========================================================

# import random
# s = input()
# sl = [c for c in s]
# random.shuffle(sl)
# print(''.join(sl))

#========================================================

# import random


# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# matrix = []
# base = []

# while True:
#     r = random.randint(1, 75)
#     if r not in base:
#         base.append(r)    
#     if len(base) == 75:
#         break

# for i in range(5):
#     nums = random.sample(base, 5)
#     matrix.append(nums)
#     for num in nums:
#         if num in base:
#             base.remove(num)
# matrix[2][2] = 0

# print_matrix(matrix, 5, 5, 3)

#=================================================================================
# import random

# n = int(input())
# out = []
# base = []

# for i in range(n):
#     name = input()
#     out.append([name])
#     base.append(name)

# for n in out:
#     for m in base:
#         r = random.choice(base)
#         if r != n[0]:
#             n.append(r)
#             base.remove(r)
#             break

# for n in out:
#     print(' - '.join(n))

#===================================================================================
# import random
# import string

# n = int(input())
# m = int(input())
# check = 'lI1oO0'
# for i in range(n):
#     password = ''
#     count = 0
#     while True:
#         count += 1
#         base = [1, 2, 3]
#         ch = random.choice(base)
#         if ch == 1:
#             l = random.choice(string.ascii_lowercase)
#             if l not in check:
#                 password += l
#             else:
#                 count -= 1
#                 continue
#         elif ch == 2:
#             l1 = random.choice(string.ascii_uppercase)
#             if l1 not in check:
#                 password += l1
#             else:
#                 count -= 1
#                 continue
#         else:
#             l2 = random.randint(0, 9)
#             if str(l2) not in check:
#                 password += str(l2)
#             else:
#                 count -= 1
#                 continue
#         if count == m:
#             break
#     print(password)
#================================================================================
# import random
# import string

# def generate_password(length):
#     check = 'lI1oO0'
#     password = ''
#     count = 0
#     while True:
#         count += 1
#         base = [1, 2, 3]
#         ch = random.choice(base)
#         if ch == 1:
#             l = random.choice(string.ascii_lowercase)
#             if l not in check:
#                 password += l
#             else:
#                 count -= 1
#                 continue
#         elif ch == 2:
#             l1 = random.choice(string.ascii_uppercase)
#             if l1 not in check:
#                 password += l1
#             else:
#                 count -= 1
#                 continue
#         else:
#             l2 = random.randint(0, 9)
#             if str(l2) not in check:
#                 password += str(l2)
#             else:
#                 count -= 1
#                 continue
#         if count == length:
#             break
#     return password


# def generate_passwords(count, length):
#     passwords = [generate_password(length) for _ in range(count)]
#     return print(*passwords, sep='\n')
    
        
# n, m = int(input()), int(input())
# generate_passwords(n, m)
#===================================================================================
# import random
# import string

# def generate_password(length):
#     check = 'lI1oO0'
#     password = ''
#     count = 0
#     while True:
#         count += 1
#         base = [1, 2, 3]
#         ch = random.choice(base)
#         if ch == 1:
#             l = random.choice(string.ascii_lowercase)
#             if l not in check:
#                 password += l
#             else:
#                 count -= 1
#                 continue
#         elif ch == 2:
#             l1 = random.choice(string.ascii_uppercase)
#             if l1 not in check:
#                 password += l1
#             else:
#                 count -= 1
#                 continue
#         else:
#             l2 = random.randint(0, 9)
#             if str(l2) not in check:
#                 password += str(l2)
#             else:
#                 count -= 1
#                 continue
#         if len(password) == length:
#             cnt = ''
#             for c in password:
#                 if 'a' in cnt and 'A' in cnt and 'n' in cnt:
#                     break
#                 if c in string.ascii_lowercase:
#                     cnt += 'a'
#                     continue
#                 elif c in string.ascii_uppercase:
#                     cnt += 'A'
#                     continue
#                 elif c in '1234567890':
#                     cnt += 'n'
#                     continue
                
#             if 'a' in cnt and 'A' in cnt and 'n' in cnt:
#                 break
#             else:
#                 password = ''
#                 continue
#     return password


# def generate_passwords(count, length):
#     passwords = [generate_password(length) for _ in range(count)]
#     return print(*passwords, sep='\n')
    
        
# n, m = int(input()), int(input())
# generate_passwords(n, m)
#==================================================================================

# def matrix(n=1, m=0, value=0):
#     matrix = []
#     if m == 0:
#         for i in range(n):
#             r = [value] * n 
#             matrix.append(r)
#         return matrix
#     for i in range(n):
#         r = [value] * m 
#         matrix.append(r)
#     return matrix
# print(matrix(3, 1))

#=====================================================================================

# def count_args(*args):
#     return len(args)
# print(count_args(10))

#=====================================================================================

# def sq_sum(*args):
#     return sum(arg**2 for arg in args)
# print(sq_sum(1.5, 2.5))

#=====================================================================================

# def mean(*args):
#     nums = [arg for arg in args if type(arg) == int or type(arg) == float]
#     if len(nums) != 0:
#         return sum(nums)/len(nums)
#     else:
#         return float(len(nums))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#====================================================================================

# def greet(name, *args):
#     if len(args) == 0:
#         return f'Hello, {name}!'
#     else:
#         return f'Hello, {name} and ' + ' and '.join(args) + '!'
    
# print(greet('Roma', 'Timur'))

#=====================================================================================

# def print_products(*args):
#     fruits = [arg for arg in args if type(arg) == str] 
#     count = 0
#     for i in range(len(fruits)):
#         if fruits[i] != '' and len(fruits) > 1:
#             count += 1
#             print(f'{count}) {fruits[i]}')
#         elif fruits[i] == '' and len(fruits) == 1:
#             print('Нет продуктов')

# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '') 

#=====================================================================================

# def info_kwargs(**kwargs):
    
#     for k, v in sorted(kwargs.items()):
#         print(f'{k}: {v}', sep='\n')


# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 
#================================================================================

# s1 = 'python'
# s2 = 'stepicon'
# s3 = 'beegeek'
 
# print(min(s1, s2, s3))
# print(max(s1, s2, s3))

#====================================================================================

# def comparator(pair):
#     return pair[1]


# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator)
# print(pairs)

#===================================================================================

# def comparator(pair):
#     return pair[0] + pair[1]


# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator, reverse=True)
# print(pairs)

#===================================================================================

# def average(arg):
#     return sum(arg)/len(arg)
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

# print(min(numbers, key=average))
# print(max(numbers, key=average))

#====================================================================================
# import math
# def distance(arg):
#     return math.sqrt(arg[0]**2 + arg[1]**2)
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# print(sorted(points, key=distance))
#
#====================================================================================

# def summary(arg):
#     return min(arg) + max(arg)
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

# print(sorted(numbers, key=summary))

#====================================================================================
# def names(arg):
#     return arg[0]
# def ages(arg):
#     return arg[1]
# def heights(arg):
#     return arg[2]
# def weights(arg):
#     return arg[3]

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

# functions = {1: names, 2: ages, 3: heights, 4: weights}

# n = int(input())

# result = sorted(athletes, key=functions[n])
# for w in result:
#     print(*w)

#================================================================================
# import math

# def square(arg):
#     return arg**2
# def cube(arg):
#     return arg**3
# def sqrt(arg):
#     return math.sqrt(arg)
# def absolute(arg):
#     return abs(arg)
# def sinus(arg):
#     math.radians(arg)
#     return math.sin(arg)


# functions = {'квадрат': square, 'куб': cube, 'корень': sqrt, 'модуль': absolute, 'синус': sinus}

# n = int(input())

# s = input()

# print(functions[s](n))
#=================================================================================
# def func(arg):
#     sorted_nums = dict(sorted(arg.items(), key=lambda item: item[1]))
#     ret = [k for k in sorted_nums.keys()]
#     return ret
      

# nums  = [int(c) for c in input().split()]
# nums.sort()
# sum_of_digits = {}
# for i in nums:
#     num = []
#     j = i
#     while j > 0:
#         last_digit = j % 10
#         num.append(last_digit)
#         j = j // 10
#     r = sum(num)
#     sum_of_digits[i] = r

# print(*func(sum_of_digits))

#==================================================================================
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def func(arg):
#     return round(arg, 2)

# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# res = map(func, numbers)
# print(*res, sep='\n')

#==================================================================================

# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc

# def square(arg):
#     return arg**2
# def summary(x, y):
#     return x + y

# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

# res_reduce = reduce(summary, map(square, numbers), 0)
# print(f'res_reduce: {res_reduce}')
# sum_map = sum(map(square, numbers))
# print(f'sum_map: {sum_map}')

#==================================================================================


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# def predicate(arg):
#     if len(str(arg)) == 2:
#         if arg % 7 == 0:
#             return True


# def square(arg):
#     return arg**2


# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

# res = sum(map(square, filter(predicate, numbers)))
# print(res)

#=======================================================================================

# def func_apply(function, arg_list):
#     res = map(function, arg_list)
#     return list(res)


# def add3(x):
#     return x + 3


# def mul7(x):
#     return x * 7


# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

#======================================================================================

# iterable = [[1], [2], [3]]
# result = list(map(len, iterable))
# print(result)    

#====================================================================================

# from operator import add
# from functools import reduce

# result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)

#============================================================================================
# from decimal import Decimal as D
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'

# d_nums = [D(i) for i in s.split()]

# res = min(d_nums) + max(d_nums)
# print(res)
#============================================================================================

# from decimal import Decimal as D
# from functools import reduce
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13' 
# d_nums = [D(i) for i in s.split()]

# # d_sum = reduce(lambda x, y: x + y, d_nums, 0)
# d_sum = sum(d_nums)
# print(d_sum)
# res = sorted(d_nums, reverse=True)

# print(*res[:5])

#=============================================================================================

# from decimal import Decimal as D

# s = D(input())
# num_tuple = s.as_tuple()
# d = num_tuple.digits

# if -1 < s < 1:
#     print(0 + max(d))
# else:
#     print(min(d) + max(d))

#=========================================================================================

# from decimal import Decimal as D

# num = D(input())
# res = num.exp() + num.ln() + num.log10() + num.sqrt()
# print(res)

#==========================================================================================

# from fractions import Fraction as F

# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

# res = [F(i) for i in numbers]

# for i in range(len(numbers)):
#     print(f'{numbers[i]} = {res[i]}')

#==========================================================================================

# from fractions import Fraction as F

# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# nums = s.split()
# f_nums = [F(i) for i in nums]

# print(min(f_nums) + max(f_nums))

#===

# from fractions import Fraction as F

# m = int(input())
# n = int(input())

# num = F(m, n)
# print(num)

#===

# from fractions import Fraction as F

# n = (input())
# m = (input())

# print(f'{n} + {m} = {F(n) + F(m)}')
# print(f'{n} - {m} = {F(n) - F(m)}')
# print(f'{n} * {m} = {F(n) * F(m)}')
# print(f'{n} / {m} = {F(n) / F(m)}')

#===
# from functools import reduce
# from fractions import Fraction as F
# #n = int(input())
# nums = [F(1, i**2) for i in range(1, int(input()) + 1)]
# #result = reduce(lambda x, y: x + y, nums, 0)
# print(reduce(lambda x, y: x + y, nums, 0))

#===
# from fractions import Fraction as F
# def func(arg):
#     if arg[0] < arg[1]:
#         return True
# n = int(input())
# nums = [F(i, n - i) for i in range(n)]
# t_nums = [i.as_integer_ratio() for i in nums] 
# r_nums = list(filter(func, t_nums))
# print(F(f'{max(r_nums)[0]}/{max(r_nums)[1]}'))

#===

# from fractions import Fraction as F

# fracs = set()
# for i in range(1, int(input()) + 1):
#     for j in range(1, i):
#         fracs.add(F(j, i))
# print(*sorted(fracs), sep='\n')

#===


# z1 = complex('2+5j')
# z2 = complex('3+j')
# print(z1 / z2)
#===
# z1 = complex(input())
# z2 = complex(input())


# print(f'{z1} + {z2} = {z1 + z2}')
# print(f'{z1} - {z2} = {z1 - z2}')
# print(f'{z1} * {z2} = {z1 * z2}')

#===

# from functools import reduce

# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]

# res = list(map(lambda x: x[0], filter(lambda x: x[2] == 'primary', filter(lambda x: x[1] > 10000000, data))))
# print('Cities:', end=' ')
# print(*sorted(res), sep=', ')

#===

# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))

#===

# ch = 'aA'
# func = lambda x: True if x[0] in ch and x[-1] in ch else False
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))

#===

# is_non_negative_num = lambda x: True if x.replace('.', '').isdigit() and x.count('.') < 2 else False
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

#===

# is_num = lambda x: True if x.replace('.', '').replace('-', '', 1).isdigit() and x.count('.') < 2 and x.count('-') < 2 else False
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))

#===

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

# res = sorted(list((filter(lambda x: len(x) == 6, words))))
# print(*res)

#===

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# res = list(map(lambda x: x // 2 if x % 2 == 0 else x, list(filter(lambda x: not(x % 2 != 0 and x > 47), numbers))))
# print(*res, sep=' ')

#===

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# res = sorted(data, key=lambda x: x[1][-1], reverse=True)
# for d in res:
#     print(f'{d[1]}: {d[0]}')

#===

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# res = sorted(data, key=lambda x: len(x))
# res1 = sorted(data, key=lambda x: x)
# print(*res)
# print(*res1)

#===

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
# res = max(mixed_list, key=lambda x: x if type(x) == int else 0)
# print(res)

#===

# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
# res = sorted(mixed_list, key=lambda x: str(x))
# print(*res)

#===

# print(*list(map(lambda x: 255 - int(x), input().split())))

#===
# from functools import reduce
# def evaluate(coefficients, x):
#     c = [int(i) for i in coefficients]
#     return reduce(lambda z, j: z + j, map(lambda i: c[::-1][i] * (x ** i), range(len(coefficients))),  0)
    

# print(evaluate(input().split(), int(input())))

#===
# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: True if x in command else False, ignore))

# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
# print(ignore_command('trancate'))
#===

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

# res = zip(countries, capitals, population)

# for p in res:
#     print(f'{p[1]} is the capital of {p[0]}, population equal {p[2]} people.')

#===

# ТЗ
# mylist = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
# res = set(map(lambda x: tuple(x.items()), mylist))
# res1 = list(map(lambda x: dict(x), res))
# print(res1)

# def func(arg):
#     ret = []
#     for d in arg:
#         if d not in ret:
#             ret.append(d)
#     return ret

# print(func(mylist))

#===
# R = 2
# a = input().split()
# o = input().split()
# ap = input().split()
# abscissas = [float(i) for i in a]
# ordinates = [float(i) for i in o]
# applicates = [float(i) for i in ap]

# #print(list(zip(abscissas, ordinates, applicates)))

# r = all(list(map(lambda x: True if x[0]**2 + x[1]**2 + x[2]**2 <= R**2 else False, list(zip(abscissas, ordinates, applicates)))))
# print(r)

#===

# print(all(list(map(lambda x: True if x.isdigit() else False, input().split('.')))))
# r = list(map(lambda x: x if x.isdigit() else -1, input().split('.')))

# res = all(list(map(lambda x: 0 <= int(x) <= 255, r)))
# print(res)

#===
# a = int(input())
# b = int(input())

# def func(arg):
#     num = arg
#     if '0' not in str(num):
#         n = ''
#         while num > 0:
#             last_digit = num % 10 
#             if arg % last_digit == 0:
#                 n += str(last_digit)
#             num //= 10
#         if n[::-1] == str(arg):
#             return arg
    
# res = list(map(func, range(a, b + 1)))
# result = [i for i in res if i != None]
# print(*result)

#===

# n = int(input())
# res = []
# for i in range(n):
#     k = int(input())
#     c = []
#     for j in range(k):
#         s = input().split()
#         c.append(s[1])
#     r = any(list(map(lambda x: True if x == '5' else False, c)))
#     res.append(r)
# if all(res):
#     print('YES')
# else:
#     print('NO')

#===

# def add_five(a, b):
#     return a+5, b+5

# result = add_five(3, 2)
# print(result)
#===

# def display(**kwargs):
#     for i in kwargs:
#         print(i, end=' ')

# display(emp='Kelly', salary=9000)
#===

# def outer_func(a, b):
#     def inner_func(c, d):
#         return c + d + a*b
#     return inner_func

# res = outer_func(5, 10)(3, 2)

# print(res)
#===

# num = int('1000001')
# print(num)
# num = int('1000001', 2)
# print(num)

# func = lambda x: x**2
# print(func(2))    

# print((lambda x: (x + 3) * 5 / 2)(3))

# data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
# result = list(map(lambda x: '.'.join(x), data))
# print(result[1])

# result = list(filter(str.swapcase, ['a', '1', '', 'b', '2']))

# print(result)

# print(list(filter(None, ['', 1, 7, 'beegeek', None, False, 0])))

# from functools import reduce

# words = ['beegeek', 'stepik', 'python', 'iq-option']
# result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
# print(result)

# from functools import reduce

# result = reduce(lambda s, x: s + str(x), [1, 2, 3, 4, 5], '+')
# print(result)

# from functools import reduce
# import operator

# def flatten(data):
#     return reduce(operator.concat, data, [])

# result = flatten([[1, 2], [3, 4], [], [5]])

# print(result)
#===
# from functools import reduce
# def concat(*args, sep = ' '):
#     return reduce(lambda x, y: x + sep + y, args)
#===
# from functools import reduce
# def product_of_odds(data):
#     return reduce(lambda x,y: x*y, list(filter(lambda x: x % 2 == 1, data)), 1)
# product = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(product_of_odds(product))
#===
# words = 'the world is mine take a look what you have started'.split()

# print(*list(map(lambda x: '\"' + x + '\"', words)))

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*list(filter(lambda x: True if str(x) != str(x)[::-1] else False, numbers)))

#===

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

# sorted_numbers = sorted(numbers, key = lambda x: sum(x)/len(x), reverse=True)

# print(sorted_numbers)
#===

# def mul7(x):
#     return x * 7


# def add2(x, y):
#     return x + y


# def add3(x, y, z):
#     return x + y + z


# def call(func, *args):
#     return func(*args)

# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))

#===
# def add3(x):
#     return x + 3


# def mul7(x):
#     return x * 7


# def compose(func1, func2):
#     return lambda x: func1(func2(x))

# print(compose(mul7, add3)(1))

#===

# import operator
# def arithmetic_operation(operation):
#     if operation == '+':
#         return lambda x, y: operator.add(x, y)
#     elif operation == '-':
#         return lambda x, y: operator.sub(x, y)
#     elif operation == '/':
#         return lambda x, y: operator.truediv(x, y)
#     elif operation == '*':
#         return lambda x, y: operator.mul(x, y)
    
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))

#===

# s = input().split()

# print(*sorted(s, key=lambda x: x.lower()))
#===
# def gematry(word):
#     res = 0
#     for c in word.upper():
#         r = ord(c) - ord('A')
#         res += r
#     return res


# n = int(input())
# words = [input() for _ in range(n)]
# words.sort()
# print(*sorted(words, key=gematry), sep='\n')

#===
# from functools import reduce

# def dec(arg):
#     total, deg = 0, 3
#     for c in arg.split('.'):
#         r = int(c)*256**deg
#         total += r
#         deg -= 1
#     return total

# n = int(input())
# ips = [input() for _ in range(n)]
# print(*sorted(ips, key=dec), sep='\n')

#===

# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'


# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))

#===

# def pretty_print(data, side='-', delimiter='|'):
#     s_data = [str(i) for i in data]
#     sd = ' ' + delimiter + ' '
#     result = delimiter + ' ' + sd.join(s_data) + ' ' + delimiter

#     print(' ' + side*len(result[:-2]))
#     print(result)
#     print(' ' + side*len(result[:-2]))



# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

#===

# file = input()

# descriptor = open(file, 'r', encoding='utf-8')
# content = descriptor.read()
# print(content)

# descriptor.close()

#===
# import random

# file = input()

# descriptor = open(file, 'r', encoding='utf-8')
# content = descriptor.readlines()
# x =  random.randint(0, len(content) - 1)
# print(content[x])

# descriptor.close()

#===
# from functools import reduce
# descriptor = open('numbers.txt', 'r')

# content = descriptor.readlines()

# print(reduce(lambda x, y: int(x) + int(y), content))

# descriptor.close()
#===

# from functools import reduce
# descriptor = open('nums.txt', 'r')

# line = descriptor.readline()
# content = []
# while line != '':
#     content.append(line.strip())
#     line = descriptor.readline()

# print(reduce(lambda x, y: int(x) + int(y), list(filter(lambda x: x != '', content))))

# descriptor.close()

#===
# from functools import reduce

# def multy(arg):
#     return int(arg[1]) * int(arg[2]) 


# d = open('prices.txt', 'r', encoding='utf-8')

# lines = d.readlines()
# data = [s.split('\t') for s in lines]
# result = []
# for f in data:
#     part = []
#     for c in f:
#         v = c.strip()
#         part.append(v)
#     result.append(part)


# res = reduce(lambda x, y: x + y, list(map(multy, result)))
# print(res)
# # print(f'data: {data}')
# # print(f'result: {result}')
# d.close()

#===

# with open('text.txt', 'r') as file:
#     print(file.readline()[::-1])

#===

# with open('data.txt', 'r') as file:
#     content = file.readlines()
#     for s in content[::-1]:
#         print(s[::-1].strip())

#===
# with open('lines.txt', 'r') as file:
#     content = file.readlines()
#     lenghts = [len(s) for s in content]
#     largest = max(lenghts)
#     res = list(map(lambda x: x.strip() if len(x) == largest else '', content))
#     result = [s for s in res if s != '']
#     print(*result, sep='\n') 

#===

# def convert(arg):
#     dig = [int(i) for i in arg]
#     return sum(dig)
# with open('numbers.txt', 'r') as file:
#     data = file.readlines()
#     content = [s.strip().split() for s in data]
#     nums = list(map(convert, content))
#     print(*nums, sep='\n')

#===
# import string
# def check(arg):
#     mystr = ''
#     for c in arg:
#         if c in string.ascii_letters:
#             c = ' '
#             mystr += c
#         mystr += c
#     return mystr
# def convert(arg):
#     dig = [int(i) for i in arg]
#     return sum(dig)

# with open('nums.txt', 'r') as file:
#     content = file.readlines()
#     data = [s.strip() for s in content]
#     res = list(map(check, data))
#     result = [s.split() for s in res]
#     nums = list(map(convert, result))
#     print(sum(nums))

#===
# from functools import reduce
# import string
# def check(arg):
#     mystr = ''
#     for c in arg:
#         if c.isalpha():
#             mystr += c
#     return mystr
# with open('file.txt', 'r') as file:
#     content = file.readlines()
#     lines = len(content)
#     data = [s.strip() for s in content]
#     res = list(map(check, data))
#     # let = [len(s) for s in res]
#     # print(sum(let)) 
#     # print(res)
#     letters = reduce(lambda x, y: x + y, list(map(lambda x: len(x), res)))

#     # print(letters)
#     words = reduce(lambda x, y: x + y, list(map(lambda x: len(x.split()), content)))
#     # print(words)
#     print(f'Input file contains:\n{letters} letters\n{words} words\n{lines} lines')

#===
# import random
# with open('first_names.txt', 'r') as file:
#     names = file.readlines()
#     names1 = [s.strip() for s in names]
# with open('last_names.txt', 'r') as file1:
#     last_names = file1.readlines()
#     last_names1 = [s.strip() for s in names]

# # print(f'names: {len(names)}\nlast_names: {len(last_names)}')


# for i in range(3):
#     num_name = random.randint(1, len(names) - 1)
#     num_lname = random.randint(1, len(last_names) - 1)
#     print(f'{names1[num_name]} {last_names1[num_lname]}')

# import random
# with open('first_names.txt', 'r') as file, open('last_names.txt', 'r') as file1:
#     names = file.readlines()
#     names1 = [s.strip() for s in names]
#     last_names = file1.readlines()
#     last_names1 = [s.strip() for s in last_names]

# # print(f'names: {len(names)}\nlast_names: {len(last_names)}')


# for i in range(3):
#     num_name = random.randint(1, len(names) - 1)
#     num_lname = random.randint(1, len(last_names) - 1)
#     print(f'{names1[num_name]} {last_names1[num_lname]}')

#===

# with open('population.txt', 'r') as file:
#     print(*list(map(lambda x: x[0], list(filter(lambda x: x != '', map(lambda x: x if x[0][0] == 'G' and int(x[1]) > 500000 else '', [s.strip().split('\t') for s in file.readlines()]))))), sep='\n')

#===

# def read_csv():
#     with open('data.csv', 'r') as file:
#         content = file.readline()
#         data = content.split(',')
#         keys = [k.strip() for k in data]
#         # print(keys)
#         result = []
#         while content != '':
#             content = file.readline()
#             data = content.split(',')
#             values = [v.strip() for v in data]
#             result.append(dict(zip(keys, values)))
            
#         return result[:-1]
        
# print(read_csv())

#===

# with open('words.txt', 'w') as output:
#     print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
#     print('python', file=output)

#===

# import random

# with open('random.txt', 'a') as file:
#     for i in range(25):
#         file.write(str(random.randint(111, 778))+'\n')

#===

# with open('input.txt', 'r') as file:
#     content = file.readlines()
#     data = [s.strip() for s in content]
# with open('output.txt', 'w') as file1:
#     for i, val in enumerate(data, start=1):
#         print(f'{i}) {val}', file=file1)

#===

# def add(arg):
#     elem = int(arg[1]) + 5
#     if elem > 100:
#         elem = 100
#     res = arg[0] + ' ' + str(elem) + '\n'
#     return res
# with open('class_scores.txt', 'r', encoding='utf-8') as file, open('new_scores.txt', 'w') as file1:
#     content = file.readlines()
#     data = [s.strip().split() for s in content]
#     result = list(map(add, data))
#     file1.writelines(result)

#===
# def counter(goat):
#     res = data.count(goat)
#     return res

# with open('goats.txt', 'r') as file, open('answer.txt', 'w') as file1:
#     line = file.readline()
#     k = []
#     while line != 'GOATS\n':
#         line = file.readline()
#         k.append(line)
#     keys = [e.strip() for e in k[:-1]]

#     print(keys)
#     content = file.readlines()
#     # print(content)
#     data = [s.strip() for s in content]
#     # print(data)
#     values = list(map(counter, keys))
#     print(values)
#     result =  dict(zip(keys, values))
#     print(result)
#     count = len(data)
#     print(count)
#     res = [k for k, v in result.items() if v > count/100 * 7 ]
#     print(res)

#     print(*res, sep='\n', file=file1)
#===

# n = int(input())
# files = [input() for _ in range(n)]

# with open('output.txt', 'w') as file:
#     for f in files:
#         descriptor = open(f, 'r', encoding='utf-8')
#         d = descriptor.read()
#         file.write(d)
#         descriptor.close()
    
#===

# def minutes(x):
#     e = x.strip()
#     res=[int(i) for i in e.split(':')]
#     return res[0]*60+res[1]

# with open('logfile.txt', 'r', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as file1:
#     content = file.readlines()
#     data = [s.strip().split(',') for s in content] 
#     print(data)
#     times = list(map(lambda x: abs(minutes(x[1]) - minutes(x[2])), data))
#     print(times)
#     names = list(map(lambda x: x[0], data))
#     print(names)
#     result = dict(zip(names, times))
#     print(result)
#     res = [k for k, v in result.items() if v >= 60]
#     print(res)
#     print(*res, sep='\n', file=file1)

#===

# s = input()

# with open(s, 'r', encoding='utf-8') as file:
#     content = file.readlines()
#     print(len(content))
#===
# from functools import reduce
# with open('ledger.txt', 'r') as file:
#     content = file.readlines()
#     data = list(map(lambda x: x[1:].strip(), content))
#     result = reduce(lambda x, y: x + y, [int(c) for c in data])
#     print(f'${result}')

#===


# with open('grades.txt', 'r') as file:
#     content = file.readlines()
#     data = [s.strip().split() for s in content]
#     res = list(filter(lambda x: x != '', list(map(lambda x: x[0] if int(x[1]) >= 65 and int(x[2]) >= 65 and int(x[3]) >= 65 else '', data))))
#     print(len(res))

#===

# with open('words.txt', 'r') as file:
#     content = file.readlines()
#     data = [s.strip().split() for s in content]
#     words = []
#     for l in data:
#         for s in l:
#             words.append(s)
#     lenghts = [len(s) for s in words]
#     maxlen = max(lenghts)
#     # print(lenghts)
#     # print(words)
#     res = dict(zip(words, lenghts))
#     # print(res)
#     result = []
#     for k, v in res.items():
#         if v == maxlen:
#             result.append(k)
#     print(*result, sep='\n')

#===

# s = input()
# with open(s, 'r') as file: 
#     content = file.readlines()
#     cont = [e.strip() for e in content]
#     lines = content[-10:]
#     text = [e.strip() for e in lines]
#     if len(cont) <= 10:
#         print(*cont, sep='\n')
#     else:
#         print(*text, sep='\n')

#===

# s = input()
# with open('forbidden_words.txt', 'r', encoding='utf-8') as file, open(s, 'r', encoding='utf-8') as file1:
#     fw = file.read()
#     forbidden_words = fw.split()
#     content = file1.read()
#     data = content.lower()
#     res = ''
#     for w in forbidden_words:
#         data = data.replace(w.lower(), '*' * len(w))
#     for c in range(len(data)):
#         if data[c] != '*':
#             res += content[c]
#         else:
#             res += '*'               
#     print(res)
        
#===

# d = { 'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya' }

# with open('cyrillic.txt', 'r', encoding='utf-8') as file, open('transliteration.txt', 'w', encoding='utf-8') as file1:
#     content = file.read()
#     res = ''
#     for c in content:
#         if c in d:
#             c = d[c]
#             res += c
#         else:
#             res += c
#     print(res, file=file1)

#===

# s = input()
# with open(s, 'r', encoding='utf-8') as file:
#     content = file.readlines()
#     res = []
#     for i in range(len(content)):
#         if 'def' in content[i] and '#' not in content[i-1]:
#             res.append(content[i])
    
#     if res == []:
#         print('Best Programming Team')
#     else:
#         result = [s[4:] for s in res]
#         finish = []    
#         for f in result:
#             foo = ''
#             for c in f:
#                 if c == '(':
#                     break
#                 else:
#                     foo += c
#             finish.append(foo)
#         print(*finish, sep='\n')
    
# Курс для профессионалов!===

# def hide_card(card):
#     if ' ' in card:
#         card = card.replace(' ', '')
#         ret = '*' * 12 + card[-4:]
#         return ret
#     else:
#         ret = '*' * 12 + card[-4:]
#         return ret

# card = '1234567890123456'

# print(hide_card(card))

#===

# def same_parity(numbers):
#     if numbers == []:
#         return numbers
#     elif numbers[0] % 2 == 0:
#         ret = [i for i in numbers if i % 2 == 0]
#         return ret
#     elif numbers[0] % 2 != 0:
#         ret = [i for i in numbers if i % 2 != 0]
#         return ret
    

# print(same_parity([6, 0, 67, -7, 10, -20]))

#===

# def is_valid(pin):
#     if 4 <= len(pin) <= 6 and ' ' not in pin and pin.isdigit():
#         return True
#     else:
#         return False

#===

# def print_given(*args, **kwargs):
#     position = [e for e in args]
#     names = {k: v for k, v in kwargs.items()}
#     for i in position:
#         print(f'{i} {type(i)}')
#     for k, v in sorted(names.items()):
#         print(f'{k} {v} {type(v)}')

# print_given(1, [1, 2, 3], 'three', two=2)
    
#===
# from string import ascii_letters
# def convert(string):
#     c_low = 0
#     c_up = 0
#     for c in string:
#         if c in ascii_letters:
#             if c.isupper():
#                 c_up += 1
#             else:
#                 c_low += 1
#     if c_low >= c_up:
#         return string.lower() 
#     elif c_up > c_low:
#         return string.upper()

#===

# def filter_anagrams(word, words):
#     data = [s for s in words]
#     result = []
#     for s in range(len(data)):
#         w = ''
#         for c in range(len(word)):
#             if word[c] in data[s]:
#                 data [s] = data[s].replace(word[c], '', 1)
#                 w += word[c]
#                 if data[s] == '' and len(w) == len(word):
#                     result.append(words[s])
#             else:
#                 break
#     return result
             
# word = 'abba'
# anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

# print(filter_anagrams(word, anagrams))
# print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))

#===

# def likes(names):
#     if names == []:
#         return 'Никто не оценил данную запись'
#     elif names != []:
#         if len(names) == 1:
#             return f'{names[0]} оценил(а) данную запись'
#         elif len(names) == 2:
#             return f'{names[0]} и {names[1]} оценили данную запись'
#         elif len(names) == 3:
#             return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
#         elif len(names) > 3:
#             return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'    
        
# print(likes(['Эндрю', 'Тоби', 'Том']))
# print(likes([]))
# print(likes(['Дима', 'Алиса']))
# print(likes(['Том']))

#===
# def index_of_nearest(numbers, number):
#     smallest = {}
#     if numbers == []:
#         return -1
#     else:
#         nums = []
#         for i in numbers:
#             smallest[i] = abs(number - i)
#         for k, v in smallest.items():
#             if v == min(smallest.values()):
#                 nums.append(k)
#         indexes = [numbers.index(n) for n in nums]
#         return min(indexes)
# print(index_of_nearest([], 17))
# print(index_of_nearest([7, 13, 3, 5, 18], 0))
# print(index_of_nearest([9, 5, 3, 2, 11], 4))
# print(index_of_nearest([7, 5, 4, 4, 3], 4))
#===
# def spell(*args):
#     let = [s[0].lower() for s in args]
#     lens = []
#     words = [w.lower() for w in args]
#     for l in let:
#         j = []
#         for w in words:
#             if l == w[0]:
#                 j.append(len(w))
#         lens.append(max(j))
#     ret = dict(zip(let, lens))
#     return ret

# words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

# print(spell(*words))
# print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
# words = ['fruit', 'football', 'February', 'forest', 'Family']
# print(spell(*words))
#===

# def choose_plural(amount, declensions):

#     a = str(amount)
#     am = int(a[-2:])
#     if 11 <= am <= 14:
        
#         if am == 1:
#             return f'{amount} {declensions[0]}'
#         elif 2 <= am < 5:
#             return f'{amount} {declensions[1]}'
#         else:
#             return f'{amount} {declensions[2]}'
#     else:
#         bm = int(a[-1])
#         if bm == 1:
#             return f'{amount} {declensions[0]}'
#         elif 2 <= bm < 5:
#             return f'{amount} {declensions[1]}'
#         else:
#             return f'{amount} {declensions[2]}'
    
# print(choose_plural(21, ('пример', 'примера', 'примеров')))
# print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
# print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
# print(choose_plural(512312, ('цент', 'цента', 'центов')))

#===

# def get_biggest(numbers):
#     if  numbers == []:
#         return -1
#     else:
#         len_nums = list(map(lambda x: len(str(x)), numbers))
#         n = sorted(numbers, key=lambda x: str(x) * max(len_nums), reverse=True)
#         s_nums = ''.join([str(i) for i in n])
#         return int(s_nums)     
# print(get_biggest([1, 2, 3]))   
# print(get_biggest([61, 228, 9, 3, 11]))     
# print(get_biggest([7, 71, 72]))

#===

# d1, d2, d3 = int(input()), int(input()), int(input())

# p = [d1, d2, d3]
# p1 = sum(p)

# z_max = max(p)
# z_min = min(p)
# del p[p.index(z_max)]
# del p[p.index(z_min)]

# p_a = p[0]
# p2 = z_min*2+p_a*2
# print(min(p1, p2))

#===

# en, ru = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'

# letters = [input() for _ in range(3)]

# e = all(list(map(lambda x: x in en, letters)))
# r = all(list(map(lambda x: x in ru, letters)))
# if e:
#     print('en')
# elif r:
#     print('ru')
# else:
#     print('mix')

#===

# s_nums = input().split()
# nums = [int(c) for c in s_nums]
# n = nums[0]
# i_nums = [i for i in range(1, n+1)]
# X, Y, A, B = nums[1], nums[2], nums[3], nums[4]
# xl = i_nums[X-1:Y]
# for i in range(len(i_nums)):
#     for j in xl:
#         if i == X-1:
#             i_nums.insert(X-1, j)
#         if len(i_nums) == n:
#             break
# del i_nums[X-1 + len(xl):Y + len(xl)]
# al = i_nums[A-1: B]
# for i in range(len(i_nums)):
#     for j in al:
#         if i == A-1:
#             i_nums.insert(A-1, j)
#         if len(i_nums) == n:
#             break
# del i_nums[A-1 + len(al):B + len(al)]
# print(*i_nums)

#===

# nums = list(map(lambda x: int(x), input().split()))
# res = list(filter(lambda x: nums.count(x) > 1, nums))
# print(*sorted(set(res)))

#===

# nums = [i for i in range(1, int(input()) + 1)]
# res = list(map(lambda x: sum(map(int, list(str(x)))), nums))
# result = list(filter(lambda x: res.count(x) > 1, res))
# ret = []
# if result != []:
#     for i in result:
#         s = []
#         for j in result:
#             if i == j:
#                 s.append(i)
#         ret.append(s)
#     print(max(len(e) for e in ret))
# else:
#     print(max(len(str(e)) for e in res))

#===

# peoples = [input().split(', ') for _ in range(int(input()))]
# languages = set()
# all_answers = []
# for people in peoples:
#     for language in people:
#         languages.add(language)
#         all_answers.append(language)
# result = dict.fromkeys(languages, 0)
# for k, v in result.items():
#     if k in all_answers:
#         v += all_answers.count(k)
#         result[k] = v
# res = []
# for k, v in result.items():
#     if v == len(peoples):
#         res.append(k)
# if res != []:
#     print(', '.join(sorted(res)))
# else:
#     print('Сериал снять не удастся')

#===

# s = input()
# words = [input() for _ in range(int(input()))]
# vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# s_indexes = []
# for c in range(len(s)):
#     if s[c] in vowels:
#         s_indexes.append(c)
# all_indexes = []        
# for w in words:
#     w_indexes = []   
#     for c in range(len(w)):
#         if w[c] in vowels:
#             w_indexes.append(c)
#     all_indexes.append(w_indexes)
# result = [k for k, v in dict(zip(words, all_indexes)).items() if v == s_indexes]
# print(*result, sep='\n')

#===
# import string
# issued_emails = [input() for _ in range(int(input()))]
# new_employees = [input() for _ in range(int(input()))]
# old_employees = [s[:-12] for s in issued_emails]
# d_old_emp = {}
# for e in old_employees:
#     d_old_emp.setdefault(e.rstrip(string.digits), []).append(e[len(e.rstrip(string.digits)):])
# all_employees = []
# for n in new_employees:
#     if n not in d_old_emp:
#         d_old_emp.setdefault(n, [''])
#     else:
#         for k, v in d_old_emp.items():
#             if k == n:
#                 for i in range(len(v)+1):    
#                     if n[len(n.rstrip(string.digits)):] in v:
#                         n = ''
#                         n += str(i+1)
#                     else:
#                         v.append(n[len(n.rstrip(string.digits)):])
# email='@beegeek.bzz'
# for k,v in d_old_emp.items():
#     for i in v:
#         all_employees.append(k + i + email)
# result = [i for i in all_employees if i not in issued_emails]
# res = [s[:-12] for s in result]
# res_dict = {}
# for e in res:
#     res_dict.setdefault(e.rstrip(string.digits), []).append(e[len(e.rstrip(string.digits)):])
# final = []
# for x in new_employees:
#     for k, v in res_dict.items():
#         for i in v:
#             if x == k:
#                 final.append(k + i + email)
# final1 = []
# for i in final:
#     if i not in final1:
#         final1.append(i)

# # print(*result, sep='\n')
# print(*final1, sep='\n')

#===
# def transp(lst):
#     if lst[1] == 'B':
#         return int(lst[0]) 
#     elif lst[1] == 'KB':
#         return int(lst[0]) * 1024
#     elif lst[1] == 'MB':
#         return (int(lst[0]) * 1024) * 1024
#     elif lst[1] == 'GB':
#         return ((int(lst[0]) * 1024) * 1024) * 1024

# def calc(n, w):
#     if w == 0:
#         ret = str(n) + ' ' + 'B'
#         return ret
#     elif w == 1:
#         ret = str(round(n / 1024)) + ' ' + 'KB'
#         return ret
#     elif w == 2:
#         ret = str(round((n / 1024) / 1024)) + ' ' + 'MB'
#         return ret
#     elif w == 3:
#         ret = str(round(((n / 1024) / 1024) / 1024)) + ' ' + 'GB'
#         return ret
    
# def calc1(n):
#     if n > 1023:
#         ret = str(round(n / 1024)) + ' ' + 'KB'
#         kb = round(n / 1024)
#         if kb > 1023:
#             ret = str(round((n / 1024) / 1024)) + ' ' + 'MB'
#             mb = round((n / 1024) / 1024)
#             if mb > 1023:
#                 ret = str(round(((n / 1024) / 1024) / 1024)) + ' ' + 'GB'
#                 # gb = round(((n / 1024) / 1024) / 1024)
#     return ret


# with open('files.txt', 'r',encoding='utf-8') as file:
#     content = file.readlines()
#     mylist = [s.strip().split() for s in content]
#     # print(mylist)
#     f_dict = {}
#     files = [file[0].split('.') for file in mylist]
#     for i in range(len(mylist)):
#         files[i].append(mylist[i][1:])
#     # print(files)
#     for f in files:
#         f_dict.setdefault(f[1], [])
#     for f in files:
#         for k, v in f_dict.items():
#             if f[1] == k:
#                 v.append(f[0])
#                 f_dict[k] = v
#     v_dict = {}
#     for v in files:
#         v_dict.setdefault(v[1], [])
#     for f in files:
#         for k, v in v_dict.items():
#             if f[1] == k:
#                 v.append(f[2])
#                 v_dict[k] = v
#     ext = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
#     weight = []
#     for k, v in sorted(v_dict.items()):
#         w = []
#         total = 0 # В байтах
#         for val in v:
#             if val[1] == 'B':
#                 w.append(0)    
#             elif val[1] == 'KB':
#                 w.append(1)
#             elif val[1] == 'MB':
#                 w.append(2)
#             elif val[1] == 'GB':
#                 w.append(3)
#             total += transp(val)
#         # weight.append(calc(total, max(w)))
#         weight.append(calc1(total))
#     # print(weight)
#     # for k,v in f_dict.items():
#     #     print(f'{k}: {v}')
#     # for k,v in sorted(v_dict.items()):
#     #     print(f'{k}: {v}')
#     extensions = [k for k in f_dict.keys()]
#     # print(extensions)
#     exten = sorted(extensions)
#     # print(exten)
#     for i in range(len(exten)):
#         for k, v in f_dict.items():
#             if exten[i] == k:
#                 for val in sorted(v):
#                     print(f'{val}.{k}')
#         print('-' * 10)
#         print(f'Summary: {weight[i]}\n')
        
#===

# импортируем тип date из модуля datetime
# from datetime import date

# # выводим текущую дату
# print(date.today())        

#===

# from datetime import date

# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
# res = []
# for d in dates:
#     if 1 <= d.month < 4:
#         res.append(f'{d.year}-Q1')
#     elif 4 <= d.month < 7:
#         res.append(f'{d.year}-Q2')    
#     elif 7 <= d.month < 10:
#         res.append(f'{d.year}-Q3')    
#     else:
#         res.append(f'{d.year}-Q4')    
# print(*res, sep='\n')

#===
# from datetime import date
# def get_min_max(dates):
#     if dates != []:
#         min_date = min(dates)
#         max_date = max(dates)
#         return (min_date, max_date)
#     else:
#         return ()
    

# # dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]

# # print(get_min_max(dates))
        
# print(get_min_max([]))

#===

# from datetime import date, timedelta
# def get_date_range(start, end):
#     delta =  end - start
#     if delta.days < 0:
#         return []
#     else:
#         ret = []
#         for i in range(delta.days + 1):
#             ret.append(start + timedelta(i))
#     return ret
        
# # date1 = date(2021, 10, 1)
# # date2 = date(2021, 10, 5)

# # print(*get_date_range(date1, date2), sep='\n')

# date1 = date(2019, 6, 5)
# date2 = date(2019, 6, 5)

# print(get_date_range(date1, date2))

#===
# from datetime import date, timedelta

# def saturdays_between_two_dates(start, end):
#     delta = end - start
#     a_delta = abs(delta)
#     ret = 0
#     for i in range(a_delta.days+1):
#         if start != date(2020, 7, 26):
#             d = start + timedelta(i+1)
#             if d.weekday() == 6:
#                 ret += 1
#         else:
#             d = start + timedelta(i)
#             if d.weekday() == 6:
#                 ret += 1       
#     return ret

#===

# from datetime import time

# alarm = time(7, 30, 25)

# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))

#===

# from datetime import date

# birthday = date(1992, 10, 6)

# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))

#===

# from datetime import date

# florida_hurricane_dates = [date(1950, 12, 10)]
# first_date = min(florida_hurricane_dates)

# iso = 'Дата первого урагана в ISO формате: ' + first_date.strftime('%Y-%m-%d')
# ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
# us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

# print(iso)
# print(ru)
# print(us)

#===

# from datetime import date

# andrew = date(1992, 8, 24)

# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number

#===

# from datetime import date
# d1, d2 = input(), input()

# md = (min(date.fromisoformat(d1), date.fromisoformat(d2)))
# print(md.strftime('%d-%m (%Y)'))

#===

# from datetime import date
# dates = [date.fromisoformat(input()) for _ in range(int(input()))]
# result = [d.strftime('%d/%m/%Y') for d in sorted(dates)]
# print(*result, sep='\n')

#===

# from datetime import date
# def print_good_dates(dates):
#     year_t = 1992
#     age_t = 29
#     interest_dates_y = list(filter(lambda x: x.year == year_t, dates))
#     interest_dates_a = list(filter(lambda x: int(x.month) + int(x.day) == age_t, interest_dates_y))
#     result = [d.strftime('%B %d, %Y') for d in sorted(interest_dates_a)]
#     if result:
#         return print(*result, sep='\n')

# dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
# print_good_dates(dates)
# dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
# print_good_dates(dates)
    
#===

# from datetime import date
# def is_correct(day, month, year):
#     try:
#         d = date(int(year), int(month), int(day))
#         return True
#     except:
#         return False

# print(is_correct(31, 12, 2021))    

#===

# from datetime import date
# def is_correct(arg):
#     try:
#         d = [i for i in arg.split('.')]
#         date(int(d[2]), int(d[1]), int(d[0]))
#         return 'Корректная'
#     except:
#         return 'Некорректная'
# dates = []    
# while True:
#     s = input()
#     if s == 'end':
#         break
#     dates.append(s)
# result = list(map(is_correct, dates))
# print(*result, sep='\n')
# n = len(list(filter(lambda x: x == 'Корректная', result)))
# print(n)

#===

# from datetime import datetime

# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), 
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), 
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53), 
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3), 
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5), 
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54), 
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45), 
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57), 
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42), 
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12), 
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27), 
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41), 
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44), 
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

# my_times = [t.time() for t in times_of_purchases]
# res = list(map(lambda x: 'После полудня' if x.hour >= 12 else 'До полудня', my_times))
# if res.count('До полудня') > res.count('После полудня'):
#     print('До полудня')
# else:
#     print('После полудня')

#===

# from datetime import date, time, datetime

# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24), 
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59), 
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2), 
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

# res = [datetime.combine(dates[i], times[i]) for i in range(len(dates))]

# print(*sorted(res, key=lambda x: x.second), sep='\n')

#===

# from datetime import datetime

# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

# scores = dict()
# l_score = []
# for k, v in data.items():
#     scores[k] = abs(datetime.timestamp(datetime.strptime(v[0], '%d.%m.%Y %H:%M:%S')) - datetime.timestamp(datetime.strptime(v[1], '%d.%m.%Y %H:%M:%S')))
# for k, v in scores.items():
#     l_score.append(v)
# smallest = min(l_score)
# for k, v in scores.items():
#     if smallest == v:
#         print(k)

#===

# from datetime import datetime
# with open('diary.txt', 'r', encoding='utf-8') as file:
#     content = file.readlines()
#     my_list = [s.strip() for s in content if s != '\n']
#     data = []
#     for s in my_list:
#         try:
#             data.append(datetime.strptime(s, '%d.%m.%Y; %H:%M'))
#         except:
#             data.append(s)
#     dates_t = [e for e in data if type(e) == datetime]
#     text = []
#     txt = []
#     for e in data:
#         if type(e) == str:
#             txt.append(e)
#             continue
#         if txt != []:
#             text.append(txt)
#             txt = []
#     ch = list(data[-3:])
#     text.append(ch)
#     res = dict(zip(dates_t, text))
#     for k, v in sorted(res.items()):
#         print(datetime.strftime(k, '%d.%m.%Y; %H:%M'))
#         print(*v, sep='\n')
#         print()

#===

# from datetime import datetime, date

# def is_available_date(book_dates, date_for_booking):
#     un_dates = []
#     for d in book_dates:
#         if  '-' not in d:
#             un_dates.append(datetime.strptime(d, '%d.%m.%Y').toordinal())
#         else:
#             u_date = d.split('-')
#             start = datetime.strptime(u_date[0], '%d.%m.%Y')
#             end = datetime.strptime(u_date[1], '%d.%m.%Y') 
#             un_dates.append(start.toordinal())
#             n = start.toordinal()
#             count = 0
#             while n < end.toordinal():
#                 count += 1
#                 n = start.toordinal() + count
#                 un_dates.append(n)
#     n_dates = []
#     if  '-' not in date_for_booking:
#         n_dates.append(datetime.strptime(date_for_booking, '%d.%m.%Y').toordinal())
#     else:
#         n_date = date_for_booking.split('-')
#         start = datetime.strptime(n_date[0], '%d.%m.%Y')
#         end = datetime.strptime(n_date[1], '%d.%m.%Y') 
#         n_dates.append(start.toordinal())
#         n = start.toordinal()
#         count = 0
#         while n < end.toordinal():
#             count += 1
#             n = start.toordinal() + count
#             n_dates.append(n)
#     if len(n_dates) == 1:
#         if n_dates[0] in un_dates:
#             return False
#         else:
#             return True
#     else:
#         check = set(n_dates).difference(set(un_dates))
#         if len(check) != len(n_dates):
#             return False
#         else:
#             return True
#     # return f'Недоступные даты: {un_dates}, запрашиваемые даты: {n_dates}'


# # TEST_1:
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))

# # TEST_2:
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021-04.11.2021'
# print(is_available_date(dates, some_date))

# # TEST_3:
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '06.11.2021'
# print(is_available_date(dates, some_date))

#===

# from datetime import datetime, timedelta

# dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

# print(dt.strftime('%d.%m.%Y %H:%M:%S'))

#===

# from datetime import date, timedelta

# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)

# days = birthday - today

# print(days.days)
# print(type(days))

#===

# from datetime import datetime, timedelta
# d = datetime.strptime(input(), '%d.%m.%Y')
# delta = timedelta(days=1)
# print(datetime.strftime(d - delta, '%d.%m.%Y'))
# print(datetime.strftime(d + delta, '%d.%m.%Y'))

#===

# from datetime import datetime, timedelta

# d = datetime.strptime(input(), '%H:%M:%S')
# start = datetime(1, 1, 1, 0, 0, 0)
# delta = d - start
# print(delta.seconds)

#===

# from datetime import datetime, timedelta

# d = datetime.strptime(input(), '%H:%M:%S')
# n = int(input())
# delta = d + timedelta(seconds=n)
# print(delta.strftime('%H:%M:%S'))

#===

# from datetime import datetime, timedelta

# def num_of_sundays(year):
#     d = datetime(year, 12, 31, 0, 0, 0)
#     delta = d.strftime('%U')
#     return delta

#===

# from datetime import datetime, timedelta
# d = datetime.strptime(input(), '%d.%m.%Y')
# i = 1
# dates = []
# dates.append(d.strftime('%d.%m.%Y'))
# for t in range(1, 10):
#     i += t
#     date = d + timedelta(days=i)
#     dates.append(date.strftime('%d.%m.%Y'))
#     i += 1
# print(*dates, sep='\n')

#===

# from datetime import datetime, timedelta
# s = [datetime.strptime(d, '%d.%m.%Y') for d in input().split()]    
# res = []
# if s:
#     j = 0
#     for i in range(1, len(s) + 1):
#         try:
#             r = s[j:i+1]  
#             res.append(abs(r[0] - r[1]).days)
#             j+=1
#         except:
#             print(res)
# else:
#     print([])

#===

# from datetime import datetime, timedelta

# def fill_up_missing_dates(dates):
#     d_dates = [datetime.strptime(d, '%d.%m.%Y') for d in dates]
#     delta = timedelta(days=1)
#     result = []
#     m = min(d_dates)
#     while m <= max(d_dates):
#         result.append(m.strftime('%d.%m.%Y'))
#         m+=delta    
#     return result

# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

# print(fill_up_missing_dates(dates))

#===

# from datetime import datetime, timedelta
# s_time = datetime.strptime(input(), '%H:%M')
# e_time = datetime.strptime(input(), '%H:%M')
# timeout = timedelta(minutes=10)
# lesson = timedelta(minutes=45)
# time = s_time + lesson
# while time <= e_time:
#     print(s_time.strftime('%H:%M'), '-', time.strftime('%H:%M'))
#     s_time = time + timeout
#     time = time + timeout + lesson

#===

# from datetime import date, time, datetime, timedelta

# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
# count = 0
# for t in data:
#     t_s = datetime.strptime(t[0], '%H:%M')
#     t_e = datetime.strptime(t[1], '%H:%M')
#     delta = t_e - t_s
#     count += delta.seconds//60
# print(count)

#===

# from datetime import datetime, timedelta

# nums_of_days = []

# start = datetime(1, 1, 1, 0, 0, 0)
# end = datetime(9999, 12, 30, 0, 0, 0)
# # print(start.weekday())
# delta = timedelta(days=1)
# result = [0, 0, 0, 0, 0, 0, 0]
# while start <= end:
#     if start.day == 13:
#         name_d = start.weekday()
#         if name_d == 0:
#             result[0] += 1
#         elif name_d == 1:
#             result[1] += 1
#         elif name_d == 2:
#             result[2] += 1
#         elif name_d == 3:
#             result[3] += 1
#         elif name_d == 4:
#             result[4] += 1
#         elif name_d == 5:
#             result[5] += 1
#         else:
#             result[6] += 1
            
#     start += delta
    
# print(*result, sep='\n')

#===

# from datetime import datetime, timedelta, time
# date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# weekdays = {}.fromkeys([i for i in range(5)], (datetime(year=1, month=1, day=1, hour=9, minute=0, second=0), datetime(year=1, month=1, day=1, hour=21, minute=0, second=0)))
# weekends = {}.fromkeys([i for i in range(5, 7)], (datetime(year=1, month=1, day=1, hour=10, minute=0, second=0), datetime(year=1, month=1, day=1, hour=18, minute=0, second=0)))
# if date.weekday() in weekdays:
#     if weekdays[date.weekday()][0].time() <= date.time() < weekdays[date.weekday()][1].time():
#         print((weekdays[date.weekday()][1] - date).seconds // 60)
#     else:
#         print('Магазин не работает')
# elif date.weekday() in weekends:
#     if weekends[date.weekday()][0].time() <= date.time() < weekends[date.weekday()][1].time():
#         print((weekends[date.weekday()][1] - date).seconds // 60)
#     else:
#         print('Магазин не работает')
        
#===

# from datetime import datetime, timedelta 

# date1 = datetime.strptime(input(), '%d.%m.%Y')
# date2 = datetime.strptime(input(), '%d.%m.%Y')
# check = [0, 3]
# while (date1.day + date1.month) % 2 == 0:
#     date1+=timedelta(days=1)
# while date1 <= date2:
#     if date1.weekday() not in check:
#         print(date1.strftime('%d.%m.%Y'))
#     date1+=timedelta(days=3)

#===

# from datetime import datetime

# employee = [input().split() for _ in range(int(input()))]
# age_employee = [datetime.strptime(e[2], '%d.%m.%Y') for e in employee]
# check = min(age_employee)
# name_employees = [' '.join(e[:2]) for e in employee]
# res = dict(zip(name_employees, age_employee))
# result = []
# for k, v in res.items():
#     if v == check:
#         result.append(k)
# if len(result) == 1:
#     for k, v in res.items():
#         if k == result[0]:
#             print(v.strftime('%d.%m.%Y'), k)
# else:
#     print(check.strftime('%d.%m.%Y'), len(result))

#===


# from datetime import datetime
# employee = [input().split() for _ in range(int(input()))]
# births = [datetime.strptime(e[2], '%d.%m.%Y') for e in employee]
# name_employees = [' '.join(e[:2]) for e in employee]
# res = dict(zip(name_employees, births))
# counter = [births.count(b) for b in births]
# result = dict(zip(births, counter))
# out = [k for k, v in result.items() if v == max(counter)]
# out_r = [d.strftime('%d.%m.%Y') for d in sorted(out)]
# print(*out_r, sep='\n')

#===

# from datetime import datetime

# data = datetime.strptime(input(), '%d.%m.%Y')
# employee = [input().split() for _ in range(int(input()))]
# births = [datetime.strptime(e[2], '%d.%m.%Y') for e in employee]
# uptd_births = list(map(lambda x: x.replace(year=data.year), births))
# name_employees = [' '.join(e[:2]) for e in employee]
# difference = []
# for i in range(len(uptd_births)):
#     if data.month != 12:
#         r = abs(uptd_births[i] - data).days
#     else:
#         r = abs(uptd_births[i] - data.replace(year=uptd_births[i].year-1)).days
#     if r <= 7 and r != 0:
#         y = births[i]
#         difference.append((y, r))
# test = dict(difference)
# if len(difference) == 0:
#     print('Дни рождения не планируются')
# else:
#     res = dict(zip(name_employees, births))
#     for k, v in res.items():
#         if max(test) == v:
#             print(k)

#===

# from datetime import datetime

# def choose_plural(n, form1, form2, form5):
#     if n % 100 in [11, 12, 13, 14]:
#         return form5
#     elif n % 10 == 1:
#         return form1
#     elif n % 10 in [2, 3, 4]:
#         return form2
#     else:
#         return form5

# current_datetime_str = input()
# current_datetime = datetime.strptime(current_datetime_str, '%d.%m.%Y %H:%M')

# course_datetime_str = '08.11.2022 12:00'
# course_datetime = datetime.strptime(course_datetime_str, '%d.%m.%Y %H:%M')

# if current_datetime >= course_datetime:
#     print('Курс уже вышел!')
# else:
#     time_left = course_datetime - current_datetime
#     days_left = time_left.days
#     hours_left = time_left.seconds // 3600
#     minutes_left = (time_left.seconds % 3600) // 60

#     if days_left > 0:
#         hours_text = choose_plural(hours_left, 'час', 'часа', 'часов')
#         days_text = choose_plural(days_left, 'день', 'дня', 'дней')
#         if hours_left != 0:
#             print(f'До выхода курса осталось: {days_left} {days_text} и {hours_left} {hours_text}')
#         else:
#             print(f'До выхода курса осталось: {days_left} {days_text}')
#     elif hours_left > 0:
#         minutes_text = choose_plural(minutes_left, 'минута', 'минуты', 'минут')
#         hours_text = choose_plural(hours_left, 'час', 'часа', 'часов')
#         if minutes_left != 0: 
#             print(f'До выхода курса осталось: {hours_left} {hours_text} и {minutes_left} {minutes_text}')
#         else:
#             print(f'До выхода курса осталось: {hours_left} {hours_text}')
#     else:
#         minutes_text = choose_plural(minutes_left, 'минута', 'минуты', 'минут')
#         print(f'До выхода курса осталось: {minutes_left} {minutes_text}')

#===

# from time import monotonic, sleep, time

# def calculate_it(func, *args):
#     start_time = monotonic() 
#     r = func(*args)
#     end_time = monotonic()
#     elapsed_time = end_time - start_time
#     res = (r, elapsed_time)
#     return res

# def add(a, b, c):
#     sleep(3)
#     return a + b + c

# print(calculate_it(add, 1, 2, 3))

#===

# from math import factorial  
# import time

# def get_the_fastest_func(funcs, arg):
#     fastest_func = None
#     min_execution_time = float('inf')

#     for func in funcs:
#         start_time = time.time()
#         func(arg)
#         end_time = time.time()
#         execution_time = end_time - start_time

#         if execution_time < min_execution_time:
#             min_execution_time = execution_time
#             fastest_func = func

#     return fastest_func



# def factorial_recurrent(n=0):                  # рекурсивная функция
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)    


# def factorial_classic(n=0):                    # итеративная функция
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# print(get_the_fastest_func([factorial, factorial_recurrent, factorial_classic], 900))

#===

# import calendar
# print(*[calendar.isleap(int(input())) for _ in range(int(input()))], sep='\n')

#===

# import calendar
# s = input().split()
# year = int(s[0])
# month = s[1]
# months = list(calendar.month_abbr)
# for i in range(len(months)):
#     if month == months[i]:
#         print(calendar.month(year, i))

#===

# import calendar
# names = list(calendar.day_name)
# s = [int(i) for i in input().split('-')]
# print(names[calendar.weekday(s[0], s[1], s[2])])

#===

# import calendar
# s = [int(i) for i in input().split()]
# print(calendar.monthrange(s[0], s[1])[1])

#===

# import calendar
# s = input().split()
# names = list(calendar.month_name)
# i = names.index(s[1])
# print(calendar.monthrange(int(s[0]), i)[1])

#===

# import datetime
# import calendar
# def get_days_in_month(year, month):
#     names = list(calendar.month_name)
#     mth = calendar.monthrange(year, names.index(month))
#     lst = [datetime.date(year=year, month=names.index(month), day=i) for i in range(1, mth[1]+1)]
#     return lst

# print(get_days_in_month(1982, 'January'))

#===

# import datetime
# import calendar

# def get_all_mondays(year):
#     names = list(calendar.month_name)
#     lst = []
#     for i in range(1, len(names)): 
#         mths = calendar.monthrange(year, i)
#         for j in range(1, mths[1]+1):
#             if calendar.weekday(year, i, j) == 0:
#                 lst.append(datetime.date(year=year, month=i, day=j))
#     return lst
# print(get_all_mondays(2021))

#===

# import datetime
# import calendar

# def get_third_thurhsdays(year):
#     names = list(calendar.month_name)
#     lst = []
#     for i in range(1, len(names)): 
#         mths = calendar.monthrange(year, i)
#         thursdays = []
#         for j in range(1, mths[1]+1):
#             if calendar.weekday(year, i, j) == 3:
#                 thursdays.append(datetime.date(year=year, month=i, day=j))
#         lst.append(thursdays[2])
#     ret = [d.strftime('%d.%m.%Y') for d in lst]
#     return ret
# y = int(input())
# print(*get_third_thurhsdays(y), sep='\n')

#===

# import sys
# for e in sys.stdin.readlines():
#     print(e[::-1].strip())

#===

# import sys, datetime

# dates = [datetime.datetime.strptime(d.strip(), '%Y-%m-%d') for d in sys.stdin.readlines()]
# print((max(dates)-min(dates)).days)

#===

# import sys
# socks = [int(c) for c in sys.stdin.readlines()]
# print(socks)
# for i in range(1, len(socks)+1):
#     if i == (len(socks)):
#         if i % 2 == 0:
#             if socks[i-1] % 2 == 0:
#                 print('Дима')
#             else:
#                 print('Анри')
#         else: 
#             if socks[i-1] % 2 == 0:
#                 print('Анри')
#             else:
#                 print('Дима')

#===

# import sys
# heights = [int(c) for c in sys.stdin.readlines()]
# if heights:
#     print(f'Рост самого низкого ученика: {min(heights)}')
#     print(f'Рост самого высокого ученика: {max(heights)}')
#     print(f'Средний рост: {sum(heights)/len(heights)}')
# else:
#     print('нет учеников')

#===

# import sys
# code = [s.strip() for s in sys.stdin.readlines()]
# count = 0
# for s in code:
#     if s.startswith('#'):
#         count += 1
# print(count)

#===

# import sys
# print(*[s for s in sys.stdin.readlines() if not s.strip().startswith('#') ], sep="")

#===

# import sys
# news = [s.strip() for s in sys.stdin.readlines()]
# category = news.pop(-1)
# f_cat = list(filter(lambda x: x[1] == category, [s.split(' / ') for s in news]))
# xf_cat = [float(x[2]) for x in f_cat]
# f = [f[0] for f in f_cat]
# d = dict(zip(f, xf_cat))
# sorted_d = dict(sorted(d.items(), key=lambda x: (x[1], x)))
# print(*sorted_d, sep='\n')

#===


# import sys
# numbers = []
# for line in sys.stdin:
#     num = line.strip()
#     numbers.append(num)

# nums = [int(i) for i in numbers]
# diff = nums[1] - nums[0]
# is_a = all(nums[i+1] - nums[i] == diff for i in range(len(nums)-1))
# if is_a:
#     print("Арифметическая прогрессия")
# else: 
#     ratio = nums[1] / nums[0]
#     is_g = all(nums[i+1] / nums[i] == ratio for i in range(len(nums)-1))
#     if is_g:
#         print("Геометрическая прогрессия")
#     else:
#         print("Не прогрессия")

#===

# import csv

# with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
#     # создаем writer объект и указываем названия столбцов
#     writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
#     # записываем первую строку с названиями столбцов
#     writer.writeheader()
#     # записываем строку с данными
#     writer.writerow({'first_col': 'value1', 'second_col': 'value2'})

#===

# import csv
# with open('sales.csv', 'r', encoding='utf-8') as csv_file:
#     rows = csv.reader(csv_file, delimiter=';')
#     sales = list(filter(lambda x: int(x[1]) > int(x[2]), list(rows)[1:]))
#     for product in sales:
#         print(product[0])

#===

# import csv

# # Открываем файл salary_data.csv в режиме чтения с явным указанием кодировки UTF-8
# with open('salary_data.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=';')
#     next(reader)  # Пропускаем заголовок

#     # Создаем словарь для хранения суммы зарплат и количества сотрудников для каждой компании
#     company_stats = {}

#     for row in reader:
#         company = row[0]
#         salary = int(row[1])

#         if company in company_stats:
#             company_stats[company][0] += salary  # Увеличиваем сумму зарплат
#             company_stats[company][1] += 1       # Увеличиваем количество сотрудников
#         else:
#             company_stats[company] = [salary, 1]  # Добавляем новую компанию в словарь

# # Сортируем компании по возрастанию средней зарплаты
# sorted_companies = sorted(company_stats.keys(), key=lambda x: (company_stats[x][0] / company_stats[x][1], x))

# # Выводим названия компаний
# for company in sorted_companies:
#     print(company)

#===

# import csv

# def count_domains(input_file, output_file):
#     domain_counts = {}
#     with open(input_file, 'r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         headers = next(reader)  # Читаем первую строку с названиями столбцов
#         email_index = headers.index('email')
        
#         for row in reader:
#             email = row[email_index]
#             domain = email.split('@')[1]
#             if domain in domain_counts:
#                 domain_counts[domain] += 1
#             else:
#                 domain_counts[domain] = 1
    
#     sorted_domains = sorted(domain_counts.items(), key=lambda x: (x[1], x[0]))
    
#     with open(output_file, 'w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['domain', 'count'])
#         writer.writerows(sorted_domains)


# count_domains('data.csv', 'domain_usage.csv')

#===

# import csv

# def condense_csv(filename, id_name):
#     data = {}
    
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             line = line.strip().split(',')
#             obj_name = line[0]
#             prop_name = line[1]
#             prop_value = ','.join(line[2:])
            
#             if obj_name not in data:
#                 data[obj_name] = {}
            
#             data[obj_name][prop_name] = prop_value
    
#     properties = sorted(set(prop_name for obj in data.values() for prop_name in obj))
    
#     with open('condensed.csv', 'w', encoding='utf-8') as file:
#         file.write(f"{id_name},{','.join(properties)}\n")
#         for obj_name, obj in sorted(data.items()):
#             values = [obj.get(prop_name, '') for prop_name in properties]
#             file.write(f"{obj_name},{','.join(values)}\n")

# condense_csv('data.csv', id_name='ID')

#===

# import csv

# # Открываем исходный файл для чтения
# with open('student_counts.csv', 'r', encoding='utf-8') as input_file:
#     reader = csv.reader(input_file)
#     data = list(reader)

# # Получаем заголовки столбцов (классы) из первой строки
# classes = data[0][1:]

# # Сортируем классы в порядке возрастания
# sorted_classes = sorted(classes, key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))

# # Создаем новую отсортированную таблицу
# sorted_data = [data[0]]  # Заголовки столбцов

# # Для каждого года сортируем данные по классам
# for row in data[1:]:
#     sorted_row = [row[0]]  # Год
#     sorted_row.extend(row[classes.index(cls) + 1] for cls in sorted_classes)
#     sorted_data.append(sorted_row)

# # Записываем отсортированные данные в новый файл
# with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as output_file:
#     writer = csv.writer(output_file)
#     writer.writerows(sorted_data)

#===

# import csv
# # Открываем исходный файл для чтения
# with open('student_counts.csv', 'r', encoding='utf-8') as input_file:
#     reader = csv.reader(input_file)
#     data = list(reader)
# # Получаем заголовки столбцов (классы) из первой строки
# classes = data[0][1:]
# # Сортируем классы в порядке возрастания
# sorted_classes = sorted(classes, key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
# # Создаем новую отсортированную таблицу
# sorted_data = [data[0]]  # Заголовки столбцов
# # Для каждого года сортируем данные по классам
# for row in data[1:]:
#     sorted_row = [row[0]]  # Год
#     sorted_row.extend(row[classes.index(cls) + 1] for cls in sorted_classes)
#     sorted_data.append(sorted_row)
# # Записываем отсортированные данные в новый файл
# with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as output_file:
#     writer = csv.writer(output_file)
#     writer.writerows(sorted_data)
# # Чтение содержимого файла
# with open('sorted_student_counts.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     lines = list(reader)
# # Разделение каждой строки на ячейки
# header = lines[0]
# data = lines[1:]
# # Определение порядка сортировки названий столбцов
# order = ['year', '1-А', '1-Б', '2-А', '2-Б', '2-В', '2-Г', '3-А', '3-Б', '3-В', '3-Г', '4-А', '5-А', '5-Б', '6-А', '6-Б', '7-А', '7-Б', '7-В', '8-А', '8-Б', '8-В', '8-Г', '9-А', '10-А', '11-А', '11-Б', '11-В']
# # Получение индексов названий столбцов в порядке сортировки
# column_indices = [header.index(column) for column in order]
# # Сортировка названий столбцов
# header_sorted = [header[index] for index in column_indices]
# # Запись отсортированных названий столбцов в файл
# lines_sorted = [header_sorted] + data
# with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(lines_sorted)

#===

# import csv

# # Открываем файл
# with open('prices.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=';')
#     next(reader)  # Пропускаем заголовок

#     # Инициализируем переменные для хранения самого дешевого продукта и магазина
#     cheapest_product = None
#     cheapest_store = None
#     cheapest_price = float('inf')  # Изначально устанавливаем очень большую цену

#     # Перебираем строки файла
#     for row in reader:
#         store = row[0]  # Название магазина

#         # Перебираем цены на продукты в текущей строке
#         for i in range(1, len(row)):
#             product = row[i]  # Название продукта

#             # Пропускаем названия магазинов в столбцах
#             if ':' in product:
#                 continue

#             price = int(row[i])  # Цена продукта

#             # Если текущая цена меньше самой дешевой цены, обновляем значения
#             if price < cheapest_price:
#                 cheapest_product = product
#                 cheapest_store = store
#                 cheapest_price = price

# # Выводим результат
# print(f"{cheapest_product}: {cheapest_store}")

# import csv

# # Открываем файл
# with open('prices.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=';')
#     next(reader)  # Пропускаем заголовок

#     # Инициализируем переменные для хранения самого дешевого продукта и магазина
#     cheapest_product = None
#     cheapest_store = None
#     cheapest_price = float('inf')  # Изначально устанавливаем очень большую цену

#     # Перебираем строки файла
#     for row in reader:
#         store = row[0]  # Название магазина

#         # Перебираем цены на продукты в текущей строке
#         for i in range(1, len(row)):
#             product = row[i]  # Название продукта

#             # Пропускаем названия магазинов в столбцах
#             if ':' in product:
#                 continue

#             price = int(row[i])  # Цена продукта

#             # Если текущая цена меньше самой дешевой цены, обновляем значения
#             if price < cheapest_price:
#                 cheapest_product = product
#                 cheapest_store = store
#                 cheapest_price = price

# # Выводим результат
# print(f"{cheapest_product}: {cheapest_store}")

#===

# import csv

# # Открываем файл
# with open('prices.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=';')
#     next(reader)  # Пропускаем заголовок

#     # Инициализируем переменные для хранения самого дешевого продукта и магазина
#     cheapest_product = None
#     cheapest_store = None
#     cheapest_price = float('inf')  # Изначально устанавливаем очень большую цену

#     # Перебираем строки файла
#     for row in reader:
#         store = row[0]  # Название магазина

#         # Перебираем цены на продукты в текущей строке
#         for i in range(1, len(row)):
#             product = row[i]  # Название продукта

#             # Пропускаем названия магазинов в столбцах
#             if ':' in product:
#                 continue

#             price = int(row[i])  # Цена продукта

#             # Если текущая цена меньше самой дешевой цены, обновляем значения
#             if price < cheapest_price:
#                 cheapest_product = product
#                 cheapest_store = store
#                 cheapest_price = price

# # Выводим результат
# print(f"Вареники: {cheapest_store}")

#===

# import json

# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

# json_countries = json.dumps(countries, indent = 3, separators=(',', ' - '), sort_keys=True)
# print(json_countries)

#===

# import json

# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }

# data_json = json.dumps(words, skipkeys=True)
# print(data_json)

#===


# import sys

# nums1 = [1, 2, 3]
# nums2 = nums1
# nums3 = [nums1, nums2]

# del nums1

# print(sys.getrefcount(nums2))

#=== Обработка исключений

# total = 0

# with open('data.txt', 'r', encoding='utf-8') as file:
#     for _ in range(len(file.readlines())):
#         total += 1

# print(total)

#===

# def swapcase_vowels(string):
#     vowels = 'aeiouy'
#     swapped_string = ''

#     for char in string:
#         if char in vowels:
#             swapped_string += char.upper() 
#         else:
#             swapped_string += char

#     return swapped_string


# swapcase_vowels('hello worldj')

#===

# a = int(input())
# b = int(input())
# numbers = []

# for i in range(a, b + 1):
#     if i % 7 == 0:
#         numbers.append(i)

# print(numbers)

#===

# def get_max_index(numbers):
#     max_index = 0
#     max_value = numbers[0]

#     for index, value in enumerate(numbers): 
#         if value > max_value:
#             max_index = index
#             max_value = value

#     return max_index

#===

# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, 
#               {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#               {'Comments': 4, 'Shares': 2}, 
#               {'Photos': 8, 'Comments': 1, 'Shares': 1}, 
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]

# total_likes = 0

# for post in blog_posts:
#     try:
#         total_likes += post['Likes']
#     except:
#         total_likes += -1

# print(total_likes)

#===

# food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
# fifth = []

# for x in food:
#     try:
#         fifth.append(x[4])
#     except:
#         fifth.append('_')
# print(fifth)

#===

# numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

# remainders = []

# for number in numbers:
#     try:
#         remainders.append(36 % number)
#     except:
#         pass

# print(remainders)

#===

# import sys

# nums = sys.stdin.readlines()
# res = 0
# other = []

# for num in nums:
#     try:
#         res += int(num)
#     except (ValueError, TypeError):
#         try:
#             res += float(num)
#         except ValueError:
#             other.append(num)
        
# print(res)
# print(len(other))

#===

# import calendar
# months = dict(zip([num for num in range(1, 13)], calendar.month_name[1:]))
# print(months)
# s = input()
# try:
#     print(months[int(s)])
# except ValueError:
#     print('Введено некорректное значение')
# except KeyError:
#     print('Введено число из недопустимого диапазона')

#===

# import string
# a, s = input(), input()
# alp = string.ascii_lowercase
# base = dict(zip(alp, a))
# res = ''
# for c in s:
#     if c.lower() in alp:
#         res += base[c.lower()]
#     else:
#         res += c
# print(res)

#===

# import json

# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
# clubs = [club1, club2, club3]

# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(clubs, file, indent=3)

#===

# import json

# specs = {
#          'Модель': 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }

# specs_json = json.dumps(specs, indent=3, ensure_ascii=False)

# print(specs_json)

#===

# import json
# def is_correct_json(string):
#     try:
#         json.loads(string) 
#         return True
#     except ValueError:
#         return False

# data = '''{
#         "beegeek": 2018,
#         "stepik": 2013
#        }'''
# print(is_correct_json('["beegeek", 1, 2, 3]'))

#===

# import json
# import sys

# for k, v in json.load(sys.stdin).items():
#     if type(v) != list:
#         print(f'{k}: {v}')
#     else:
#         print(f'{k}: {", ".join(map(str,v))}')

#===

# from zipfile import ZipFile

# with ZipFile('test.zip') as zip_file:
#     zip_file.printdir()

# from zipfile import ZipFile

# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time) 

# from zipfile import ZipFile

# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(*info, sep='\n')


# from zipfile import ZipFile

# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()                # получаем названия всех файлов архива
#     last_file = zip_file.getinfo(info[-4])    # получаем информацию об отдельном файле
#     print(last_file.file_size)
#     print(last_file.compress_size)
#     print(last_file.filename)
#     print(last_file.date_time)

#===
# from zipfile import ZipFile

# with ZipFile('workbook.zip') as zip_file:
#     count = 0
#     info = zip_file.infolist()
#     for i in info:
#         if not i.is_dir():
#             count += 1
#     print(count)
            
#===

# from zipfile import ZipFile

# with ZipFile('workbook.zip') as zip_file:
#     uncompressed_size = 0
#     compressed_size = 0
#     for i in zip_file.infolist():
#         if not i.is_dir():
#             uncompressed_size += i.file_size
#             compressed_size += i.compress_size
#     print(f"Объем исходных файлов: {uncompressed_size} байт(а)")
#     print(f"Объем сжатых файлов: {compressed_size} байт(а)")

#===

# import zipfile

# def calculate_compression_ratio(file_size, compressed_size):
#     if file_size == 0:
#         return 0
#     return (file_size - compressed_size) / file_size * 100

# def find_best_compression_ratio(file_path):
#     best_ratio = None
#     best_file = None

#     with zipfile.ZipFile(file_path, 'r') as zip_ref:
#         for file_info in zip_ref.infolist():
#             ratio = calculate_compression_ratio(file_info.file_size, file_info.compress_size)
#             if best_ratio is None or ratio > best_ratio:
#                 best_ratio = ratio
#                 best_file = file_info.filename

#     return best_file

# archive_path = 'workbook.zip'
# best_file = find_best_compression_ratio(archive_path)
# best = best_file[best_file.find('/') + 1:]

# # print(f"The file with the best compression ratio is: {best}")
# print(best)

#===

# from zipfile import ZipFile
# from datetime import datetime

# # Функция для проверки, был ли файл создан или изменен позднее указанной даты
# def check_date(fileinfo, date_str):
#     timestamp = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").timestamp()
#     return fileinfo.date_time > (timestamp, 0)

# # Открытие архива и получение списка файлов, удовлетворяющих условию
# with ZipFile("workbook.zip") as zip_file:
#     file_list = [name.split("/")[-1] for name in zip_file.namelist() if not name.endswith("/") and check_date(zip_file.getinfo(name), "2021-11-30 14:22:00")]

# # Сортировка списка файлов
# file_list = sorted(file_list)

# # Вывод списка файлов по одному на строке
# for name in file_list:
#     print(name)

#===

# import json

# # открытие файла data.json и чтение списка объектов
# with open("data.json", encoding="utf-8") as file:
#     data = json.load(file)

# # цикл по всем объектам списка
# for i, obj in enumerate(data):
#     # проверка типа объекта и выполнение нужной операции
#     if isinstance(obj, str):
#         data[i] += "!"
#     elif isinstance(obj, bool):
#         data[i] = not obj
#     elif isinstance(obj, int):
#         data[i] += 1
#     # elif isinstance(obj, bool):
#     #     data[i] = not obj
#     elif isinstance(obj, list):
#         data[i] *= 2
#     elif isinstance(obj, dict):
#         data[i]["newkey"] = None
#     elif obj is None:
#        pass  # ничего не делаем
# res = list(filter(lambda x: x is not None, data))
# # запись обновленного списка в файл updated_data.json
# with open("updated_data.json", "w", encoding="utf-8") as file:
#     json.dump(res, file, indent=3, ensure_ascii=True)


#===

# from zipfile import ZipFile
# from datetime import datetime


# # функция для проверки, был ли файл создан или изменен позднее указанной даты
# def check_date(fileinfo, date_str):
#     date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
#     return datetime(*fileinfo.date_time) > date

# # открытие архива и получение списка файлов, удовлетворяющих условию
# with ZipFile("workbook.zip") as zip_file:
#     file_list = sorted([name for name in zip_file.namelist() if not name.endswith("/") and check_date(zip_file.getinfo(name), "2021-11-30 14:22:00")])
#     res = [name.split("/")[-1] for name in file_list]
# for name in sorted(res):
#     print(name)

# ===

# import string 
# for l in string.ascii_lowercase:
#     print(l)

# ===

# def convert(number):
#     if number >= 0:
#         return (str(bin(number))[2:], str(oct(number))[2:], str(hex(number))[2:].upper())
#     else:
#         return ('-' + str(bin(number))[3:], '-' + str(oct(number))[3:], '-' + (str(hex(number))[3:]).upper())


# print(convert(-15))

# print(convert(1))

# ===

# films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
#          'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
#          'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
#          'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
#          'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
#          'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
#          'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
#          'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
#          'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
#          'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
#          'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}


# lst = []
# for k, v in films.items():
#     val = []
#     for i, j in v.items():
#         val.append(j)
#     lst.append([k, val])
# average = list(map(lambda x: (x[0], float(sum(x[1])/2)), lst))
# print(sorted(average, key=lambda x: x[1])[0][0])

# ===

# def non_negative_even(numbers):
#     if all(map(lambda x: True if x % 2 == 0 and x >= 0 else False, numbers)):
#         return True
#     else:
#         return False
    

# print(non_negative_even([0, 2, 4, 8, 16]))
# print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))

# ===

# def is_greater(lists, number):
#     if any(map(lambda x: True if sum(x) > number else False, lists)):
#         return True
#     else:
#         return False
    
# data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]

# print(is_greater(data, 10))
# data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

# print(is_greater(data, 2))

# ===

    
# def custom_isinstance(objects, typeinfo):
#     counter = 0
#     if type(typeinfo) != tuple:
#         for object in objects:
#             if isinstance(object, typeinfo):
#                 counter += 1
#     else:
#         for object in objects:
#             if type(object) in typeinfo:
#                 counter += 1
#     return counter

# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, int))
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, (int, float)))

# ===

# numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]

# print(numbers.index(max(numbers)))

# ===

# def my_pow(number):
#     res = 0
#     for i, j in enumerate(str(number), 1):
#         res += int(j)**i
#     return res

# print(my_pow(139))
# print(my_pow(123))

# ===

# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

# profit = [i[1] - i[0] for i in list(zip(budgets, box_offices))]
# result = dict(zip(names, profit))
# for k, v in sorted(result.items()):
#     print(f'{k}: {v}$')

# ===

# def add_to_list_in_dict(data, key, element):
#     try:
#         if isinstance(data[key], list):
#             data[key].append(element)
#         else:
#             data[key] = [data[key], element]
#     except KeyError:
#         data[key] = [element]
#     return data

# # data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# # add_to_list_in_dict(data, 'b', 7)
# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'c', 7)
# print(data)

# ===

# try:
#     with open(input(), 'r', encoding='UTF-8') as file:
#         for f in file.readlines():
#             print(f.rstrip())
# except: 
#     print('Файл не найден')

# ===

# import pickle

# dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}

# with open('dogs.pkl', mode='wb') as file:
#     pickle.dump(dogs, file)

# ===

# import sys
# def check_coords(coords):
#     data = [tuple(c) for c in coords]
#     # base = list(map(lambda x: True if -90 < int(x[0]) < 90 and -180 < int(x[1]) < 180 else False, data))
#     return data


# coordinates = [s.rstrip() for s in sys.stdin.readlines()]
# res = [tuple(s) for s in coordinates]
# print(coordinates)
# print(res)

# ===

# def zip_longest(*args, fill = None):
#     max_len = 0
#     for i in args:
#         if len(i) > max_len:
#             max_len = len(i)
#     for i in args:
#         while len(i) < max_len:
#             i.append(fill)
#     zipped = zip(*args)
#     return list(zipped)


# zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_')
# data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
# print(zip_longest(*data))

# ===

# result = sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))
# result = ''.join(result)
# print(result)

# ===

# def hash_as_key(objects):
#     result = {}
#     for obj in objects:
#         key = hash(obj)
#         if key not in result:
#             result[key] = obj
#         else:
#             if not isinstance(result[key], list):
#                 result[key] = [result[key]]
#             result[key].append(obj)
#     return result

# data = [1, 2, 3, 4, 5, 5]

# print(hash_as_key(data))

# ===

# s = eval(input())
# if isinstance(s, list):
#     print(s[-1])
# elif isinstance(s, tuple):
#     print(s[0])
# else:
#     print(len(s))

# ===

# import sys
# print(max([eval(expression) for expression in sys.stdin.readlines()]))

# ===

# f = input()
# stub = input().split()
# int_stub = [int(i) for i in stub]
# results = [eval(f) for x in range(int_stub[0], int_stub[1]+1)]
# print(f'Минимальное значение функции {f} на отрезке [{stub[0]}; {stub[1]}] равно {min(results)}')
# print(f'Максимальное значение функции {f} на отрезке [{stub[0]}; {stub[1]}] равно {max(results)}')

# ===

# import json

# with open('data1.json') as file1:
#     data1 = json.load(file1)
# with open('data2.json') as file2:
#     data2 = json.load(file2)

# data3 = {}
# for k1, v1 in data1.items():
#     for k2, v2 in data2.items():
#         if k1 not in data2:
#             data3[k1] = v1
#         elif k1 == k2:
#             data3[k1] = v2
#         elif k2 not in data1:
#             data3[k2] = v2

# # print(data3)

# with open('data_merge.json', 'w') as file3:
#     json.dump(data3, file3, indent=3)

# ===

# import json

# with open('people.json') as file:
#     data = json.load(file)

# all_keys = set()

# for dict in data:
#     for k in dict.keys():
#         all_keys.add(k)
# for k in list(all_keys):
#     for dict in data:
#         if k not in dict:
#             dict[k] = None

# with open('updated_people.json', 'w') as file1:
#     json.dump(data, file1, indent=3)

# import json

# with open('countries.json') as file:
#     data = json.load(file)
# relig_dict = {}
# for d in data:
#     relig = d['religion']
#     country = d['country']
#     relig_dict.setdefault(relig, []).append(country)

# with open('religion.json', 'w') as file1:
#     json.dump(relig_dict, file1, indent=3)

# ===

# import csv
# import json

# adm = {}
# with open('playgrounds.csv', encoding='UTF-8') as file:
#     rows = csv.reader(file, delimiter=';')
#     data = []
#     for row in rows:
#         data.append(row)
#     for ObjectName, AdmArea, District, Address in data[1:]:
#         adm.setdefault(AdmArea, {}).setdefault(District, []).append(Address)    
# with open('addresses.json', 'w', encoding='UTF-8') as file1:
#     json.dump(adm, file1, indent=3, ensure_ascii=False)

# ===

# import json
# import csv

# with open('students.json') as file:
#     data = json.load(file)
# columns = ['name', 'phone']
# base = []
# for d in data:
#     lst = []
#     if d['progress'] >= 75 and d['age'] >= 18:
#         lst.append(d['name'])
#         lst.append(d['phone'])
#     if lst:
#         base.append(lst)
# with open('data.csv', 'w', encoding='UTF-8', newline='') as file1:
#     writer = csv.writer(file1)
#     writer.writerow(columns)
#     for row in sorted(base, key=lambda x: x[0]):
#         writer.writerow(row)

# ===

# import json
# from datetime import time
# t_start = time(10, 0, 0)
# t_end = time(12, 0, 0)

# with open('pools.json', 'r', encoding='UTF-8') as file:
#     data = json.load(file)
# lenghts = []
# widths = []
# max_lenght = 0
# max_width = 0
# for p in data:
#     t = (p['WorkingHoursSummer']['Понедельник']).split('-')
#     t_ss = t[0].split(':')
#     t_se = t[1].split(':')
#     if time(int(t_ss[0]), int(t_ss[1], 0)) <= t_start and time(int(t_se[0]), int(t_se[1], 0)) >= t_end:
#         if p['DimensionsSummer']['Length'] > max_lenght:
#             max_lenght = p['DimensionsSummer']['Length']
#             lenghts.append(max_lenght)
#             if p['DimensionsSummer']['Width'] > max_width:
#                 max_width = p['DimensionsSummer']['Width']
#                 widths.append(max_width)
# results = []
# for p in data:
#     t = (p['WorkingHoursSummer']['Понедельник']).split('-')
#     t_ss = t[0].split(':')
#     t_se = t[1].split(':')
#     if time(int(t_ss[0]), int(t_ss[1], 0)) <= t_start and time(int(t_se[0]), int(t_se[1], 0)) >= t_end:
#         if p['DimensionsSummer']['Length'] == max_lenght:
#             r = []
#             r.append(p['DimensionsSummer']['Width'])
#             r.append(p['DimensionsSummer']['Length'])
#             r.append(p['Address'])
#             results.append(r)
# res = sorted(results, key=lambda x: x[2], reverse=True)
# print(f'{res[0][1]}x{res[0][0]}')
# print(res[0][2])

# ===

# import csv
# import json
# from datetime import datetime

# data = []
# with open('exam_results.csv', encoding='UTF-8') as file:
#     rows = csv.DictReader(file, delimiter=',')
#     for row in rows:
#         data.append(row)
# base = sorted(data, key=lambda x:x['email'])
# scores = []
# student = {}
# for d in base:
#     student.setdefault(d['email'], {}).setdefault(int(d['score']), []).append(d['date_and_time'])
#     scores.append(student)
# res = {}
# for k, v in student.items():
#     dates = []
#     for i in max(v.values()):
#         dates.append(datetime.strptime(i, '%Y-%m-%d %H:%M:%S'))
#     res.setdefault(k, {}).setdefault(max(v), max(dates).strftime('%Y-%m-%d %H:%M:%S'))
# result = []
# for k, v in res.items():
#     end = {}
#     for z in base:
        
#         zem = k
#         zsc = str(list(v.keys())[0])
#         zdt = list(v.values())[0]
#         if z['email'] == k and z['score'] == str(list(v.keys())[0]) and z['date_and_time'] == list(v.values())[0]:
#            end['name'] = z['name']
#            end['surname'] = z['surname'] 
#            end['best_score'] = z['score']
#            end['date_and_time'] = z['date_and_time']
#            end['email'] = z['email']
#     result.append(end)

# with open('best_scores.json', 'w', encoding='UTF-8') as file1:
#     json.dump(result, file1, indent=3, ensure_ascii=False)

    
# +++++

# import csv
# import json
# from datetime import datetime

# with open('exam_results.csv', encoding='UTF-8') as file:
#     rows = csv.DictReader(file, delimiter=',')
#     data = [row for row in rows]
# base = sorted(data, key=lambda x:x['email'])
# student = {}
# scores = [student.setdefault(d['email'], {}).setdefault(int(d['score']), []).append(d['date_and_time']) for d in base]

# res = {}
# for k, v in student.items():
#     dates = []
#     for i in max(v.values()):
#         dates.append(datetime.strptime(i, '%Y-%m-%d %H:%M:%S'))
#     res.setdefault(k, {}).setdefault(max(v), max(dates).strftime('%Y-%m-%d %H:%M:%S'))
# result = []
# for k, v in res.items():
#     end = {}
#     for z in base:
#         zem = k
#         zsc = str(list(v.keys())[0])
#         zdt = list(v.values())[0]
#         if z['email'] == k and z['score'] == str(list(v.keys())[0]) and z['date_and_time'] == list(v.values())[0]:
#            end['name'] = z['name']
#            end['surname'] = z['surname'] 
#            end['best_score'] = int(z['score'])
#            end['date_and_time'] = z['date_and_time']
#            end['email'] = z['email']
#     result.append(end)

# with open('best_scores.json', 'w', encoding='UTF-8') as file1:
#     json.dump(result, file1, indent=3, ensure_ascii=False)  

# ===

# import json

# with open('food_services.json', 'r', encoding='UTF-8') as file:
#     data = json.load(file)
# res = {}
# for d in data:
#     res.setdefault(d['District'], []).append(d['Name'])
# districts = []
# for k, v in res.items():
#     count = {}
#     count[k] = len(v)
#     districts.append(count)
# v_max = 0
# for d in districts:
#     if list(d.values())[0] > v_max:
#         v_max = list(d.values())[0]
# for d in districts:
#     if v_max in d.values():
#         dist = d
# nets = []
# rest = {}
# for z in data:
#     zdist = list(dist.keys())[0]
#     if z["IsNetObject"] == 'да':
#         rest.setdefault(z['OperatingCompany'], []).append(z['Name'])
# count_rest = {}
# for k, v in rest.items():
#     count_rest[k] = len(v)
# r_max = 0
# for k, v in count_rest.items():
#     if v > r_max:
#         r_max = v
# for k, v in dist.items():
#     print(f'{k}: {v}')
# for k, v in count_rest.items():
#     if v == r_max:
#         print(f'{k}: {v}')

# ===

# import json

# with open('food_services.json', 'r', encoding='UTF-8') as file:
#     data = json.load(file)
# dct = {}
# for d in data:
#     dct.setdefault(d['TypeObject'], {}).setdefault(d['Name'], {}).setdefault(d['SeatsCount'], d['Address'])
# seats = []
# for k, v in dct.items():
#     max_seats = 0
#     for k1, v1 in v.items():
#         for k2, v2 in v1.items():
#             if k2 > max_seats:
#                 max_seats = k2
#     seats.append(max_seats)
# rests = []
# for index, (k, v) in enumerate(dct.items()):
#     for k1, v1 in v.items():
#         values = list(v1.keys())
#         if seats[index] in values:
#             rest = k1
#             ret = f'{k}: {rest}, {seats[index]}'
#             rests.append(ret)
# print(*sorted(rests), sep='\n')

# ===

# from zipfile import ZipFile
# from datetime import datetime

# with ZipFile('workbook.zip') as zip_file:
#     info = ZipFile.infolist(zip_file)
# files = [file for file in info if file.is_dir() == False]
# files_not_dirs = [list(map(lambda x: [x.filename, x.date_time, x.file_size, x.compress_size] if '/' not in x.filename else [x.filename[x.filename.find('/')+1:], x.date_time, x.file_size, x.compress_size], files))]

# for f in files_not_dirs:
#     for file in sorted(f):
#         print(f'{file[0]}' + '\n' + f'  Дата модификации файла: {datetime(*file[1])}' + '\n' + f'  Объем исходного файла: {file[2]} байт(а)' + '\n' + f'  Объем сжатого файла: {file[3]} байт(а)')
#         print()   

# ===

# from zipfile import ZipFile

# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

# with ZipFile('files.zip', mode='w') as zip_file:
#     for f in file_names:
#         zip_file.write(f, arcname=None)

# ===

# from zipfile import ZipFile

# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
# for file_name in file_names:
#     with open(file_name, 'rb') as file:
#         bytes_count = len(file.read())
#         if bytes_count <= 100:
#             with ZipFile('files.zip', 'a') as zip_file:
#                 zip_file.write(file.name, arcname=file.name)

# ===

# from zipfile import ZipFile

# def extract_this(zip_name, *args):
#     if args:
#         with ZipFile(zip_name) as zip_file:
#             for f in args:
#                 zip_file.extract(f)
#     else:
#         with ZipFile(zip_name) as zip_file:
#             zip_file.extractall()

# ===

# import json
# from zipfile import ZipFile


# def is_correct_json(string):
#     try:
#         data = json.dumps(string) 
#         return True
#     except ValueError:
#         return False
    

# with ZipFile('data.zip') as zip_file:
#     info = ZipFile.infolist(zip_file)
#     files = [file for file in info if file.is_dir() == False]
#     files_with_dirs = list(map(lambda x: x.filename, files))
#     jfiles = []
#     for filewd in files_with_dirs:
#         try:
#             with zip_file.open(filewd) as jfile:
#                 interlayer = jfile.read().decode('utf-8')
#                 inter = json.loads(interlayer)
#                 if is_correct_json(interlayer):
#                     jfiles.append(inter)
#                 else:
#                     continue
#         except:
#             continue
# arsenal_players = [[d['first_name'], d['last_name']] for d in jfiles if d['team'] == 'Arsenal']
# result = sorted(arsenal_players, key=lambda x: x[0])

# for p in result:
#     print(f'{p[0]} {p[1]}')

# ===

# from zipfile import ZipFile

# with ZipFile('desktop.zip') as zip_file:

# import os
# import zipfile


# def get_size(size):
#     size_rounded = round(int(size) / 1024, 0)
#     if size_rounded == 0:
#         return str(size) + " B"
#     if size_rounded >= 1024:
#         size_rounded = round(size / 1024 / 1024, 0)
#         return str(int(size_rounded)) + " MB"
#     return str(int(size_rounded)) + " KB"

# with zipfile.ZipFile('desktop.zip', 'r') as zip_ref:
#     for entry in zip_ref.infolist():
#         file_path_in_zip = entry.filename
#         nesting_level = file_path_in_zip.count('/') - 1
#         file_name = entry.filename
#         if '.' not in file_name:
#             file_name = entry.filename
#             while file_name.count('/') > 1:
#                 file_name = file_name[file_name.find('/')+1:]
#             print(' ' * (nesting_level * 2) + file_name[:-1])
#         else:
#             while file_name.count('/') > 0:
#                 file_name = file_name[file_name.find('/')+1:]
#             try:
#                 print(' ' * (nesting_level * 2 + 2) + file_name, get_size(entry.file_size))
#             except FileNotFoundError as e:
#                 print(' ' * (nesting_level * 2) + file_name, 'File not found in archive:', e.filename) 

# ===

# import pickle
# import sys

# with open(input(), 'rb') as file:
#     obj = pickle.load(file) 
#     data = list(map(lambda x: x.strip(), sys.stdin))
#     obj(*data)

# ===

# import pickle
# def filter_dump(filename, objects, typename):
#     data = [x for x in objects if isinstance(x, typename)]
#     with open(filename, 'wb') as file:
#         pickle.dump(data, file)

# typename = int
# object = [1,2,3,"d"]
# name = "some_file"
# filter_dump(name, object, typename)

# ===

# import pickle

# file_name, сhecksum = input(), int(input())
# with open(file_name, 'rb') as file:
#     data = pickle.load(file)
# if isinstance(data, dict):
#     my_keys = [x for x in data.keys() if isinstance(x, int)] 
#     if my_keys:
#         my_sum = sum(my_keys)
#     else:
#         my_sum = 0    
# else:
#     my_lst = [x for x in data if isinstance(x, int)]
#     if my_lst:
#         my_sum = min(my_lst) * max(my_lst)
#     else:
#         my_sum = 0 

# if сhecksum == my_sum:
#     print('Контрольные суммы совпадают')
# else:
#     print('Контрольные суммы не совпадают')

# ===

# from collections import namedtuple

# Resolution = namedtuple('Resolution', ['horizontal', 'vertical'])

# full_hd = Resolution(1920, 1070)

# full_hd = full_hd._replace(vertical=1080)

# print(full_hd.vertical)

# =

# from collections import namedtuple

# PcHardware = namedtuple('PcHardware', 'cpu,gpu,motherboard,ram', defaults=[None, None])

# print(PcHardware._field_defaults)

# =

# from collections import namedtuple

# App = namedtuple('App', ['name', 'apptype', 'size'])

# app = App._make('Discord messenger 200'.split())

# print(*app)

# =

# from collections import namedtuple

# Device = namedtuple('Device', ['devicetype', 'model'])

# device1 = Device(**{'devicetype': 'keyboard', 'model': 'Logitech G213'})
# device2 = Device(*{'devicetype': 'keyboard', 'model': 'Logitech G213'})

# print(*device1, sep=', ')
# print(*device2, sep=', ')

# ===

# from collections import namedtuple

# Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])

# ===

# from collections import namedtuple

# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

# ===
 
# from collections import namedtuple
# import pickle
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
# with open('data.pkl', 'rb') as file:
#     animals = pickle.load(file)
# for animal in animals:
#     for field, value in zip(Animal._fields, animal):
#         print(f'{field}: {value}')
#     print()

# ===

# from collections import namedtuple

# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

# def sort_function(user):
#     plan_score = {'Gold': 3, 'Silver': 2, 'Bronze': 1, 'Basic': 0}
#     return (-plan_score[user.plan], user.email)

# users_sorted = sorted(users, key=sort_function)

# for user in users_sorted:
#     print(f"{user.name} {user.surname}")
#     print(f"  Email: {user.email}")
#     print(f"  Plan: {user.plan}")
#     print()

# ===

# import csv
# from datetime import datetime

# def read_meetings(filename):
#     meetings = []
#     with open(filename, 'r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         next(reader)  # пропускаем заголовок
#         for row in reader:
#             surname = row[0]
#             name = row[1]
#             date_time_str = row[2] + ' ' + row[3]  # объединяем дату и время
#             date_time = datetime.strptime(date_time_str, '%d.%m.%Y %H:%M')
#             meetings.append((surname, name, date_time))
#     return meetings

# def print_sorted_meetings(meetings):
#     sorted_meetings = sorted(meetings, key=lambda x: x[2])  # сортируем по дате и времени
#     for meeting in sorted_meetings:
#         print(meeting[0], meeting[1])

# filename = 'meetings.csv'
# meetings = read_meetings(filename)
# print_sorted_meetings(meetings)

# ===

# from collections import defaultdict

# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]

# product_income = defaultdict(int)
# for product, income in data:
#     product_income[product] += income
    
# for product in sorted(product_income):
#     print(f"{product}: ${product_income[product]}")

# === 

# from collections import defaultdict

# staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

# depart_employee = defaultdict(int)
# for depart, employee in staff:
#     depart_employee[depart] += 1

# for depart in sorted(depart_employee):
#     print(f'{depart}: {depart_employee[depart]}')

# ===

# from collections import defaultdict

# staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'), ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'), ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'), ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'), ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'), ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'), ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'), ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Dale Houston')]

# depart_employee = defaultdict(set)
# for depart, employee in staff_broken:
#     depart_employee[depart].add(employee)

# for depart in sorted(depart_employee):
#     value = sorted(depart_employee[depart])
#     print(f"{depart}: {', '.join(value)}")

# ===

# from collections import defaultdict
# def wins(pairs):
#     winner_loser = defaultdict(set) 
#     for winner, loser in pairs:
#         winner_loser[winner].add(loser)
#     return winner_loser

# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))

# ===

# from collections import defaultdict

# def flip_dict(dict_of_lists):
#     dict_flip = defaultdict(list)
#     for k, v in dict_of_lists.items():
#         for i in v:
#             dict_flip[i].append(k)
#     return dict_flip

# print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

# ===

# from collections import defaultdict

# def best_sender(messages, senders):
#     sender_word_count = defaultdict(int)  # словарь со значением по умолчанию 0 для подсчета слов

#     for message, sender in zip(messages, senders):
#         word_count = len(message.split())
#         sender_word_count[sender] += word_count

#     max_word_count = max(sender_word_count.values())
#     best_senders = [sender for sender, count in sender_word_count.items() if count == max_word_count]
#     best_sender_name = max(best_senders)
    
#     return best_sender_name


    
# messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
# senders = ['Bob', 'Charlie']
# print(best_sender(messages, senders))

# ===

# from collections import OrderedDict

# data = OrderedDict(key1='value1')

# data['key2'] = 'value2'
# data['key3'] = 'value3'

# for key, value in data.items():
#     print(f'{key} -> {value}')

# =

# from collections import OrderedDict

# cloth = OrderedDict({'name': 'pants', 'size': 'm', 'color': 'grey'})

# cloth['name'] = 'shirt'
# cloth.update(size='s')

# for key, value in cloth.items():
#     print(f'{key}: {value}')

# =

# country1 = dict(name='Finland', capital='Helsinki', currency='euro')
# country2 = dict(capital='Helsinki', name='Finland', currency='euro')

# print(country1 == country2)

# =

# from collections import OrderedDict

# planets1 = OrderedDict(Mercury=None, Venues=2, Earth=None, Mars=4, Jupiter=5)
# planets2 = OrderedDict(Mercury=1, Saturn=6, Uranus=7, Neptune=8, Earth=3)

# solar_system = planets1 | planets2

# print(*solar_system)

# = 

# from collections import OrderedDict

# flower = OrderedDict([('name', 'Rose'), ('family', 'Rosaceae'), ('kingdom', 'Plantae')])

# flower.move_to_end('family')

# for key, value in flower.items():
#     print(f'{key}: {value}')

# =

# from collections import OrderedDict

# vector = OrderedDict(x=3, y=4, module=5)

# print(*reversed(vector))

# ===

# from collections import OrderedDict

# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

# reversed_data = OrderedDict(reversed(list(data.items())))

# print(reversed_data)

# ===
# from collections import OrderedDict

# grades = OrderedDict(Timur=100, Arthur=84, Anri=94, Dima=98)
# new_grades = OrderedDict()

# for rule in (True, False, False, True):
#     name, grade = grades.popitem(last=rule)
#     new_grades[name] = grade
    
# print(*new_grades)

# =

# from collections import OrderedDict
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
# new_data = OrderedDict()
# for i in range(1, len(data)+1):
#     if i % 2 == 0:
#         key, value = data.popitem(last=True)
#         new_data[key] = value
#     else:
#         key, value = data.popitem(last=False)
#         new_data[key] = value
# output_data = OrderedDict(list(new_data.items()))
# print(output_data)

# ===

# from collections import OrderedDict

# data = OrderedDict({'Law & Order': 1990, 'The Practice': 1997, 'Six Feet Under': 2001, 'Joan of Arcadia': 2003, 'The West Wing': 1999, 'Deadwood': 2004, 'The Sopranos': 1999, 'Boston Legal': 2004, 'ER': 1994, 'Friday Night Lights': 2006, '24': 2001, 'Heroes': 2006, 'Lost': 2004, 'Dexter': 2006, 'Damages': 2007, 'Big Love': 2006, 'House': 2004, 'Downton Abbey': 2010, "Grey's Anatomy": 2005, 'Homeland': 2011, 'Breaking Bad': 2008, 'Game of Thrones': 2011, 'CSI: Crime Scene Investigations': 2000, 'Boardwalk Empire': 2010, 'True Blood': 2008, 'House of Cards': 2013, 'True Detective': 2014})

# data.sorted_keys = lambda reverse=False: sorted(data.keys(), reverse=reverse)
# data.sorted_values = lambda reverse=False: sorted(data.values(), reverse=reverse)
# print(data.sorted_values(reverse=True))
# print(data.sorted_keys())

# ===

# from collections import OrderedDict

# def custom_sort(ordered_dict, by_values=False):
#     if by_values:
#         for value in OrderedDict(sorted(ordered_dict.items(), key=lambda item: item[1])):
#             ordered_dict.move_to_end(value)
#     else:
#         for key in sorted(ordered_dict):
#             ordered_dict.move_to_end(key)
#     return ordered_dict

# # data = OrderedDict([('Dustin', 29), ('Anabel', 17), ('Brian', 40), ('Carol', 16)])
# # print(custom_sort(data))

# # print(data)

# data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
# print(custom_sort(data, by_values=True))

# print(*data.items())

# ===

# from collections import Counter

# browsers = Counter(['Firefox', 'Chrome', 'Edge', 'Edge' 'Chrome', 'Firefox', 'Opera', 'Yandex', 'Chrome'])

# print(browsers['Firefox'])

# =

# from collections import Counter

# counter = Counter({1: 11, 2: 22, 3: 33})

# print(max(counter.keys()) + min(counter.values()))

# =

# from collections import Counter

# pets = Counter(cat=3, dog=3, fox=2, hamster=1)

# print(pets['elephant'])
# print(*pets)

# =

# from collections import Counter

# letters = Counter(set('Beautiful is better than ugly'))

# print(letters['t'])

# = 

# from collections import Counter

# vegetables = Counter({'cabbage': 10, 'pepper': 7, 'pumpkin': 4})

# vegetables.update(['pepper', 'pepper', 'pepper'])

# print(vegetables['pepper'])

# =

# from collections import Counter

# vegetables1 = Counter({'cabbage': 'ten', 'pepper': 'seven', 'pumpkin': 'four'})
# vegetables2 = Counter({'cabbage': 3, 'pepper': 2})

# vegetables1.update(vegetables2)

# print(vegetables1['pepper'])

# = 

# from collections import Counter

# vegetables = Counter({'cabbage': 10, 'pepper': 'seven', 'pumpkin': 'four'})

# vegetables.update({'cabbage': 5, 'pepper': 'two'})

# print(vegetables['pepper'])
# print(vegetables['cabbage'])

# =

# from collections import Counter

# clothes = Counter([('shirt', 3), ('dress', 1), ('shirt', 3)])

# print(clothes['shirt'])

# =

# from collections import Counter

# letters1 = Counter('abcd')
# letters2 = Counter('abcd')

# letters2.update(e=0)

# print(letters1 == letters2)

# ===

# from collections import Counter

# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

# ext_files = list(map(lambda x: x[x.find('.')+1:], files))
# result = Counter(ext_files)
# for k, v in sorted(result.items()):
#     print(f'{k}: {v}')

# ===

# from collections import Counter

# def count_occurences(word, words):
#     counts = Counter(list(map(lambda x: x.lower(), words.split())))
#     return counts[word.lower()]

# word = 'python'
# words = 'Python Conferences python training python events'

# print(count_occurences(word, words))

# ===

# from collections import Counter

# products = Counter(input().split(','))
# for product, count in sorted(products.items()):
#     print(f'{product}: {count}')

# ===

# from collections import Counter

# products = Counter(input().split(','))
# max_len = max(list(map(lambda x: len(x), products.keys())))
# for key, value in sorted(products.items()):
#     price_per_item = [ord(letter) for letter in key if letter != ' ']
#     total_price = sum(price_per_item) * value
#     print(f"{key + ' ' * (max_len - len(key))}: {sum(price_per_item)} UC x {value} = {total_price} UC")

# ===

# import string
# from collections import Counter

# with open('pythonzen.txt', 'r', encoding='UTF-8') as file:
#     edit_text = [x.strip() for x in file.readlines()]
# letters = [letter.lower() for letter in ' '.join(edit_text) if letter in string.ascii_letters]
# number_of_letters = Counter(''.join(letters))
# for letter, count in sorted(number_of_letters.items()):
#     print(f"{letter}: {count}")

# ===

# from collections import Counter

# money = Counter({'rub': 1000, 'eur': 2000, 'usd': 2000, 'uah': 1900, 'cad': 2100})

# print(*money.most_common())

# = 

# from collections import Counter

# money = Counter({'rub': 900, 'eur': 1100, 'usd': 500, 'uah': 990, 'cad': 100, 'jpy': 1120})

# print(*money.most_common(3))

# =

# from collections import Counter

# letters = Counter(s=0, b=1, e=4, t=-2, g=2, k=1)

# print(*letters.elements())

# =

# from collections import Counter

# left_pocket = Counter(coin=11, candy=4, key=1)
# right_pocket = Counter(coin=19, candy=1, key=2, card=2)

# print(left_pocket.total() + right_pocket.total())

# =

# from collections import Counter

# counter1 = Counter(a=2, b=3, c=6)
# counter2 = Counter(a=5, b=7, c=1)

# print(counter1 + counter2)
# print(counter1 - counter2)
# print(counter1 & counter2)
# print(counter1 | counter2)

# = 

# from collections import Counter

# letters1 = Counter('stepik')
# letters2 = {'s': 1, 't': 1, 'e': 1, 'p': 1, 'i': 1, 'k': 1}

# print(letters1 + letters2)

# =

# from collections import Counter

# word = 'stepik'

# counter1 = Counter(word)
# counter2 = Counter(word * 3)

# print(counter1 < counter2)
# print(counter2)

# ===

# from collections import Counter

# words = Counter([w.lower() for w in input().split()])
# print(*dict(words.most_common(1)).keys())

# ===

# from collections import Counter

# words = Counter([w.lower() for w in input().split()])
# min_count = words.most_common()[-1]
# result = [k for k, v in words.items() if v == min_count[1]]
# print(', '.join(sorted(result)))

# ===

# from collections import Counter

# words = Counter([w.lower() for w in input().split()])
# max_count = words.most_common()[0]
# result = [k for k, v in words.items() if v == max_count[1]]
# print(max(result))

# ===

# from collections import Counter, OrderedDict

# mylst = [len(x) for x in input().split()]
# words = Counter(mylst)
# lst = list(words.elements())
# ordered_words1 = OrderedDict(sorted(words.items(), key=lambda x: x[1]))
# for item in ordered_words1:
#     print(f"Слов длины {item}: {ordered_words1[item]}")

# ===

# import sys
# from collections import Counter

# dct = dict([tuple(s.split()) for s in sys.stdin])
# dct1 = {k: int(v) for k, v in dct.items()}
# cntr = Counter(dct1)
# print(cntr.most_common()[-2][0])

# data.sorted_values = lambda reverse=False: sorted(data.values(), reverse=reverse)

# ===

# from collections import Counter

# data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

# data.__dict__['min_values'] = lambda: [x for x in data.items() if x[1] == min(data.values())]
# data.__dict__['max_values'] = lambda: [x for x in data.items() if x[1] == max(data.values())]

# ===

# import csv
# from collections import Counter

# with open('name_log.csv', 'r', encoding='UTF-8') as file:
#     rows = csv.DictReader(file, delimiter=',')
#     names = [row['email'] for row in rows]
#     for email in Counter(sorted(names)):
#         print(f"{email}: {Counter(sorted(names))[email]}")
    

# ===

# from collections import Counter

# def scrabble(symbols, word):
#     letters = Counter([l.lower() for l in symbols])
#     word_letters = Counter([wl.lower() for wl in word])
#     counter = 0
#     for k, v in letters.items():
#         for k1, v1 in word_letters.items():
#             if k1 == k:
#                 if v1 <= v:
#                     counter += 1
#     if counter == len(set(word)):
#         return True
#     else:
#         return False

# print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
# print(scrabble('begk', 'beegeek'))   

# ===

# from collections import Counter

# def print_bar_chart(data, mark):
#     max_len = max([len(x) for x in data])
#     words = Counter(data).most_common()
#     for key, value in words:
#         print(f"{key + ' ' * (max_len-len(key))} |{mark * value}")

# print_bar_chart('beegeek', '+')
# languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

# print_bar_chart(languages, '#')

# ===

# import csv, json
# from collections import Counter

# with open('quarter1.csv', 'r', encoding='UTF-8') as file1, open('quarter2.csv', 'r', encoding='UTF-8') as file2, open('quarter3.csv', 'r', encoding='UTF-8') as file3, open('quarter4.csv', 'r', encoding='UTF-8') as file4, open('prices.json', 'r', encoding='UTF-8') as file5:
#     files = [file1, file2, file3, file4]
#     all_products = [csv.DictReader(f, delimiter=',') for f in files]
#     prices = json.load(file5)
#     all_prods = []
#     for products in all_products:
#         prods = {}
#         for product in products:
#             prods.setdefault(product['продукт'], sum([int(x) for x in [product[list(product.keys())[1]], product[list(product.keys())[2]], product[list(product.keys())[3]]]]))
#         all_prods.append(prods)
#     data = []
#     for prods in all_prods:
#         res = {}
#         for k, v in prices.items():
#             if k in prods:
#                 res.setdefault(k, prods[k]*v)
#         data.append(res)    
#     result = sum([Counter(x).total() for x in data])
#     print(result)

# ===
# from collections import Counter

# classes_books = Counter(input().split())
# buys = [input().split() for _ in range(int(input()))]
# books = Counter([x[0] for x in buys])
# # prices = 
# res = books - classes_books
# print(classes_books)
# # print(buys)
# print(books)
# print(res)

# ===

# from collections import Counter

# books_available = Counter(input().split())
# n = int(input())
# total_earnings = 0

# for _ in range(n):
#     class_num, price = map(int, input().split())
#     if books_available[str(class_num)] > 0:
#         total_earnings += price
#         books_available[str(class_num)] -= 1

# print(total_earnings)

# ===

# from collections import ChainMap, Counter
# import json

# with open('zoo.json', 'r', encoding='UTF-8') as file:
#     print(Counter(ChainMap(*json.load(file))).total())

# ===

# from collections import ChainMap, Counter        

# bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
# meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
# sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
# vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
# toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

# data = ChainMap(bread, meat, sauce, vegetables, toppings)
# order = Counter(input().split(','))
# price = {}
# for k, v in order.items():
#     price.setdefault(k, data[k]*v)
# max_length = len(max(order, key=len))
# for k, v in sorted(order.items()):
#     s = f"{k.ljust(max_length)} x {v}"
#     print(s)
# total_print = f"ИТОГ: {Counter(price).total()}р"
# if len(total_print) > max_length:
#     print('-'*len(total_print))
# else:
#     print('-'*((max_length)+3+len(str(max(list(order.values()))))))
# print(total_print)

# ===

# from collections import ChainMap

# def get_all_values(chainmap, key):
#     try:
#         ret = set(d[key] for d in chainmap.maps if key in d)
#     except KeyError:
#         ret = set()
#     return ret

# # chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# # result = get_all_values(chainmap, 'name')

# # print(*sorted(result))

# # chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# # result = get_all_values(chainmap, 'age')

# # print(result)

# chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
# result = get_all_values(chainmap, 'age')

# print(*sorted(result))

# ===

# from collections import ChainMap

# def deep_update(chainmap, key, value):
#     for d in chainmap.maps:
#         if key in d:
#             d[key] = value
#         if key not in chainmap:
#             d[key] = value
    
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'age', 20)

# print(chainmap)

# ===

# from collections import ChainMap

# def get_value(chainmap, key, from_left=True):
#     if key not in chainmap:
#         return None
#     if from_left:
#         for d in chainmap.maps:
#             if key not in d:
#                 continue
#             else:
#                 return d[key]
#     else:
#         for d in reversed(chainmap.maps):
#             if key not in d:
#                 continue
#             else:
#                 return d[key]

# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

# print(get_value(chainmap, 'name'))
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

# print(get_value(chainmap, 'name', False))
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

# print(get_value(chainmap, 'age'))

# ===

# try:
#     raise ValueError('oops')
# except ValueError as e:
#     print(e)
#     print(e.args)
#     print(type(e.args))

# try:
#     raise ValueError('oops', 'something went wrong')
# except ValueError as e:
#     print(e)
#     print(e.args)

# data = {'Chrome': 'browser', 'Discord': 'messenger', 'Steam': 'digital distributor'}

# try:    
#     try:
#         app_name = 'Firefox'
#         app_type = data[app_name]
#     except:
#         raise KeyError('Not found', app_name)
# except KeyError as e:
#     print(e.args)

# ===

# import calendar
# import locale

# def get_weekday(number):
#     locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#     days_of_week = dict(zip(range(1, 8), [day.title() for day in list(calendar.day_name)]))
#     if isinstance(number, int):
#         if number in range(1, 8):
#             return days_of_week[number]
#         else:
#             raise ValueError('Аргумент не принадлежит требуемому диапазону')
#     else:
#         raise TypeError('Аргумент не является целым числом')

# ===

# def get_id(names, name):
#     if isinstance(name, str):
#         if name.isalpha() and name.istitle():
#             names.append(name)
#             return len(names)
#         else:
#             raise ValueError('Имя не является корректным')
#     else:
#         raise TypeError('Имя не является строкой')
    
# names = ['Timur', 'Anri', 'Dima', 'Roma', 'Gvido', 'Rosy', 'Soslan', 'Natasha', 'Arthur']
# name = 'Arthur'

# print(get_id(names, name))

# ===

# import json

# try:
#     with open(input(), 'r', encoding='UTF-8') as file:
#         try:
#             data = json.load(file)
#             print(data)
#         except json.JSONDecodeError:
#             print("Ошибка при десериализации")
# except FileNotFoundError:
#     print("Файл не найден.")

# ===

# class NumberNotInRangeError(Exception):
#     pass

# try:
#     number = int('3999')
#     if not 4000 < number < 8000:
#         raise NumberNotInRangeError('Число из недопустимого диапазона')
#     print(number)
# except NumberNotInRangeError as e:
#     print(e)

# ===

# def is_good_password(string):
#     if len(string) >= 9 and any(l.isdigit() for l in string) and any(l.isupper() for l in string) and any(l.islower() for l in string):
#         return True
#     else:
#         return False

# print(is_good_password('41157082'))
# print(is_good_password('МойПарольСамыйЛучший111'))

# ===

# class PasswordError(Exception):
#     pass

# class LengthError(PasswordError):
#     pass

# class LetterError(PasswordError):
#     pass

# class DigitError(PasswordError):
#     pass

# def is_good_password(string):
#     try:
#         if len(string) >= 9:
#             try:
#                 if any(l.isupper() for l in string) and any(l.islower() for l in string):
#                     try:
#                         if any(l.isdigit() for l in string):
#                             return True
#                         else:
#                             raise DigitError
#                     except DigitError:
#                         raise DigitError
#                 else:
#                     raise LetterError
#             except LetterError:
#                 raise LetterError
#         else:
#             raise LengthError
#     except LengthError:
#         raise LengthError

# # try:
# #     print(is_good_password('Short7'))
# # except Exception as err:
# #     print(type(err))

# # print(is_good_password('еПQSНгиfУЙ70qE'))

# try:
#     print(is_good_password('41157081231232'))
# except Exception as err:
#     print(type(err))
# ===

# import sys
# import itertools
# class PasswordError(Exception):
#     pass

# class LengthError(PasswordError):
#     pass

# class LetterError(PasswordError):
#     pass

# class DigitError(PasswordError):
#     pass

# def is_good_password(string):
#     try:
#         if len(string) >= 9:
#             try:
#                 if any(l.isupper() for l in string) and any(l.islower() for l in string):
#                     try:
#                         if any(l.isdigit() for l in string):
#                             return 'Success!'
#                         else:
#                             raise DigitError
#                     except DigitError:
#                         return 'DigitError'
#                 else:
#                     raise LetterError
#             except LetterError:
#                 return 'LetterError'
#         else:
#             raise LengthError
#     except LengthError:
#         return 'LengthError'

# passwords = [p.strip() for p in sys.stdin.readlines()]
# # result = list(map(lambda x: print(is_good_password(x)), passwords))
# # list(itertools.takewhile(lambda x: 'Success!', map(print(is_good_password), passwords)))
# result = list(itertools.takewhile(lambda x: x != "Success!", map(lambda password: is_good_password(password), passwords)))
# result.append('Success!')
# print(*result, sep='\n')

# ===

# def message(times):
#     if times > 0:
#         print('Это рекурсивная функция.')
#         message(times - 1)
#         print(times)

# message(5)

# = 

# def bee(n):
#     if n < 5:
#         print(n)
#     else:
#         bee(n + 1)

# bee(7)

# ===

# def traffic(n):
#     if n > 0:
#         print('Не парковаться')
#         traffic(n-1)
    
# traffic(5)

# ===

# def print_nums(n):
#     if n <= 100:
#         print(n)
#         print_nums(n+1)
# print_nums(1)

# ===

# def show_lst(lst):
#     def rec(index):
#         if index < len(lst):
#             print(f'Элемент {index}: {lst[index]}')
#             rec(index + 1)
#     rec(0)
    

# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]

# show_lst(numbers)

# ===

# def nums(n = int(input())):
#     if n != 0:
#         nums(n = int(input()))
#         print(n)
#     else:
#         print(0)
# nums()

# ===

# def triangle(h):
#     def rec(step):
#         if step - h:
#             print('*'*(h - step))
#             rec(step+1)
#     rec(0)

# triangle(3)

# ===

# def triangle(h):
#     def rec(step):
#         if step - h-1:
#             print('*'*(step))
#             rec(step+1)
#     rec(1)

# triangle(3)

# ===

# def hourglass(n, m = 16):
#     if n < 4:
#         print((str(n)*m).center(16))
#         hourglass(n + 1, m - 4)
#     print((str(n)*m).center(16))
# hourglass(1)

# ===

# def print_digits(number):
#     if number:
#         print(number % 10)
#         print_digits(number // 10)

# print_digits(12345) 

# ===

# def print_digits(number):
#     if number:
#         print_digits(number // 10)
#     if number > 0:
#         print(number % 10)

# print_digits(12345) 

# ===

# def f(n):
#     if n in (1, 2, 3):
#         return 1
#     else:
#         return 2*f(n - 1) + 4*f(n - 3) + f(n - 2)

# print(f(4))

# ===

# def count_digits(n, count=0):
#     if n == 0:
#         return count
#     else:
#         return count_digits(n // 10, count+1)

# print(count_digits(int(input())))

# ===

# def count_digits(n, sum=0):
#     if n == 0:
#         return sum
#     else:
#         last_digit = n % 10
#         return count_digits(n // 10, sum+last_digit)

# print(count_digits(int(input())))

# ===

# def number_of_frogs(year):
#     if year == 1:
#         return 77
#     else:
#         return 3*(number_of_frogs(year-1)-30)

# print(number_of_frogs(int(input())))

# ===

# def range_sum(numbers, start, end):
#     if start > end:
#         return 0
#     elif start == end:
#         return numbers[start]
#     else:
#         return numbers[start] + range_sum(numbers, start+1, end)

# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))

# ===

# def get_pow(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * get_pow(a, n-1)
    
# print(get_pow(5, 2))

# ===

# def get_fast_pow(a, n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         half_pow = get_fast_pow(a, n // 2)
#         return half_pow * half_pow
#     else:
#         return a * get_fast_pow(a, n - 1)

# print(get_fast_pow(2, 10))

# ===

# def recursive_sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return recursive_sum(a + 1, b - 1)
    
# print(recursive_sum(10, 22))

# ===

# def is_power(number):
#     if number == 1:
#         return True
#     elif number % 2 == 0:
#         return is_power(number // 2)
#     else:
#         return False
    
# print(is_power(512))

# ===

# def tribonacci(n, memo={}):
#     if n == 1 or n == 2 or n == 3:
#         return 1
#     elif n in memo:
#         return memo[n]
#     else:
#         result = tribonacci(n-1, memo) + tribonacci(n-2, memo) + tribonacci(n-3, memo)
#         memo[n] = result
#         return result
    
# print(tribonacci(7))

# ===

# def is_palindrome(string):
#     if len(string) <= 1:
#         return True
#     elif string[0] != string[-1]:
#         return False
#     else:
#         return is_palindrome(string[1:-1])
    
# print(is_palindrome('level'))

# ===

# def to_binary(number):
#     if number == 0:
#         return '0'
#     elif number == 1:
#         return '1'
#     else:
#         return to_binary(number // 2) + str(number % 2)
# print(to_binary(15))

# ===

# def recursive_operations(n):
#     if n <= 0:
#         print(n)
#         return
#     else:
#         print(n)
#         recursive_operations(n - 5)
#         print(n)

# recursive_operations(int(input()))

# ===

# def recursive_sum(nested_lists):
#     if not nested_lists:  # Если список пустой
#         return 0
#     else:
#         total_sum = 0
#         for element in nested_lists:
#             if isinstance(element, int):  # Если элемент является целым числом
#                 total_sum += element
#             elif isinstance(element, list):  # Если элемент является списком
#                 total_sum += recursive_sum(element)
#         return total_sum
    
# my_list = [1, [4, 4], 2, [1, [2, 10]]]

# print(recursive_sum(my_list))

# ===

# def linear(nested_lists):
#     result = []
#     for element in nested_lists:
#         if isinstance(element, int):
#             result.append(element)
#         elif isinstance(element, list):
#             result.extend(linear(element))
#     return result

# my_list = [3, [4], [5, [6, [7, 8]]]]

# print(linear(my_list))

# ===

# def get_value(nested_dicts, key):
#     if key in nested_dicts:
#         return nested_dicts[key]
#     for value in nested_dicts.values():
#         if isinstance(value, dict):
#             result = get_value(value, key)
#             if result is not None:
#                 return result

# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

# print(get_value(data, 'cityName'))

# ===

# def get_all_values(nested_dicts, key):
#     values = set()
#     if key in nested_dicts:
#         values.add(nested_dicts[key])
#     for value in nested_dicts.values():
#         if isinstance(value, dict):
#             values.update(get_all_values(value, key))
#     return values

# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_values(my_dict, 'top_grade')

# print(*sorted(result))

# ===

# def dict_travel(nested_dicts, prefix=''):
#     for key, value in sorted(nested_dicts.items()):
#         if isinstance(value, dict):
#             dict_travel(value, prefix + key + '.')
#         else:
#             print(prefix + key + ':', value)

# data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

# dict_travel(data)

# positive = [1, 2, 3, 4, 5]
# negative = [-1, -2, -3]
# combined = [1, 2, -3, 4]

# result = map(lambda a, b, c: a + b + c, positive, negative, combined)

# print(*result)

# =

# numbers = filter(lambda x: x > 0, [-3, -2, -1, 0, 1, 2, 3])

# if 1 in numbers:
#     print('bee')
# if 1 in numbers:
#     print('geek')

# = 
# result = (lambda x: x > 5)(3)

# print(result)
# =

# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]

# numbers = filter(lambda x: isinstance(x, (int, float)), data)
# integers = map(lambda x: int(x) if isinstance(x, float) else x, numbers)
# for integer in integers:
#     print(integer)

# ===

# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]

# filtered_numbers = filter(lambda x: 9 <= abs(x) < 100 and x % 9 == 0, numbers)
# sum_of_squares = sum(map(lambda x: x**2, filtered_numbers))

# print(sum_of_squares)

# ===

# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']

# filtered_names = filter(lambda name: name[0].lower() in ['а', 'м'] and len(name) > 4, names)
# sorted_names = sorted(filtered_names, key=lambda name: name.capitalize())

# output = ' '.join(map(lambda name: name.capitalize(), sorted_names))
# print(output)

# ===

# fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)

# ===

# def print_operation_table(operation, rows, cols):
#     for i in range(1, rows + 1):
#         for j in range(1, cols + 1):
#             result = operation(i, j)
#             print(result, end=" ")
#         print()

# print_operation_table(lambda a, b: a * b, 5, 5)

# ===

# def verification(login, password, success, failure):
#     has_latin_letters = any(c.isalpha() and c.isascii() for c in password)
#     has_uppercase = any(c.isupper() for c in password)
#     has_lowercase = any(c.islower() and c.isascii() for c in password)
#     has_digit = any(c.isdigit() for c in password)

#     if not has_latin_letters:
#         failure(login, 'в пароле нет ни одной буквы')
#     elif not has_uppercase:
#         failure(login, 'в пароле нет ни одной заглавной буквы')
#     elif not has_lowercase:
#         failure(login, 'в пароле нет ни одной строчной буквы')
#     elif not has_digit:
#         failure(login, 'в пароле нет ни одной цифры')
#     else:
#         success(login)

# def success(login):
#     print(f'Здравствуйте, {login}!')


# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')


# verification('Arthur_Davletov', 'мойпароль123', success, failure)

# ===
# def numbers_sum(elems):
#     # """
#     # Принимает список и возвращает сумму его чисел (int, float),
#     # игнорируя нечисловые объекты. 0 - если в списке чисел нет.
#     # """
#     return sum(num for num in elems if isinstance(num, (int, float)))

# print(numbers_sum([1, '2', 3, 4, 'five']))

# ===

# old_print = print
# def print(*args, sep=' ', end='\n'):
#     modified_args = list(map(lambda x: str(x).upper() if isinstance(x, str) else x, args))
#     modified_sep = str(sep).upper()
#     modified_end = str(end).upper()
#     old_print(*modified_args, sep=modified_sep, end=modified_end)


# # words = [['black', 'white', 'grey', 'black-1', 'white-1', 'python']]
# # print(words, sep=' to ', end=' LOVE')

# print('beegeek', [1, 2, 3], 4)

# ===

# def polynom(x):
#     result = x**2+1
#     polynom.values.add(result)
#     return result

# polynom.values = set()

# print(polynom(5))
# print(polynom.values)

# ===

# def remove_marks(text, marks):
#     remove_marks.count += 1
#     return ''.join(char for char in text if char not in marks)

# remove_marks.count = 0

# text = 'Hi! Will we go together?'

# print(remove_marks(text, '!?'))
# print(remove_marks.count)

# ===

# def outer(x):
#     def inner():
#         return x + 1
#     return inner

# print(inner(10))

# def outer(x):
#     def inner():
#         return x + 1
#     return inner

# print(outer.inner(10))

# def outer(x):
#     y = 5
#     z = 10
#     def inner():
#         nonlocal y
#         y += 1
#         z = 20
#         print('x =', x)
#         print('z =', z)
#     inner()
#     print('x =', x)
#     print('y =', y)
#     print('z =', z)

# outer(5)

# =

# def outer(x):
#     y = 20
#     def inner(z):
#         t = 30
#         return x + y + z + t
#     return inner

# func = outer(10)

# for var in func.__closure__:
#     print(var.cell_contents)

# =

# def outer():
#     x = 'bee'
#     def inner():
#         x = 'geek'
#         print(x)
#     inner()
#     print(x)
    
# outer()

# def outer():
#     x = 'bee'
#     def inner():
#         nonlocal x
#         x = 'geek'
#         print(x)
#     inner()
#     print(x)

# outer()

# =

# def outer(x):
#     def inner():
#         return x
#     x = None
#     return inner

# print(outer(10)())

# =

# def outer(x, y=2):
#     def inner(z=y):
#         return x, z
#     x, y = None, None
#     return inner

# print(outer(10)())

# =

# def make_counter(i):
#     def counter():
#         nonlocal i
#         i += 1
#         return i
#     return counter

# counter1 = make_counter(100)
# counter2 = make_counter(200)

# print(counter1(), counter1())
# print(counter2(), counter2())

# =

# def greeting(language):
#     def greeting_ru():
#         print('Привет!')
#     def greeting_fr():
#         print('Bonjour!')
    
#     if language == 'ru':
#         return greeting_ru
#     if language == 'fr':
#         return greeting_fr
    
# func = greeting('fr')
# func()

# =

# def power(degree):
#     def inner(x):
#         return x**degree
#     return inner

# square = power(2)
# print(square(5))

# ===

# def generator_square_polynom(a,b,c):
#     def inner(x):
#         return a*x**2 + b*x + c
#     return inner

# f = generator_square_polynom(1, 2, 1)
# print(f(5))

# ===

# def sourcetemplate(url):
#     def generate_query_string(**kwargs):
#         if kwargs:
#             sorted_params = sorted(kwargs.items())
#             query_string = '&'.join([f"{key}={value}" for key, value in sorted_params])
#             return f"{url}?{query_string}"
#         else:
#             return url
    
#     return generate_query_string

# url = 'https://beegeek.ru'
# load = sourcetemplate(url)
# print(load(name='timur'))

# ===

# from datetime import date

# def date_formatter(country_code):
#     def format_date(date_obj):
#         if country_code == 'ru':
#             return date_obj.strftime("%d.%m.%Y")
#         elif country_code == 'us':
#             return date_obj.strftime("%m-%d-%Y")
#         elif country_code == 'ca':
#             return date_obj.strftime("%Y-%m-%d")
#         elif country_code == 'br':
#             return date_obj.strftime("%d/%m/%Y")
#         elif country_code == 'fr':
#             return date_obj.strftime("%d.%m.%Y")
#         elif country_code == 'pt':
#             return date_obj.strftime("%d-%m-%Y")
    
#     return format_date

# date_ru = date_formatter('ru')
# today = date(2022, 1, 25)
# print(date_ru(today))

# ===

# def get_digits(number: int | float) -> list[int]:
#     lst = []
#     if '.' in str(number):
#         num = [digit for digit in str(number) if digit != '.']
#         number = int(''.join(num))
#     while number != 0:
#         last_digit = number % 10
#         lst.append(last_digit)
#         number //= 10
#     return list(reversed(lst))

# # print(get_digits(16733))
# print(get_digits(13.909934))

# ===

# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     name = grades['name']
#     highest_grade = max(grades['grades'])
#     return {'name': name, 'top_grade': highest_grade}

# print(*top_grade.__annotations__.values())

# ===

# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     n = len(numbers)
#     step %= n  # Приводим step к значению в диапазоне [0, n)
#     numbers[:] = numbers[-step:] + numbers[:-step]

# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, 1)

# print(numbers)

# annotations = cyclic_shift.__annotations__
# print(annotations['return'])
# print(annotations['step'])+

# ===

# def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
#     return {i+1: row for i, row in enumerate(matrix)}


# matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

# print(matrix_to_dict(matrix))

# ===

# def null_decorator(func):
#     return func
# def say():
#     print('Привет Мир!')

# say = null_decorator(say)      # декорируем функцию

# say()                          # вызываем декорированную функцию

# =

# def sample_decorator(func):          # определяем декоратор
#     def wrapper():
#         print('Начало функции')
#         func()
#         print('Конец функции')
#     return wrapper

# def say():
#     print('Привет Мир!')

# say = sample_decorator(say)          # декорируем функцию

# say()                                # вызываем декорированную функцию

# =

# def uppercase_decorator(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper

# @uppercase_decorator
# def greet():
#     return 'Hello world!'

# print(greet())

# =

# def bold(func):
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     return wrapper

# def greet(name):
#     return f'Hello {name}!'

# @bold
# def greet1(name):
#     return f'Hello {name}!'

# @bold
# def greet2():
#     return 'Hello world!'

# @bold
# def greet3(name, surname):
#     return f'Hello {name} {surname}!'

# print(greet1('Timur'))
# print(greet2())
# print(greet3('Timur', 'Guev'))

# =

# def talk(func):
#     def wrapper(*args, **kwargs):
#         dash = '-' * 15
#         print(dash)
#         func(*args, **kwargs)           # вызываем декорируемую функцию
#         print(dash)
#     return wrapper

# @talk
# def greet(name):
#     return f'Hello {name}!'
# =

# def make_upper(func):
#     def wrapper():
#         return func().upper()
#     return wrapper

# def beegeek():
#     return 'beegeek'

# new_beegeek = make_upper(beegeek)

# print(beegeek())
# print(new_beegeek())

# ===

# def add_dollar_prefix(func):
#     def wrapper():
#         result = str(func())
#         return '$' + result
#     return wrapper

# @add_dollar_prefix
# def get_price(item):
#     prices = {'comic book': 5, 'puzzle': 15}
#     return prices[item]

# print(get_price('comic book'))

# def add_dollar_prefix(func):
#     def wrapper(*args, **kwargs):
#         result = str(func(*args, **kwargs))
#         return '$' + result
#     return wrapper

# @add_dollar_prefix
# def get_price(item):
#     prices = {'comic book': 5, 'puzzle': 20}
#     return prices[item]

# print(get_price(item='puzzle'))

# = 

# def double(func):
#     def wrapper(*args, **kwargs):
#         doubled_result = func(*args, **kwargs) * 2
#     return wrapper

# @double
# def get_color_code(color):
#     color_codes = {'black': '#000000', 'white': '#FFFFFF'}
#     return color_codes[color]

# print(get_color_code('white'))

# ===

# def sandwich(func):
#     def wrapper(*args, **kwargs):
#         print('---- Верхний ломтик хлеба ----')
#         f = func(*args, **kwargs)
#         print('---- Нижний ломтик хлеба ----')
#         return f
#     return wrapper


# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))

# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

# @sandwich
# def beegeek():
#     return 'beegeek'
    
# print(beegeek())

# ===
        
# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Преобразование всех аргументов в верхний регистр
#         args = [str(arg).upper() for arg in args]
#         kwargs = {key: str(value).upper() for key, value in kwargs.items()}

#         # Вызов оригинальной функции print() с измененными аргументами
#         print = func(*args, **kwargs)
#         return print
#     return wrapper
# print = uppercase_decorator(print)
# print('hi', 'there', end='!')

# ===

# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
    
#     return wrapper

# @do_twice
# def beegeek():
#     print('beegeek')
    
# beegeek()

# ===

# def reverse_args(func):
#     def wrapper(*args, **kwargs):
#         a = reversed(args)
#         f = func(*a, **kwargs)
#         return f
#     return wrapper

# @reverse_args
# def concat(a, b, c):
#     return a + b + c
    
# print(concat('apple', 'cherry', 'melon'))

# ===

# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             foo = func(*args, **kwargs)
#             return (foo, 'Функция выполнилась без ошибок')
#         except:
#             return (None, 'При вызове функции произошла ошибка')
#     return wrapper

# @exception_decorator
# def f(x):
#     return x**2 + 2*x + 1

# print(f(7))

# sum = exception_decorator(sum)

# print(sum(['199', '1', 187]))

# ===

# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         if all(list(map(lambda x: isinstance(x, int), args))) and all(list(map(lambda x: isinstance(x, int), kwargs.values()))):
#             if all(list(map(lambda x: x > 0, args))) and all(list(map(lambda x: x > 0, kwargs.values()))):
#                 f = func(*args, **kwargs)
#                 return f
#             else:
#                 return ValueError
#         else:
#             return TypeError 
#     return wrapper


# @takes_positive
# def positive_sum(*args):
#     return sum(args)
    
# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
    
# try:
#     print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
# except Exception as err:
#     print(type(err))

# ===

# import functools

# def bold(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     return wrapper

# @bold
# def greet(name):
#     '''Функция приветствие пользователя.'''
#     return f'Hello {name}!'

# print(greet.__name__)
# print(greet.__doc__)

# =

# import functools

# def make_capitalize(func):
#     @functools.wraps
#     def wrapper():
#         return func().capitalize()
#     return wrapper

# @make_capitalize
# def beegeek():
#     '''documentation'''
#     return 'beegeek'

# print(beegeek.__name__)
# print(beegeek.__doc__)

# = Шаблон декоратора общего назначения:

# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Что-то выполняется до вызова декорируемой функции
#         value = func(*args, **kwargs)
#         # декорируется возвращаемое значение функции
#         # или что-то выполняется после вызова декорируемой функции
#         return value
#     return wrapper

# =

# import functools
# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         value = func(*args, **kwargs)
#         return value**2
#     return wrapper

# @square
# def add(a, b):
#     return a + b

# print(add(3, 7))

# ===

# import functools
# def returns_string(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         f = func(*args, **kwargs)
#         if isinstance(f, str):
#             return f
#         else:
#             raise TypeError
#     return wrapper

# @returns_string
# def nothing():
#     return

# print(nothing.__name__)
# print(nothing.__doc__)

# try:
#     nothing()
# except TypeError as e:
#     print(type(e))

# ===
# import functools

# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
#         f = func(*args, **kwargs)
#         print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(f)}')
#         return f
#     return wrapper

# # @trace
# # def beegeek():
# #     '''beegeek docs'''
# #     return 'beegeek'

# # print(beegeek())    
# # print(beegeek.__name__)
# # print(beegeek.__doc__)
# @trace
# def add(a, b, c):
#     '''docs'''
#     return a + b + c

# print(add(1, 2, 3))    
# print(add.__name__)
# print(add.__doc__)

# def add_smiley_face(face):
#     def smiley_face_decorator(func):
#         def wrapper():
#             return func() + ' ' + face
#         return wrapper
#     return smiley_face_decorator

# @add_smiley_face('^~^')
# def beegeek():
#     return 'beegeek'

# print(beegeek())
# =
# def make_upper(func):
#     def wrapper():
#         return func().upper()
#     return wrapper

# def del_first_char(func):
#     def wrapper():
#         return func()[1:]
#     return wrapper

# def reverse(func):
#     def wrapper():
#         return func()[::-1]
#     return wrapper

# @reverse
# @del_first_char
# @make_upper
# def beegeek():
#     return 'beegeek'

# print(beegeek())

# =

# import functools

# def prefix(string, to_the_end=False):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             f = func(*args, **kwargs)
#             if to_the_end:
#                 return f + string
#             else:
#                 return string + f
#         return wrapper
#     return decorator

# @prefix('€')
# def get_bonus():
#     return '2000'
    
# print(get_bonus())

# @prefix('$$$', to_the_end=True)
# def get_bonus():
#     return '2000'
       
# print(get_bonus())

# ===
# import functools

# def make_html(tag):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             value = func(*args, **kwargs)
#             return f'<{tag}>{value}</{tag}>'
#         return wrapper
#     return decorator

# @make_html('del')
# def get_text(text):
#     return text
    
# print(get_text('Python'))

# ===

# import functools

# def repeat(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator            

# @repeat(3)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
    
# say_beegeek()

# ===

# import functools

# def strip_range(start, end, char='.'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             ret = ''
#             r = range(start, end)
#             value = func(*args, **kwargs)
#             for l in range(len(value)):
#                 if l in r:
#                     ret += char
#                 else:
#                     ret += value[l]
#             return ret
#         return wrapper
#     return decorator

# @strip_range(3, 5)
# def beegeek():
#     return 'beegeek'
    
# print(beegeek())

# ===

# import functools

# def returns(datatype):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             ret = func(*args, **kwargs)
#             if isinstance(ret, datatype):
#                 return ret
#             else:
#                 return TypeError
#         return wrapper
#     return decorator

# @returns(int)
# def add(a, b):
#     return a + b

# print(add(10, 5))
# @returns(int)
# def add(a, b):
#     return a + b

# try:
#     print(add('199', '1'))
# except TypeError as e:
#     print(type(e))

# ===

# import functools

# def takes(*args1):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             ret = func(*args, **kwargs)
#             if all(list(map(lambda x: type(x) in args1, args))):
#                 if all(list(map(lambda x: type(x) in args1, kwargs.values()))):
#                     return ret
#                 else:
#                     return TypeError
#             else:
#                 return TypeError
#         return wrapper
#     return decorator

# # TEST_11:
# @takes(str)
# def beegeek(word, repeat):
#     return word * repeat
    
# try:
#     print(beegeek('beegeek', repeat=2))
# except TypeError as e:
#     print(type(e))

# @takes(list, int, tuple, str)
# def add(a, b):
#     '''add docs'''
#     return a + b

# print(add.__name__)
# print(add.__doc__)

# try:
#     print(add(a='a', b='c'))
# except TypeError as e:
#     print(type(e))

# ===

# import functools

# def add_attrs(**kwargs1):
#     def decorator(func):
#         for k, v in kwargs1.items():
#             setattr(func, k, v)
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# @add_attrs(attr1='bee', attr2='geek')
# def beegeek():
#     return 'beegeek'

# print(beegeek.attr1)
# print(beegeek.attr2)

# ===

# import functools

# def ignore_exception(*args1):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 f = func(*args, **kwargs)
#                 return f
#             except Exception as e:
#                 if type(e) in args1:
#                     print(f'Исключение {type(e).__name__} обработано')
#                 else:
#                     raise type(e)
#         return wrapper
#     return decorator
                
# # TEST_9:
# @ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
# def beegeek():
#     return 'beegeek'
    
# print(beegeek())

# ===

# import functools

# class MaxRetriesException(Exception):
#     pass

# def retry(num):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 try:
#                     return func(*args, **kwargs)
#                 except:
#                     pass
#             raise MaxRetriesException
#         return wrapper
#     return decorator

# @retry(8)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 5:
#         raise ValueError
#     print('beegeek')
    
# beegeek()

# ===

# from functools import partial

# beegeek = partial(print, 'bee', 'geek', end='!')

# print(beegeek.args)
# print(beegeek.keywords)

# ===

# from functools import partial

# to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru', 'text')
# send_an_invitation = partial(send_email, name, email_address, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')

# ===

# from functools import lru_cache

# @lru_cache()
# def average(numbers):
#     return sum(numbers) / len(numbers)

# numbers = [1, 2, 3, 4, 5]

# print(average(numbers))
# print(average(numbers))

# ===

# from functools import lru_cache

# @lru_cache(typed=True)
# def return_this(a, b):
#     return a, b

# print(return_this(True, True))
# print(return_this(1.0, 1.0))
# print(return_this(1, 1))

# ===

# words = []
# while True:
#     try:
#         words.append(input().strip())
#     except:
#         break

# for word in words:
#     print(''.join(sorted(word))) 

# ===

# from functools import lru_cache

# @lru_cache
# def ways(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 4:
#         return ways(n-1) + ways(n-3) + ways(n-4)
#     if n > 3:
#         return ways(n-1) + ways(n-3)
#     if n > 1:
#         return ways(n-1)
    
    

# print(ways(5))

# =

# numbers = (-2, -1, 0, 1, 2)

# non_zero = filter(None, numbers)
# positive = map(abs, non_zero)

# print(*positive)

# =

# numbers = filter(None, [0, 1, 2, 3])

# next(numbers)
# next(numbers)
# next(numbers)

# try:
#     print(next(numbers))
# except StopIteration:
#     print('Error')

# =

# from sys import getsizeof

# numbers1 = range(10)
# numbers2 = range(10000000)

# size1 = getsizeof(numbers1)
# size2 = getsizeof(numbers2)

# print(size1 == size2)

# ===

# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
# nums_iterator = iter(numbers)
# next(nums_iterator)
# next(nums_iterator)
# next(nums_iterator)

# print(next(nums_iterator))

# ===

# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
# iterator = iter(numbers)
# last = None
# try:
#     while True:
#         last = next(iterator)
# except StopIteration:
#     pass

# print(last)

# =

# non_zero = filter(None, [0, 1, 2, 3, 4])

# for _ in non_zero:
#     pass

# print(next(non_zero))

# =

# non_zero = filter(None, [-2, -1, 0, 1, 2])
# positive = map(abs, non_zero)

# print(list(non_zero))
# print(list(positive))

# =

# non_zero = filter(None, [-2, -1, 0, 1, 2])
# positive = map(abs, non_zero)

# print(list(positive))
# print(list(non_zero))

# =

# positive = (1, 2, 3)
# negative = map(lambda x: -x, positive)

# for a, b in zip(positive, negative):
#     print(a + b)

# =

# def filterfalse(predicate, iterable):
#     iterator = filter(predicate, iterable)    
#     lst = list(iterator)
#     ret = [i for i in iterable if i not in lst]
#     return ret

# objects = [0, 1, True, False, 17, []]

# print(*filterfalse(None, objects))

# def transpose(matrix):
#     return [list(x) for x in zip(*matrix)]

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# for row in transpose(matrix):
#     print(row)

# ===

# def get_min_max(data):
#     if not data:
#         return None
#     min_index = max_index = 0
#     for i, elem in enumerate(data):
#         if elem < data[min_index]:
#             min_index = i
#         elif elem > data[max_index]:
#             max_index = i
#     return (min_index, max_index)

# data = [2, 3, 8, 1, 7]

# print(get_min_max(data))

# ===

# def starmap(func, iterable):
#     return map(lambda args: func(*args), iterable)
# pairs = [(1, 3), (2, 5), (6, 4)]

# print(*starmap(lambda a, b: a + b, pairs))

# ===

# def get_min_max(iterable):
#     try:
#         min_value = max_value = next(iter(iterable))
#     except StopIteration:
#         return None
#     for value in iterable:
#         if value < min_value:
#             min_value = value
#         if value > max_value:
#             max_value = value
#     return min_value, max_value

# iterable = iter(range(10))

# print(get_min_max(iterable))

# iterable = [6, 4, 2, 33, 19, 1]

# print(get_min_max(iterable))
# iterable = iter([])

# print(get_min_max(iterable))
# data = iter(range(100_000_000))

# print(get_min_max(data))

# =

# iterator = iter(lambda: 2, 10)

# print(next(iterator) + next(iterator))

# ===

# def love():
#     while True:
#         return 'i love beegeek!'

# infinite_love = iter(love, None)


# print(next(infinite_love))

# ===

# def is_iterator(obj):
#     try:
#         next(obj)
#         return True
#     except TypeError:
#         return False
    

# print(is_iterator([1, 2, 3, 4, 5]))

# ===

# import random

# def random_numbers(left, right):
#     while True:
#         yield random.randint(left, right)

# iterator = random_numbers(1, 1)

# print(next(iterator))

# ===

# numbers = [1, 2, 3, 4, 5]

# iterator = iter(numbers)

# del numbers[0]
# del numbers[1]

# print(next(iterator))

# =

# numbers = [1, 2, 3, 4, 5]

# iterator = iter(numbers)

# next(iterator)
# next(iterator)

# del numbers[0]
# del numbers[1]

# print(next(iterator))

# ===

# class Repeater:
#     def __init__(self, obj):
#         self.obj = obj

#     def __iter__(self):
#         return self

#     def __next__(self):
#         return self.obj
    
# ===

# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.times:
#             self.current += 1
#             return self.obj
#         else:
#             raise StopIteration

# ===

# class Square: 
#     def __init__(self, n): 
#         self.n = n 
#         self.current = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.n:
#             raise StopIteration
#         result = self.current ** 2
#         self.current += 1
#         return result

# ===

# class Fibonacci: 
#     def __init__(self): 
#         self.current = 1 
#         self.previous = 0

#     def __iter__(self):
#         return self
        
#     def __next__(self):
#         result = self.current
#         self.current += self.previous
#         self.previous = result
#         return result

# fibonacci = Fibonacci()

# print(next(fibonacci))

# ===

# class PowerOf:
#     def __init__(self, number):
#         self.number = number
#         self.current = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         result = self.current
#         self.current *= self.number
#         return result

# ===

# class DictItemsIterator:
#     def __init__(self, data):
#         self.data = data
#         self.keys = list(data.keys())
#         self.index = 0
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.keys):
#             raise StopIteration
#         key = self.keys[self.index]
#         value = self.data[key]
#         self.index += 1
#         return (key, value)
    
# pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

# ===

# class CardDeck:
#     def __init__(self):
#         self.nominals = "2 3 4 5 6 7 8 9 10 валет дама король туз".split()
#         self.suits = "пик треф бубен червей".split()
#         self.cards = [f"{nominal} {suit}" for suit in self.suits for nominal in self.nominals]

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.cards:
#             return self.cards.pop(0)
#         else:
#             raise StopIteration
        

# cards = CardDeck()

# print(next(cards))
# print(next(cards))

# ===

# class Cycle():
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = 0
    
#     def __iter__(self):
#         return self

    
#     def __next__(self):
#         if len(self.iterable) == 0:
#             raise StopIteration
#         result = self.iterable[self.index % len(self.iterable)]
#         self.index += 1
#         return result

# cycle = Cycle('be')

# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))

# ===

# import random

# class RandomNumbers:
#     def __init__(self, left, right, n):
#         self.left = left
#         self.right = right
#         self.n = n
#         self.count = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count >= self.n:
#             raise StopIteration
#         self.count += 1
#         return random.randint(self.left, self.right)
    
# iterator = RandomNumbers(1, 1, 3)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# ===

# class Alphabet: 
#     RU_ALPHABET = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' 
#     EN_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

#     def __init__(self, language):
#         self.index = 0
#         if language == 'ru':
#             self.alphabet = self.RU_ALPHABET
#         elif language == 'en':
#             self.alphabet = self.EN_ALPHABET

#     def __iter__(self):
#         return self

#     def __next__(self):
#         current_letter = self.alphabet[self.index % len(self.alphabet)]
#         self.index += 1
#         return current_letter
    
# ru_alpha = Alphabet('ru')

# print(next(ru_alpha))
# print(next(ru_alpha))
# print(next(ru_alpha))

# ===

# class Xrange:
#     def __init__(self, start, end, step=1):
#         self.start = start
#         self.end = end
#         self.step = step

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if isinstance(self.start, float) or isinstance(self.step, float):
#             if isinstance(self.step, float):
#                 t = type(self.step)
#                 self.start = t(self.start)
#             else:
#                 t = type(self.start)
#                 self.step = t(self.step)
#         if self.step > 0 and self.start >= self.end:
#             raise StopIteration
#         elif self.step < 0 and self.start <= self.end:
#             raise StopIteration
#         current_num = self.start
#         self.start += self.step
#         return current_num
    
# xrange = Xrange(5.9, 44, 3)

# print(tuple(xrange))

# ===

# def bee():
#     yield 'b'
#     yield 'e'
#     yield 'e'

# generator = bee()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# =

# def bee():
#     yield 'b'
#     yield 'e'
#     yield 'e'

# print(next(bee()))
# print(next(bee()))
# print(next(bee()))

# =

# def beegeek():
#     for char in 'bee':
#         yield char
#     for char in 'geek':
#         yield char

# generator = beegeek()

# print(*generator)

# =

# def bee():
#     yield 'b'
#     print('--')
#     yield 'e'
#     print('--')
#     yield 'e'

# for elem in bee():
#     print(elem)

# =

# def simple_sequence():
#     start = 1
#     while True:
#         yield start
#         start += 1
#         for i in range(start-1):
#             yield start

# generator = simple_sequence()
# numbers = [next(generator) for _ in range(10)]

# print(*numbers)

# =

# def alternating_sequence(count = None):
#     start = 0 
#     # yield start
#     if count == None:
#         while True:
#             start += 1
#             yield start
#             start += 1
#             yield -start
#     if count == 1:
#        for i in range(count):
#         start += 1
#         yield start
        
#     for i in range(count//2):
#         start += 1
#         yield start
#         start += 1
#         yield -start



# generator = alternating_sequence(1)

# try:
#     print(next(generator))
#     print(next(generator))
# except StopIteration:
#     print('Error')

# =


# from math import sqrt

# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
    
# def primes(left, right):
#     for n in range(left, right + 1):
#         if is_prime(n):
#             yield n
    
# generator = primes(1, 15)

# print(*generator)

# ===

# def reverse(sequence):
#     rev = reversed(sequence)
#     for r in rev:
#         yield r

# generator = reverse('beegeek')

# print(type(generator))
# print(*generator)

# ===

# from datetime import date, timedelta

# def dates(start, count=None):
#     delta = timedelta(days=1) 
#     if count == None:
#         yield start
#         while True:
#             if start == date(9999, 12, 31):
#                 break
#             start += delta
#             yield start
#     else:
#         yield start
#         for i in range(count-1):
#             start += delta
#             yield start


# generator = dates(date(9999, 1, 7))

# for _ in range(348):
#     next(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# try:
#    print(next(generator))
# except StopIteration:
#     print('Error')

# ===

                
# def card_deck(suit):
#     nominals = "2 3 4 5 6 7 8 9 10 валет дама король туз".split()
#     suits = "пик треф бубен червей".split()
#     cards = [f"{nominal} {suit}" for suit in suits for nominal in nominals]
#     while True:
#         for card in cards:
#             if suit not in card:
#                 yield card 

# generator = card_deck('треф')
# cards = [next(generator) for _ in range(40)]

# print(*cards)

# ===

# def bee():
#     yield 'b'
#     yield 'e'
#     yield 'e'

# def geek():
#     yield from 'geek'

# print(*bee())
# print(*geek())

# =

# def bee():
#     for char in 'bee':
#         yield char

# def geek():
#     yield from 'geek'

# print(*bee())
# print(*geek())

# =

# def bee():
#     yield from 'bee'

# def geek():
#     yield from 'geek'

# def beegeek():
#     yield from bee()
#     yield from geek()

# print(*beegeek())

# ===

# def matrix_by_elem(matrix):
#     for row in matrix:
#         yield from row

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# print(*matrix_by_elem(matrix))

# ===

# def palindromes():
#     start = 0
#     while True:
#         start += 1
#         if str(start) == str(start)[::-1]:
#             yield start


# generator = palindromes()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# ===

# def flatten(nested_list):
#     for element in nested_list:
#         if isinstance(element, int):
#             yield element
#         elif isinstance(element, list):
#             yield from flatten(element)
    

# generator = flatten([[1, 2], [[3]], [[4], 5]])

# print(*generator)

# ===

# def cubes_of_odds(iterable):
#     return (number**3 for number in iterable if number % 2)

# print(*cubes_of_odds([1, 2, 3, 4, 5]))

# ===

# def is_prime(number):
#     if number < 2:
#         return False
#     return all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))

# print(is_prime(7))
# print(is_prime(8))

# ===

# def count_iterable(iterable):
#     counter = 0
#     generator = (i for i in iterable)
#     for i in generator:
#         counter +=1
#     return counter
# print(count_iterable([1, 2, 3, 4, 5]))

# ===

# def all_together(*args):
#     for i in args:
#         yield from i

# objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
# print(*all_together(*objects))

# ===

# def interleave(*args):
#     for seq in zip(*args):
#         yield from seq

# ===

# def digits(number):
#     for digit in str(number):
#         yield int(digit)
    
# def cubed(numbers):
#     for number in numbers:
#         yield number ** 3

# def odds(numbers):
#     for number in numbers:
#         if number % 2:
#             yield number
            
# numbers = cubed(odds(digits(1234321)))

# print(*numbers)

# ===

# from itertools import repeat

# repeater = repeat('bee')

# for _ in range(100):
#     next(repeater)

# print(next(repeater))
# print(next(repeater))

# =

# from itertools import repeat

# repeater = repeat('geek', 4)

# print(list(repeater))

# =

# from collections import namedtuple

# Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

# persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
#            Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
#            Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
#            Person('Genevieve Asse', 'French', 'female', 1949, 0),
#            Person('Irene Adler', 'Swedish', 'female', 2005, 0),
#            Person('Sergio Asti', 'Italian', 'male', 1926, 0),
#            Person('Olof Backman', 'Swedish', 'male', 1999, 0),
#            Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
#            Person('Dana Atchley', 'American', 'female', 1941, 2000),
#            Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
#            Person('Shura_Stone', 'Russian', 'male', 2000, 0),
#            Person('Jon Bale', 'Swedish', 'male', 2000, 0)]


# youngest_alive_swede = swedens(mans(alives(persons)))

# print(*youngest_alive_swede)

# youngest_male_swedish = max((p for p in persons if p.nationality == 'Swedish' and p.sex == 'male' and p.death == 0), key=lambda p: p.birth)
# print(youngest_male_swedish.name)

# ===

# def parse_ranges(ranges):
#     for ran in ranges.split(','):
#         bounds = list(map(int, ran.split('-')))
#         for num in range(bounds[0], bounds[-1] + 1):
#             yield num

# print(*parse_ranges('1-2,4-4,8-10'))

# ===

# def filter_names(names, ignore_char, max_names):
#     count = 0
#     for name in names:
#         if count == max_names:
#             break
#         if name[0].lower() == ignore_char.lower() or any(char.isdigit() for char in name):
#             continue
#         yield name 
#         count += 1

# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

# print(*filter_names(data, 'D', 3))

# ===

# import csv

# with open('data.csv', 'r', newline='', encoding='utf-8') as file:
#     file_lines = (line for line in file)
#     line_values = (line.rstrip().split(',') for line in file_lines)
#     file_headers = next(line_values)
#     sum = 0
#     for line in line_values:
#         if line[2] == 'a':
#             sum += int(line[1])
#     print(sum)

# ===

# from datetime import date, timedelta

# def years_days(year):
#     current_date = date(year=year, month=1, day=1)
#     end_date = date(year=year, month=12, day=31)
#     while current_date <= end_date:
#         yield current_date
#         current_date += timedelta(days=1)

# ===


# def recviz(fn):
#     def wrapped(*args, **kwargs):
#         arg_str = ""
#         for i, arg in enumerate(args):
#             if i > 0:
#                 arg_str += ", "
#             arg_str += str(arg)

#         for kw, val in kwargs.items():
#             if arg_str:
#                 arg_str += ", "
#             arg_str += kw + "=" + str(val)

#         print(f"-> {fn.__name__}({arg_str})")
#         res = fn(*args, **kwargs)
#         print("<-", res)

#         return res

#     return wrapped

# @recviz
# def add(a, b, c, d, e):
#     return (a + b + c) * (d + e)

# add('a', b='b', c='c', d=3, e=True)


def recviz(fn):
    def wrapped(*args, **kwargs):
        arg_str = ""
        for i, arg in enumerate(args):
            if i > 0:
                arg_str += ", "
            arg_str += str(arg)

        for kw, val in kwargs.items():
            if arg_str:
                arg_str += ", "
            arg_str += kw + "=" + str(val)

        print(f"-> {fn.__name__}({arg_str})")
        res = fn(*args, **kwargs)
        print("<-", res)

        return res

    return wrapped

@recviz

def add(a, b, c, d, e):
    return (a + b + c) * (d + e)

add('a', b='b', c='c', d=3, e=True)


