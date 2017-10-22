#import StringBinOperator

def main():
        lines = []
        a = 0
        print('@@@\nstate:')
       # print('\tpc %d' )
        print('\tmemory:')
        with open('out.o','r') as out:
                while a < 10:  
                        for line in out:
                                line = line.strip()
                                print('\t\tmem[%d]: %s' %(a,line))
                                a += 1
                print('\tregisters:')
                for b in range(0,8):
                        print('\t\treg[%d]: 0' %b)
                print('End state\n@@@')    

def 
                
if __name__ == "__main__":
    main()
