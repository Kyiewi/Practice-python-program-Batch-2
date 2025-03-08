#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

number = [int(input("Enter a number: ")) for i in range (10)]
even_number = [1 for num in number if num %2==0]

print("Total of even numbers: ", sum(even_number))
