#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "admin" and password == "12345":
        return "Access granted"
    if username == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    if temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    if temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    pass

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2
    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation!")
        return None
    pass
