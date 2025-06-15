from module_b import greeting as greeting_module_b, Person  # import Person class and greeting function from module_b
from module_c import greeting as greeting_module_c  # import greeting function from module_c

if __name__ == "__main__":  # This block will only run if this file is executed directly
    p1 = Person("Dendi", 32)  # Create an instance of Person
    greeting_module_b(p1.name)  # Call the greeting function with the name of the person
    greeting_module_c(p1.name)
