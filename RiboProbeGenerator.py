#!/usr/bin/python3
import sys
#version: 2018-12-20, Hanwen Gu

def Complementer(String):
    StringList = list(String)
    for i in range(len(StringList)):
        # Substitution based on 'Nucleic acid notation'
        # For canonical bases:
        if StringList[i] == "A":
            StringList[i] = "T"
        elif StringList[i] == "a":
            StringList[i] = "t"
        elif StringList[i] == "T":
            StringList[i] = "A"
        elif StringList[i] == "t":
            StringList[i] = "a"
        elif StringList[i] == "G":
            StringList[i] = "C"
        elif StringList[i] == "g":
            StringList[i] = "c"
        elif StringList[i] == "C":
            StringList[i] = "G"
        elif StringList[i] == "c":
            StringList[i] = "g"
        # For degenerate nucleotides:
        elif StringList[i] == "W":
            StringList[i] = "S"
        elif StringList[i] == "w":
            StringList[i] = "s"
        elif StringList[i] == "S":
            StringList[i] = "W"
        elif StringList[i] == "s":
            StringList[i] = "w"
        elif StringList[i] == "M":
            StringList[i] = "K"
        elif StringList[i] == "m":
            StringList[i] = "k"
        elif StringList[i] == "K":
            StringList[i] = "M"
        elif StringList[i] == "k":
            StringList[i] = "m"
        elif StringList[i] == "R":
            StringList[i] = "Y"
        elif StringList[i] == "r":
            StringList[i] = "y"
        elif StringList[i] == "Y":
            StringList[i] = "R"
        elif StringList[i] == "y":
            StringList[i] = "r"
        elif StringList[i] == "B":
            StringList[i] = "V"
        elif StringList[i] == "b":
            StringList[i] = "v"
        elif StringList[i] == "V":
            StringList[i] = "B"
        elif StringList[i] == "v":
            StringList[i] = "b"
        elif StringList[i] == "D":
            StringList[i] = "H"
        elif StringList[i] == "d":
            StringList[i] = "h"
        elif StringList[i] == "H":
            StringList[i] = "D"
        elif StringList[i] == "h":
            StringList[i] = "d"
        elif StringList[i] == "N":
            StringList[i] = "N"
        elif StringList[i] == "n":
            StringList[i] = "n"
        else:
            StringList[i] = "N"
    return "".join(map(str, StringList))


def FastaSeqReverser():
    fi = open(sys.argv[1], 'r')
    fo = open(sys.argv[2], 'w')

    for line in fi:
        interval = 50
        if line.startswith(">") == True:
            header = line.strip()
        else:
            sequence=line.strip()

            seqlength = len(sequence)

            for x in range(0, seqlength, interval):
                seg=sequence[x:x + interval]
                reline = seg[::-1]
                relinecom = Complementer(reline)
                fo.write(header + "_" + str(x) + "\n" + relinecom + "\n")

    fi.close()
    fo.close()


if len(sys.argv) != 3:
    print("This is a script to cleave the current FASTA input into fragments (default size: 50 nt) and generate reverse complemantary sequence of each fragments")
    print("Input: Any multi-FASTA DNA file, but with ONE-LINE sequences")
    print("If the FASTA sequences are not one-line, please use FastaSeqLinearizer to convert it to one-line sequences first")
    print("or it will only reverse complement the seq fragments that are in the same line , but not the full sequences")
    print("Usage: [FastaSeqReverser.py] [FASTA DNA Input] [FASTA DNA Output]")
else:
    FastaSeqReverser()
