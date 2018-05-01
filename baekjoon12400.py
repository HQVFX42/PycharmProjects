str1 = " abcdefghijklmnopqrstuvwxyz"
str2 = " yhesocvxduiglbkrztnwjpfmaq"
rule = {'a':'y',
        'b':'h',
        'c':'e',
        'd':'s',
        'e':'o',
        'f':'c',
        'g':'v',
        'h':'x',
        'i':'d',
        'j': 'u',
        'k': 'i',
        'l': 'g',
        'm': 'l',
        'n': 'b',
        'o': 'k',
        'p': 'r',
        'q': 'z',
        'r': 't',
        's': 'n',
        't': 'w',
        'u': 'j',
        'v': 'p',
        'w': 'f',
        'x': 'm',
        'y': 'a',
        'z': 'q',
        }
strList = []
T = eval(input("길이를 입력하세요: "))
for i in range(T):
    G = input("문자열을 입력하세요: ")
    strList.append(G)
for i in range(T):
    convertStr =""
    for c in strList[i]:
        convertStr += rule[c]

    print("Case #", i+1, ":")
    print(convertStr)
