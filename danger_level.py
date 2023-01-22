import spoonacular as sp

api = sp.API("3b96443ec65e48bfa8d08693fcc54e97")

# fix required
def lf_dangerous_equip(keyword: str):
    """Search for the dangerous equipments used by the recipe. add 1 to the counter if it is used
    """
    search_recipes_r = api.search_recipes_complex(keyword, number=10)
    data_s = search_recipes_r.json()

    search_results = data_s["results"]
    if not search_results:
        return "No results found"
    a = []
    for i in range(len(search_results)):

        get_equipments = api.visualize_equipment(search_results[i]['id'])
        data = get_equipments.json()

        for j in range(len(data["equipment"])):
            if data["equipment"][j]["name"] == ("knife" or "oven" or "stove"):
                a.append({
                    'image': data['image'], 'title': data['title'], 'sourceUrl': data['sourceUrl'], 'Dangerous': True
                })
            else:
                a.append({
                    'image': data['image'], 'title': data['title'], 'sourceUrl': data['sourceUrl'], 'Dangerous': False
                })

    return a


if __name__ == '__main__':
    lf_dangerous_equip("chicken")
