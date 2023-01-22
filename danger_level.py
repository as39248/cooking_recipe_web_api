import spoonacular as sp

api = sp.API("e86e7107f9724c0797f751fba55182cc")

# preferences values
# knife = Bool value from preferences
# sharp = Bool value from preferences
# oven = Bool value from preferences
# stove = Bool value from preferences
# raw = Bool value from preferences
# irritants = Bool value from preferences


def lf_dangerous_equip(keyword: str):
    """Search for the dangerous equipments used by the recipe. add 1 to the counter if it is used
    """


# head: 0
# sous: 1 to 4
# apprentice 5 to 6
def recipe_sorter(dict_of_recipes):
    head = []
    sous = []
    apprentice = []
    for i in range(len(dict_of_recipes)):
        key = str("recipe" + str(i))
        if dict_of_recipes[key] < 1:
            head.append(key)
        if 0 < dict_of_recipes[key] < 5:
            sous.append(key)
        if dict_of_recipes[key] >= 5:
            apprentice.append(key)
    print(head)
    print(sous)
    print(apprentice)


dicttest = {
    "recipe0": 0,
    "recipe1": 0,
    "recipe2": 0
}
recipe_sorter(dicttest)
