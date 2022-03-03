class Enigma:
    def __inti__(self):
        self.no_cycles = 0
        self.rotors = 0

        self.rotors = []
        self.rotorsettings = [("I" , 0),("II",0),("III",0)]


class Rotor:
    def __init__(self, settings):
        self.setting = settings[0]
        