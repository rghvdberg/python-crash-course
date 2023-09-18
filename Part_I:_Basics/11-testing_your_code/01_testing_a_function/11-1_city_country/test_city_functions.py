from city_functions import get_formatted_city


def test_city_country():
    """Do cities like 'Amsterdam, The Netherlands' work?"""
    formatted_city = get_formatted_city("amsterdam", "the netherlands")
    assert formatted_city == "Amsterdam, The Netherlands"


def test_city_country_population():
    """Do cities like 'Naaldwijk, The Netherlands - population 22130' work?"""
    formatted_city = get_formatted_city("naaldwijk", "the netherlands", 22130)
    assert formatted_city == "Naaldwijk, The Netherlands - population 22130"
