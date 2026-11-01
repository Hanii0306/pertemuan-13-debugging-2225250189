# PRAKTIK 4: DEBUGGING DAN TESTING

KKM = 60


def validasi_nilai(nilai):
    if not isinstance(nilai, (int, float)):
        return False

    if nilai < 0 or nilai > 100:
        return False

    return True


def hitung_rata_rata(daftar_nilai):
    if not daftar_nilai:
        return 0

    return sum(daftar_nilai) / len(daftar_nilai)


def status_kelulusan(nilai):
    if not validasi_nilai(nilai):
        return "Nilai tidak valid"

    if nilai >= KKM:
        return "Lulus"

    return "Tidak Lulus"


def jalankan_test():
    test_case = [
        {
            "input": 75,
            "expected": "Lulus"
        },
        {
            "input": 60,
            "expected": "Lulus"
        },
        {
            "input": 59,
            "expected": "Tidak Lulus"
        },
        {
            "input": 120,
            "expected": "Nilai tidak valid"
        },
        {
            "input": -5,
            "expected": "Nilai tidak valid"
        }
    ]

    jumlah_pass = 0
    jumlah_fail = 0

    print("\nHASIL TESTING")
    print("========================")

    for nomor, test in enumerate(test_case, start=1):
        actual = status_kelulusan(test["input"])
        expected = test["expected"]

        if actual == expected:
            status = "PASS"
            jumlah_pass += 1
        else:
            status = "FAIL"
            jumlah_fail += 1

        print(f"Test Case {nomor}")
        print("Input:", test["input"])
        print("Expected:", expected)
        print("Actual:", actual)
        print("Status:", status)
        print("------------------------")

    print("Jumlah PASS:", jumlah_pass)
    print("Jumlah FAIL:", jumlah_fail)


def main():
    daftar_nilai = [80, 90, 75, 60, 55]

    print("PRAKTIK DEBUGGING NILAI MAHASISWA")
    print("================================")

    print("Daftar nilai:", daftar_nilai)

    rata_rata = hitung_rata_rata(daftar_nilai)

    print("Rata-rata:", rata_rata)

    for nilai in daftar_nilai:
        print(
            f"Nilai {nilai}: "
            f"{status_kelulusan(nilai)}"
        )

    jalankan_test()


if __name__ == "__main__":
    main()