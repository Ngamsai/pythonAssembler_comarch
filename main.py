import Linker
import StringBinOperator

def splitWord(lines):
    out = []
    outFile = []
    for line in lines:
        line = line.split('\t')
        line.append(line.pop().split('\n')[0])
        #print(line)
        out.append(line)
        outFile.append('0000000')

    return out,outFile

def collectLabel(lines):
    out = []
    for line in lines:
        out.append(line[0])
    return out



def main():

    file = open('test/basic.asm','r')
    lines = file.readlines()
    file.close()
    splittedlines,outFileBinary = splitWord(lines)
    Linker.labelList = collectLabel(splittedlines)
    #print(splittedlines)
    out = Linker.opcodeAndRegisterTranslator(splittedlines,outFileBinary)
    out = StringBinOperator.binaryList_to_decimal(out)
    print(out)
    file = open('out.o','w')
    for line in out:
        file.writelines(str(line)+'\n')

if __name__ == "__main__":
    main()
