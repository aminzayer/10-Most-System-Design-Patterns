# Singleton Pattern:
# Description: Ensures a class has only one instance and provides a global point of access.
# This pattern is useful when exactly one object is needed to coordinate actions across the system.


class Singleton:
    # The private class variable to store the single instance.
    _instance = None

    def __new__(cls):
        # The `__new__` method is overridden to control the object creation process.
        if cls._instance is None:
            # If the instance does not exist, create a new one.
            cls._instance = super(Singleton, cls).__new__(cls)
        # Return the single instance.
        return cls._instance


# Factory Method Pattern:
# Description: Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.
# This pattern promotes loose coupling by allowing the client to create objects without knowing their concrete classes.

# The Product interface declares the operations that all concrete products must implement.
class Product:
    pass


# The ConcreteProduct class implements the Product interface.
class ConcreteProduct(Product):
    pass


# The Factory class declares the factory method, which returns an object of type Product.
class Factory:

    def create_product(self):
        # This method is intended to be overridden by subclasses.
        pass


# The ConcreteFactory class overrides the factory method to return an instance of a ConcreteProduct.
class ConcreteFactory(Factory):

    def create_product(self):
        # Creates and returns a ConcreteProduct instance.
        return ConcreteProduct()


# Abstract Factory Pattern:
# Description: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
# This pattern is useful when a system needs to be independent of how its products are created, composed, and represented.

# The AbstractProductA interface declares operations for a type of product.
class AbstractProductA:
    pass

# The AbstractProductB interface declares operations for another type of product.
class AbstractProductB:
    pass

# ConcreteProductA1 implements the AbstractProductA interface.
class ConcreteProductA1(AbstractProductA):
    pass

# ConcreteProductA2 implements the AbstractProductA interface.
class ConcreteProductA2(AbstractProductA):
    pass

# ConcreteProductB1 implements the AbstractProductB interface.
class ConcreteProductB1(AbstractProductB):
    pass

# ConcreteProductB2 implements the AbstractProductB interface.
class ConcreteProductB2(AbstractProductB):
    pass

# The AbstractFactory interface declares a set of methods for creating each type of abstract product.
class AbstractFactory:

    def create_product_a(self):
        # This method is intended to be overridden by concrete factories.
        pass

    def create_product_b(self):
        # This method is intended to be overridden by concrete factories.
        pass

# The ConcreteFactory1 class implements the operations to create concrete product objects.
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        # Creates and returns a ConcreteProductA1 instance.
        return ConcreteProductA1()

    def create_product_b(self):
        # Creates and returns a ConcreteProductB1 instance.
        return ConcreteProductB1()

# The ConcreteFactory2 class implements the operations to create concrete product objects.
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        # Creates and returns a ConcreteProductA2 instance.
        return ConcreteProductA2()

    def create_product_b(self):
        # Creates and returns a ConcreteProductB2 instance.
        return ConcreteProductB2()


# Builder Pattern:
# Description: Separates the construction of a complex object from its representation, allowing the same construction process to create various representations.
# This pattern allows for step-by-step construction of complex objects, providing control over the construction process.

# The Product class represents the complex object under construction.
class Product:
    def __init__(self):
        # Initializes a list to store the parts of the product.
        self.parts = []

    def add(self, part):
        # Adds a part to the product.
        self.parts.append(part)

    def list_parts(self):
        # Returns a string representation of the product's parts.
        return f"Product parts: {', '.join(self.parts)}"

# The Director class is responsible for managing the construction process using a builder object.
class Director:
    def construct(self, builder):
        # Instructs the builder to build part A.
        builder.build_part_a()
        # Instructs the builder to build part B.
        builder.build_part_b()

# The Builder interface specifies methods for creating the different parts of the Product.
class Builder:
    def __init__(self):
        # Initializes a new Product instance.
        self.product = Product()

    def build_part_a(self):
        # Abstract method for building part A.
        pass

    def build_part_b(self):
        # Abstract method for building part B.
        pass

    def get_product(self):
        # Returns the constructed product.
        return self.product

# The ConcreteBuilder class implements the Builder interface and provides specific implementations for building parts.
class ConcreteBuilder(Builder):
    def build_part_a(self):
        # Builds part A and adds it to the product.
        self.product.add("PartA")

    def build_part_b(self):
        # Builds part B and adds it to the product.
        self.product.add("PartB")


# Prototype Pattern:
# Description: Specifies the kind of objects to create using a prototypical instance and creates new objects by copying this prototype.
# This pattern is used to create new objects by copying an existing object, known as the prototype. It is useful when creating an object is more expensive than copying one.
import copy

# The Prototype class declares a cloning method.
class Prototype:

    def clone(self):
        # Creates a clone of the object.
        # `copy.deepcopy()` is used to create a deep copy of the object,
        # ensuring that all nested objects are also copied, rather than just referenced.
        return copy.deepcopy(self)


# Adapter Pattern:
# Description: Converts the interface of a class into another interface that clients expect.
# This pattern allows classes with incompatible interfaces to work together.

