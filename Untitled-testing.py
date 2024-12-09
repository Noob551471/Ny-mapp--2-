class MyClass:
    # Class-level attribute
    my_class_attribute = "Hello from class"

    def __init__(self):
        self.my_instance_attribute = "Hello from instance"

    # Class-level method
    @classmethod
    def my_class_method(cls):
        return "This is a class method"

    # Instance method
    def my_instance_method(self):
        return "This is an instance method"

# Accessing class-level attributes and methods directly
print(MyClass.my_class_attribute)  # Outputs: Hello from class
result = MyClass.my_class_method()
print(result)  # Outputs: This is a class method

# Creating an instance of the class
obj = MyClass()

# Accessing instance-level attribute
print(obj.my_instance_attribute)  # Outputs: Hello from instance

# Calling instance method
result = obj.my_instance_method()
print(result)  # Outputs: This is an instance method

# You can also access class-level attributes directly
print(MyClass.my_class_attribute)
print(MyClass.my_class_method())
