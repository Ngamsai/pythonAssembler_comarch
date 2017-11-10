def printState(reg,pc,lines):
    print('\n@@@')
    print('state:')
    print('\tpc' , pc )
    print('\tmemory:')
    for i in range(0,len(lines)):
        print("\t\tmem[ {0} ] {1}".format(i,lines[i]))
    print('\tregisters:')
    for b in range(0, 8):
        print('\t\treg[ %d ] ' % b, reg[b])
    print('end state')
     
def main():

    lines = []
    reg = [0, 0, 0, 0, 0, 0, 0, 0]
    with open('allinstruct.out','r') as out:
        for line in out:
            line = line.strip()
            lines.append(line)

    count = 0
    pc = 0
    inst = 0 
    
    while (pc >= 0 ):
        DectoBin = ToBin(int(lines[inst]))
        OP = str(DectoBin)[0:3]
                 

#add
        if OP == '000':
            printState(reg,pc,lines)
            regA = int((DectoBin)[3:6],2)
            regB = int((DectoBin)[6:9],2)
            Bit15_3 = int((DectoBin)[9:22],2)
            destReg = int((DectoBin)[22:25],2)
  
            add = reg[regA] + reg[regB]
            value = '{0:b}'.format(add)

            if len(value) > 32:
                value = value[len(value)-32:]
                
            reg[destReg] = int ((value),2)
            
            inst+=1
            pc+=1
            count+=1
#nand
        elif OP == '001':
            printState(reg,pc,lines)
            regAa =  int((DectoBin)[3:6],2)
            regBb =  int((DectoBin)[6:9],2)
            Bit15_3 = int((DectoBin)[9:22],2)
            destReg1 = int((DectoBin)[22:25],2)

            regA = reg[regAa]
            regB = reg[regBb]
            if regA < 0 :
                newregA = regA*(-1)
            else:
                newregA = regA
            if regB < 0 :
                newregB = regB*(-1)
            else:
                newregB = regB
            
            regAA = '{0:b}'.format(newregA)
            if regA < 0:
                regA1 = bwBitBin(regAA)
            else:
                regA1 = incrBit0(regAA,len(regAA))
            
            regBB = '{0:b}'.format(newregB)
            if regB < 0:
                regB1 = bwBitBin(regBB)
            else:
                regB1 = incrBit0(regBB,len(regBB))

            destReg = ''
            for i in range(0,len(regA1)):
                if regA1[i] == '1' and regB1[i] == '1':
                    destReg += '0'
                else:
                    destReg += '1'
            print(destReg,'dst')
            
            if destReg[0] =='1':
                bww = int(bwBit(destReg),2)+1
                dec = bww*(-1)
            else:
                dec = int(destReg,2)
            print(dec,'dec')
            reg[destReg1] = dec

            inst+=1
            pc+=1
            count+=1
            
#lw
        elif (OP == '010'):
            printState(reg,pc,lines)
            regA = int((DectoBin)[3:6],2)
            regB = int((DectoBin)[6:9],2)
            offset = (DectoBin)[9:25]
            offsetfield = two_cmp(offset)
            memA = offsetfield + reg[regA]
            reg[regB] = int(lines[memA])

            inst+=1
            pc+=1
            count+=1

#sw
        elif OP == '011':
            printState(reg,inst,lines)
            regA = int((DectoBin)[3:6],2)
            regB = int((DectoBin)[6:9],2)
            offset = (DectoBin)[9:25]
            offsetfield = two_cmp(offset)
            memA = offsetfield + reg[regA]
            if memA > len(lines):
                lines.append(reg[regB])
            else:
                lines[memA] = (reg[regB])
                
            pc+=1
            inst+=1
            count+=1
  
            
#beq
        elif OP == '100':
            printState(reg,pc,lines)
            beq_pc = -1
            regA = int((DectoBin)[3:6],2)
            regB = int((DectoBin)[6:9],2)
            offset = (DectoBin)[9:25]
            offsetfield = two_cmp(offset)
            
            regA = reg[regA]
            regB = reg[regB]

            
            if regA == regB :
                addr = (beq_pc+1)+offsetfield
                inst = inst + addr +1
                pc = lines.index(lines[inst])
            else :
                inst+=1
                pc+=1
            count+=1
            
                
                
#jalr
        elif OP == '101':
            print(inst)
            printState(reg,pc,lines)
            inst = pc
            regA = int((DectoBin)[3:6],2)
            regB = int((DectoBin)[6:9],2)
            Bit15_0 = int((DectoBin)[9:25],2)

            addrRegB = pc+1
            addr = reg[regA]

            if regA == regB:
                pc = addrRegB
                inst = pc
            else:
                pc = addr
                inst = pc
            count+=1


#halt
        elif OP == '110':
            Bit21_0 = int((DectoBin)[3:25],2)
            printState(reg,pc,lines)
            count+=1
            print('machine halted')
            print('total of {0} instructions executed'.format(count))
            print('final state of machine:')
            printState(reg,pc+1,lines)
            break

#noop
        elif OP == '111' :
            Bit21_0 = int((DectoBin)[3:25],2)
            count+=1
            
        else:
            fill = DectoBin


         

def ToBin(dec):
    if dec > 0 :
        DectoBin = '{0:025b}'.format(dec)
        return DectoBin

    else :
        return dec
    

def convertNum(bin16):
    #convert a 16-bit number into a 32-bit integer
    Bin1 = '1111111111111111'
    Bin0 = '0000000000000000'
    if bin16[0] == '1':
        newBin32 = Bin1 + bin16
        return newBin32
    else:
        newBin32 = Bin0 + bin16
        return newBin32

def two_cmp(offset):
    bin32 = convertNum(offset)
    if bin32[0] =='1':
        bw = int(bwBit(bin32),2)+1
        dec = bw*(-1)
    else:
        dec = int(bin32,2)
    return dec
    

def bwBit(bitBin):
    bwBit = ''
    for i in range(0,len(bitBin)): #convert
            if bitBin[i] == '1':
                bwBit += '0'
            else:
                bwBit += '1'        
    return bwBit
    
def bwBitBin(reg):
    incrr = ''
    bwB = ''
    for i in range(0,len(reg)): 
        if reg[i] == '1':
            bwB += '0'
        else:
            bwB += '1'
    
    bw = int(bwB,2)+1
    bw  = '{0:0b}'.format(bw)

    s = len(reg)
    
    for m in range(0,s-len(bw)):
        incrr += '0'
        
    bw = incrr + bw
    regA1 = incrBit1(bw,s)

    return regA1
    
def incrBit1(bit,s):
    incr = ''
    for n in range(0,32-s):
        incr += '1'
    reg = incr + bit
    return reg

def incrBit0(bit,s):
    incr = ''
    for n in range(0,32-s):
        incr += '0'
    reg = incr + bit
    return reg
    
if __name__ == "__main__":
    main()