# The Target interface defines the domain-specific interface that Client uses.
class Target:

    def request(self):
        # This is the method that the client expects to call.
        pass

# The Adaptee class has an incompatible interface that needs adapting.
class Adaptee:
    def specific_request(self):
        # This is the specific method of the Adaptee class.
        return "Adaptee's specific request."

# The Adapter class makes the Adaptee's interface compatible with the Target's interface.
class Adapter(Target):

    def __init__(self, adaptee):
        # The Adapter holds an instance of the Adaptee.
        self.adaptee = adaptee

    def request(self):
        # The Adapter translates the request from the Target interface to the Adaptee's specific request.
        return self.adaptee.specific_request()


# Decorator Pattern:
# Description: Attaches additional responsibilities to an object dynamically.
# Decorators provide a flexible alternative to subclassing for extending functionality.

# The Component interface defines the interface for objects that can have responsibilities added to them dynamically.
class Component:

    def operation(self):
        # This method is implemented by concrete components and decorators.
        pass

# The ConcreteComponent class is an object to which additional responsibilities can be attached.
class ConcreteComponent(Component):

    def operation(self):
        # Implements the Component interface.
        return "ConcreteComponent"

# The Decorator class maintains a reference to a Component object and defines an interface that conforms to Component's interface.
class Decorator(Component):

    def __init__(self, component):
        # The Decorator wraps a Component object.
        self.component = component

    def operation(self):
        # Delegates the operation to the wrapped component.
        # Subclasses of Decorator can add their own behavior before or after delegating.
        return f"Decorator({self.component.operation()})"


# Observer Pattern:
# Description: Defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.
# This pattern is crucial for implementing distributed event handling systems.

# The Observer interface declares the update method, used by subjects to notify observers of state changes.
class Observer:
    def update(self, subject_state):
        # This method is called when the subject's state changes.
        pass

# The ConcreteObserver implements the Observer interface and stores state that should stay consistent with the subject's.
class ConcreteObserver(Observer):
    def __init__(self, name):
        # A name to identify the observer.
        self.name = name
        self._observer_state = None

    def update(self, subject_state):
        # Updates the observer's state based on the subject's state and prints a notification.
        self._observer_state = subject_state
        print(f"{self.name} received update: {self._observer_state}")

# The Subject class provides an interface for attaching and detaching Observer objects.
class Subject:
    def __init__(self):
        # A list to store registered observers.
        self._observers = []

    def add_observer(self, observer):
        # Registers an observer.
        self._observers.append(observer)

    def remove_observer(self, observer):
        # Unregisters an observer.
        self._observers.remove(observer)

    def notify_observers(self):
        # Notifies all registered observers about an event.
        # Concrete subjects will call this method to notify observers about state changes.
        pass

# The ConcreteSubject stores state of interest to ConcreteObserver objects and sends a notification to its observers when its state changes.
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        # The state of the ConcreteSubject.
        self._subject_state = None

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, state):
        self._subject_state = state
        # Notifies observers when the state changes.
        self.notify_observers()

    def notify_observers(self):
        # Notifies all observers about the state change.
        for observer in self._observers:
            observer.update(self._subject_state)


# Strategy Pattern:
# Description: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
# This pattern allows the algorithm to vary independently from clients that use it.

# The Context class uses a Strategy object to implement its behavior.
class Context:

    def __init__(self, strategy):
        # Initializes with a specific strategy.
        self._strategy = strategy

    def set_strategy(self, strategy):
        # Allows changing the strategy at runtime.
        self._strategy = strategy

    def execute_strategy(self):
        # Delegates the work to the strategy object.
        return self._strategy.execute()

# The Strategy interface declares an operation common to all supported versions of the algorithm.
class Strategy:

    def execute(self):
        # This method will be implemented by concrete strategies.
        pass

# ConcreteStrategyA implements the algorithm using the Strategy interface.
class ConcreteStrategyA(Strategy):
    def execute(self):
        # Implements the algorithm.
        return "Executing ConcreteStrategyA."

# ConcreteStrategyB implements a different algorithm using the Strategy interface.
class ConcreteStrategyB(Strategy):
    def execute(self):
        # Implements the algorithm.
        return "Executing ConcreteStrategyB."


# Command Pattern:
# Description: Encapsulates a request as an object, allowing for parameterization of clients with queues, requests, and operations.
# This pattern turns a request into a stand-alone object that contains all information about the request.

# The Command interface declares a method for executing a command.
class Command:

    def execute(self):
        # This method will be implemented by concrete commands.
        pass

# The Receiver class knows how to perform the operations associated with carrying out a request.
class Receiver:

    def action(self):
        # Performs the actual work.
        return "Receiver action"

# The ConcreteCommand defines a binding between a Receiver object and an action.
class ConcreteCommand(Command):

    def __init__(self, receiver):
        # Stores the Receiver instance.
        self._receiver = receiver

    def execute(self):
        # Executes the command by calling the action on the Receiver.
        return self._receiver.action()