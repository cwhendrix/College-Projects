#!/usr/bin/python3
### JSON+ Parser - Cooper Hendrix
DESCRIPTION = '''
A homebrew JSON parser which extends standard JSON with sets and complex numbers.
'''

'''
JSON Grammar Definition
V - {OBJ, LP, K, V, LIST, SET}
Σ - {INT, BOOL, FLOAT, STR, COMPLEX, :, {, }, [, ], , }
S - OBJ
R: 
    OBJ -> { LP }
    LP -> K : V, LP | ε
    K -> STR
    V -> INT | BOOL | FLT | STR | LIST | OBJ | SET
    LIST -> [ V, LIST ] | ε
    SET -> { V, SET } | ε
'''

import argparse
import os.path

YOUR_NAME_HERE = "Cooper hendrix" # Replace this with your name.

def rem_white_space(string):
    ignore_chars = " \n\t\r"
    in_quotes = False
    return_str = ""
    for i in range(len(string)):
        if string[i] == "\"" and not in_quotes:
            in_quotes = True
        elif string[i] == "\"" and in_quotes:
            in_quotes = False
        if in_quotes:
            return_str += string[i]
        elif string[i] not in ignore_chars and not in_quotes:
            return_str += string[i]
    
    return return_str


def tokenize(file_name) -> list:
    file = open(file_name, "r")
    contents = file.read()
    contents = rem_white_space(contents)
    # print(contents)
    tokens = []
    temp = ""
    in_quotes = False
    for i in range(len(contents)):
        if contents[i] in "{}[],:":
            if temp != "":
                tokens.append(temp)
                temp = ""
            tokens.append(contents[i])
        else:
            temp += contents[i]
    file.close()
    print(tokens)
    return tokens

### Parse Objects
def parse_obj(tokens):
    assert tokens[0] == '{'
    assert tokens[len(tokens)-1] == '}'
    parsed_dict = dict()
    parsed_dict = parse_LP(parsed_dict, tokens[1:])

    return parsed_dict, tokens

### Parse List
def parse_LP(parsed, tokens):
    assert tokens[1] == ":"
    key = tokens[0]
    value, tokens = parse_V(tokens[2:])
    parsed[key] = value
    if tokens[0] == ",":
        parsed = parse_LP(parsed, tokens[1:])
    return parsed
    
### Parse Value
def parse_V(tokens):
    val_type = ""
    value = ""
    if tokens[0] == "{":
        if tokens[2] == ":":
            ### the value is an object
            val_type = "OBJ"
        else:
            ### the value is a set
            val_type = "SET"
    elif tokens[0] == "[":
        ### the value is a list
        val_type = "LIST"
    else:
        try:
            float(tokens[0])
        except:
            print("not float")
        else:   # Value is a float
            val_type = "FLOAT"
            value = float(tokens[0])

        try:
            int(tokens[0])
        except:
            print("not int")
        else: # value is an int
            val_type = "INT"
            value = int(tokens[0])
        
        try:
            complex(tokens[0])
        except:
            print("not complex")
        else:
            if val_type != "INT" and val_type != "FLOAT":
                val_type = "COMP"
                value = complex(tokens[0])
        
        if tokens[0] == "True" or tokens[0] == "False":
            val_type = "BOOL"
            value = bool(tokens[0])
            
        if val_type == "":  #string should work for whatever else
            val_type = "STR"
            value = str(tokens[0])
        
    match val_type:
        case "OBJ":
            obj_val, tokens = parse_obj(tokens)
            return obj_val, tokens
        case "SET":
            # Handle Set
            set_val, tokens = parse_set(tokens)
            return set_val, tokens
        case "LIST":
            # Handle List
            list_val, tokens = parse_list(tokens)
            return list_val, tokens
        case "FLOAT" | "INT" | "STR" | "BOOL" | "COMP":
            return value, tokens[1:]
        
def parse_list(tokens):
    assert tokens[0] == "["
    list_val = []
    new_val = ""
    i = 0
    while i < len(tokens):
        if tokens[i] == "]":
            break
        elif tokens[i] == "[" and i != 0:
            new_val, rand, increase = parse_sublist(tokens[i:])
            list_val.append(new_val)
            i += increase
        elif tokens[i] not in "[,":
            new_val, rand = parse_V(tokens[i:])
            list_val.append(new_val)
        i += 1
    return list_val, tokens[i+1:]

def parse_sublist(tokens):
    assert tokens[0] == "["
    list_val = []
    new_val = ""
    i = 0
    while i < len(tokens):
        if tokens[i] == "]":
            break
        elif tokens[i] == "[" and i != 0:
            new_val, rand, increase = parse_sublist(tokens[i:])
            list_val.append(new_val)
            i += increase
        elif tokens[i] not in "[,":
            new_val, rand = parse_V(tokens[i:])
            list_val.append(new_val)
        i += 1
    return list_val, tokens[i+1:], i

def parse_set(tokens):
    assert tokens[0] == "{"
    set_val = []
    new_val = ""
    i = 0
    while i < len(tokens):
        if tokens[i] == "}":
            break
        elif tokens[i] not in "{,":
            new_val, rand = parse_V(tokens[i:])
            set_val.append(new_val)
        i += 1
    return set_val, tokens[i+1:]


def parse_file(file_name) -> dict:
    curr_tokens = tokenize("Sample JSON Input Files-20240404/easy_complex_test.json")
    parsed_tokens, tokens = parse_obj(curr_tokens)
    return parsed_tokens


def main():
    ap = argparse.ArgumentParser(description=(DESCRIPTION + f"\nBy: {YOUR_NAME_HERE}"))
    ap.add_argument('file_name', action='store', help='Name of the JSON file to read.')
    args = ap.parse_args()

    file_name = args.file_name
    local_dir = os.path.dirname(__file__)
    file_path = os.path.join(local_dir, file_name)

    dictionary = parse_file(file_path)

    print('DICTIONARY:')
    print(dictionary)


if __name__ == '__main__':
    main()