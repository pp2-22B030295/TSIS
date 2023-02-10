def getString():
    x = str(input())

def prinString(s):
    print(s)

class string:
    def __init__(self , string):
        self.string = string
    def __str__(self):
        return f"{self.string}"

string = getString()
printString(string)

