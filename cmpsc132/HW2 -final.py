# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        return f'{self.cid}({self.credits}): {self.cname}'

    __repr__ = __str__

    def __eq__(self, other):
        if type(other) == Course:
            if self.cid == other.cid:
                return True
        return False



class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        if cid not in self.courseOfferings:
            course = Course(cid, cname, credits)
            self.courseOfferings[cid] = course
            return 'Course added Successfully'
        else:
            return 'Course already added'

    def removeCourse(self, cid):
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return 'Course removed successfully'
        else:
            return 'Course not found'

    def _loadCatalog(self, file):
        with open(file, 'r') as f: 
            course_info = f.readlines()  # You might change .readlines() for .read() if it suits your implementation 
        for info in course_info:
            entry = info.rstrip('\n')
            entrylst = entry.split(',')
            self.addCourse(entrylst[0], entrylst[1], int(entrylst[2]))
        


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self):
        self.courses = {}



    def __str__(self):
        if len(self.courses) == 0:
            return 'No courses'
        return '; '.join(self.courses.keys())

    __repr__ = __str__

    def addCourse(self, course):
        if course.cid not in self.courses:
            self.courses[course.cid] = course
        else:
            return 'Course already added'

    def dropCourse(self, course):
        if course.cid not in self.courses:
            return 'No such course'
        else:
            del self.courses[course.cid]

    @property
    def totalCredits(self):
        total = 0
        for course in self.courses.values():
            total += course.credits
        return total

    @property
    def isFullTime(self):
        return self.totalCredits >= 12

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        self.amount = amount
        self.loan_id = self.__getloanID


    def __str__(self):
        return f'Balance: ${self.amount}'

    __repr__ = __str__


    @property
    def __getloanID(self):
        return random.randint(10000, 99999)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ssn
        

    def __str__(self):
        last4 = f'{self.get_ssn()[7]}{self.get_ssn()[8]}{self.get_ssn()[9]}{self.get_ssn()[10]}'    #brokedown the string for ssn into the last 4 digits and set it to last4
        return f'Person({self.name}, ***-**-{last4})'

    __repr__ = __str__

    def get_ssn(self):
        return self.__ssn

    def __eq__(self, other):
        if type(other) == Person:
            if self.__ssn == other.get_ssn():
                return True
        return False

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name, ssn)
        self.__supervisor = supervisor

    def __str__(self):
        return f'Staff({self.name}, {self.id})'

    __repr__ = __str__


    @property
    def id(self):
        #isolating the last 4 digits of the ssn   
        last4 = f'{self.get_ssn()[7]}{self.get_ssn()[8]}{self.get_ssn()[9]}{self.get_ssn()[10]}'

        #isolating the initials of the name
        lstname = self.name.split()
        initials = f'{lstname[0][0]}{lstname[1][0]}'
        initials = initials.lower()
        
        return f'905{initials}{last4}'

    @property   
    def getSupervisor(self):
        return self.__supervisor

    def setSupervisor(self, new_supervisor):
        if type(new_supervisor) == Staff:
            self.__supervisor = new_supervisor
            return 'Completed!'
        return None
            

    def applyHold(self, student):
        if type(student) == Student:
            student.hold = True
            return 'Completed!'
        else:
            return None

    def removeHold(self, student):
        if type(student) == Student:
            student.hold = False
            return 'Completed!'
        else:
            return None

    def unenrollStudent(self, student):
        if type(student) == Student:
            student.active = False
            return 'Completed!'
        else:
            return None

    def createStudent(self, person):
        newstudent = Student(person.name, person.get_ssn(), 'Freshman')
        return newstudent
        




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''

    def __init__(self, name, ssn, year):
        random.seed(1)
        super().__init__(name, ssn)
        self.hold = False
        self.active = True 
        self.semesters = {}
        self.account = self.__createStudentAccount()
        self.classCode = year
         

    def __str__(self):
        return f'Student({self.name}, {self.id}, {self.classCode})'

    __repr__ = __str__

    def __createStudentAccount(self):
        return StudentAccount(self)


    @property
    def id(self):
        last4 = f'{self.get_ssn()[7]}{self.get_ssn()[8]}{self.get_ssn()[9]}{self.get_ssn()[10]}'

        #isolating the initials of the name
        lstname = self.name.split()
        initials = f'{lstname[0][0]}{lstname[1][0]}'
        initials = initials.lower()
        
        return f'{initials}{last4}'

    def registerSemester(self):
        if self.active == True and self.hold == False:
            key = len(self.semesters) + 1
            self.semesters[key] = Semester()
            if key >= 1 and key <= 2:
                self.classCode = 'Freshman'
            elif key > 2 and key <= 4:
                self.classCode = 'Sophomore'
            elif key > 4 and key <= 6:
                self.classCode = 'Junior'
            else:
                self.classCode = 'Senior'
            return None
        return 'Unsuccessful operation'



    def enrollCourse(self, cid, catalog):
        if self.hold == False and self.active == True:
            if cid in catalog.courseOfferings:
                if cid not in self.semesters[len(self.semesters)].courses:
                    self.semesters[len(self.semesters)].addCourse(catalog.courseOfferings[cid])
                    self.account.chargeAccount(catalog.courseOfferings[cid].credits * self.account.CREDIT_PRICE)
                    return "Course added successfully"
                else:
                    return 'Course already enrolled'
            else:
                return 'Course not found'
        return 'Unsuccessful operation'


    def dropCourse(self, cid):
        if self.hold == False and self.active != False:
            if cid in self.semesters[len(self.semesters)].courses:
                self.account.makePayment(self.semesters[len(self.semesters)].courses[cid].credits * self.account.CREDIT_PRICE * 0.5)
                self.semesters[len(self.semesters)].dropCourse(self.semesters[len(self.semesters)].courses[cid])
                return 'Course dropped successfully'
            else:
                return'Course not found'
        return 'Unsuccessful operation'


    def getLoan(self, amount):
        if self.active == True:
            if self.semesters[len(self.semesters)].isFullTime == True:
                loan = Loan(amount)
                self.account.loans[loan.loan_id] = loan
                self.account.makePayment(amount)
                return None
            else:
                return "Not full-time"
        return 'Unsuccessful operation'





class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    
    CREDIT_PRICE = 1000

    def __init__(self, student):
        self.student = student
        self.balance = 0
        self.loans = {}


    def __str__(self):
        return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'

    __repr__ = __str__


    def makePayment(self, amount):
        self.balance -= amount
        return self.balance


    def chargeAccount(self, amount):
        self.balance += amount
        return self.balance




def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=False)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    # doctest.run_docstring_examples(Student, globals(), name='HW2',verbose=False)   

if __name__ == "__main__":
    run_tests()