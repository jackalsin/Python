from AbstractHuman import AbstractHuman 

class Staff(AbstractHuman):
    
    position = ''
    salary = 0

    def printDetail(self):
        print 'Name: '+self.name+'.'
        print 'Age: '+str(self.age)+'.'
        print 'Position: '+self.position+'.'
        print 'Department: '+self.department+'.'
        print 'Salary: '+str(self.salary)+'.'
