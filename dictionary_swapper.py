def dict_swap(data):
    swapped_dict = {}
    for key, value in data.items():
        try:
            swapped_dict[value] = key
        except TypeError:
            pass  # Skip non-hashable values
    return swapped_dict

data = {"key1": 25, 100: "value100", "cadabra": "abra", (1,2): (3,4), "shmobject": object, False: None}
print(dict_swap(data))
