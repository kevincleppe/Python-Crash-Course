def get_city_country(city, country, population):
    if population:
        full_name=f"{city.title()} {country.title()} {population}"
    else:
        full_name=f"{city.title()} {country.title()}"
    return full_name.title()