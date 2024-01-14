def bieu_dien_dang_binary(n):
    binary_format = bin(n)[2:]
    print(f"{n} trong hệ nhị phân: {binary_format}")

def tinh_tong_digits(n):
    return sum(int(digit) for digit in str(n))

def reverse_number(n):
    return int(str(n)[::-1])

def main():
    while True:
        try:
            n = int(input("Nhập một số nguyên(n): "))
            break
        except ValueError:
            print("Hãy nhập 1 số nguyên.")

    bieu_dien_dang_binary(n)

    m = reverse_number(n)
    print(f"số đối của {n} là: {m}")

    n = int(input("Nhập giá trị n: "))
    digit_sum = tinh_tong_digits(n)
    print(f"tổng của digits của {n} là: {digit_sum}")

if __name__ == "__main__":
    main()