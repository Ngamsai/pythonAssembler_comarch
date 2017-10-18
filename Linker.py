opcodeDict = {'add': '000',
              'nand': '001',
              'lw': '010',
              'sw': '011',
              'beq': '100',
              'jalr': '101',
              'halt': '110',
              'noop': '111'}

typeList = {'I': ['010', '011', '100'],
            'R': ['000,001'],
            'J': ['101'],
            'O': ['110', '111']}


def opcodeAndRegisterTranslator(lines, outfileBinary):
    i = 0
    for line in lines:
        i += 1
        try:
            # print(opcodeDict[line[1]])
            outfileBinary[i - 1] += opcodeDict[line[1]]

            # if opcodeDict[line[1]] in:


            print(outfileBinary[i - 1])
        except KeyError:
            if line[1] == '.fill':
                continue
            exit(1)


def I_typeRegisterTranslator():
    print()


def R_typeRegisterTranslator():
    print()


def J_typeRegisterTranslator():
    print()


def O_typeRegisterTranslator():
    print()
