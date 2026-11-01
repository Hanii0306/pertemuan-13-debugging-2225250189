# LATIHAN 3: TEST CASE

def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"

    return "Tidak Lulus"


def jalankan_test():
    daftar_test = [
        (75, "Lulus"),
        (60, "Lulus"),
        (59, "Tidak Lulus"),
        (0, "Tidak Lulus"),
        (100, "Lulus")
    ]

    print("HASIL PENGUJIAN")
    print("================")

    for nomor, (input_nilai, expected) in enumerate(
        daftar_test, start=1
    ):
        actual = status_lulus(input_nilai)

        if actual == expected:
            status = "PASS"
        else:
            status = "FAIL"

        print(f"Test {nomor}")
        print("Input:", input_nilai)
        print("Expected:", expected)
        print("Actual:", actual)
        print("Status:", status)
        print("----------------")


if __name__ == "__main__":
    jalankan_test()