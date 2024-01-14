def tinh_S1(n):
    return sum(range(1, n + 1))

def tinh_S2(n):
    result = 1
    for i in range(1, n + 1):
        result = i*(i-1) 
    return result

def tinh_S3(n):
    return sum(1 / i for i in range(1, n + 1))

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    while True:
        n = int(input("Nhập số nguyên: "))
        if n <= 5:
            print("Nhập số nguyên lớn hơn 5")
        else:
            break

    S1 = tinh_S1(n)
    S2 = tinh_S2(n)
    S3 = tinh_S3(n)

    print(f"S1 = {S1}")
    print(f"S2 = {S2}")
    print(f"S3 = {S3}")

    if prime(n):
        print(f"{n} là số nguyên")
    else:
        print(f"{n} không phải là số nguyên")

if __name__ == "__main__":
    main()
