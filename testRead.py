import json
def read_data_write_to_web():
    data_dict={}
    with open("foo.txt") as f:
        for line in f:
            (key, val) = line.split(':')
            data_dict[key] = val
    return data_dict
    # for i,j in data_js.items():
    #     print(f'{i}::{j}')

read_data_write_to_web()
