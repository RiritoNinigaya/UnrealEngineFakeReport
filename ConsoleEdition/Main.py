import ctypes
import win32
import win32file
import win32gui
import os
class Report():
    def Main(gamename: str, gamename_short: str, exefile_name: str):
        print("Woops... You're Game Is Crashed!!!")
        unrealeng = input("Would You Like Restart Game Again?")
        if unrealeng == "yes":
            os.system("start E:\\SteamLibrary\\steamapps\\common\\{}\\{}\\Binaries\\Win64\\{}.exe".format(gamename, gamename_short, exefile_name))
if __name__ == "__main__":
    Report.Main("Palworld", "Pal", "Palworld-Win64-Shipping")