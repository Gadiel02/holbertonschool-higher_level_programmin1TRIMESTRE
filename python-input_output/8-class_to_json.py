#!/usr/bin/python3
def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as f:
        json_str = f.read()
        return parse_json(json_str)

def parse_json(json_str):
    stack = []
    current_object = {}
    key = ''
    i = 0
    while i < len(json_str):
        if json_str[i] == '{':
            stack.append(current_object)
            current_object = {}
        elif json_str[i] == '}':
            if stack:
                parent_object = stack.pop()
                parent_object[key] = current_object
                current_object = parent_object
                key = ''
        elif json_str[i] == '"':
            i += 1
            j = i
            while json_str[i] != '"':
                i += 1
            if not key:
                key = json_str[j:i]
            else:
                current_object[key] = json_str[j:i]
                key = ''
        elif json_str[i] == ':':
            i += 1
        elif json_str[i] == ',':
            pass
        i += 1
    return current_object

# Testing the function
# Replace 'filename.json' with the actual filename
result = load_from_json_file('filename.json')
print(result)
