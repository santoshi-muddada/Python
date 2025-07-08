#  multilevel inheritance
class parent:
    def function1 (self):
        print("this is parent class")
class child(parent):
    def function2 (self):
        print("this is child class")
class grandchild(child):
    def function3(self):
        print("this grandchild class")
        print("__________________")

object=grandchild()
object.function1()
object.function2()
object.function3() 