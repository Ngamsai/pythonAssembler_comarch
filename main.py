import Linker
import StringBinOperator
import sys

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
            if(line[0] == ''):
                raise ValueError
            if(out.index(line[0]) >= 0):
                exit(1) #detect duplicate label error(2)
        except ValueError:
            out.append(line[0])
            continue
    return out



def main():
    #print(sys.argv)
    try:
        inFile = sys.argv[1]
    except IndexError:
        inFile = 'test/basic.asm'

    try:
        outFile = sys.argv[2]
    except IndexError:
        outFile = 'out.o'

    file = open(inFile,'r')
    lines = file.readlines()
    file.close()
    splittedlines,outFileBinary = splitWord(lines)
    Linker.labelList = collectLabel(splittedlines)
    out = Linker.opcodeAndRegisterTranslator(splittedlines,outFileBinary)
    out = StringBinOperator.binaryList_to_decimal(out)
    #print(out)
    file = open(outFile,'w')
    for i in range(out.__len__()):
        if i == out.__len__() - 1:
            file.writelines(str(out[i]))
            break
        file.writelines(str(out[i])+'\n')

if __name__ == "__main__":
    main()
