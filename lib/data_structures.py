spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Return a list of names of spicy foods."""
    return [food["name"] for food in spicy_foods]
# Output: ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']😂😂😂😂


def get_spiciest_foods(spicy_foods):
    """returns a list of dictionaries where the heat level of the food is greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]
# Output: [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level

    

def print_spicy_foods(spicy_foods):
    """output to the terminal each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶🌶🌶'}"
              f"{'🌶' * (food['heat_level'] - 3)}")
        # Output: Buffalo Wings (American) | Heat Level: 🌶🌶
            

        

        


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method."""
    return next((food for food in spicy_foods if food["cuisine"] == cuisine),None)
# Output: {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat
# level': 3}

    

def print_spiciest_foods(spicy_foods):
    """outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format: Buffalo Wings (American) | Heat Level: 🌶🌶🌶."""
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶🌶🌶'}"
                  f"{'🌶' * (food['heat_level'] - 3)}")
                 
                  # Output: Green Curry (Thai) | Heat Level: 🌶🌶


    
   

def get_average_heat_level(spicy_foods):
    """returns an integer representing the average heat level of all the spicy foods in the array. """
    return sum(food["heat_level"] for food in spicy_foods) // len(spicy_foods)

    
 

def create_spicy_food(spicy_foods, spicy_food):
    """adds a new spicy food to the array of spicy foods and returns the original list with the new spicy_food added."""
    spicy_foods.append(spicy_food)
    return spicy_foods
# Output: [{'name': 'Buffalo Wings', 'cuisine': 'American', 'heat
# level': 3}, {'name': 'Green Curry', 'cuisine': 'Thai',

