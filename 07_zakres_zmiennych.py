# %%

i = 2
j = i
i = 3

# %%
a = 5


def fun_1():
    print(a)


fun_1()

# %%
a = 5


def fun_2():
    a = 4
    print(a)


fun_2()

# %%


def fun_3():
    x = 4
    print(x)


fun_3()
print(x)

# %%
tech = 'python'


def change_tech(new_tech):
    tech = new_tech


print(tech)
change_tech('java')
print(tech)
# %%
tech = 'python'


def change_tech(new_tech):
    global tech
    tech = new_tech


print(tech)
change_tech('java')
print(tech)

# %%
level = 0


def f1():
    level = 1

    def f2():
        level = 2
        print('funkcja f2: ', level)

    f2()
    print('funkcja f1: ', level)


f1()
print('Globalnie : ', level)

# %%
level = 0


def f1():
    level = 1

    def f2():
        nonlocal level
        level = 2
        print('funkcja f2: ', level)

    f2()
    print('funkcja f1: ', level)


f1()
print('Globalnie : ', level)

# %%
