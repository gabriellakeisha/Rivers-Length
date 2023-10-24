rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]
sum = 0 

#print out each river's name
for river in rivers: 
    print (river ["name"])
#add up and print out the total length of all the rivers
for river in rivers:
    sum += river["length"]
print (f"The total length of all rivers is {sum} miles")
#print out every river's name that begins with the letter M
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])
#the length of the rivers are in miles, print out every river's length in kilometres
#1 mile is roughly 1.6 km
conversion = 1.6
for river in rivers :
    river_name = river["name"]
    river_length_miles = river["length"]
    river_length_kilometers = river_length_miles * conversion
    print(f"The length of the {river_name} river is approximately {river_length_kilometers:.2f} kilometers.")



        