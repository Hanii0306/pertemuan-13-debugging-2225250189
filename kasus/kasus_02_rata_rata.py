# KASUS 2: BUG PERHITUNGAN RATA-RATA

def hitung_rata_rata(daftar_nilai):
    total = sum(daftar_nilai)

    # BUG: pembagi dibuat tetap 3
    rata_rata = total / 3

    return rata_rata


def main():
    print("PROGRAM PERHITUNGAN RATA-RATA")
    print("=============================")

    nilai = [80, 90, 70, 60]

    hasil = hitung_rata_rata(nilai)

    print("Daftar nilai:", nilai)
    print("Rata-rata:", hasil)


if __name__ == "__main__":
    main()