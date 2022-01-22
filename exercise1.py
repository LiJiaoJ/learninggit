print("练习3.1")
print ("Hello World!")
print ("Hello Again")
print ("I like typing this")
print ("This is fun")
print ("Yay!Printing")
print ("I'd much rather you 'not.")
print ("I \"said\" do not touch this.")


#练习3.4
print("练习3.4")
print ("I will now count my chickens:")

print ("Hens", 25 + 30 / 6)
print ("Roosters", 100 - 25 * 3 % 4)

print ("Now I will count the eggs:")

print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print ("Is it true that 3 + 2 < 5 - 7?")

print (3 + 2 < 5 - 7)

print ("What is 3 + 2?", 3 + 2)
print ("What is 5 - 7?", 5 - 7)

print ("Oh, that's why it's False.")

print ("How about some more.")

print ("Is it greater? 5 > -2", 5 > -2)
print ("Is it greater or equal? 5 >= -2", 5 >= -2)
print ("Is it less or equal?5 <= -2", 5 <= -2)

#练习3.5
print("练习3.5")
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

#练习3.6
print("练习3.6")
my_name = 'LiJiaojiao'
my_age = 19
my_height = 161#cm
my_ideal_weight = 47 #kliograms
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print("Let's talk about %s." %my_name)
print("She is %d cm tall." %my_height)
print("She is %d kilograms heavy." %my_ideal_weight)
print("Actually that is ideal weight.")
print("She's got %s eyes and %s hair." %(my_eyes, my_hair))
print("Her teeth are %s depending on the good habit." %my_teeth)

print("if I add %d, %d and %d ,I get %d." %(my_age,my_height,my_ideal_weight,my_age+my_height+my_ideal_weight))
