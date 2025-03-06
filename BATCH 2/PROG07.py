#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

noomber = [int(input("Enter a number: ")) for i in range (10)]
even_noomber = [1 for num in noomber if num %2==0]

print("Total of even numbers: ", sum(even_noomber))
