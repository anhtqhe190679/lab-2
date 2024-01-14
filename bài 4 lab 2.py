def la_so_palindrome(num):
    chuoi_so = str(num)
    return chuoi_so == chuoi_so[::-1]

def hien_thi_so_palindrome(m, n):
    so_palindrome = []
    for num in range(m, n + 1):
        if la_so_palindrome(num):
            so_palindrome.append(num)
    return so_palindrome

def main():
    m = int(input("Nhập số nguyên thứ nhất (m): "))
    n = int(input("Nhập số nguyên thứ hai (n): "))
    if m >= n:
        print("Nhập m nhỏ hơn n")
        return
    so_palindrome = hien_thi_so_palindrome(m, n)
    print(f"Các số palindrome trong khoảng từ {m} đến {n}:")
    if so_palindrome:
        print(so_palindrome)
    else:
        print("Không tìm thấy số palindrome trong khoảng")

if __name__ == "__main__":
    main()