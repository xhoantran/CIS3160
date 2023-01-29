"""=============================================================================
| Assignment: pa02 - Calculating an 8, 16, or 32 bit
| checksum on an ASCII input file
|
| Author: Hoan Tran
| Language: c, c++, Java, GO, Python
|
| To Compile: javac pa02.java
| gcc -o pa02 pa02.c
| g++ -o pa02 pa02.cpp
| go build pa02.go
| python pa02.py //Caution - expecting input parameters
|
| To Execute: java -> java pa02 inputFile.txt 8
| or c++ -> ./pa02 inputFile.txt 8
| or c -> ./pa02 inputFile.txt 8
| or go -> ./pa02 inputFile.txt 8
| or python-> python pa02.py inputFile.txt 8
| where inputFile.txt is an ASCII input file
| and the number 8 could also be 16 or 32
| which are the valid checksum sizes, all
| other values are rejected with an error message
| and program termination
|
| Note: All input files are simple 8 bit ASCII input
|
| Class: CIS3360 - Security in Computing - Fall 2022
| Instructor: McAlpin
| Due Date: per assignment
|
+============================================================================="""

import os
import sys


def padding(file_content, checksum_size):
    divisor = checksum_size // 8

    if len(file_content) % divisor != 0:
        # calculate number of X to add
        number_of_x = divisor - (len(file_content) % divisor)
        # add X to file content
        file_content += "X" * number_of_x
    return file_content


def checksum(file_content, checksum_size):
    total = 0
    step = checksum_size // 8
    for i in range(0, len(file_content), step):
        for j in range(step):
            total += ord(file_content[i + j]) * (256 ** (step - j - 1))
    return total % (256**step)


def main(argv):
    # check for correct number of arguments
    if len(argv) != 3:
        sys.stderr.write("Usage: python pa02.py <input file> <size of the checksum>")
        return

    # check if valid file
    if not os.path.isfile(argv[1]):
        sys.stderr.write("Error: input file does not exist")
        return

    valid_checksum_size = ["8", "16", "32"]
    if argv[2] not in valid_checksum_size:
        sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
        return
    checksum_size = int(argv[2])

    # open file
    file = open(argv[1], "r")

    # read file
    file_content = file.read()

    # add padding
    file_content = padding(file_content, checksum_size)

    # Echo the input text file
    sys.stdout.write("\n")
    for i in range(0, len(file_content), 80):
        sys.stdout.write(file_content[i : i + 80] + "\n")

    # calculate checksum
    checksum_value = checksum(file_content, checksum_size)

    # convert checksum to hex
    checksum_value = hex(checksum_value)[2:]

    # print checksum
    sys.stdout.write(
        f"{checksum_size:2} bit checksum is {checksum_value:>8} for all {len(file_content):>4} chars\n"
    )


if __name__ == "__main__":
    main(sys.argv)


"""=============================================================================
| I Hoan Tran (5373946) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================"""
