filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

print(count_char(text, "r"))

# Print percentage of every letter from the entire text
for char in "abcdefhijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round (perc, 2)))

# Prevent program from automatically exiting
dark = input()
