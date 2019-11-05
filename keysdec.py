keys = [None, ## Reserved codes
        None,
        None,
        None,
         'a',
         'b',
         'c',
         'd',
         'e',
         'f',
         'g',
         'h',
         'i',
         'j',
         'k',
         'l',
         'm',
         'n',
         'o',
         'p',
         'q',
         'r',
         's',
         't',
         'u',
         'v',
         'w',
         'x',
         'y',
         'z',
         '1',
         '2',
         '3',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9',
         '0',
        None, ## ENTER
        None, ## ESC
        None, ## DEL
        None, ## TAB
        None, ## SPACE
         '-',
         '=',
         '[',
         ']',
         '\\',
        None, ## Non-US `
         ';',
         "'",
         '`',
         ',',
         '.',
         '/']

skeys = [None,  ## Reserved codes
         None,
         None,
         None,
         'A',   ## A = 0x04 = 4
         'B',
         'C',
         'D',
         'E',
         'F',
         'G',
         'H',
         'I',
         'J',
         'K',
         'L',
         'M',
         'N',
         'O',
         'P',
         'Q',
         'R',
         'S',
         'T',
         'U',
         'V',
         'W',
         'X',
         'Y',
         'Z',
         '!',
         '@',
         '#',
         '$',
         '%',
         '^',
         '&',
         '*',
         '(',
         ')',
         None, ## ENTER
         None, ## ESC
         None, ## DEL
         None, ## TAB
         None, ## SPACE
         '_',
         '+',
         '{',
         '}',
         '|',
         None, ## Non-US ~
         ':',
         '"',
         '~',
         '<',
         '>',
         '?']

akeys = {"n":40,
         "e":41,
         "b":42,
         "t":43,
         "s":44}

def getChr(key):
    try:
        return chr(keys.index(key))
    except ValueError:
        if key == " ":
            return chr(44)
        else:
            return None

def getUpChr(key):
    try:
        return chr(skeys.index(key))
    except ValueError:
        return None

def getAct(code):
    try:
        return chr(akeys[code])
    except KeyError:
        return None

def printKeys():
    for i in enumerate(keys):
        print(i)
