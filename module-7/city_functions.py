# set a function that accepts a city name & a country 
# Return a string
def city_country(city, country, population=None, language=None):
    # Return only city and country if no population included
    if population and language:
        return f'{city}, {country} - population {population}, {language}'
    elif population:
        return f'{city}, {country} - population {population}'
    elif language:
        return f'{city}, {country}, {language}'
    return f'{city}, {country}'

# Call the function three times
print(city_country('San Diego', 'United States'))
print(city_country('Amsterdam', 'Netherlands', 921402, 'Dutch'))
print(city_country('Rome', 'Italy', 2759629, 'Italian'))
