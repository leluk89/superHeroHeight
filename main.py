import requests

API_URL = "https://akabab.github.io/superhero-api/api/all.json"

def get_heroes_list():
    response = requests.get(API_URL)

    if response.status_code != 200:
        print(f"Error: Response status code: {response.status_code}")
        return None

    if response.text == '':
        print(f"Error: Response is empty!")
        return None

    try:
        heroes_list = response.json()

        if heroes_list:
            return heroes_list
        else:
            print(f"Error: JSON has empty list!")
            return None
    except ValueError:
        print(f"Error: JSON decoding has failed!")
        return None

def get_tallest_superhero(heroes_list, gender, has_job):
    if heroes_list:
        if len(heroes_list) == 0:
            print(f"Error: JSON has empty list!")
            return None
        else:
            filtered_heroes = sorted(heroes_list, key = lambda item: (
                item['appearance'] != '',
                item['appearance']['height'] != '',
                item['appearance']['gender'] == gender,
                (has_job and item['work'] != '' and item['work']['occupation'] != '') or has_job == False,
                len(item['appearance']['height']) > 0,
                float(item['appearance']['height'][1].split(' ')[0])
            ), reverse = True)
            if len(filtered_heroes) > 0:
                return filtered_heroes[0]
            else:
                return None

full_heroes_list = get_heroes_list()

if full_heroes_list is None or len(full_heroes_list) == 0:
    print(f"Error: JSON has empty list!")
    exit()

print(get_tallest_superhero(full_heroes_list, "Male", True))
print(get_tallest_superhero(full_heroes_list, "Male", False))
print(get_tallest_superhero(full_heroes_list, "Female", True))
print(get_tallest_superhero(full_heroes_list, "Female", False))