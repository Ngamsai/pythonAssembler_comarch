opCodeDict = {'add': '000',
              'nand':'001',
              'lw':'010',
              'sw':'011',
              'beq':'100',
              'jalr':'101',
              'halt':'110',
              'nooop':'111'}


def splitWord(lines):
    out = []
    for line in lines:
        line = line.split('\t')
        line.append(line.pop().split('\n')[0])
        #print(line)
        out.append(line)

    return out

def collectLabel(lines):
    out = []
    for line in lines:
        out.append(line[0])
    return out


def main():

    file = open('test/basic.asm','r')
    lines = file.readlines()
    file.close()
    splittedlines = splitWord(lines)
    labelList = collectLabel(splittedlines)
    try:
        print(opCodeDict['add'])
    except KeyError:
        print("exit")

    print(splittedlines)




if __name__ == "__main__":
    main()
