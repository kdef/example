import sys

# print all permutations of an input string

def permute(str_in, str_out):
    if len(str_in) == 0:
        print str_out
    else:
        for i in range(len(str_in)):
            tmp = str_out + str_in[i]
            rest = str_in[:i] + str_in[i+1:]
            permute(rest, tmp)
try:
    test = sys.argv[1]
except IndexError:
    test = "ABC"
permute(test, "")
