import ctypes
import win32
import win32file
import win32gui
import os
class Report():
    def Main(idgame: str):
        print("Woops... You're Game Is Crashed!!!")
        unrealeng = input("Would You Like Restart Game Again?")
        if unrealeng == "yes":
            os.system("start steam://rungameid/{}".format(idgame))
        else:
            os._exit(3003)
if __name__ == "__main__":
    Report.Main("1623730")
