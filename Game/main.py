from enemy import Enemy, Troll

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother_troll = Troll("Urg")
print("Brother troll - {}".format(brother_troll))

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()
