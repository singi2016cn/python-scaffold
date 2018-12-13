"""城市和国家"""


def city_country(city, country, population=''):
    if population:
        return city.title() + ',' + country.title() + ' - population ' + str(population)
    else:
        return city.title() + ',' + country.title()

