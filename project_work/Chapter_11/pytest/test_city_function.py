from city_function import city_country

def test_city_country():
    """Does it print out the correct output of city,country"""
    citytest = city_country("paris", "france", 500000)
    assert citytest == 'Paris,France -- Population: 500000'