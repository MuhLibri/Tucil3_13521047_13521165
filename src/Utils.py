import tkinter as tk
from tkinter import filedialog


class Utils:
    def checkValid(adjecencyMatrix: list[list[str]]) -> str:
        if (len(adjecencyMatrix) < 8 or len(adjecencyMatrix[0]) < 8):
            return "too_small"
        elif (len(adjecencyMatrix) != len(adjecencyMatrix[0])):
            return "size_diff"
        for i in range (len(adjecencyMatrix)):
            for j in range (len(adjecencyMatrix[0])):
                if (not adjecencyMatrix[i][j].isdigit()):
                    return "not_number"
        return "valid"

    def readFile() -> list[list[int]]:
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfile()
        adjecencyMatrix = [[num.strip() for num in line.split(',')] for line in file]
        status = Utils.checkValid(adjecencyMatrix)

        if (status == "valid"):
            adjecencyMatrix = [list(map(int, x)) for x in adjecencyMatrix]
        elif (status == "too_small"):
            print("Ukuran matrix minimal 8 x 8")
        elif (status == "size_diff"):
            print("Ukuran baris dan kolom harus sama")
        else:
            print("Matrix hanya dapat berupa angka")

        file.close()
        return adjecencyMatrix