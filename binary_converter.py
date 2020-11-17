# Binary to Decimal Conversion
# Take a 1001 input, convert to decimal
# 
# 
# 

def converter(binary):
    """
        Formula: d = num*2^p
        Count each num = p
        Take each num in input, do 0*2+num = pre
    """
    length = len(str(binary))
    pre = 0
    iteration = 0
    for num in str(binary):
        num = int(num)
        if iteration >= length:
            return
        else:
            math = pre*2+num
            pre = math
    return pre
    
def long_conversion(binary):
    binary = str(binary)
    final = ""
    for it in binary.split():
        final += f"{str(converter(it))} "
        
    return final

def is_whole(n):
    return n % 1 == 0

def convert_to_binary(asci):
    asci_txt = str(asci)
    binary = ""
    
    while round(asci) != 0:
        #print(f"pre math: {asci}")
        m = int(asci) / 2
        if is_whole(m):
            binary += "0"
        else:
            binary += "1"
        #print(f"post math: {m}")
        asci = m
        #print(binary)
        #print("-------------------")
        
    return binary[::-1]

def convert_all_to_binary(in_ascii):
    binary = ""
    for it in str(in_ascii).split():
        b = convert_to_binary(int(it))
        binary += b
        binary += " "
    return binary

# 79 = 1001111
# 80 = 1010000