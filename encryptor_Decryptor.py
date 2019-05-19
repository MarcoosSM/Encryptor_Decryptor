import textwrap
import gui

#Estos son los diccionarios creados para que la aplicación pueda funcionar.
diccionarioCifrado={'A':'000000','B':'000001','C':'000010','D':'000011','E':'000100','F':'000101','G':'000110',
'H':'000111','I':'001000','J':'001001','K':'001010','L':'001011','M':'001100','N':'001101','Ñ':'001110','O':'001111',
'P':'010000','Q':'010001','R':'010010','S':'010011','T':'010100','U':'010101','V':'010110','W':'010111','X':'011000',
'Y':'011001', 'Z':'011010',' ':'011011','1':'011100','2':'011101','3':'011110','4':'011111','5':'100000','6':'100001',
'7':'100010','8':'100011','9':'100100','0':'100101','Á':'100110','É':'100111','Í':'101000','Ó':'101001','Ú':'101010',
',':'101011','.':'101100','¿':'101101','?':'101110','¡':'101111','!':'110000','Ç':'110001','(':'110010',')':'110011',
'@':'110100','%':'110101','$':'110110','€':'110111','&':'111000','-':'111001','#':'111010','/':'111011','+':'111100',
'=':'111101','*':'111110','º':'111111'}
diccionarioDescifrado={'000000':'A','000001':'B','000010':'C','000011':'D','000100':'E','000101':'F','000110':'G',
'000111':'H','001000':'I','001001':'J','001010':'K','001011':'L','001100':'M','001101':'N','001110':'Ñ','001111':'O',
'010000':'P','010001':'Q','010010':'R','010011':'S','010100':'T','010101':'U','010110':'V','010111':'W','011000':'X',
'011001':'Y','011010':'Z','011011':' ','011100':'1','011101':'2','011110':'3','011111':'4','100000':'5','100001':'6',
'100010':'7','100011':'8','100100':'9','100101':'0','100110':'Á','100111':'É','101000':'Í','101001':'Ó','101010':'Ú',
'101011':',','101100':'.','101101':'¿','101110':'?','101111':'¡','110000':'!','110001':'Ç','110010':'(','110011':')',
'110100':'@','110101':'%','110110':'$','110111':'€','111000':'&','111001':'-','111010':'#','111011':'/','111100':'+',
'111101':'=','111110':'*','111111':'º'}
HexadecimalBinario={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
'9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
BinarioHexadecimal={'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7',
'1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
option=0

#Esta función se encarga de encriptar el mensaje dado por el usuario.
def encrypt(messageC):
    #primero se pasa el mensaje a mayúsculas para que no haya ningún problema con el diccionario.
    messageC = messageC.upper()
    result = ""
    finalresult = ""
    noValidChar = False
    #Este for convierte el mensaje del usuario en binario y además comprueba si algún carácter no es válido.
    for cont in range(0,len(messageC)):
        if messageC[cont] in diccionarioCifrado:
            result = result + diccionarioCifrado[messageC[cont]]
            cont+=1
        else:
            noValidChar = True
    #Este if llama a una función de la interfaz en el caso de que haya caracteres no validos para avisar al usuario.
    if noValidChar:
        gui.invalidCharMessage()
    #A continuación se comprueba si se puede dividir el binario en grupos de 4 bits, si no es así se añaden tantos 
    # ceros al inicio como sea necesario y luego pasa el binario a hexadecimal y lo devuelve.
    if len(result)%4 == 0:
        resultList = textwrap.wrap(result, 4)
        for cont in range(0,len(resultList)):
            if resultList[cont] in BinarioHexadecimal:
                finalresult = finalresult + BinarioHexadecimal[resultList[cont]]
                cont+=1    
    else:
        resultList = textwrap.wrap(result, 4)
        n = len(resultList[-1])
        if n == 1:
            result = '0'*3 + result
        elif n == 2:
            result = '0'*2 + result
        elif n == 3:
            result = '0'*1 + result
        resultList = textwrap.wrap(result, 4)
        for cont in range(0,len(resultList)):
            if resultList[cont] in BinarioHexadecimal:
                finalresult = finalresult + BinarioHexadecimal[resultList[cont]]
                cont+=1
    return finalresult

#Esta función se encarga de desencriptar el mensaje dado por el usuario.
def decrypt(messageD):
    result=""
    finalresult=""
    #Lo primero que se hace es comprobar si el mensaje a descifrar es hexadecimal, si lo es, se ejecuta la función, si 
    # no, avisa al usuario.
    try:
        if int(messageD, 16):
            #Este for convierte el mensaje en hexadecimal a binario.
            for cont in range(0,len(messageD)):
                if messageD[cont] in HexadecimalBinario:
                    result = result + HexadecimalBinario[messageD[cont]]
                    cont+=1
            #A continuación se comprueba si se puede dividir el binario en grupos de 6 bits, si no es así se suprimen 
            # tantos bits al inicio como sea necesario y luego pasa el binario al mensaje descifrado y lo devuelve.
            if len(result)%6 == 0:
                letters = textwrap.wrap(result, 6)
                for cont in range(0, len(letters)):
                    if letters[cont] in diccionarioDescifrado:
                        finalresult= finalresult + diccionarioDescifrado[letters[cont]]
                        cont+=1
            else:
                resultList = textwrap.wrap(result, 6)
                n = len(resultList[-1])
                if n == 1:
                    result = result[1:]
                elif n == 2:
                    result = result[2:]
                elif n == 3:
                    result = result[3:]
                resultList = textwrap.wrap(result, 6)
                for cont in range(0,len(resultList)):
                    if resultList[cont] in diccionarioDescifrado:
                        finalresult = finalresult + diccionarioDescifrado[resultList[cont]]
                        cont+=1
    except ValueError:
        gui.noHexDecrypt()
    return finalresult