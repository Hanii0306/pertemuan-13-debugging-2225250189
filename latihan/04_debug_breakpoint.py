# LATIHAN 4: DEBUGGING MENGGUNAKAN BREAKPOINT

def hitung_total(daftar_nilai):
    total = 0

    for nilai in daftar_nilai:
        total += nilai

    return total


def main():
    daftar_nilai = [70, 80, 90, 85]

    hasil = hitung_total(daftar_nilai)

    print("Daftar nilai:", daftar_nilai)
    print("Total nilai:", hasil)


if __name__ == "__main__":
    main()