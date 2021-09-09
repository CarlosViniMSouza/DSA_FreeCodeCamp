import sys
import load_strings

names = load_strings.strings(sys.argv[1])

search_names = ["Francina Vigneault", "Lucie Hansman",
                "Nancie Rubalcaba", "Elida Sleight",
                "Guy Lashbaugh", "Ginger Schlossman",
                "Suellen Luaces", "Jamey Kirchgesler",
                "Amiee Elwer", "Lacresha Peet",
                "Leonia Goretti", "Carina Bunge",
                "Renee Brendeland", "Andrew Mcgibney",
                "Gina Degon", "Deandra Pihl",
                "Desmond Steindorf", "Magda Growney",
                "Tawana Srivastava", "Tammi Todman"]

def index_of_item(collection, target):

    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None

    for n in search_names:
        index = index_of_item(names, n)
        print(index)
