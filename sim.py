#import StringBinOperator

def main():
        lines = []
        a = 0
        mem = []
        print('@@@\nstate:')
       # print('\tpc %d' )
        print('\tmemory:')
        with open('out.o','r') as out:
                while a < 10:  
                        for line in out:
                                line = line.strip()
                                print('\t\tmem[%d]: %s' %(a,line))
                                line = int(str(line))
                                Bin = bin(line)
                                #D = '{0:025b}'.format(Bin)
                                #print(Bin)        
                                Opcode = str(Bin[0:3])
                                print(Opcode)   
                                a += 1
                print('\tregisters:')
                for b in range(0,8):
                        print('\t\treg[%d]: 0' %b)
                print('End state\n')    

#def

def FillBin(Bin):
                Bin25 = '{0:025b}'.format(Bin)
                return Bin25
      

    
               

if __name__ == "__main__":
    main()
