# LATIHAN 2: TRACING FUNGSI

def hitung_total(nilai1, nilai2, nilai3):
    total = nilai1 + nilai2 + nilai3
    return total


def hitung_rata_rata(total, jumlah_data):
    rata_rata = total / jumlah_data
    return rata_rata


def main():
    a = 80
    b = 90
    c = 70

    total = hitung_total(a, b, c)

    rata_rata = hitung_rata_rata(total, 3)

    print("Nilai pertama:", a)
    print("Nilai kedua:", b)
    print("Nilai ketiga:", c)
    print("Total nilai:", total)
    print("Rata-rata:", rata_rata)


if __name__ == "__main__":
    main()