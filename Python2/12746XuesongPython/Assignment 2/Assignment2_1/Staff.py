class Staff:
    name = ''
    age = 0
    position = ''
    department = ''
    salary = 0

    def printName(self):        # This method will just print out the student's name
        print self.name

    def printDetail(self):
        print 'Name: '+self.name+'.'
        print 'Age: '+str(self.age)+'.'
        print 'Position: '+self.position+'.'
        print 'Department: '+self.department+'.'
        print 'Salary: '+str(self.salary)+'.'
