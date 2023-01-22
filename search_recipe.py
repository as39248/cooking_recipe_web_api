import spoonacular as sp

api = sp.API("3b96443ec65e48bfa8d08693fcc54e97")


def search_recipes(keyword: str):
    """
    Search and display 10 recipes. print "No result found" if there is no relevant result for the keyword.
    :param: keyword
    :return:
    """
    search_recipes_r = api.search_recipes_complex(keyword, number=10)
    data_s = search_recipes_r.json()

    search_results = data_s["results"]
    if not search_results:
        return "No results found"
    a = []
    for i in range(len(search_results)):
        get_recipes_r = api.get_recipe_information(search_results[i]['id'])
        data_g = get_recipes_r.json()
        a.append({
            'image': data_g['image'], 'title': data_g['title'], 'sourceUrl': data_g['sourceUrl']
        })
    print(a)
    return a


if __name__ == '__main__':
    search_recipes("chicken")

