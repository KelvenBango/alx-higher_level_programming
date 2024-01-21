#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
splited_string = str.split(',')
print(f'{splited_string[2][1:28]} {splited_string[2][69:73]} {splited_string[0][:6]}')
