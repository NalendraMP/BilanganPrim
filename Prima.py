def hitung_prima(number):
    """Fungsi ini memeriksa apakah suatu bilangan prima atau bukan."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    """Fungsi untuk menguji bilangan prima."""
    try:
        input_number = int(input("Masukkan sebuah bilangan: "))
        if hitung_prima(input_number):
            print(f"{input_number} adalah bilangan prima.")
        else:
            print(f"{input_number} bukan bilangan prima.")
    except ValueError:
        print("Masukkan harus bilangan bulat.")

if __name__ == "__main__":
    main()

