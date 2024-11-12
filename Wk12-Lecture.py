#https://thartmanoftheredwoods.github.io/CIS-12/week_12py.html

# Chapter 13 - Files and Databases

import shelve

# Writing to a shelf
with shelve.open('data_store') as db:
    db['username'] = 'john_doe'
    db['is_active'] = True
    db['last_login'] = '2024-11-08'

# Reading from a shelf
with shelve.open('data_store') as db:
    print("Username:", db['username'])
    print("Is active:", db['is_active'])
    print("Last login:", db['last_login'])

# Differences Between Shelves and Dictionaries

my_dict = {}
with shelve.open('data_store') as my_shelf:
    for i,v in enumerate({'a','b','c','a'}):
        my_dict.setdefault(v, []).append(i)
        if v in my_shelf:
            my_list = my_shelf[v]
            my_list.append(i)
            my_shelf[v] = my_list
        else:
            my_shelf[v] = [i]
    print("Dictionary: ", my_dict)
    for k, v in my_shelf.items():
        print(k,v)

# Checking File Equivalency Using Hash Functions

import hashlib

my_string = 'hello world'
my_string2 = 'hello world'

print(hashlib.md5(my_string.encode('utf-8')).hexdigest())
print(hashlib.md5(my_string2.encode('utf-8')).hexdigest())

# Exercises Thursday