#Input
code = input('Enter code: ')
#code = 'AUC8EH'
#code = 'ZY12QHPO94TR'
#code = 'ZY12QHPO94TO'

#Process
def masking_spell(code):
    if len(code) < 8:
        print('Unstable code')  #<--- code is too weak to protect

    elif code[-1] in {'A', 'E', 'I', 'O', 'U'}:
        print('Dark Magic Detected')  #<--- dark magic

    masked_code = code[-4::]

    print(masked_code)

masking_spell(code)
