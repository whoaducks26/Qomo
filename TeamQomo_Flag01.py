#Input
#code = input('Enter code: ')
#code = 'AUC8EH'
#code = 'ZY12QHPO94TR'
#code = 'ZY12QHPO94TO'

#Process
def masking_spell(code):
    if len(code) < 8:
        print('Unstable code')  #<--- code is too weak to protect
    
    else:
        masked_code = "*"*len(code[:-4]) + code[-4::]


        if code[-1] in {'A', 'E', 'I', 'O', 'U'}:
            masked_code += '- Dark Magic Detected'  #<--- dark magic

        print(masked_code)

masking_spell(code="AUC8EH")
masking_spell(code="ZY12QHPO94TR")
masking_spell(code="ZY12QHPO94TO")
