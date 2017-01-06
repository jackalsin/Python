# This example shows how to create a class and then use it to create instances to represent data.

###############################################
# This is the class definition. A class only defines attributes and methods that are
# commonly used in all it's instances/objects. It does not define any specific values.
#
class Drawing():


    def __init__(self, bn,yc,con,f,s,file,n):
        self.buildingName = bn
        self.yearConstructed = yc
        self.contractor = con
        self.floor = f
        self.shop = s
        self.imageFile = file
        self.name = n

    def porterHallDrawing(self):
        if self.buildingName == "Porter Hall":
            print self.yearConstructed


# This is the end of the class definition. If there is no instance/object created,
# this class definition will do nothing. A class is an abstract template. It does not
# represent any actual thing or values. Only by creating instance/object from the class,
# you are describing a realworld thing.
###############################################

