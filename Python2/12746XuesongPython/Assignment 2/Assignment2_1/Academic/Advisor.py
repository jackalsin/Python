from AbstractHuman import AbstractHuman 

class Advisor(AbstractHuman):

    researchTopic = ''
    salary = 0

    def printDetail(self):
        print 'Name: '+self.name+'.'
        print 'Age: '+str(self.age)+'.'
        print 'Research Topic: '+self.researchTopic+'.'
        print 'Department: '+self.department+'.'
        print 'Salary: '+str(self.salary)+'.'