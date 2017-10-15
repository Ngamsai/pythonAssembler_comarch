def two_complement(num):
    if num >= 0:
        return '{0:016b}'.format(num)
    else:
        return '{0:016b}'.format((int(not_binary('{0:016b}'.format(num)),2)))

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
