import re
import os
import sys
import time
import random as rnd

class Main():
    def __init__(self):
        # game params
        self.MAGIC_WORDS = ["mercurio", "venus", "tierra"]
        self.lives = 3

    def isvalidinput(self, string):
        pattern = re.compile("[A-Za-z]+")
        match = pattern.fullmatch(string)
        if match is not None:
            return True
        else: 
            return False

            
    def configure_game(self):
        self.word_list_size = len(self.MAGIC_WORDS)
        self.num = rnd.randrange(0, self.word_list_size) 
        self.magic_word = self.MAGIC_WORDS[self.num]
        self.magic_word_size = len(self.magic_word)
        self.solution = ["_"] * self.magic_word_size

    def play_game(self):

        print("*** {} ***\n".format(self.magic_word))
        
        self.configure_game()
        
        while self.lives > 0:
            user_input = input("ingrese una letra o la palabra magica:  ")
            print()

            if self.isvalidinput(user_input):
                # si el usuario ingresa la palabra magica correcta
                if user_input == self.magic_word or self.solution == self.magic_word:                    
                    self.solution = list(user_input.strip(" "))
                    print("felicidades!, has ganado el juego del ahorcado")
                    print("")
                    time.sleep(5)
                    break
                # valida que ya se haya ingresado esa letra
                elif user_input in self.solution:
                    print("Ya has ingresado esa letra, intenta de nuevo")
                # si la letra coincide con la palabra magica entonces se agrega a la solucion
                elif user_input in self.magic_word:
                    word_index_list = [i for i, element in enumerate(self.magic_word) if element == user_input]
                    for i in word_index_list:
                        self.solution[i] = user_input
                else:
                    print("Te equivocaste!, intenta nuevamente")
                    self.lives -= 1    
            else:
                print("Sólo se permite 1 letra o la palabra mágica :D")

            print(self.solution)
            print()
            
        print("No te quedan vidas, fin del juego uwu . . .")

    def run(self):
        while True:
            os.system("cls")
            print("Elija una opcion:")
            print()
            print("1. Iniciar juego")
            print("2. Salir")
            print()
            
            user_input = int(input(''))

            if user_input == 1:
                os.system("cls")
                self.play_game()
            if user_input == 5:
                sys.exit("Juego Terminado, ¡gracias por jugar!")  

if __name__ == "__main__":
    main = Main()
    main.run()

    # os.system("cls")   
    # os.system("clear") # Linux         

