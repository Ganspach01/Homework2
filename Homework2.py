#Grace Anspach
#Question 1
def print_name(name):
    print("The name is", name)

print_name("Grace")

#Question 2
def ninety(a,b,c):
    d=360-(a+b+c)
    return d
print(ninety(15,28,46))

#Question 3
def miles_per_hour(miles,hours,minutes,seconds):
    total_hours=hours+(minutes/60)+(seconds/3600)
    mph=miles/total_hours
    return miles_per_hour
print(miles_per_hour(20,2,21,16))

#Question 4
def greetings(n):
    if n="Chris":
        print("Hello, Chris!")
    else:
        print("goodbye", n)

greetings("Chris")
greetings("Grace")

#Question 5
def convert_temperature(temp,units):
    if units=="celcius":
        print("The temperature",temp,"in fahrenheit is",(temp*(9/5)+32),"celcius")
    if units=="fahrenheit":
        print("The temperature", temp,"in celcius is",((temp-32)*5/9),"fahrenheit")

convert_temperature(90,"fahrenheit")
convert_temperature(32.2,"celcius")

#Problem 6
def calculate_grade(x):
    if x>=90:
        return("Your grade is an A")
    if 80<x<90:
        return("Your grade is a B")
    if 70<x<80:
        return("Your grade is a C")
    if 60<x<70:
        return("Your grade is a D")
    if x<60:
        return("Your grade is a F")

print(calculate_grade(95))
print(calculate_grade(85))
print(calculate_grade(75))
print(calculate_grade(65))
print(calculate_grade(15))
