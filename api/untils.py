import json
def is__json(data):
    try:
        p_dict=json.loads(data)
        valid=True
    except ValueError:
        valid=False
    return valid