# prompt
is_it_raining = input("Is it currently raining? ")

# responses
response_bus = "You should take the bus."
response_bike = "You should ride your bike."
response_walk = "You should walk."

if is_it_raining.casefold() == "yes" or is_it_raining.casefold() == "y":
    print(response_bus)
else:
    travel_distance = input("How far in km do you need to travel? ")

    if int(travel_distance) > 10:
        print(response_bus)
    elif 2 <= int(travel_distance) <= 10:
        print(response_bike)
    else:
        print(response_walk)
