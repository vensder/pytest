class Grades():
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty book"""
        self.students = list()  #  list of Student 
        self.gradesd = dict()   #  maps idNum -> list of grades
        self.isSorted = True    #  True if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Dublicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = list()
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrade(self, student):
        """Return a list of grades for student"""
        try:    #  Return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]  #  Return copy of list of students
        

def gradeReport(course):
    """Assumes: course is of type grades"""
    report = list()
    for s in course.allStudents():
        tot = .0
        numGades = 0
        for g in course.getGrades(s):
            tot +=g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


