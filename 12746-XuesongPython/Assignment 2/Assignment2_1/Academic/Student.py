from AbstractHuman import AbstractHuman 

class Student(AbstractHuman):
    advisor = None  # None is a keyword in Python means that there is no value in a variable that is an instance
    totalUnits = 0

    def assignAdvisor(self, ad):
       self.advisor = ad

    def addUnits(self,u):
        self.totalUnits = self.totalUnits+u

    def addUnitsFromCourse(self,c):
        self.totalUnits = self.totalUnits+c.unit

    def printDetail(self):
        print 'Name: '+self.name+'.'
        print 'Age: '+str(self.age)+'.'
        print 'Total Units: '+str(self.totalUnits)+'.'
        print 'Department: '+self.department+'.'
        print 'Advisor: '+self.advisor.name+'.'