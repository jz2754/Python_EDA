
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +"." +last +"@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("jingwei", "zhou", 500)
emp_2 = Employee("user", "test", 500)

# emp_1.first = 'jingwei'
# emp_1.last = 'zhou'
# emp_1.email = '841566649.qq.com'
# emp_1.pay = 500

print(emp_1.email)
print(emp_2.email)

print(Employee.fullname(emp_2))
print(emp_1.fullname())


# another example


class coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"



c = coordinate(3,4)
O = coordinate(0,0)
print(c.x)
print(c.distance(O))



# inheritance:

class animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class cat(animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)


class Person(animal):
    def __init__(self, name, age):
        animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.age - other.age
        prints(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)



p1 = Person("jingwei", 32)
p2 = Person("nini", 26)

p1.get_name()
p1.speak()

c = cat(10)
c.get_name()
c.set_name('kk')
c.get_name()
c.name

































