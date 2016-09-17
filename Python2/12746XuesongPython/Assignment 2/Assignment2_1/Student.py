class Student:
    name = ''
    advisor = None  # None is a keyword in Python means that there is no value in a variable that is an instance
    totalUnits = 0
    age = 0
    department = ''

    def assignAdvisor(self, ad):
       self.advisor = ad

    def addUnits(self,u):
        self.totalUnits = self.totalUnits+u

    def addUnitsFromCourse(self,c):
        self.totalUnits = self.totalUnits+c.unit

    def printName(self):        # This method will just print out the student's name
        print self.name

    def printDetail(self):
        print 'Name: '+self.name+'.'
        print 'Age: '+str(self.age)+'.'
        print 'Total Units: '+str(self.totalUnits)+'.'
        print 'Department: '+self.department+'.'
        print 'Advisor: '+self.advisor.name+'.'