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
        lexemes = re.findall(r'\w+|[^\w\s]+|!=|<=|>=|\|\||&&|==', file_data) 
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
            elif re.match(r'\d+',lexeme):
                if punctuations[1] in lexeme:
                    if lexeme not in doubleLiteralsSet:
                        counterDouble += 1
                        doubleLiteralsSet.add(lexeme)
                else:
                    if lexeme not in integerLiteralsSet:
                        counterInteger += 1
                        integerLiteralsSet.add(lexeme)
            else:
                if lexeme not in otherSet:
                    counterOther += 1
                    otherSet.add(lexeme)
        
        if counterKey == 0:
            print('Keywords: { } ')
        else:
            print('Keywords: ', counterKey,' : ',keywordSet)
        if counterArithmetic == 0:
            print('Arithmetic Operators: { } ')
        else:
            print('Arithmetic Operators: ', counterArithmetic,' : ',arithmeticOpSet)
        if counterComparison == 0:
            print('Comparison Operators: { } ')
        else:
            print('Comparison Operators: ', counterComparison, ' : ', comparisonOpSet)
        if counterLogical == 0:
            print('Logical Operators: { } ')
        else:
            print('Logical Operators: ', counterLogical, ' : ', logicalOpSet)
        if counterPunctuations == 0:
            print('Punctuations: { } ')
        else:
            print('Punctuations: ', counterPunctuations, ' : ', punctuationSet)
        if counterDouble == 0:
            print('Double Literals: { }')
        else:
             print('Double Literals: ', counterDouble, ' : ', doubleLiteralsSet)
        if counterInteger == 0:
            print('Integer Literals: { }')
        else:
            print('Integer Literals: ', counterInteger, ' : ', integerLiteralsSet)
        if counterOther == 0:
            print('Other Lexemes: { }')
        else:
            print('Other Lexemes: ', counterOther, ' : ', otherSet)
else:
    print("Wrong file type.")
