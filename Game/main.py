from enemy import Enemy, Troll, Vampire

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother_troll = Troll("Urg")
print("Brother troll - {}".format(brother_troll))

basic_vampire = Vampire("Vlad")
print("Vlad - {}".format(basic_vampire))

basic_vampire.take_damage(7)

print("Vlad - {}".format(basic_vampire))

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()

print("-" * 40)

while basic_vampire.alive:
    basic_vampire.take_damage(1)
    print(basic_vampire)

