import csv
from sys import argv, exit


def main():
    if len(argv) < 3:
        exit(1);

    dna_data = list()

    with open (argv[1]) as dna_databases:
        dna_reader = csv.reader(dna_databases)
        #copy databases into a list
        for row in dna_reader:
            dna_data.append(row)


    with open (argv[2]) as people_sequence:
        people_reader = csv.reader(people_sequence)
        #copy the sequences to be analysed into a string
        for row in people_reader:
            sequence = "".join(row)

    result = str_count(dna_data, sequence)
    # print(result)
    person = identify(dna_data, result)
    print(person)

    # print(dna_data[0])

    # for x in dna_data:
    #     print(x)

    # print(sequence)

def str_count(dna_data, sequence):
    seq_length = len(sequence)
    # interested only in the str sequence
    database = dna_data[0]
    # remove 'name' from the index 0 in the list
    database.pop(0)
    str_count = list()

    for str_dna in database:
        str_dna_length = len(str_dna)
        max_count = 0
        # print(str_dna)

        for i in range(seq_length):
            count = 0

            if sequence[i: i + str_dna_length] == str_dna:
                count += 1
                # print(count, end = "")
                while(sequence[i: i + str_dna_length] == sequence[i + str_dna_length : i + str_dna_length * 2]):
                    i += str_dna_length
                    count += 1
                    # print(count, end = "")
                # print()

                if count > max_count:
                    max_count = count

        str_count.append(max_count);

    return str_count

def identify(dna_data, result):
    # only interested in the names and the str count
    dna_data.pop(0)

    # convert result from a list with int to a list with str
    for i in range(len(result)):
        result[i] = str(result[i])

    for people in dna_data:
        # if match, return the name
        if result == people[1:len(people)]:
            return people[0]

    # if no match after looking through the whole list, return No Match
    return "No Match"

main()