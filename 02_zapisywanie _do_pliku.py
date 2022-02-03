# %%
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)

# %%
even_number = list(range(100))[::2]

with open('numbers.txt', 'w') as file:
    for number in even_number:
        file.write(str(number) + '\n')

# %%
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'a') as file:
    for tech in techs:
        print(tech, file=file)

# %%
technologies = []

with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line)

print(technologies)

# %%
technologies = []

with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line[:-1])

print(technologies)

# %%
