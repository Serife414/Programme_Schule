import math
#Eingabenpopi
l = int(input("Länge eingeben: "))
b = int(input("Breite eingeben: "))
h = int(input("Höhe eingeben: "))
def find_surafce_area(l, b, h):
    Surface_area = 2 * (l * b + b * h + h * l)

    print("Das Oberflächeninhalt beträgt: ",Surface_area)


def find_volume(l, b, h):
    Volume = (l * b * h)

    print("Das Volumen Berträgt: ",Volume)

def find_space_diagonal(l, b, h):
    Space_diagonal = math.sqrt(l ** 2 + b ** 2 + h ** 2)

    print("Raumdiagonale ist: ",Space_diagonal)

find_surafce_area(l, b, h)

find_volume(l, b, h)

find_space_diagonal(l, b, h)