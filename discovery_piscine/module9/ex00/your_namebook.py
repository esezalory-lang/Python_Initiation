#!/bin/python3

def array_of_names(persons):
    namebook = []
    for frst_name in persons:
        namebook.append(frst_name.capitalize() + " " + persons.get(frst_name).capitalize())
    return namebook

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier",
}

print(array_of_names(persons))