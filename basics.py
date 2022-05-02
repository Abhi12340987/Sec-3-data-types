#variables

import datetime

time_now = datetime.datetime.now()

print(time_now)

mynumber = 10

mytext = "hello"

print(mynumber, mytext)



#coding exercise
#integers, strings and floats

x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y 

print(sum1, sum2)
print(type(x), type(y), type(z))



#list types
student_grades = [9.1, 8.8, 7.5]
print(student_grades)
#You can create a list of numbers automatically using a range. 
print(list(range(1, 11)))
print(list(range(1, 11, 2)))

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)

#dictionary types

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}


#Tuple type, faster than lists, they are immutable; not changable, lists are changable
monday_temperature = (1, 4, 5)
print(monday_temperature)

#More lists
tuesday_temperature = [9.1, 8.8, 7.5]
print(len(tuesday_temperature))
print(tuesday_temperature[1:4])
tuesday_temperature[0:4]
tuesday_temperature[:4]


firday_temp = ['hello', 1, 2, 3]

#dictionaries

grades_studs = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

eng_port = {"rain": "chuva", "sun": "sol"}

#creating functions

student_grades = [9.1, 8.8, 7.5] #traditional method

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)

#new method: using functions

def cal_mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(cal_mean([1, 4, 5]))



def convert(oz):
    the_convert = oz * 29.57353
    return the_convert

print(convert(2))




#print or return
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return None #have to use return statement for all functions
print(mean([1, 4, 6]))


#conditional statements

def cal_mean(value):
    if type(value) == dict:
        the_mean = sum(value.value()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
print(student_grades)

def mean(value):
    if isinstance(value, dict): 
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean

monday_temperature = [8.8, 9.1, 9.9]
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

print(mean(student_grades))

#elif: if, elif, and else, this order




#User Input

def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))


#String Formatting
input_use = input("Enter your name: ")
message = "Hello %s" % input_use #python 2
message = f"Hello {user_input}" #python 3
print(message)


name = input("Enter your name: ")
surname = input("Enter your surname: ")

message = "Hello %s %s" % (name, surname) #python 2
message = f"Hello {name} {surname}" #python 3
print(message)

name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))

saturday_temperature = [9.1, 8.8, 7.6]

for temperature in saturday_temperature:
    print(round(temperature))
    print("done")

for letter in 'hello':
    print(letter.title())



#looping through a dictionary

my_grades = {"Math": 9.1, "Science": 8.8, "Geo": 7.5}

for grades in my_grades.items(): #.items, .values, .keys can be used
    print(grades) #prints out A tuple



phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))


#while loops

for i in [1, 2, 3]:
    print(i)


username = ''

while username != 'pypy':
    username = input("enter username: ")

while True:
    username = input("enter username: ")
    if username == "pypy":
        break
    else:
        continue