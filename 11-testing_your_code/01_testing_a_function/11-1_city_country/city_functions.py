def get_formatted_city(city, country, population=None):
    city = city.title()
    country = country.title()
    if population:
        formatted_city = f"{city}, {country} - population {population}"
    else:
        formatted_city = f"{city}, {country}"
    return formatted_city
