def find_last_name(names_dict, first_name):
    return names_dict.get(first_name)

names_dict={
    "emmanuel": "kpendo",
    "dela": "ricch",
    "emm": None
}

print(find_last_name(names_dict, "emm"))