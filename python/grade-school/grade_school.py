# Define a custom sorting function to sort by grade levels first and then by names
def custom_sort_key(item):
    # First, sort by grade levels (the second element of the tuple)
    grade = item[1]
    # Then, sort by names (the first element of the tuple)
    name = item[0]
    return (grade, name)

class School:
    def __init__(self):
        self.students = {}
        self.history = []

    def add_student(self, name, grade):
        if name not in self.students:
            self.students.update({name: grade})
            sorted_students = sorted(self.students.items(), key=custom_sort_key)
            self.students = dict(sorted_students)
            self.history.append(True)
        else:
            self.history.append(False)


    def roster(self):
        roster = []
        for student in self.students.items():
            roster.append(student[0])
        return roster
        

    def grade(self, grade_number):
        student_list = []
        for student, grade in self.students.items():
            if grade == grade_number:
                student_list.append(student)
        return student_list

    def added(self):
        return self.history
