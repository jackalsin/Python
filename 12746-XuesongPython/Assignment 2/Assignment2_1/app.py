from Academic.Advisor import Advisor
from Academic.Course import Course

from Assignment2_1.Academic.Student import Student

advisor1 = Advisor()
advisor1.name = 'Pine Liu'
advisor1.researchTopic = 'Building Information Modeling'
advisor1.department = 'CEE&FMS'
advisor1.age = 29

advisor1.printDetail()

student1 = Student()
student1.name = 'Jingkun Gao'
student1.printName()

student1.assignAdvisor(advisor1)

student1.addUnits(12)
student1.addUnits(6)
student1.addUnits(12)
student1.addUnits(12)

course1 = Course()
course1.name = 'Python Prototyping'
course1.unit = 6
course1.ID = '12-746'

student1.addUnitsFromCourse(course1)
student1.printDetail()



