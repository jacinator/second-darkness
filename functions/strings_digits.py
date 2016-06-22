def EvenDivide(amount, divider):
    while amount % divider != 0:
        amount -= 1
    amount = amount / divider
    return amount

def LengthManager(string, length):
    string_length = len(string)
    if string_length > length:
        string = string[: length - 3].__add__('...')
    else:
        addition = length - string_length
        for x in range(addition):
            string = string + ' '
    return string

def capfirst(phrase):
    try:
        phrase = phrase[0].upper() + phrase[1:]
    except IndexError:
        phrase = phrase.upper()
    return phrase

def NumberSuffix(number):
    number = str(number)
    if number[-1:] == '1':
        suffix_added = number.__add__('st')
    elif number[-1:] == '2':
        suffix_added = number.__add__('nd')
    elif number[-1:] == '3':
        suffix_added = number.__add__('rd')
    else:
        suffix_added = number.__add__('th')
    return suffix_added

def space(text, after = True, before = False):
    if before == True:
        text = ' '.__add__(text)
    if after == True:
        text = text.__add__(' ')
    return text

def idnumber(number):
    zeroes = 3 - len(str(number))
    for X in range(zeroes):
        number = '0' + str(number)
    number = '#' + number
    return number
    
def pluralize(word, count):
    if count > 1:
        return word.__add__('s')
    else:
        return word

def SearchCapitalization(string):
    if string[:4] == 'find':
        string = string[5:]
    elif string[:6] == 'search':
        string = string[7:]
    Space = string.find(' ')
    BeforeSpace = string[:Space + 1]
    AfterSpace = string[Space + 1:]
    String = BeforeSpace.capitalize() + AfterSpace.capitalize()
    return String