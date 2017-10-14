def two_complement(num):
    if num >= 0:
        return '{0:016b}'.format(num)
    else:
        return '{0:016b}'.format((int(not_binary('{0:016b}'.format(num)),2)+1))

def not_binary(binary):
    for i in range(binary.__len__()):
        if binary[i] == '1':
            binary[i] = '0'
        else:
            binary[i] = '1'
    return binary
