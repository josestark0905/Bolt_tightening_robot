import pygame

keys = {'动作1': 'w', '动作2': 'a', '动作3': 's', '动作4': 'd'}
new_keys = {'Driver Moving Left': "left",
            'Driver Moving Right': "right",
            'Middle Leg Rising': "up",
            'Middle Leg Descending': "down",
            'Side Legs Lifting': "space",
            'Side Legs Descending': "left shift",
            'Climbing Up': "w",
            'Climbing Down': "s",
            'Turning Left': "a",
            'Turning Right': "d",
            'Driver Working': "r",
            'All Electromagnets Deactivated': "p",
            'Front Electromagnet Activated': "1",
            'Middle Electromagnet Activated': "2",
            'Rear Electromagnet Activated': "3",
            'Front Electromagnet Deactivated': "8",
            'Middle Electromagnet Deactivated': "9",
            'Rear Electromagnet Deactivated': "0",
            'Front Leg Lifting': "e",
            'Front Leg Descending': "q",
            'Rear Leg Lifting': "z",
            'Rear Leg Descending': "c"
            }

default_keys = {'Driver Moving Left': "left",
                'Driver Moving Right': "right",
                'Middle Leg Rising': "up",
                'Middle Leg Descending': "down",
                'Side Legs Lifting': "space",
                'Side Legs Descending': "left shift",
                'Climbing Up': "w",
                'Climbing Down': "s",
                'Turning Left': "a",
                'Turning Right': "d",
                'Driver Working': "r",
                'All Electromagnets Deactivated': "p",
                'Front Electromagnet Activated': "1",
                'Middle Electromagnet Activated': "2",
                'Rear Electromagnet Activated': "3",
                'Front Electromagnet Deactivated': "8",
                'Middle Electromagnet Deactivated': "9",
                'Rear Electromagnet Deactivated': "0",
                'Front Leg Lifting': "e",
                'Front Leg Descending': "q",
                'Rear Leg Lifting': "z",
                'Rear Leg Descending': "c"
                }


def set_value(key, value):
    try:
        pygame.key.key_code(value)
        result = True
    except ValueError:
        result = False
    if result:
        if key in new_keys.keys() and value not in new_keys.values():
            new_keys[key] = value


def get_value(key):
    if key in new_keys.keys():
        return new_keys[key]
    else:
        return 'No such key'


def get_key_value(key):
    if key in new_keys.keys():
        return pygame.key.key_code(new_keys[key])
    else:
        return 'No such key'


def get_keys():
    return list(new_keys.keys())


def show_keys():
    # print(new_keys)
    dic = ''
    for each in new_keys.keys():
        dic += each + ":"
        dic += new_keys[each] + " "
    return dic


def reset():
    for each in new_keys.keys():
        new_keys[each] = default_keys[each]


if __name__ == '__main__':
    print(get_key_value("Driver Moving Right"))
    print(pygame.key.key_code("right"))
