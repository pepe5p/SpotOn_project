from food_search import find_food


def main():
    included_ingr = ['chicken', 'rice']
    find_food(included_ingr)

    # TODO: getting input from user or from command

    # translation = translate_ingr(result['results'][0]['title'])
    # print(translation)
    #
    # translation = translate_ingr(result['results'][1]['title'])
    # print(translation)


if __name__ == '__main__':
    main()
