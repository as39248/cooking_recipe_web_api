import spoonacular as sp

api = sp.API("3b96443ec65e48bfa8d08693fcc54e97")


def recommended_recipe():
    """Precondition: Assume all the recipes contain images.

    Recommend 2 random recipes"""
    response = api.get_random_recipes(number=2)
    data = response.json()
    recipes = data['recipes']
    a = []
    for i in range(len(recipes)):
        a.append({'title': recipes[i]['title'], 'image': recipes[i]['image'], 'sourceUrl': recipes[i]['sourceUrl']})
    return a[0]


if __name__ == '__main__':
    recommended_recipe()
