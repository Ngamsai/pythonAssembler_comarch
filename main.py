opcodeDict = {'add': '000',
              'nand':'001',
              'lw':'010',
              'sw':'011',
              'beq':'100',
              'jalr':'101',
              'halt':'110',
              'noop':'111'}


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

def opcodeLinker(lines,outfileBinary):
    i = 0
    for line in lines:
        i += 1
        try:
            #print(opcodeDict[line[1]])
            outfileBinary[i-1] += opcodeDict[line[1]]
            print(outfileBinary[i-1])
        except KeyError:
            if line[1] == '.fill':
                continue
            print("exit")


def main():

    file = open('test/basic.asm','r')
    lines = file.readlines()
    file.close()
    splittedlines,outFileBinary = splitWord(lines)
    labelList = collectLabel(splittedlines)
    opcodeLinker(splittedlines,outFileBinary)


    print(splittedlines)




if __name__ == "__main__":
    main()
