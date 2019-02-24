import pickle

with open('Data/data.csv', 'w', errors='ignore') as f:

    ### ANGER ###
    with open('Data/anger_t.txt', errors='ignore') as j:
        lines = j.read().splitlines()

    for line in lines:
        line.replace(',', '') # Replaces commas
        line = line[6:-11] # Gets rid of id number and description

        f.write(line + ',anger\n') # Print in csv format

    with open('Data/anger_d.txt', errors='ignore') as j:
        lines = j.read().splitlines()

    for line in lines:
        line.replace(',', '')  # Replaces commas
        line = line[6:-11]  # Gets rid of id number and description

        f.write(line + ',anger\n')  # Print in csv format

    ### FEAR ###
    with open('Data/fear_t.txt', errors='ignore') as j:
        lines = j.read().splitlines()

    for line in lines:
        line.replace(',', '')  # Replaces commas
        line = line[6:-10]  # Gets rid of id number and description

        f.write(line + ',fear\n')  # Print in csv format

    with open('Data/fear_d.txt', errors='ignore') as j:
        lines = j.read().splitlines()

    for line in lines:
        line.replace(',', '')  # Replaces commas
        line = line[6:-10]  # Gets rid of id number and description

        f.write(line + ',fear\n')  # Print in csv format

    ### JOY ###
    with open('Data/joy_t.txt', errors='ignore') as j:
        lines = j.read().splitlines()

    for line in lines:
        line.replace(',', '')  # Replaces commas
        line = line[6:-9]  # Gets rid of id number and description

        f.write(line + ',joy\n')  # Print in csv format

    with open('Data/joy_d.txt', errors='ignore') as j:
        lines = j.read().splitlines()

    for line in lines:
        line.replace(',', '')  # Replaces commas
        line = line[6:-9]  # Gets rid of id number and description

        f.write(line + ',joy\n')  # Print in csv format

    ### SADNESS ###
    with open('Data/sadness_t.txt', errors='ignore') as j:
        lines = j.read().splitlines()

    for line in lines:
        line.replace(',', '')  # Replaces commas
        line = line[6:-12]  # Gets rid of id number and description

        f.write(line + ',sadness\n')  # Print in csv format

    with open('Data/sadness_d.txt', errors='ignore') as j:
        lines = j.read().splitlines()

    for line in lines:
        line = line.replace(',', ' ')  # Replaces commas
        line = line[6:-12]  # Gets rid of id number and description

        f.write(line + ',sadness\n')  # Print in csv format

