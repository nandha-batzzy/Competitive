

def back_space(string):
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string
    if "#" not in string:
        return string
    lenn = len(string) - 1
    i = 0
    str1 = ""
    while i <= lenn:
        if string[i] == "#":
            if i == 0:
                lenn = lenn-1
                string = string[(i + 1):]
                str1 = string
                i =i-1
                continue
            c = i-1
            m = i+1
            string = string[:c] + string[m:]
            i = c-1
            lenn = lenn-2
        str1 = string
        i = i+1
    return str1

def compare1(stra,strb):
    if stra == strb:
        return True
    else:
        return False

s = "#f#"
t = "#f"


stra = back_space(s)
strb = back_space(t)

print(compare1(stra,strb))
