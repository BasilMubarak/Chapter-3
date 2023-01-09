guests = ['rami', 'marya', 'judy']

name = guests[0].title()
print(name + ", it would be lovely if you could join me in eating dinner.")

name = guests[1].title()
print(name + ", it would be lovely if you could join me in eating dinner.")

name = guests[2].title()
print(name + ", it would be lovely if you could join me in eating dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[1])
guests.insert(1, 'adel')

name = guests[0].title()
print("\n" + name + ", it would be lovely if you could join me in eating dinner.")

name = guests[1].title()
print(name + ", it would be lovely if you could join me in eating dinner")

name = guests[2].title()
print(name + ", it would be lovely if you could join me in eating dinner.")