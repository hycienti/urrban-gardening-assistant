import sys
import json

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

# Load preferences if they exist
def load_preferences():
    try:
        with open("preferences.json", "r") as file:
            global user_preferences
            user_preferences = json.load(file)
            print("Loaded your saved preferences.")
    except FileNotFoundError:
        print("No saved preferences found. Starting fresh.")

# Save user preferences
def save_preferences():
    with open("preferences.json", "w") as file:
        json.dump(user_preferences, file)
    print("Your preferences have been saved.")

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
    """
    Prompts the user to enter their gardening preferences for sunlight, space type, and plant types.
    Saves these preferences to be used for tailored recommendations and other functionalities.
    """
    print("\nEnter your gardening preferences:\n")
    user_preferences['sunlight'] = input("Amount of sunlight (Full Sun, Partial Shade, Shade): ").capitalize()
    user_preferences['space'] = input("Type of space (Balcony, Windowsill, Rooftop, Indoor): ").capitalize()
    user_preferences['plant_type'] = input("Preferred plant types (Flowers, Herbs, Vegetables, Succulents): ").capitalize()
    # Confirm plant type existence
    if user_preferences['plant_type'] not in plants_data:
        print("Invalid plant type. Available options are: Flowers, Herbs, Vegetables, Succulents.")
        return  # Return to the main menu without saving preferences

    save_preferences()
    print("Preferences saved!")

def plant_recommendations():
    """
    Provides plant recommendations based on the user's preferences.
    Displays plants that match the user's preferred type and sunlight requirement, allowing them to add plants to favorites.
    """
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
    """
    Provides general gardening tips to help users maximize their gardening efforts.
    Covers topics like space optimization, eco-friendly pest control, and container gardening.
    """
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
    """
    Provides general gardening tips to help users maximize their gardening efforts.
    Covers topics like space optimization, eco-friendly pest control, and container gardening.
    """
    print("\nGeneral Gardening Tips:\n")
    print("1. Maximize space with vertical gardening or hanging pots.")
    print("2. Use eco-friendly pest control methods like neem oil or soapy water.")
    print("3. Choose soil types based on the plant requirements for best results.")
    print("4. Consider container gardening if you have limited space.")
    print("5. Use compost to enrich your soil for sustainable gardening.\n")

def community_tips():
    """
    Shares additional gardening tips from the community.
    Includes practices like using coffee grounds as fertilizer, grouping plants by water needs, and collecting rainwater.
    """
    print("\nCommunity Tips:\n")
    print("1. **Use coffee grounds as a natural fertilizer**.")
    print("2. **Place plants with similar water needs together to simplify watering.**")
    print("3. **Collect rainwater to water plants and reduce water usage.**")
    print("4. **Plant pollinator-friendly flowers to support local bees and butterflies.**\n")

def add_to_favorites(plant):
    """
    Prompts the user to add a plant to their list of favorites.
    If confirmed, the plant is added to the user's favorites list for easy access.
    """
    # Avoid duplicating entries
    if any(fav["name"].lower() == plant["name"].lower() for fav in user_preferences["favorites"]):
        print(f"{plant['name']} is already in your favorites.")
    else:
        add_fav = input(f"Do you want to add {plant['name']} to your favorites? (y/n): ").lower()
        if add_fav == 'y':
            user_preferences["favorites"].append(plant)
            print(f"{plant['name']} has been added to your favorites.")

def view_favorites():
    """
    Displays the user's favorite plants.
    Lists each favorite plant's name and sunlight requirement if there are any favorites saved.
    """
    print("\nYour Favorite Plants:\n")
    if not user_preferences["favorites"]:
        print("You have no favorite plants yet.")
    else:
        for plant in user_preferences["favorites"]:
            print(f"- {plant['name']} ({plant['sunlight']})")

def exit_program():
    """
    Confirms if the user wants to exit the program.
    Saves the current preferences if the user confirms, then exits the program gracefully.
    """
    confirm = input("Are you sure you want to exit? (y/n): ").lower()
    if confirm == 'y':
        save_preferences()
        print("Thank you for using the Urban Gardening Assistant!")
        sys.exit()
    else:
        print("Returning to main menu.")

# Load preferences at the start of the application
load_preferences()

# Start the application
welcome()
main_menu()
