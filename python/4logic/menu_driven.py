while True:
    print("\n1. Factorial")
    print("2. Count Digit")
    print("3. Sum of Digits")
    print("4. Prime Number")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Factorial
    if choice == 1:
        num = int(input("Enter number: "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print("Factorial is:", fact)

    # 2. Count Digits
    elif choice == 2:
        num = int(input("Enter number: "))
        count = 0
        temp = num

        while temp != 0:
            temp = temp // 10
            count += 1

        print("Total digits:", count)

    # 3. Sum of Digits + Even & Odd Count
    elif choice == 3:
        num = int(input("Enter number: "))
        temp = num
        sum_digits = 0
        even_count = 0
        odd_count = 0

        while temp != 0:
            rem = temp % 10

            sum_digits += rem

            if rem % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

            temp = temp // 10

        print("Sum of digits:", sum_digits)
        print("Even digits:", even_count)
        print("Odd digits:", odd_count)

    # 4. Prime Number
    elif choice == 4:
        num = int(input("Enter number: "))
        
        if num <= 1:
            print(num, "is not prime")
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(num, "is prime")
            else:
                print(num, "is not prime")

    # 5. Exit
    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid choice!")