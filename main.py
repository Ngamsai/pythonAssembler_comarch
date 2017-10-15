import Linker

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
    print(splittedlines)
    Linker.opcodeAndRegisterTranslator(splittedlines,outFileBinary)


if __name__ == "__main__":
    main()
