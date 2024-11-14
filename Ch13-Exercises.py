# Chapter 13 - Exercises (pg 206-208)
# https://allendowney.github.io/ThinkPython/chap13.html

# 13.10.1 Virtual Assistant Exercise done verbally in class

# 13.10.2

import re

def replace_all_conrad(pattern,replacement,source_file,output_file):
    source_file = open(source_file, 'r')
    output_file = open(output_file, 'w')
    text = re.sub(pattern, replacement, source_file.read())
    output_file.write(text)
    source_file.close()
    output_file.close()

def replace_all(pattern_string,replacement_string,filename1,filename2):
    with open(filename1, 'r') as filepath1, open(filename2, 'w') as filepath2:
        for line in filepath1:
            line = re.sub(pattern_string, replacement_string, line)
            filepath2.write(line)

def replace_all_v2(str_pattern, str_replace, file1, file2):
    with open(file1, 'r') as fp1, open(file2, 'w') as fp2:
        fp2.write(re.sub(str_pattern, str_replace, fp1.read()))

# replace_all('photos','images','note.txt', 'new_note.txt')

# 13.10.3

import yaml, os

def get_anagram_dict(file_path):
    anagram_dict = {}
    with open(file_path, 'r') as words:
        for word in words:
            word = word.strip().lower()
            key = ''.join(sorted(word))
            anagram_dict.setdefault(key, []).append(word)
    return anagram_dict

def load_yaml(file_path = 'files/word.txt',yaml_path = 'files/anagram_yaml'):
    if not os.path.isfile(yaml_path):
        anagram_dict = get_anagram_dict(file_path)
        with open(yaml_path, 'w') as fp:
            yaml.safe_dump(anagram_dict, fp)
    with open(yaml_path, 'r') as fp:
        return yaml.safe_load(fp)

def add_word_yaml(my_str, yaml_path):
    key = ''.join(sorted(my_str))
    db = load_yaml(yaml_path=yaml_path)
    if key in db:
        db[key].append(my_str)
    else:
        db[key] = [my_str]
    save_dict_to_yaml(db, yaml_path)

def save_dict_to_yaml(my_dict, file_path):
    with open(file_path, 'w') as fp:
        yaml.safe_dump(my_dict,fp)

def main():
    yaml_path = 'files/db.yaml'
    add_word_yaml('christine', yaml_path)
    db = load_yaml(yaml_path=yaml_path)
    for k, v in db.items():
        if len(v) > 1:
            print(k, v)

if __name__ == '__main__':
    main()