class Roomlight():
    def __init__(self):
        self.__light="OFF"
    def turn_on(self):
        self.__light="ON"
    def turn_off(self):
        self.__light="OFF"
    def show_light(self):
        print("The light is",self.__light)
light=Roomlight()
light.turn_on()
light.turn_off()
light.show_light()