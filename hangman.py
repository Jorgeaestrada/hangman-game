import os
import sys
import time
import platform
import random as rnd


class Main():
    def __init__(self):
        self.MAGIC_WORD_LIST = ["venus", "tierra", "marte"]
        self.DELAY = 1

    def cleardisplay(self, delay=0):
        if delay != 0:
            time.sleep(delay)
        operative_system = platform.system()
        if operative_system == "Windows":
            os.system("cls")
        elif operative_system == "Linux":
            os.system("clear")

    def play_game(self):
        lives = 3
        magic_word = rnd.choice(self.MAGIC_WORD_LIST)
        magic_word_size = len(magic_word)
        solution = ["_"] * magic_word_size
        red_heart_unicode_list = ["\u2764\uFE0F"] * lives
        white_heart_unicode = "\u2661"

        self.cleardisplay()

        print("Vidas:    {}".format('  '.join(red_heart_unicode_list)))
        print('MAGIC_WORD:  {}\n'.format(solution))

        while lives > 0:
            user_input = input("ingrese una letra o la palabra magica:\n")
            print()
            if user_input.isalpha():
                # si el usuario ingresa la palabra magica correcta o ya se tiene la solucion
                if user_input == magic_word:
                    solution = list(user_input.strip(" "))
                    print("felicidades!, has ganado el juego del ahorcado\n")
                    print("MAGIC_WORD:    {}".format(magic_word))
                    self.cleardisplay(self.DELAY)
                    return
                # valida que ya se haya ingresado esa letra
                elif user_input in solution:
                    print("Ya has ingresado esa letra, intenta de nuevo")
                    self.cleardisplay(self.DELAY)
                # si la letra se encuentra en la palabra magica entonces se agrega a la solucion
                elif user_input in magic_word:
                    word_index_list = [i for i, element in enumerate(
                        magic_word) if element == user_input]
                    for i in word_index_list:
                        solution[i] = user_input
                    if magic_word == ''.join(solution):
                        print("felicidades!, has ganado el juego del ahorcado\n")
                        print("MAGIC_WORD:    {}".format(magic_word))
                        self.cleardisplay(self.DELAY)
                        return
                else:
                    lives -= 1
                    red_heart_unicode_list[lives] = white_heart_unicode
                    if lives > 0:
                        print("Te equivocaste!, intenta nuevamente")
                    self.cleardisplay(self.DELAY)
            else:
                print("Sólo se permite 1 letra o la palabra mágica :D")
                self.cleardisplay(self.DELAY)
            self.cleardisplay()
            print("Vidas:    {}".format('  '.join(red_heart_unicode_list)))
            print('MAGIC_WORD:  {}\n'.format(solution))
        
        print('No te quedan vidas uwu. . . Fin del juego.')
        self.cleardisplay(self.DELAY * 3)

    def run(self):
        self.cleardisplay()
        while True:
            print("Elige una opcion:\n")
            print("1. Iniciar juego")
            print("2. Salir\n")

            user_option = input('')
            if user_option.isnumeric():
                user_option = int(user_option)
                if user_option == 1:
                    self.play_game()
                elif user_option == 2:
                    sys.exit("Juego Terminado, ¡gracias por jugar!")
                else:
                    print('Opción inválida. . .\n')
                    self.cleardisplay(self.DELAY)
            else:
                print('Sólo se permiten números. . .\n')
                self.cleardisplay(self.DELAY)


if __name__ == "__main__":
    main = Main()
    main.run()
