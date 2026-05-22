#!/bin/python3


def find_the_redheads(family):
   redheads = []
   for relative in family:
      if "red" in family.get(relative):
         redheads.append(relative)
   return redheads


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))