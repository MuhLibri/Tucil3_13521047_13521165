import tkinter as tk
from tkinter import filedialog


class Utils:
    def checkValid(adjecencyMatrix: list[list[str]]) -> bool:
        for i in range (len(adjecencyMatrix)):
            for j in range (len(adjecencyMatrix[0])):
                if (not adjecencyMatrix[i][j].isdigit()):
                    return False
        return True

    def readFile() -> list[list[int]]:
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfile()
        adjecencyMatrix = [[num.strip() for num in line.split(',')] for line in file]
        valid = Utils.checkValid(adjecencyMatrix)

        if (valid):
            adjecencyMatrix = [list(map(int, x)) for x in adjecencyMatrix]
        else:
            print("Input graf hanya dapat berupa angka")

        print(adjecencyMatrix)
        file.close()
        return adjecencyMatrix