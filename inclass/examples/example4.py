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

class Yoda(Jedi):
    pass

class JarJar(Sith):
    pass

characters = [Anakin(), Luke(), Yoda(), JarJar()]
for character in characters:
    print(f'{type(character).__name__}\'s aligment is {character.alignment()}')