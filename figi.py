import json


def get_figi():
    with open('figi.json', 'r') as file:
        return json.load(file)

def add_figi(figi_name, figi_id):
    FIGI = get_figi()
    FIGI[figi_name] = figi_id
    with open('figi.json', 'w') as file:
        return json.dump(FIGI, file, indent=2)


FIGI = get_figi()
