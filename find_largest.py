#Base function to find larger number
def find_larger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))
n3 = int(input("Enter the third integer: "))
n4 = int(input("Enter the fourth integer: "))

#Finding the largest number from both brackets
larger1 = find_larger(n1, n2)
larger2 = find_larger(n3, n4)
largest = find_larger(larger1, larger2)

print("The largest integer is: ")