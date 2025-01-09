import random
import string

def generate_random_names(n):
    """Menghasilkan daftar nama acak sebanyak n."""
    names = []
    for _ in range(n):
        name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        names.append(name)
    return names

def menu():
    print("\nTes Program AKA")
    print("1. Function Iteratif")
    print("2. Function Rekursif")
    print("0. Keluar")

def count_arrangements_iterative(n, k):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            dp[i] += dp[i - j]
    return dp[n]

def count_arrangements_recursive(n, k):
    if n == 0 or k == 0:
        return 1
    return count_arrangements_recursive(n - 1, k) + count_arrangements_recursive(n - 1, k - 1)

def main():
    while True:
        menu()
        choice = input("Pilih opsi: ")
        if choice == "1":
            try:
                n = int(input("Masukkan jumlah kursi (n): "))
                k = int(input("Masukkan ukuran maksimum kelompok (k): "))
                random_names = generate_random_names(n)
                print(f"Nama-nama acak: {random_names[:10]}...")  # Tampilkan sebagian untuk mempermudah
                result = count_arrangements_iterative(n, k)
                print(f"Hasil (Iteratif): {result}")
            except ValueError:
                print("Harap masukkan angka yang valid!")
        elif choice == "2":
            try:
                n = int(input("Masukkan jumlah kursi (n): "))
                k = int(input("Masukkan ukuran maksimum kelompok (k): "))
                random_names = generate_random_names(n)
                print(f"Nama-nama acak: {random_names[:10]}...")  # Tampilkan sebagian untuk mempermudah
                result = count_arrangements_recursive(n, k)
                print(f"Hasil (Rekursif): {result}")
            except ValueError:
                print("Harap masukkan angka yang valid!")
        elif choice == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
