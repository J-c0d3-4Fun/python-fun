def city_country(city,country,population=""):
    if population:
        place = f"{city},{country} -- population: {population}"
    else:
        place = f"{city},{country}"

    return place.title()