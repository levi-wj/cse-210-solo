class Jedi:
    def alignment(self):
        return 'lawful good'

class Sith:
    def alignment(self):
        return 'chaotic evil'

class Anakin(Sith, Jedi):
    pass

class Luke(Jedi, Sith):
    pass

anakin = Anakin()
luke = Luke()

print(anakin.alignment())
print(luke.alignment())







# Method Resolution Order
# print(Anakin.__mro__)
# print(Luke.__mro__)