class StudentProfile:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_info(self, new_name, new_id, new_major):
        self.name = new_name
        self.id = new_id
        self.major = new_major


class GPAManager:
    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        return sum(self.grades) / len(self.grades)


class PrintGPAReport:
    def __init__(self, student_profile, gpa_manager):
        self.student_profile = student_profile
        self.gpa_manager = gpa_manager

    def print_report(self):
        print(
            "코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}".format(
                self.student_profile.name,
                self.student_profile.id,
                self.student_profile.major,
                self.gpa_manager.get_average_gpa(),
            )
        )


class Student:
    def __init__(self, name, id, major):
        self.profile = StudentProfile(name, id, major)
        self.grades = []
        self.gpa_manager = GPAManager(self.grades)
        self.print_gpa_report = PrintGPAReport(self.profile, self.gpa_manager)


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.profile.change_info("강영훈", 20130024, "컴퓨터 공학과")

# 성적 추가
younghoon.gpa_manager.add_grade(3.0)
younghoon.gpa_manager.add_grade(3.33)
younghoon.gpa_manager.add_grade(3.67)
younghoon.gpa_manager.add_grade(4.3)

# 학생성적표
younghoon.print_gpa_report.print_report()
