## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Animal is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee, has-a salary of 120000 
frank = Employee("Frank", 120000)

## mary has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()







class Person:
    ''' The class define Person. '''
    population = 0
    
    def __init__(self, name):
        '''Initializes the person's data'''
        self.name = name
        print 'Intializing ' + name
        self.__class__.population += 1
    
    def __del__(self):
        "I'm dying... "
        print self.name + " die."
        self.__class__.population -= 1
        print "there's %d left" % self.__class__.population
    
    def hello(self):
        '''Say Hello..'''
        print 'Hello, my name is %s' % self.name
    
    @staticmethod
    def howmany():
        print "there's %d left" % Person.population

tom = Person("tom")
tom.hello()
Person.howmany()

cat = Person("cat")
cat.hello()
Person.howmany()



class Parent(object):
    color = 'red'
    def __init__(self, color):
        self.color = color

class Child(Parent):
    color = 'green'
    def __init__(self, color):
        self.color = color

dad = Parent('yellow')
son = Child('blue')


print son.color
print son.__class__.color
print super(son.__class__, son).color

