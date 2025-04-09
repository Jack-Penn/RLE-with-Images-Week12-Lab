import console_gfx

print("Welcome to the RLE image encoder!")
print("Displaying Spectrum Image:")
console_gfx.display_image(console_gfx.test_rainbow)

print("RLE Menu")
print("--------")

currentImage = []

class MenuOption:
    def __init__(self, name: str, function = lambda : print("Function Not Implemented Yet")):
        self.name = name
        self.function = function

def loadFile():
    global currentImage
    fileName = input("Enter name of file to load: ")
    currentImage = console_gfx.load_file(fileName)

def loadTestImage():
    global currentImage
    currentImage = console_gfx.test_image
    print("Test image data loaded")

def displayImage():
    console_gfx.display_image(currentImage)

selectedOption = 1
while selectedOption != 0:
    Menu = [MenuOption("Exit", lambda *args : None),
            MenuOption("Load File", loadFile),
            MenuOption("Load Test Image", loadTestImage),
            MenuOption("Read RLE String"),
            MenuOption("Read RLE Hex String"),
            MenuOption("Read Data Hex String"),
            MenuOption("Display Image", displayImage),
            MenuOption("Display RLE String"),
            MenuOption("Display Hex RLE Data"),
            MenuOption("Display Hex Flat Data")]

    for i in range(len(Menu)):
        print(str(i) + ". " + Menu[i].name)

    selectedOption = int(input("\nSelect a Menu Option: "))
    Menu[selectedOption].function()