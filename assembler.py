import sys

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

def two_complement(num):
    if num >= 0:
        return '{0:016b}'.format(num)
    else:
        # not binary +1
        return '{0:016b}'.format((int(not_binary('{0:016b}'.format(num)),2)+1))

def not_binary(binary):
    out = ''
    for i in range(binary.__len__()):
        if binary[i] == '1':
            out += '0'
        else:
            out += '1'
    return out

def binaryList_to_decimal(binaryList):
    out = []
    for line in binaryList:
        try:
            out.append(int(line,2))
        except TypeError:
            out.append(line)
    return out


def opcodeAndRegisterTranslator(lines, outfileBinary ,labelList):
    i = 0
    for line in lines:
        i += 1
        try:
            # print(opcodeDict[line[1]])
            outfileBinary[i - 1] += opcodeDict[line[1]]

            if opcodeDict[line[1]] in typeList['I']:
                outfileBinary[i - 1] += I_typeRegisterTranslator(line,i-1,labelList)

            elif opcodeDict[line[1]] in typeList['R']:
                outfileBinary[i - 1] += R_typeRegisterTranslator(line)

            elif opcodeDict[line[1]] in typeList['J']:
                outfileBinary[i - 1] += J_typeRegisterTranslator(line)

            elif opcodeDict[line[1]] in typeList['O']:
                outfileBinary[i - 1] += O_typeRegisterTranslator(line)
            else:
                exit(1) #error opcde not found error(4)

        except KeyError:
            if line[1] == '.fill':

                try:
                    outfileBinary[i - 1] = int(line[2])
                except ValueError:
                    outfileBinary[i - 1] = labelList.index(line[2])


                continue
            exit(1)
    return outfileBinary


def I_typeRegisterTranslator(line,currentLine,labelList):
    out = ''
    i = 2
    while i < line.__len__():

        if line[i].isdecimal():
            if i == line.__len__()-1:
                if(int(line[i]) > 65535):
                    exit(1) #detect more than 16 bit error(3)
                out += '{0:016b}'.format(int(line[i]))
            else:
                if(int(line[i]) > 7 or int(line[i]) < 0):
                    exit(1) #detect invalid register error(register)
                out += '{0:03b}'.format(int(line[i]))
        else:
            #print(labelList.index(line[i])-currentLine)
            try:
                #print(line[1])
                if(line[1] == 'lw' or line[1] == 'sw'):  #lw and sw (pc not +4 or currentline)
                    out += two_complement(labelList.index(line[i]))
                else: # beq( pc+4 or nextline )
                    out += two_complement(labelList.index(line[i]) - (currentLine + 1))
            except ValueError:
                exit(1) #detect undefine label error(1)
        i += 1

    return out




def R_typeRegisterTranslator(line):
    out = ''
    i = 2
    while i < line.__len__():
        if line[i].isdecimal():
            if(int(line[i]) > 7 or int(line[i]) < 0):
                    exit(1) #detect invalid register error(register)
            if i == line.__len__()-1:
                out += '0000000000000'+'{0:03b}'.format(int(line[i]))
            else:
                out += '{0:03b}'.format(int(line[i]))
        else:
            exit(1)#exit if use non number in register field.
        i += 1

    return out


def J_typeRegisterTranslator(line):
    out = ''
    i = 2
    while i < line.__len__():
        if(int(line[i]) > 7 or int(line[i]) < 0):
                    exit(1) #detect invalid register error(register)
        if line[i].isdecimal():
            out += '{0:03b}'.format(int(line[i]))
        else:
            exit(1)#exit if use non number in register field.
        i += 1
    out += '{0:016b}'.format(0)
    return out

def O_typeRegisterTranslator(line):

    return '{0:022b}'.format(0)


def splitWord(lines):
    out = []
    outFile = []
    for line in lines:
        line = line.split('\t')
        line.append(line.pop().split('\n')[0])
        out.append(line)
        outFile.append('0000000')

    return out,outFile

def collectLabel(lines):
    out = []
    for line in lines:

        try:
            if line[0] == '':
                raise ValueError
            if out.index(line[0]) >= 0:
                exit(1) #detect duplicate label error(2)
        except ValueError:
            out.append(line[0])
            continue
    return out



def main():
    #----- start load file into 'lines' ---------
    try:
        inFile = sys.argv[1]
    except IndexError:
        inFile = 'old/test/basic.asm'

    try:
        outFile = sys.argv[2]
    except IndexError:
        outFile = 'out.o'

    file = open(inFile,'r')
    lines = file.readlines()
    file.close()
    #----- end file load -------------

    #---- Split tabs and space, prepare 7 MSB in '0' ----
    splittedlines,outFileBinary = splitWord(lines)

    #---- collect label for use later ----
    labelList = collectLabel(splittedlines)

    #---- translate instructions and store a list of binary in 'out' ----
    out = opcodeAndRegisterTranslator(splittedlines, outFileBinary, labelList)

    #---- convert binary to decimal ----
    out = binaryList_to_decimal(out)

    #---- start write result to file ----
    file = open(outFile,'w')
    for i in range(out.__len__()):
        if i == out.__len__() - 1:
            file.writelines(str(out[i]))
            break
        file.writelines(str(out[i])+'\n')
    #---- end write result to file ----

if __name__ == "__main__":
    main()
