"""
*SBA Task 1A*
Name: Tsoi Kei Chiu
Class: 5B
Class number: 30
Credit: Me, GitHub Copilot (for the idea of using os.path.dirname)
"""

# Open the file at current directory (saved in the same folder as main.py)
# Written by AI. For easier debugging only.
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "participant.txt")

# Creating lists
file = open(file_path, "r")
content = file.read().replace("\n", ",").split(",")
file.close()

i = 0
N = len(content)
while i < N:
    if content[i] == "":
        content.pop(i)
        N -= 1
    else:
        i += 1

name = []
school = []
school_abbr = []
flag_seed = []

i = 0
while i < N:
    if not i % 4:
        name.append(content[i])
    elif not (i-1) % 4:
        school.append(content[i])
    elif not (i-2) % 4:
        school_abbr.append(content[i])
    else:
        flag_seed.append(content[i])
    i += 1

# Sorting
L = school_abbr
N = N//4
for i in range(0, N-1):
    min_index = i
    for j in range(i+1, N):
        if L[j] < L[min_index]:
            min_index = j
    L[i], L[min_index] = L[min_index], L[i]
    name[i], name[min_index] = name[min_index], name[i]
    school[i], school[min_index] = school[min_index], school[i]
    flag_seed[i], flag_seed[min_index] = flag_seed[min_index], flag_seed[i]

# Output
print("The total number of players:", N)    #Include 'bye'?

print("-"*50)
print("The list of player information:")
i = 0
while i < N:
    print("Name: "+name[i], "School: "+school[i], "School Abbreviation: "+school_abbr[i], "Flag of Seed Player: "+flag_seed[i], sep="\t\t")
    i += 1

print("-"*50)