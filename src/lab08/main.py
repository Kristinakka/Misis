from models import Student
from serialize import students_to_json, students_from_json


def main():
    s1 = Student("Иван Иванович Петрович", "2020/10/02", "HGHG", 3.5)
    s2 = Student("Иван Иванович", "2020/10/02", "HGHG", 4.5)
    s3 = Student("Иван Петрович", "2020/10/02", "HGHG", 2.0)
    print("Преобразую список объектов в Json...")
    students_to_json([s1, s2, s3], r"data\lab_08\students_output.json")
    print("Считываю студентов с файла Json...")
    cnt = 0
    for s in students_from_json(r"data\lab_08\students_input.json"):
        cnt += 1
        print(cnt, "Student:", s)


if __name__ == "__main__":
    main()
