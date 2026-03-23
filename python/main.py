import sys

print(sys.version)

if 5 > 2:
  print("hello, world!")

txt = "Hello, World!"
print(txt[2:5])
print(txt.upper())
name = "Python"
print(f"I love {name}")

print("\n~~~~~~~~~~~~~~~~~ LIST EXECERSICE ~~~~~~~~~~~~~~~~~\n")

color_list = ["red", "green", "blue"]
print(color_list[0])
color_list[1] = "yellow"
color_list.append("purple")
color_list.remove("red")
print(color_list)

print("\n~~~~~~~~~~~~~~~~~ TUPLE EXECERSICE ~~~~~~~~~~~~~~~~~\n")

fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(len(fruits))
(a, b, c) = fruits
print(b)

print("\n~~~~~~~~~~~~~~~~~ SET EXECERSICE ~~~~~~~~~~~~~~~~~\n")

colors = {"red", "green", "blue"}
print(colors)
colors.add("yellow")
colors.remove("green")
print(len(colors))

print("\n~~~~~~~~~~~~~~~~~ DICTIONARY EXECERSICE ~~~~~~~~~~~~~~~~~\n")

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "2024"
}
print(car["model"])
car["color"] = "red"
car.pop("brand")
print(car)

print("\n~~~~~~~~~~~~~~~~~ FUNCTION EXECERSICE ~~~~~~~~~~~~~~~~~\n")

def greet(name):
  print("Hello, " + name)

greet("Emil")