import math_tools

def main():
    with open("cal_history.txt", "a") as log:
        while True:
            first = input("Enter first number: ")
            if first.lower() == 'q':
                print("Session ended")
                break
            second = input ("Enter second number: ")
            operation = input ("Type of operation (+ - * /): ")
            try: 
                a = float(first)
                b = float(second)
            except ValueError:
                print("Only valid numbers")
                continue
            if operation == '+':
                result = math_tools.add(a, b)
            elif operation == '-':
                result = math_tools.subtract(a, b)
            elif operation == '*':
                result = math_tools.multiply(a, b)
            elif operation == '/':
                result = math_tools.divide(a, b)
            else:
                print ("error")
                continue
            print(f"Result: {result}")
            log.write(f"{a} {operation} {b} = {result}\n")
if __name__ == "__main__":
    main()