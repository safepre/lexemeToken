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
counterKey, counterArithmetic, counterComparison, counterLogical, counterPunctuations = 0, 0, 0, 0, 0
no_Duplicates = set()
fileType = filename.split(".").pop()

if fileType == 'java':
    with open(filename, "r") as file:
        file_data = file.read()
        lexemes = re.findall(r"\w+|[^\w\s]+|!=|<=|>=|\|\||&&|==", file_data)
        for lexeme in lexemes:
            if lexeme in keywords:
                counterKey += 1
                if lexeme not in no_Duplicates:
                    no_Duplicates.add(lexeme)
                    print('Keyword: ' + lexeme)
            if lexeme in arithmetic_Operators:
                counterArithmetic += 1
                if lexeme not in no_Duplicates:
                    no_Duplicates.add(lexeme)
                    print('Arithmetic Operator: ' + lexeme)
            if lexeme in comparison_Operators:
                counterComparison += 1
                if lexeme not in no_Duplicates:
                    no_Duplicates.add(lexeme)
                    print('Comparison Operator: ' + lexeme)
            if lexeme in logical_Operators:
                counterLogical += 1
                if lexeme not in no_Duplicates:
                    no_Duplicates.add(lexeme)
                    print('Logical Operator: ' + lexeme)
            if lexeme in punctuations:
                counterPunctuations += 1
                if lexeme not in no_Duplicates:
                    no_Duplicates.add(lexeme)
                    print('Punctuation: ' + lexeme)
        if counterKey == 0:
            print('Keyword is { } ')
        if counterArithmetic == 0:
            print('Arithmetic Operator is { } ')
        if counterComparison == 0:
            print('Comparison Operator is { } ')
        if counterLogical == 0:
            print('Logical Operator is { } ')
        if counterPunctuations == 0:
            print('Punctuations is { } ')
else:
    print("Wrong file type.")
