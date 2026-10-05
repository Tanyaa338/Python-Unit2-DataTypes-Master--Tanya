""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])

"test"
["t","e","s","t"]"""

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" user = input("write a sentence")
if user == "hi hi hi hi hi":
    y = user.split( )
    z = y[0]
print(y)
print(z) """ #xxxxxxxxx

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """


""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" def countwords(sentence):
    words = sentence.split( )
    return len(words)

user = input("write a sentence")
wordcount = countwords(user)
print(wordcount) """


""" def even_odd(number):
    if number % 2 == 0:
         print("even")
    else:
         print("odd")

number = input("pick a number")
even_odd(int(number)) """

""" def tip_calculator(bill, service):
    if service == "bad":
        tip_percentage = 0
    elif service == "okay":
        tip_percentage = 0.15
    elif service == "good":
        tip_percentage = 0.20
    else:
        tip_percentage = 0.25
    tip = int(bill * tip_percentage)
    total_amount = bill + tip
    print(f"tip: ${tip}")
    print(f"total amount: ${total_amount}")

bill = float(input("What's the bill amount? "))
service = input("How was the service? ")
tip_calculator(bill, service) """

def factor_finder(number):
    for i in range(1, number+1):
        if number % i == 0:
            print(i)

number = input("pick a number")
factor_finder(int(number))

# one loop for gcf
# use max or min to get the smallest number (x,y)
# check if 15 and 25 modulo i is divisible by the same number
# add and and check the other number as well.