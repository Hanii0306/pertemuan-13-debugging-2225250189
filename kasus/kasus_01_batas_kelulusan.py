# KASUS 1: BUG BATAS KELULUSAN

def status_kelulusan(nilai):
    if nilai > 60:  # BUG: seharusnya menggunakan >= 60
        return "Lulus"
    else:
        return "Tidak Lulus"


def main():
    print("PROGRAM CEK KELULUSAN")
    print("=====================")

    daftar_nilai = [75, 60, 59, 85]

    for nilai in daftar_nilai:
        hasil = status_kelulusan(nilai)

        print(f"Nilai: {nilai}")
        print(f"Status: {hasil}")
        print("---------------------")


if __name__ == "__main__":
    main()