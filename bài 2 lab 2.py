def la_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def tim_so_nguyen_to(num):
    nguyen_to = []
    for i in range(2, num + 1):
        if la_so_nguyen_to(i) and num % i == 0:
            nguyen_to.append(i)
    return nguyen_to

def tim_nguyen_to_chung(m, n):
    nguyen_to_m = set(tim_so_nguyen_to(m))
    nguyen_to_n = set(tim_so_nguyen_to(n))
    nguyen_to_chung = []

    for so in nguyen_to_m:
        if so in nguyen_to_n:
            nguyen_to_chung.append(so)

    return nguyen_to_chung

def tim_ucln(m, n):
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return abs(m)

def tim_bcnn(m, n):
    bcnn = m * n // tim_ucln(m, n)
    return abs(bcnn)

def main():
    m = int(input("Nhập số nguyên thứ nhất (m): "))
    n = int(input("Nhập số nguyên thứ hai (n): "))

    nguyen_to_chung = tim_nguyen_to_chung(m, n)
    ucln = tim_ucln(m, n)
    bcnn = tim_bcnn(m, n)

    print("Các ước số nguyên tố chung:", nguyen_to_chung)
    print("Ước số chung lớn nhất (ƯCLN):", ucln)
    print("Bội số chung nhỏ nhất (BCNN):", bcnn)

if __name__ == "__main__":
    main()