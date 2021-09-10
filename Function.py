# def user(name,age,address):
#     print(name)
#     print(age)
#     print(address)
# user('ram',20,'ktm')
# def user(name):
#     return f'your name is {name}'
# print(user("ram"))
# def add(x,y):
#     return (x-y)
# print(add(34,60))
# def add(x,y):
#     return (x+y)
# print(add(34,60))
# def add(x,y):
#     return (x*y)
# print(add(34,60))
# print("STUDENT RESULT")
#
#
# def test_marks():
#     nep = int(input("enter a marks:"))
#     eng = int(input("enter a marks:"))
#     soc = int(input("enter a marks:"))
#     pop = int(input("enter a marks:"))
#     math = int(input("enter a marks:"))
#     test_marks = [nep, eng, soc, pop, math]
#     return test_marks
#
#
# def total_marks():
#     obj = test_marks()
#     n = obj[0]
#     e = obj[1]
#     s = obj[2]
#     p = obj[3]
#     m = obj[4]
#     return n + e + s + p + m
#
#
# def division():
#     percent = total_marks()/500*100
#     if 35 < percent <= 50:
#         print("Third Division")
#     elif 50 < percent <= 65:
#         print("Second Division")
#     elif 65 < percent <= 80:
#         print("First Division")
#     elif 80 < percent <= 100:
#         print("Distinction")
#     else:
#         print("Failed")
#     return percent
#
# print(f'Your Percentage is {division()}')
# def display(**kwargs):
#     for i in kwargs:
#         print(i)
# display(emp="Kelly", salary=9000)
