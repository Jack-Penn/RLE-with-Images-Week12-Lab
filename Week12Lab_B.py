import console_gfx

# Required Functions
def to_hex_string(data): #1
    return ''.join([hex(x)[2:] for x in data])

def count_runs(flat_data): #2
    total_runs = 1
    run_count = 1
    for i in range(len(flat_data) - 1):
        if flat_data[i] != flat_data[i + 1] or run_count == 15:
            total_runs += 1
            run_count = 1
        else:
            run_count += 1
    return total_runs

def encode_rle(flat_data): #3
    encoded = []
    run_count = 1
    for i in range(len(flat_data)-1):
        if flat_data[i] != flat_data[i+1] or run_count == 15:
            encoded.extend([run_count, flat_data[i]])
            run_count = 1
        else:
            run_count += 1
    encoded.extend([run_count, flat_data[-1]])
    return encoded

def get_decoded_length(rle_data): #4
    return sum(rle_data[::2])

def decode_rle(rle_data): #5
    return flatten([[rle_data[(i+1)]]*rle_data[i] for i in range(0, len(rle_data), 2)])

def string_to_data(data_string): #6
    return [int(x, 16) for x in data_string]

def to_rle_string(rle_data): #7
    return ':'.join([str(rle_data[i]) + hex(rle_data[i+1])[2:] for i in range(0, len(rle_data), 2)])

def string_to_rle(rle_string): #8
    return flatten([(int(x[:-1]), int(x[-1], 16)) for x in rle_string.split(':')])

def flatten(data_list):
    return [x for xs in data_list for x in xs]

# Menu
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
    print("Test image data loaded.")
    global currentImage
    currentImage = console_gfx.test_image

def displayImage():
    print("Displaying image...")
    console_gfx.display_image(currentImage)

def readRleString():
    global currentImage
    rleString = input("Enter an RLE string to be decoded: ")
    currentImage = decode_rle(string_to_rle(rleString))

def readRleHexString():
    global currentImage
    rleHexString = input("Enter the hex string holding RLE data: ")
    currentImage = decode_rle(string_to_data(rleHexString))

def readDataHexString():
    global currentImage
    dataHexString = input("Enter the hex string holding flat data: ")
    currentImage = string_to_data(dataHexString)

def displayRleString():
    print("RLE representation: " + to_rle_string(encode_rle(currentImage)))

def displayHexRleData():
    print("RLE hex values: " + to_hex_string(encode_rle(currentImage)))

def displayFlatHexData():
    print("Flat hex values: " + to_hex_string(currentImage))


if __name__ == "__main__":
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)

    selectedOption = 1
    while selectedOption != 0:
        Menu = [MenuOption("Exit", lambda *args : None),
                MenuOption("Load File", loadFile),
                MenuOption("Load Test Image", loadTestImage),
                MenuOption("Read RLE String", readRleString),
                MenuOption("Read RLE Hex String", readRleHexString),
                MenuOption("Read Data Hex String", readDataHexString),
                MenuOption("Display Image", displayImage),
                MenuOption("Display RLE String", displayRleString),
                MenuOption("Display Hex RLE Data", displayHexRleData),
                MenuOption("Display Hex Flat Data", displayFlatHexData)]

        print("\n\nRLE Menu")
        print("--------")
        for i in range(len(Menu)):
            print(str(i) + ". " + Menu[i].name)

        selectedOption = int(input("\nSelect a Menu Option: "))
        Menu[selectedOption].function()