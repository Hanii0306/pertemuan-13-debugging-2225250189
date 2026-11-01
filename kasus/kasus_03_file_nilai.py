# KASUS 3: BUG PEMBACAAN FILE NILAI

def baca_nilai():
    nama_file = "data_nilai.txt"

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            daftar_nilai = []

            for baris in file:
                nilai = int(baris.strip())
                daftar_nilai.append(nilai)

        print("Data nilai:", daftar_nilai)

    except FileNotFoundError:
        print("File tidak ditemukan.")

    except ValueError:
        print("Terdapat data nilai yang bukan angka.")

    except OSError as error:
        print("Kesalahan file:", error)


if __name__ == "__main__":
    baca_nilai()