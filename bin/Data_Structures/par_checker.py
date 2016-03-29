from Abstract_Data_Types.Stack import Stack


def matches(open,close):
    #print open,close
    opens = "{(["
    closes = "})]"
    return opens.index(open) == closes.index(close)


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        #print symbol
        if symbol in "({[":
            s.push(symbol)
        else:
            #print "in else"
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1

    if balanced and s.is_empty:
        return True
    else :
        return False


def binary_to_base(dec_num,base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    while dec_num > 0:
        rem = dec_num%base
        rem_stack.push(rem)
        dec_num = dec_num//base

    bin_str = ""
    while not rem_stack.is_empty():
        bin_str = bin_str+digits[rem_stack.pop()]

    return bin_str


#print binary_to_base(29,16)
#print(par_checker('{([][])()}'))
#print(par_checker('{([][]))]}'))