# Singleton Pattern:
# Description: Ensures a class has only one instance and provides a global point of access.


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


#Factory Method Pattern:
# Description: Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.
class Factory:

    def create_product(self):
        pass


class ConcreteFactory(Factory):

    def create_product(self):
        return ConcreteProduct()


# Abstract Factory Pattern:
# Description: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
class AbstractFactory:

    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


# Builder Pattern:
# Description: Separates the construction of a complex object from its representation, allowing the same construction process to create various representations.
class Director:

    def construct(self, builder):
        builder.build_part_a()
        builder.build_part_b()


class Builder:

    def build_part_a(self):
        pass

    def build_part_b(self):
        pass


# Prototype Pattern:
# Description: Specifies the kind of objects to create using a prototypical instance and creates new objects by copying this prototype.
import copy


class Prototype:

    def clone(self):
        return copy.deepcopy(self)


# Adapter Pattern:
# Description: Converts the interface of a class into another interface that clients expect.
class Target:

    def request(self):
        pass


class Adapter(Target):

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()


# Decorator Pattern:
# Description: Attaches additional responsibilities to an object dynamically.
class Component:

    def operation(self):
        pass


class ConcreteComponent(Component):

    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):

    def __init__(self, component):
        self.component = component

    def operation(self):
        return f"Decorator({self.component.operation()})"


# Observer Pattern:
# Description: Defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.
class Subject:

    def add_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self):
        pass


class ConcreteSubject(Subject):

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()


# Strategy Pattern:
# Description: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.execute()


class Strategy:

    def execute(self):
        pass


# Command Pattern:
# Description: Encapsulates a request as an object, allowing for parameterization of clients with queues, requests, and operations.
class Command:

    def execute(self):
        pass


class Receiver:

    def action(self):
        return "Receiver action"


class ConcreteCommand(Command):

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        return self._receiver.action()