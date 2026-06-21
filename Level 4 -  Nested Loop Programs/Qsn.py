#Print a square pattern
# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()
# O/P: 
#      * * * * 
#      * * * * 
#      * * * * 
#      * * * * 


# Print a triangle pattern
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# O/P:
#      * 
#      * * 
#      * * * 
#      * * * * 
#      * * * * * 


#Print an inverted triangle.
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# O/P:
#     * * * * * 
#     * * * * 
#     * * * 
#     * * 
#     * 


# Print Floyd's Triangle
# Num=1
# for i in range(1,5):
#     for j in range(i):
#         print(Num,end=" ")
#         Num+=1
#     print()
# O/P:
#       1 
#       2 3 
#       4 5 6 
#       7 8 9 10 


#Print a multiplication table grid
# for i in range(1,5):
#     for j in range(1,5):
#         print(i*j,end=" ")
#     print()
# O/P:
#      1 2 3 4 
#      2 4 6 8 
#      3 6 9 12 
#      4 8 12 16 


# Print a pyramid pattern
# N=5
# for i in range(1,N+1):
#     for j in range(N-i):
#         print(" ",end=" ")
#     for k in range(2*i - 1):
#         print("*",end=" ")
#     print()
#     O/P:
#                 * 
#               * * * 
#             * * * * * 
#           * * * * * * * 
#         * * * * * * * * * 


# Print a diamond pattern
# N=5
# for i in range(1,N+1):
#     for j in range(N-i):
#         print(" ",end=" ")
#     for k in range(2*i - 1):
#         print("*",end=" ")
#     print()
# for i in range(N-1,0,-1):
#     for j in range(N-i):
#         print(" ",end=" ")
#     for k in range(2*i - 1):
#         print("*",end=" ")
#     print()
# 
# O/P:
#              * 
#            * * * 
#          * * * * * 
#        * * * * * * * 
#      * * * * * * * * * 
#        * * * * * * * 
#          * * * * * 
#            * * * 
#              * 