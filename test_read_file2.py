import os
with open(os.path.join('documents','zen_of_python.txt'),'rt') as file:
    for line in file:
        if "better" in line:
            print(line)