# PYTHON: loops

# Task:
# The provided code stub reads and integer, , from STDIN. For all non-negative integers i < n , print i**2

#input format: the first and only line contains the integer n

#output format: print n lines, one corresponding to each i 

# here is my code:
if __name__ == '__main__':
    n = int(input())

    for i in range (n):
        print(i**2) 
