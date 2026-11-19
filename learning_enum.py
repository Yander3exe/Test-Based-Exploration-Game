from enum import Enum, Flag, auto

#using power of 2
#class Colour(Flag):
#    RED: int = 1
#    GREEN: int = 2
#    BLUE: int = 4
#    YELLOW: int = 8
#    BLACK: int = 16

#instead of writing each value manually, auto() will assign them the correct value
#using Enum would assign numbers incrementally (eg. 1, 2, 3, ...), using flag increments 
#by the power of 2
class Colour(Flag):
    RED: int = auto()
    GREEN: int = auto()
    BLUE: int = auto()
    YELLOW: int = auto()
    BLACK: int = auto()
    #Flag also allows you to combine constants
    ALL: int = RED | GREEN | BLUE | YELLOW | BLACK


print(Colour.ALL)
#returns: Colour.ALL
print(Colour.ALL.value)
#returns: 27   sum of all of the values
print(Colour.RED in Colour.ALL)
#returns: True


#variable contains both constants YELLOW and RED
yellow_and_red: Colour = Colour.YELLOW | Colour.RED
print(yellow_and_red)
#returns: Colour.RED|YELLOW
for colour in yellow_and_red:
    print(colour)
#returns: Colour.RED
#         Colour.YELLOW

# variable: Type = Value & Value & Value
cool_colours: Colour = Colour.RED | Colour.YELLOW | Colour.BLACK
my_car_colour: Colour = Colour.GREEN

if my_car_colour in cool_colours:
    print('sick car bruh')
else:
    print('not cool bruh')
#returns: not cool bruh


combination: Colour = Colour.RED | Colour.YELLOW
print(combination.value)
print(combination)
#returns: 9
#returns: Colour.RED|Colour.YELLOW
#using power of 2 so when combining, it will not equal the value of another entry in Flag 
#and return that entry



#enums created of things with constant value
class Colour1(Enum):
    RED: str = 'R'
    GREEN: str = 'G'
    BLUE: str = 'B'


#take variable of type matching the Enum (-> None) function does not return a value
def create_car(colour: Colour1) -> None:
    #match allows matching value to input
    match colour:
        case Colour1.RED:
            print(f"ts red bruh")
        case Colour1.BLUE:
            print(f"yoo a blue car")
        case Colour1.GREEN:
            print(f"da zaza green car")
        #(case _) for if inputed value does not match
        case _:
            print(f"{colour}? what da hell, we dont have thart")

create_car(Colour1.RED)