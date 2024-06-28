import re
from unidecode import unidecode

def convert_name(name:str) -> str:
    name = unidecode(name)
    name = re.sub(r'[^a-zA-Z0-9\s-]', '', name)
    name = name.lower().strip()

    return name