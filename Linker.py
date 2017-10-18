import StringBinOperator
opcodeDict = {'add': '000',
              'nand': '001',
              'lw': '010',
              'sw': '011',
              'beq': '100',
              'jalr': '101',
              'halt': '110',
              'noop': '111'}

typeList = {'I': ['010', '011', '100'],
            'R': ['000','001'],
            'J': ['101'],
            'O': ['110', '111']}
labelList = []

def opcodeAndRegisterTranslator(lines, outfileBinary):
    i = 0
    for line in lines:
        i += 1
        try:
            # print(opcodeDict[line[1]])
            outfileBinary[i - 1] += opcodeDict[line[1]]

            if opcodeDict[line[1]] in typeList['I']:
                outfileBinary[i - 1] += I_typeRegisterTranslator(line,i-1)

            elif opcodeDict[line[1]] in typeList['R']:
                outfileBinary[i - 1] += R_typeRegisterTranslator(line)

            elif opcodeDict[line[1]] in typeList['J']:
                J_typeRegisterTranslator(line)

            elif opcodeDict[line[1]] in typeList['O']:
                outfileBinary[i - 1] += O_typeRegisterTranslator(line)

            #print(outfileBinary[i - 1])
        except KeyError:
            if line[1] == '.fill':

                try:
                    outfileBinary[i - 1] = int(line[2])
                except ValueError:
                    outfileBinary[i - 1] = labelList.index(line[2])


                continue
            exit(1)
    return outfileBinary


def I_typeRegisterTranslator(line,currentLine):
    out = ''
    i = 2
    while i < line.__len__():
        if line[i].isdecimal():
            if i == line.__len__()-1:
                out += '{0:016b}'.format(int(line[i]))
            else:
                out += '{0:03b}'.format(int(line[i]))
        else:
            #print(labelList.index(line[i])-currentLine)
            out += StringBinOperator.two_complement(labelList.index(line[i])-currentLine)
        i += 1

    return out




def R_typeRegisterTranslator(line):
    out = ''
    i = 2
    while i < line.__len__():
        if line[i].isdecimal():
            if i == line.__len__()-1:
                out += '0000000000000'+'{0:03b}'.format(int(line[i]))
            else:
                out += '{0:03b}'.format(int(line[i]))
        else:
            out += '555'
        i += 1

    return out


def J_typeRegisterTranslator(line):
    print()


def O_typeRegisterTranslator(line):

    return '{0:022b}'.format(0)
