def add_ingredient(inventory, ingredient, amount):
    inventory[ingredient] = inventory.get(ingredient, 0) + amount


def brew_potion(inventory, recipes, potion_name):
    if potion_name not in recipes:
        return False
    
    recipe = recipes[potion_name]
    
    for ingredient, needed in recipe.items():
        if inventory.get(ingredient, 0) < needed:
            return False
    
    for ingredient, needed in recipe.items():
        inventory[ingredient] -= needed
        if inventory[ingredient] == 0:
            del inventory[ingredient]
    
    return True
