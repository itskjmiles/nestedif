attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if attendees > 100:
    print("Additional facilities: audio system and projector")
else: 
    print('Additional factilities: projector')
vegetarian_choice = input("Do you want vegetarian food? (yes or no): ")
if vegetarian_choice == "yes":
    print("Recommended Caterer: Veggie Delight Caterers")
else:
    print("Recommended Caterer: Gourmet Meals Caterers")


