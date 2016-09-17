class Advisor:
    name = ''
    age = 0
    researchTopic = ''
    department = ''
    salary = 0

    def printName(self):        # This method will just print out the student's name
        print self.name

    def printDetail(self):
        print 'Name: '+self.name+'.'
        print 'Age: '+str(self.age)+'.'
        print 'Research Topic: '+self.researchTopic+'.'
        print 'Department: '+self.department+'.'
        print 'Salary: '+str(self.salary)+'.'