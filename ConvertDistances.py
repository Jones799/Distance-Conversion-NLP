import re
from nltk.stem import WordNetLemmatizer
import decimal





Input = "what is five miles in yards"






wnl = WordNetLemmatizer()


def is_number(x):
    if type(x) == str:
        x = x.replace(',', '')
    try:
        float(x)
    except:
        return False
    return True

def text2int (textnum, numwords={}):
    units = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen',
    ]
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    scales = ['hundred', 'thousand', 'million', 'billion', 'trillion']
    ordinal_words = {'first':1, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    if not numwords:
        numwords['and'] = (1, 0)
        for idx, word in enumerate(units): numwords[word] = (1, idx)
        for idx, word in enumerate(tens): numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ''
    onnumber = False
    lastunit = False
    lastscale = False

    def is_numword(x):
        if is_number(x):
            return True
        if word in numwords:
            return True
        return False

    def from_numword(x):
        if is_number(x):
            scale = 0
            increment = int(x.replace(',', ''))
            return scale, increment
        return numwords[x]

    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
            lastunit = False
            lastscale = False
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if (not is_numword(word)) or (word == 'and' and not lastscale):
                if onnumber:
                    # Flush the current number we are building
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
                lastunit = False
                lastscale = False
            else:
                scale, increment = from_numword(word)
                onnumber = True

                if lastunit and (word not in scales):
                    # Assume this is part of a string of individual numbers to
                    # be flushed, such as a zipcode "one two three four five"
                    curstring += repr(result + current)
                    result = current = 0

                if scale > 1:
                    current = max(1, current)

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0

                lastscale = False
                lastunit = False
                if word in scales:
                    lastscale = True
                elif word in units:
                    lastunit = True

    if onnumber:
        curstring += repr(result + current)

    return curstring
def Convert(string):
    li = list(string.split(" "))
    return li




input1 = text2int(Input)





units = ["inch", "foot", "meter", "millimeter", "yard", "mile", "kilometer", "centimeter",
         "inches", "feet", "meters", "millimeters", "yards", "miles", "kilometers", "centimeters"]

units2 = (Convert(Input))
Input2 = [wnl.lemmatize(i) for i in units2]

input2 = input1.replace('feet', 'foot')


Calculations = {"inch foot":".0833", "inch meter":".0254", "inch millimeter":"25.4", "inch yard":".02778", "inch mile":"63360", "inch kilometer":".0000254000508001016", "inch centimeter":"2.54", "inch feet":"12",
                "foot inch":"12", "foot meter":"0.3048", "foot millimeter":"304.8", "foot yard":"0.333333", "foot mile":"0.000189394", "foot kilometer":"0.000304800097536", "foot centimeter":"30.48",
                "meter inch":"39.37", "meter foot":"3.281", "meter millimeter":"1000", "meter yard":"1.094", "meter mile":"0.000621371", "meter kilometer":"0.001", "meter centimeter":"100", "meter feet":"3.281",
                "millimeter inch":"0.0393701", "millimeter foot":"0.003280841666667", "millimeter yard":"0.0010936138888889999563", "millimeter mile":"0.00000062137", "millimeter kilometer":"0.000001", "millimeter centimeter":"0.1", "millimeter feet":"0.00328084",
                "yard inch":"36", "yard foot":"3", "yard meter":"0.9144", "yard millimeter":"914.4", "yard mile":"0.000568182", "yard kilometer":"0.000914400292608", "yard centimeter":"91.44", "yard feet":"3",
                "mile inch":"63360", "mile foot":"5280", "mile meter":"1609.34", "mile millimeter":"1609339.99997549", "mile yard":"1759.9956255200022497", "mile kilometer":"1.60934", "mile centimeter":"160900", "mile feet":"5280",
                "kilometer inch":"39370.1", "kilometer foot":"3280.84", "kilometer meter":"1000", "kilometer millimeter":"1000000", "kilometer yard":"1093.61", "kilometer mile":"0.621371", "kilometer centimeter":"100000", "kilometer feet":"3280.84",
                "centimeter inch":"0.393701", "centimeter foot":"0.0328084", "centimeter meter":"0.01", "centimeter millimeter":"10", "centimeter yard":"0.0109361", "centimeter mile":"0.0000062137", "centimeter kilometer":"0.00001", "centimeter feet":"0.0328084",
                "feet inch":"12", "feet meter":"0.3048", "feet millimeter":"304.8", "feet yard":"0.333333", "feet mile":"0.000189394", "feet kilometer":"0.0003048", "feet centimeter":"30.48"}

if any(x in Input for x in units):
    AllMatch = [x for x in Input2 if x in units]
    firstWord = next((x for x in Input2 if x in units), "False")
    try:
        LastWord = (AllMatch[1])
        number_first = (firstWord + " " + LastWord)
        number_second = (LastWord + " " + firstWord)
        FirstWordNumber = input2.split(firstWord, 1)[0]
        SecondWordNumber = input2.split(firstWord, 1)[1]
        first = (re.findall('[0-9]+', FirstWordNumber))
        second = (re.findall('[0-9]+', SecondWordNumber))
        first1 = ' '.join(map(str,first))
        second1 = ' '.join(map(str, second))
        if len(first1.split()) > 0:
            result1 = (Calculations[number_first])
            numberone = decimal.Decimal(first1)
            numbertwo = decimal.Decimal(result1)
            answer = numberone * numbertwo
            answerround = "%.1f" % (answer)
            answer1 = str(answerround)

            if 'foot' in LastWord:
                if 'inch' in firstWord:
                    Lastword2 = LastWord.replace('foot', 'feet')
                    beginning = ('there is approximately ' + answer1 + ' ' + Lastword2 + "es" + " in " + first1 + " " + firstWord)
                    print(beginning)
                else:
                    Lastword2 = LastWord.replace('foot', 'feet')
                    beginning = ('there is approximately ' + answer1 + ' ' + Lastword2 + "s" + " in " + first1 + " " + firstWord)
                    print(beginning)
            elif 'foot' in firstWord:
                if 'inch' in LastWord:
                    Lastword2 = firstWord.replace('foot', 'feet')
                    beginning = ('there is approximately ' + answer1 + ' ' + firstWord + " in " + first1 + " " + Lastword2 + "es")
                    print(beginning)
                else:
                    Lastword2 = firstWord.replace('foot', 'feet')
                    beginning = ('there is approximately ' + answer1 + ' ' + firstWord + "s" + " in " + first1 + " " + Lastword2)
                    print(beginning)
            elif 'inch' in LastWord:
                beginning = ('there is approximately ' + answer1 + ' ' + LastWord + "s" + " in " + first1 + " " + firstWord + "es")
                print(beginning)
            elif 'inch' in firstWord:
                beginning = ('there is approximately ' + answer1 + ' ' + LastWord + "es" + " in " + first1 + " " + firstWord)
                print(beginning)
            else:
                beginning = ('there is approximately ' + answer1 + ' ' + LastWord + "s" + " in " + first1 + " " + firstWord + "s")
                print(beginning)

        if len(second1.split()) > 0:
            result1 = (Calculations[number_second])
            numberone = decimal.Decimal(second1)
            numbertwo = decimal.Decimal(result1)
            answer = numberone * numbertwo
            answerround = "%.1f" % (answer)
            answer1 = str(answerround)
            if 'foot' in LastWord:
                if 'inch' in firstWord:
                    Lastword2 = LastWord.replace('foot', 'feet')
                    beginning = ('there is approximately ' + answer1 + ' ' + firstWord + "es" + " in " + second1 + " " + Lastword2)
                    print(beginning)
                else:
                    Lastword2 = LastWord.replace('foot', 'feet')
                    beginning = ('there is approximately ' + answer1 + ' ' + firstWord + "s" + " in " + second1 + " " + Lastword2)
                    print(beginning)
            elif 'foot' in firstWord:
                if 'inch' in LastWord:
                    Lastword2 = firstWord.replace('foot', 'feet')
                    beginning = ('there is approximately ' + answer1 + ' ' + Lastword2 + " in " + second1 + " " + LastWord+ "es")
                    print(beginning)
                else:
                    Lastword2 = firstWord.replace('foot', 'feet')
                    beginning = ('there is approximately ' + answer1 + ' ' + Lastword2 + "s" + " in " + second1 + " " + LastWord)
                    print(beginning)
            elif 'inch' in LastWord:
                beginning = ('there is approximately ' + answer1 + ' ' + firstWord + "s" + " in " + second1 + " " + LastWord + "es")
                print(beginning)
            elif 'inch' in firstWord:
                beginning = ('there is approximately ' + answer1 + ' ' + firstWord + "es" + " in " + second1 + " " + LastWord)
                print(beginning)
            else:
                beginning = ('there is approximately ' + answer1 + ' ' + firstWord + "s" + " in " + second1 + " " + LastWord + "s")
                print(beginning)

    except IndexError:
        pass

    #result = (Calculations[firstWord])
else:
    print("nope")

#From Cup to Gallon Devide cup by 16 for gallon

