class Person:
    """
    Represents a person with a name and age.
    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """        
    def __init__(self, name: str, age: int):
        """
        Initializes a new instance of the Person class.
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """        
        self.name = name
        self.age = age
        
    def __repr__(self):
        """Returns a string representation of the Person object for debugging.

        Returns:
            str: A string in the format 'Person(name=<name>, age=<age>)'.
        """
        return f"Person(name={self.name}, age={self.age})"

    def __str__(self):
        """Returns a user-friendly string representation of the Person object.

        Returns:
            str: A string in the format '<name> is <age> years old.'.
        """
        return f"{self.name} is {self.age} years old."
    
    def __eq__(self, other):
        """Checks if two Person objects are equal based on their name and age.

        Args:
            other (Person): The other Person object to compare.

        Returns:
            bool: True if both name and age are equal, False otherwise.
        """
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False    
    
    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."  
    
    
def demo():
    # Create two Person objects
    alice = Person("Alice", 30)
    bob = Person("Bob", 25)

    # Print their string representations
    print(str(alice))  # Output: Alice is 30 years old.
    print(repr(bob))   # Output: Person(name=Bob, age=25)

    # Compare two persons
    print(alice == bob)  # Output: False
    print(alice == Person("Alice", 30))  # Output: True

    # Use greet method
    print(alice.greet())  # Output: Hello, my name is Alice and I am 30 years old.

# Example usage
if __name__ == "__main__":
    demo()