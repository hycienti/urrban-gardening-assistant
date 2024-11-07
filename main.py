i# Sample data for plants and their care instructions
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

def welcome():
    print("Welcome to the Urban Gardening Assistant!")
    print("This tool will help you choose plants suitable for urban spaces and provide gardening tips.")
    print("Please follow the instructions to navigate through the options.\n")

def print_menu():
    print("\nMain Menu")
    print("1. Enter Gardening Preferences")
    print("2. Get Plant Recommendations")
    print("3. View Plant Care Instructions")
    print("4. Gardening Tips")
    print("5. Community Tips")
    print("6. View Favorites")
    print("7. Exit")

# Call the function to print the menu
print_menu()

#function of getting user preferences

def get_user_preferences():
    print("\nEnter your gardening preferences:\n")
    
    # Get sunlight preference
    user_preferences['sunlight'] = input("Amount of sunlight (Full Sun, Partial Shade, Shade): ").capitalize()
    
    # Get space preference
    user_preferences['space'] = input("Type of space (Balcony, Windowsill, Rooftop, Indoor): ").capitalize()
    
    # Get plant type preference
    user_preferences['plant_type'] = input("Preferred plant types (Flowers, Herbs, Vegetables, Succulents): ").capitalize()
    
    print("Preferences saved!")

# Example of how these functions might be called
welcome()
print_menu()
get_user_preferences()
print("Your preferences:", user_preferences)   
