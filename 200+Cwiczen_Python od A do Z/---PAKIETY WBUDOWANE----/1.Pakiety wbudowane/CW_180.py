
import random


random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']
print(items[random.randint(0, len(items))])

# %%
random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']
choice = random.choice(items)
print(choice)
