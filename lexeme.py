import re

keywords = ["abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class",
		"const", "continue", "default", "double", "do", "else", "enum", "extends", "false", "final", "finally",
		"float", "for", "goto", "if", "implements", "import", "instanceof", "int", "interface", "long",
		"native", "new", "null", "package", "private", "protected", "public", "return", "short", "static",
		"strictfp", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "true", "try",
		"void", "volatile", "while" ]

arithmetic_Operators = ["+", "-", "*", "/", "%" ]

comparison_Operators = ["==", "!=", ">", ">=", "<", "<=" ]

logical_Operators = [ "&&", "||", "!" ]

punctuations = [",", ".", ";", "\"", "'", "(", ")", "{", "}", "[", "]", "=" ]

filename = input('Please enter a Java file name: ')
counterKey, counterArithmetic, counterComparison, counterLogical, counterPunctuations, counterDouble, counterInteger, counterOther = 0, 0, 0, 0, 0,0,0,0
keywordSet, logicalOpSet, arithmeticOpSet, comparisonOpSet, punctuationSet, integerLiteralsSet, doubleLiteralsSet, otherSet = set(),set(),set(),set(),set(),set(),set(),set()
fileType = filename.split(".").pop()
if fileType == 'java':
    with open(filename, "r") as file:
        file_data = file.read()
        numbers = re.findall(r'\d+(?:\.\d+)?', file_data) #https://stackoverflow.com/questions/26314092/what-does-in-a-regular-expression-mean#:~:text=It%20means%20that%20it%20is%20not%20capturing%20group.
        lexemes = re.findall(r'[a-zA-z]+|[^\w\s]+|!=|<=|>=|\|\||&&|==', file_data) 
        for lexeme in lexemes:
            if lexeme in keywords:
                if lexeme not in keywordSet:
                    counterKey += 1
                    keywordSet.add(lexeme)
            elif lexeme in arithmetic_Operators:
                if lexeme not in arithmeticOpSet:
                    counterArithmetic += 1
                    arithmeticOpSet.add(lexeme)
            elif lexeme in comparison_Operators:
                if lexeme not in comparisonOpSet:
                    counterComparison += 1
                    comparisonOpSet.add(lexeme)
            elif lexeme in logical_Operators:
                if lexeme not in logicalOpSet:
                    counterLogical += 1
                    logicalOpSet.add(lexeme)
            elif lexeme in punctuations:
                if lexeme not in punctuationSet:
                    counterPunctuations += 1
                    punctuationSet.add(lexeme)
            else:
                if lexeme not in otherSet and re.match(r'\w+',lexeme):
                    counterOther += 1
                    otherSet.add(lexeme)
        for num in numbers:
            if num.isdigit():
                if lexeme not in integerLiteralsSet:
                    int_num = int(num)
                    counterInteger += 1
                    integerLiteralsSet.add(int_num)
            else:
                if lexeme not in doubleLiteralsSet:
                    double_num = float(num)
                    counterDouble += 1
                    doubleLiteralsSet.add(double_num)
        
        if counterKey == 0:
            print('Keywords: 0 : { } ')
        else:
            print('Keywords: ', counterKey,' : ',keywordSet)
        if counterArithmetic == 0:
            print('Arithmetic Operators: 0 : { } ')
        else:
            print('Arithmetic Operators: ', counterArithmetic,' : ',arithmeticOpSet)
        if counterComparison == 0:
            print('Comparison Operators: 0 : { } ')
        else:
            print('Comparison Operators: ', counterComparison, ' : ', comparisonOpSet)
        if counterLogical == 0:
            print('Logical Operators: 0 : { } ')
        else:
            print('Logical Operators: ', counterLogical, ' : ', logicalOpSet)
        if counterPunctuations == 0:
            print('Punctuations: 0 : { } ')
        else:
            print('Punctuations: ', counterPunctuations, ' : ', punctuationSet)
        if counterDouble == 0:
            print('Double Literals: 0 : { }')
        else:
             print('Double Literals: ', counterDouble, ' : ', doubleLiteralsSet)
        if counterInteger == 0:
            print('Integer Literals: 0 : { }')
        else:
            print('Integer Literals: ', counterInteger, ' : ', integerLiteralsSet)
        if counterOther == 0:
            print('Other Lexemes: 0 : { }')
        else:
            print('Other Lexemes: ', counterOther, ' : ', otherSet)
else:
    print("Wrong file type.")
