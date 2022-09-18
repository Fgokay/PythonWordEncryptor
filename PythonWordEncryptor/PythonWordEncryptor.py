############################################## Key to Code ##############################################
varA = '1'
varB = '2'
varC = '3'
varD = '4'
varE = '5'
varF = '6'
varG = '7'
varH = '8'
varI = '9'
varJ = '10'
varK = '11'
varL = '12'
varM = '13'
varN = '14'
varO = '15'
varP = '16'
varQ = '17'
varR = '18'
varS = '19'
varT = '20'
varU = '21'
varV = '22'
varW = '23'
varX = '24'
varY = '25'
varZ = '26'
############################################## Code to Key ##############################################
var1 = 'a'
var2 = 'b'
var3 = 'c'
var4 = 'd'
var5 = 'e'
var6 = 'f'
var7 = 'g'
var8 = 'h'
var9 = 'i'
var10 = 'j'
var11 = 'k'
var12 = 'l'
var13 = 'm'
var14 = 'n'
var15 = 'o'
var16 = 'p'
var17 = 'q'
var18 = 'r'
var19 = 's'
var20 = 't'
var21 = 'u'
var22 = 'v'
var23 = 'w'
var24 = 'x'
var25 = 'y'
var26 = 'z'
############################################## Functions ##############################################
def enqrypt():
    key = input("Enter key: ")
    key = key.split(" ")
    for i in key:
        if "a" in key:
            aFind = key.index('a') 
            key[aFind] = varA
            
        if "b" in key:
            bFind = key.index('b') 
            key[bFind] = varB
            
        if "c" in key:
            cFind = key.index('c') 
            key[cFind] = varC
          
        if "d" in key:
            dFind = key.index('d') 
            key[dFind] = varD
           
        if "e" in key:
            eFind = key.index('e') 
            key[eFind] = varE
            
        if "f" in key:
            fFind = key.index('f') 
            key[fFind] = varF
            
        if "g" in key:
            gFind = key.index('g') 
            key[gFind] = varG
           
        if "h" in key:
            hFind = key.index('h') 
            key[hFind] = varH
            
        if "i" in key:
            iFind = key.index('i') 
            key[iFind] = varI
            
        if "j" in key:
            jFind = key.index('j') 
            key[jFind] = varJ
            
        if "k" in key:
            kFind = key.index('k') 
            key[kFind] = varK
            
        if "l" in key:
            lFind = key.index('l') 
            key[lFind] = varL
            
        if "m" in key:
            mFind = key.index('m') 
            key[mFind] = varM
            
        if "n" in key:
            nFind = key.index('n') 
            key[nFind] = varN
            
        if "o" in key:
            oFind = key.index('o') 
            key[oFind] = varO
            
        if "p" in key:
            pFind = key.index('p') 
            key[pFind] = varP

        if "q" in key:
            qFind = key.index('q') 
            key[qFind] = varQ

        if "r" in key:
            rFind = key.index('r') 
            key[rFind] = varR
            
        if "s" in key:
            sFind = key.index('s') 
            key[sFind] = varS

        if "t" in key:
            tFind = key.index('t') 
            key[tFind] = varT
            
        if "u" in key:
            uFind = key.index('u') 
            key[uFind] = varU
           
        if "v" in key:
            vFind = key.index('v') 
            key[vFind] = varV

        if "w" in key:
            wFind = key.index('w') 
            key[wFind] = varW
            
        if "x" in key:
            xFind = key.index('x') 
            key[xFind] = varX

        if "y" in key:
            yFind = key.index('y') 
            key[yFind] = varY
            
        if "z" in key:
            zFind = key.index('z') 
            key[zFind] = varZ

    print(key)    
            

def deEncrypt():
  code = input("code: ")
  code = code.split(" ")

  for i in code:
    if '1' in code:
        aaFind = code.index('1')
        code[aaFind] = var1

    if '2' in code:
        bbFind = code.index('2')
        code[bbFind] = var2

    if '3' in code:
        ccFind = code.index('3')
        code[ccFind] = var3

    if '4' in code:
        ddFind = code.index('4')
        code[ddFind] = var4

    if '5' in code:
        eeFind = code.index('5')
        code[eeFind] = var5

    if '6' in code:
        ffFind = code.index('6')
        code[ffFind] = var6

    if '7' in code:
        ggFind = code.index('7')
        code[ggFind] = var7

    if '8' in code:
        hhFind = code.index('8')
        code[hhFind] = var8

    if '9' in code:
        iiFind = code.index('9')
        code[iiFind] = var9

    if '10' in code:
        jjFind = code.index('10')
        code[jjFind] = var9

    if '11' in code:
        kkFind = code.index('11')
        code[kkFind] = var11

    if '12' in code:
        llFind = code.index('12')
        code[llFind] = var12

    if '13' in code:
        mmFind = code.index('13')
        code[mmFind] = var13

    if '14' in code:
        nnFind = code.index('14')
        code[nnFind] = var14
        
    if '15' in code:
        ooFind = code.index('15')
        code[ooFind] = var15

    if '16' in code:
        ppFind = code.index('16')
        code[ppFind] = var16

    if '17' in code:
        qqFind = code.index('17')
        code[qqFind] = var17

    if '18' in code:
        rrFind = code.index('18')
        code[rrFind] = var18

    if '19' in code:
        ssFind = code.index('19')
        code[ssFind] = var19

    if '20' in code:
        ttFind = code.index('20')
        code[ttFind] = var20

    if '21' in code:
        uuFind = code.index('21')
        code[uuFind] = var21

    if '22' in code:
        vvFind = code.index('22')
        code[vvFind] = var22

    if '23' in code:
        wwFind = code.index('23')
        code[wwFind] = var23

    if '24' in code:
        xxFind = code.index('24')
        code[xxFind] = var24

    if '25' in code:
        yyFind = code.index('25')
        code[yyFind] = var25

    if '26' in code:
        zzFind = code.index('26')
        code[zzFind] = var26
        
    print(code)
    
############################################## Menu ###################################################
menuQuestion = input('What do you want ? (key to code/code to key): ')

if menuQuestion == 'key to code':
    enqrypt()
elif menuQuestion == 'code to key':
    deEncrypt()


############################################## Notes ##################################################

# if you want to add a variable
##############Key to Code##############
#create a variable for code ex((key name) = 'variable code')

# create this in encrypt()
# if "variable code" in key:
#            (key name)Find = key.index('variable code') 
#            key[zFind] = var(key name)

##############Code to Key##############
#create a code for variable ex((code name) = 'key name')

#if 'code' in code:
#        (random name)Find = code.index('(key name)')
#        code[(random name)Find] = (code)



