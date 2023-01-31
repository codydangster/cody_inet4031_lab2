#!/usr/bin/env python3

with open('fileprocessor.input') as f:
    lines = f.readlines()

 
for x in lines:
	split_lines = x.split(":")
	if x[0] == "#":
		print(split_lines[0] + " is skipped because it starts with a hashtag (is commented out)")
	else:
        	print("The user " + split_lines[0] + " has a password of " + split_lines[1] + " and has a userid " + split_lines[2] + " and groupid " + split_lines[3])


