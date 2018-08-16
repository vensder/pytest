import datetime


class Person():
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split()[-1]

    def __lt__(self, other):
        """return True if self's name is lexicofraphically
            less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

##    def __gt__(self, other):
##        if self.lastName == other.lastName:
##            return self.name > other.name
##        return self.lastName > other.lastName

    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def __str__(self):
        """return self's name"""
        return self.name


class MITPerson(Person):
    nextIdNum = 0  # Next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

##    def __gt__(self, other):
##        return self.idNum > other.idNum

    def speak(self, utterance):
        return self.name + " says: " + utterance


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In cource ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

    

class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, " Yo Bro, " + utterance)


class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj,Student)



class Grades():
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty book"""
        self.students = list()  #  list of Student 
        self.grades = dict()   #  maps idNum -> list of grades
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
        numGrades = 0
        for g in course.getGrade(s):
            tot +=g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Aff', 2019)
ug3 = UG('Drew Hust', 2017)
ug4 = UG('Mark Zuck', 2017)
g1 = Grad('Bill Gat')
g2 = Grad('Steve Wozn')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug3, 85)
six00.addGrade(ug3, 75)

print('''''''''''''''''''''''''''''''''''''''''')
print(gradeReport(six00))

six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 90)
six00.addGrade(ug2, 73)

print('''''''''''''''''''''''''''''''''''''''''')
print(gradeReport(six00))

p1 = Person('Mark Zuk')
p2 = Person('Drew H')
p3 = Person('Bill G')
p4 = Person('Andr G')
p5 = Person('Steve W')


print('###################')

personList = [p1, p2, p3, p4, p5]

for p in personList:
    print(p)

personList.sort()
print('========')

for p in personList:
    print(p)


m3 = MITPerson('Mark Zuk')
Person.setBirthday(m3, 5, 14,84)
m2 = MITPerson('Drew Hu')
Person.setBirthday(m2, 3,4, 83)
m1 = MITPerson('Bill Gat')
Person.setBirthday(m1, 10,28,55)

MITPersonList = [m3,m2,m1]

print('========')
print('========')

for m in MITPersonList:
    print(m)

MITPersonList.sort()
print('========')

for m in MITPersonList:
    print(m)

print('###################')
print('###################')
print('###################')

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')

print(p1, p2, p3, p4)
pList = [p1, p2, p3, p4]

##p1 < p2
##p2 < p3
##p3 < p4

for p in pList:
    print(p)
    
pList.sort()
print('========')

for p in pList:
    print(p)


s1 = UG('Matt Dam', 2017)
s2 = UG('Ben Aff', 2017)
s3 = UG('Lin Man Mir', 2018)
s4 = Grad('Leon di Cap')

studentList = [s1, s2, s3, s4]

print(s1.speak('where is the q'))
print(s2.speak('I have no clue'))


p = Professor('Doctor Eric', 'CS')
print(p.speak('aaa'))
print(p.lecture('OOP'))
