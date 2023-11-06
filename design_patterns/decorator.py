from enum import Enum

class Colors(Enum):
    ORANGE = 1
    BLUE = 2


class Class_Type(Enum):
    MANDATORY = 1
    OPTIONAL = 2


# Component Interface
class ColorComponent:
    def get_color(self):
        pass


# Concrete Component
class ConcreteColorComponent(ColorComponent):
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


# Decorator
class ColorDecorator(ColorComponent):
    def __init__(self, component, class_type):
        self.component = component
        self.class_type = class_type

    def get_color(self):
         return self.component.get_color()


# Concrete Decorator
class MandatoryDecorator(ColorDecorator):
    def get_color(self):
        if self.class_type == Class_Type.MANDATORY:
            return Colors.BLUE


# Concrete Decorator
class OptionalDecorator(ColorDecorator):
    def get_color(self):
        if self.class_type == Class_Type.OPTIONAL:
            return Colors.ORANGE


# Usage
if __name__ == "__main__":
    base_component = ConcreteColorComponent(Colors.ORANGE)

    mandatory_decorator = ColorDecorator(base_component, Class_Type.MANDATORY)
    optional_decorator = ColorDecorator(base_component, Class_Type.OPTIONAL)

    print(mandatory_decorator.get_color())  # Output: Colors.BLUE
    print(optional_decorator.get_color())   # Output: Colors.ORANGE

    