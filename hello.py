def greet(name):
    print("Hello, " + name + "!")

def main():
    user_name = input("What's your name? ")
    greet(user_name)
    
    # Tính toán đơn giản
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for num in numbers:
        total = total + num
    print("Sum of numbers:", total)

if __name__ == "__main__":
    main()