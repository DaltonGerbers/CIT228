def get_formatted_city(city, country, population = 'none'):
    if population == 'none':
        return city.title() + ", " + country.title()
    else:
        return city.title() + ", " + country.title() + " - population " + population