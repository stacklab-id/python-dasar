grade = input("masukan grade: ")

print(grade)

match grade:
    case "A":
        print("Sangat Baik")
    case "B":
        print("Baik")
    case "C":
        print("cukup")
    case "D":
        print("kurang")
    case _:
        print("Grade yang anda masukan tidak ditemukan")