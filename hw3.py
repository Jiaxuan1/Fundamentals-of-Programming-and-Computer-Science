#################################################
# hw3.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f19_week3_linter
import math
from tkinter import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

#################################################
# patternedMessage
#################################################

# Helper function to remove the whitespace in msg
def delWhitespace(s):
    return s.replace(" ", "")

import string
def patternedMessage(msg, pattern):
    msg = delWhitespace(msg)
    newstring = ""
    flag = -1  # use flag to determine the character from msg
    for i in pattern.strip("\n"):
        if i in string.whitespace:
            newstring += i
        elif i not in string.whitespace:
            flag += 1
            while flag >= len(msg):
                flag -= len(msg)
            newstring += msg[flag]
    return newstring

#################################################
# encodeRightLeftRouteCipher + decodeRightLeftRouteCipher
#################################################

# Helper function to add lowercase letter to the cipher string 
def addLowerletter(s, rows):
    blank = rows - (len(s) % rows)
    source = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1].lower()
    for i in range(blank):
        while i >= 26:
            i -= 26
        s += source[i]
    return s

def encodeRightLeftRouteCipher(text, rows):
    text = addLowerletter(text, rows)
    newstring = ""
    for i in range(rows):
        for j in range(len(text)):
            if j % rows == i:
                newstring += text[j]
    counter = 0
    finalString = ""
    cols = int(len(text) / rows)
    while counter < rows:
        if counter % 2 == 0:
            finalString += newstring[counter*cols:counter*cols + cols]
        else:
            finalString += newstring[counter*cols:counter*cols + cols][::-1]
        counter += 1
    return str(rows) + finalString
        
def decodeRightLeftRouteCipher(cipher):
    rows = int(cipher[0])
    cipher = cipher.replace(str(rows), "")
    newstring = ""
    counter = 0
    cols = int(len(cipher) / rows)
    while counter < rows:
        if counter % 2 == 0:
            newstring += cipher[counter*cols:counter*cols + cols]
        else:
            newstring += cipher[counter*cols:counter*cols + cols][::-1]
        counter += 1
    finalString = ""
    for i in range(cols):
        for j in range(len(newstring)):
            if j % cols == i:
                finalString += newstring[j]
    for k in finalString:
        if k in string.ascii_lowercase:
            finalString = finalString.replace(k, "")
    return finalString

#################################################
# drawSimpleTortoiseProgram
#################################################

def drawSimpleTortoiseProgram(program, canvas, width, height):
    return 42

#################################################
# drawNiceRobot
#################################################

def drawNiceRobot(canvas, width, height):
    canvas.create_text(width/2, height/2, text='<TBD: Draw your Robot here!>')

#################################################
# bonus/optional getEvalSteps
#################################################

# Helper function to turn an operation into number
def calculate(s):
    if s.find("**") != -1:
        return str(int(s[0]) ** int(s[3]))
    elif s.find("*") != -1:
        return str(int(s[0]) * int(s[2]))
    elif s.find("/") != -1:
        return str(int(s[0]) / int(s[2]))
    elif s.find("//") != -1:
        return str(int(s[0]) // int(s[3]))
    elif s.find("%") != -1:
        return str(int(s[0]) % int(s[2]))
    elif s.find("+") != -1:
        return str(int(s[0]) + int(s[2]))
    elif s.find("-") != -1:
        return str(int(s[0]) - int(s[2]))

def getEvalSteps(expr):
    newstring = expr + " = "
    operator = "**, *, /, //, %, +, -"
    line = 0
    if expr.isdigit():
        newstring += expr
    else:
        while expr.isdigit() is False:
            if expr.find("**") != -1:
                idx = expr.find("**")
                expr = expr[:idx-1] + calculate(expr[idx-1:idx+3]) + \
                expr[idx+3:]
            elif expr.find("*") != -1:
                idx = expr.find("*")
                expr = expr[:idx-1] + calculate(expr[idx-1:idx+2]) + \
                expr[idx+2:]
            elif expr.find("/") != -1:
                idx = expr.find("/")
                expr = expr[:idx-1] + calculate(expr[idx-1:idx+2]) + \
                expr[idx+2:]
            elif expr.find("//") != -1:
                idx = expr.find("//")
                expr = expr[:idx-1] + calculate(expr[idx-1:idx+3]) + \
                expr[idx+3:]
            elif expr.find("%") != -1:
                idx = expr.find("%")
                expr = expr[:idx-1] + calculate(expr[idx-1:idx+2]) + \
                expr[idx+2:]
            elif expr.find("+") != -1:
                idx = expr.find("+")
                expr = expr[:idx-1] + calculate(expr[idx-1:idx+2]) + \
                expr[idx+2:]
            elif expr.find("-") != -1:
                idx = expr.find("-")
                expr = expr[:idx-1] + calculate(expr[idx-1:idx+2]) + \
                expr[idx+2:]
            if line == 0:
                    newstring += expr
                    line += 1
            else:
                newstring += "\n      = " + expr
    return newstring
            

#################################################
# bonus/optional topLevelFunctionNames
#################################################

def topLevelFunctionNames(code):
    return 42

#################################################
# Test Functions
#################################################

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    assert(patternedMessage("abc def",   "***** ***** ****")   ==
           "abcde fabcd efab")
    assert(patternedMessage("abc def", "\n***** ***** ****\n") == 
           "abcde fabcd efab")
    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        (msg,pattern) = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        assert(observed == soln)
    print("Passed!")

def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def runDrawNiceRobot(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawNiceRobot(canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawSimpleTortoiseProgram(program, width, height):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawSimpleTortoiseProgram(program, canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawSimpleTortoiseProgram():
    print("Testing drawSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    runDrawSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

    runDrawSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""", 500, 500)
    print("Done!")

def testDrawNiceRobot():
    print('Calling runDrawRobot(400, 400):')
    runDrawNiceRobot(400, 400)
    print('Calling runDrawRobot(800, 800):')
    runDrawNiceRobot(800, 800)

def testBonusTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testPatternedMessage()
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()
#    testDrawSimpleTortoiseProgram()
#    testDrawNiceRobot()
#    testBonusTopLevelFunctionNames()
    testBonusGetEvalSteps()

def main():
    cs112_f19_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
