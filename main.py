import decimal
import math 

#Exercise 1
thelist = ["first", "second", "third"]
thetuple = ("first", "second", "third")
x = float(2.7549)
y = 5
val = decimal.Decimal(3.67)
iPhone8 = {
  "brand": "Apple",
  "model": "iPhone 8",
  "RAM": "2GB",
  "camera": "12MP",
  "year": 2017
}
print("Exercise 1")
print(thelist)
print(thetuple)
print(x)
print(y)
print(val)

#Exercise 2
rounded_x = round(x)
print("Exercise 2")
print(rounded_x)

#Exercise 3
sqrt_x = math.sqrt(x)
print("Exercise 3")
print(sqrt_x)

#Exercise 4
li1 = thelist[0]
print("Exercise 4")
print(li1)

#Exercise 5
li2 = thelist[1]
print("Exercise 5")
print(li2)

#Exercise 6
thelist.append("fourth")
print("Exercise 6")
print(thelist)

#Exercise 7
thelist[0] = "foyst"
print("Exercise 7")
print(thelist)

#Exercise 8
thelist = sorted(thelist)
print("Exercise 8")
print(thelist)

#Exercise 9
l = list(thetuple)
l.insert(0, "inserted_element")
thetuple = tuple(l)

print("Exercise 9")
print(thetuple)