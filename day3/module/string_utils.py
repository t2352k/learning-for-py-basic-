def reverse_str(s):
    n=len(s)
    result=['']*n
    i=-1
    for character in s:
        result[i]=character
        i-=1
    return result

if __name__=="__main__":
    s='qwertyuiop'
    s=s.split(',')
    print(reverse_str(s))
