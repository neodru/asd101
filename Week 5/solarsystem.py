# Facts about each planet 

planets = { 
    "Mercury" : { 
        "length of year": 88, 
        "planet type": "Terrestrial", 
        "distance from sun": 0.4 
        }, 

    "Venus" : { 
        "length of year": 225, 
        "planet type": "Terrestrial", 
        "distance from sun": 0.7 
        }, 

    "Earth" : { 
        "length of year": 365, 
        "planet type": "Terrestrial", 
        "distance from sun": 1 
        }, 

    "Mars" : { 
        "length of year": 687, 
        "planet type": "Terrestrial", 
        "distance from sun": 1.5 
        }, 

    "Jupiter" : { 
        "length of year": 4333, 
        "planet type": "Gas Giant", 
        "distance from sun": 5.2 
        }, 

    "Saturn" : { 
        "length of year": 10759, 
        "planet type": "Gas Giant", 
        "distance from sun": 9.5 
        }, 

    "Uranus" : { 
        "length of year": 30687, 
        "planet type": "Ice Giant", 
        "distance from sun": 19.8 
        }, 

    "Neptune" : { 
        "length of year": 60190, 
        "planet type": "Ice Giant", 
        "distance from sun": 30 
        } 
    } 

EARTH_DAYS = 365 

# Calculate the age of a person on a planet 

def age_on_planet(age, planet): 
    new_age = (age * EARTH_DAYS) / planets[planet]["length of year"] 
    return round(new_age) 