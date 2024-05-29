#!/usr/bin/python3
import sys
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    try:
        with open("add_item.json", 'r', encoding='utf-8') as f:
            items = json.load(f)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
