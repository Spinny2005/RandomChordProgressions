import random

array = ["A", "B", "C", "D", "E", "F", "G"]

while True:
    extraNotes = ["maj", "min", "maj7", "min7", "7", "min7b5", "dim7", "6", "6/9", "min6"]
    finalChords = []
    def random_extra_notes():
        chord = extraNotes[random.randint(0, len(extraNotes) - 1)]
        return chord

    finalChords = []
    number = input("Enter the number of chords (default: 4):")
    if (number.isnumeric()):
        number = int(number)
    else:
        number = 4

    i = 0;
    selected = []
    while (i < number):
        selected = array[random.randint(0, len(array) - 1)]
        combinedChords = selected + random_extra_notes()
        finalChords.append(combinedChords)
        i = i + 1

    print("")
    print("Selected strings (" + str(number) + "):\n", *finalChords)
    print("")
