#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers = [int(input("Enter a number: ")) for i in range(10)]
diff = numbers[0] - sum(numbers[1:])

print("Result:", diff)
