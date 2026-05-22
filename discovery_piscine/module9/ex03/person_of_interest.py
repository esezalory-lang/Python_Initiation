#!/bin/python3

def remove_layer(figures):
    new_dict = {}
    for nickname in figures:
        frst_name = figures[nickname]["name"]
        birthdate = int(figures[nickname]["date_of_birth"])
        new_dict.setdefault(birthdate, frst_name)
    return new_dict


def famous_births(historical_figures):
    new_dict = remove_layer(historical_figures)
    print(new_dict)
    sorted_date_list = sorted(new_dict)
    print(sorted_date_list)
    for i in sorted_date_list:
        print(f"{new_dict[i]} is a great scientist born in {i}.")


women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)
