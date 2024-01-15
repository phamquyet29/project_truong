import math

def isPerfectSquare(num):
    # Kiểm tra xem số num có phải là số chính phương hay không
    squareRoot = int(math.sqrt(num))
    return squareRoot * squareRoot == num

def fibonacciNumbers(limit):
    # Tạo danh sách số Fibonacci nhỏ hơn hoặc bằng giới hạn
    fib_numbers = [0, 1]
    while fib_numbers[-1] + fib_numbers[-2] <= limit:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers

def sumOfDigits(num):
    # Tính tổng các chữ số của số num
    return sum(int(digit) for digit in str(num))

def main():
    # Nhập số nguyên dương n
    n = int(input("Nhập số nguyên dương n (0 <= n <= 1000): "))

    # Phần a
    perfect_squares = [i for i in range(n) if isPerfectSquare(i)]
    print ("Danh sách số chính phương nhỏ hơn", n, ":", perfect_squares)

    # Phần b
    fib_numbers = fibonacciNumbers(n)
    common_numbers = list(set(perfect_squares) & set(fib_numbers))
    print ("Số chính phương và là số Fibonacci:", common_numbers)

    # Phần c
    two_digit_squares = [i for i in perfect_squares if 10 <= i <= 99]
    sum_of_digit_values = [sumOfDigits(square) for square in two_digit_squares]
    print ("Danh sách giá trị lần lượt của tổng các chữ số của số chính phương có 2 chữ số trở lên:", sum_of_digit_values)

if __name__ == "__main__":
    main()
