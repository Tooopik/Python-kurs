members = (('Kasia', 23), ('Tomek', 19))
new_member = ('Adam', 26)
members_2 = (members[0], new_member, members[1])
print(members_2)

# -------------------------------------------------------------------------
members = (('Kasia', 23), ('Tomek', 19))
members = (members[0], ('Adam', 26), members[1])
print(members)
