import sys

# Sample data for plants and their care instructions
plants_data = {
    "Flowers": [
        {"name": "Marigold", "sunlight": "Full Sun", "water": "Once a day", "soil": "Well-drained", "pests": "Aphids"},
        {"name": "Petunia", "sunlight": "Partial Shade", "water": "Every two days", "soil": "Loamy", "pests": "Slugs"}
    ],
    "Herbs": [
        {"name": "Basil", "sunlight": "Full Sun", "water": "Once a day", "soil": "Rich soil", "pests": "Whiteflies"},
        {"name": "Mint", "sunlight": "Partial Shade", "water": "Every other day", "soil": "Moist soil", "pests": "Aphids"}
    ],
    "Vegetables": [
        {"name": "Tomato", "sunlight": "Full Sun", "water": "Every day", "soil": "Well-drained", "pests": "Tomato hornworms"},
        {"name": "Lettuce", "sunlight": "Partial Shade", "water": "Every other day", "soil": "Loamy", "pests": "Aphids"}
    ],
    "Succulents": [
        {"name": "Aloe Vera", "sunlight": "Full Sun", "water": "Once a week", "soil": "Sandy", "pests": "Mealybugs"},
        {"name": "Echeveria", "sunlight": "Partial Shade", "water": "Once a week", "soil": "Well-drained", "pests": "None"}
    ]
}

# User preferences storage
user_preferences = {
    "sunlight": "",
    "space": "",
    "plant_type": "",
    "favorites": []
}

def welcome():
    print("Welcome to the Urban Gardening Assistant!")
    print("This tool will help you choose plants suitable for urban spaces and provide gardening tips.")
    print("Please follow the instructions to navigate through the options.\n")

def print_menu():
    print("\nMain Menu:")
    print("1. Set Gardening Preferences")
    print("2. Plant Recommendations")
    print("3. Plant Care Instructions")
    print("4. General Gardening Tips")
    print("5. Community Tips")
    print("6. View Favorites")
    print("7. Exit")


def main_menu():
    while True:
        print_menu()
        choice = input("Select an option (1-7): ")
        
        if choice == '1':
            get_user_preferences()
        elif choice == '2':
            plant_recommendations()
        elif choice == '3':
            plant_care_instructions()
        elif choice == '4':
            gardening_tips()
        elif choice == '5':
            community_tips()
        elif choice == '6':
            view_favorites()
        elif choice == '7':
            exit_program()
        else:
            print("Invalid choice, please enter a number between 1 and 7.")



def get_user_preferences():
    print("\nEnter your gardening preferences:\n")
    user_preferences['sunlight'] = input("Amount of sunlight (Full Sun, Partial Shade, Shade): ").capitalize()
    user_preferences['space'] = input("Type of space (Balcony, Windowsill, Rooftop, Indoor): ").capitalize()
    user_preferences['plant_type'] = input("Preferred plant types (Flowers, Herbs, Vegetables, Succulents): ").capitalize()
    print("Preferences saved!")

def plant_recommendations():
    print("\nPlant Recommendations:\n")
    plant_type = user_preferences['plant_type']
    if plant_type and plant_type in plants_data:
        for plant in plants_data[plant_type]:
            if plant["sunlight"] == user_preferences["sunlight"]:
                print(f"Plant: {plant['name']}, Ideal for {user_preferences['sunlight']}")
                add_to_favorites(plant)
    else:
        print("No recommendations available. Please check your preferences or select a different plant type.")

def plant_care_instructions():
    plant_name = input("\nEnter the name of the plant to view care instructions: ").capitalize()
    for plant_list in plants_data.values():
        for plant in plant_list:
            if plant["name"].lower() == plant_name.lower():
                print(f"\nCare Instructions for {plant['name']}:")
                print(f"  - Sunlight: {plant['sunlight']}")
                print(f"  - Water: {plant['water']}")
                print(f"  - Soil: {plant['soil']}")
                print(f"  - Common Pests: {plant['pests']}")
                return
    print("Plant not found. Please check the spelling or try another plant.")

def gardening_tips():
    print("\nGeneral Gardening Tips:\n")
    print("1. Maximize space with vertical gardening or hanging pots.")
    print("2. Use eco-friendly pest control methods like neem oil or soapy water.")
    print("3. Choose soil types based on the plant requirements for best results.")
    print("4. Consider container gardening if you have limited space.")
    print("5. Use compost to enrich your soil for sustainable gardening.\n")

def community_tips():
    print("\nCommunity Tips:\n")
    print("1. Use coffee grounds as a natural fertilizer.")
    print("2. Place plants with similar water needs together to simplify watering.")
    print("3. Collect rainwater to water plants and reduce water usage.")
    print("4. Plant pollinator-friendly flowers to support local bees and butterflies.\n")

def add_to_favorites(plant):
    add_fav = input(f"Do you want to add {plant['name']} to your favorites? (y/n): ").lower()
    if add_fav == 'y':
        user_preferences["favorites"].append(plant)
        print(f"{plant['name']} has been added to your favorites.")

def view_favorites():
    print("\nYour Favorite Plants:\n")
    if not user_preferences["favorites"]:
        print("You have no favorite plants yet.")
    else:
        for plant in user_preferences["favorites"]:
            print(f"- {plant['name']} ({plant['sunlight']})")

def exit_program():
    print("\nThank you for using the Urban Gardening Assistant! Happy Gardening!")
    sys.exit()

# Start the application
welcome()
main_menu()
