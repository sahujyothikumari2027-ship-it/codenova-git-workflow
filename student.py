def get_student(name, course):
    return {
        "name": name,
        "course": course
    }


if __name__ == "__main__":
    student = get_student("Jyothi", "Computer Science")
    print(student)