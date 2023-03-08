import re

keywords = ["abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class",
            "const", "continue", "default", "double", "do", "else", "enum", "extends", "false", "final", "finally",
            "float", "for", "goto", "if", "implements", "import", "instanceof", "int", "interface", "long",
            "native", "new", "null", "package", "private", "protected", "public", "return", "short", "static",
            "strictfp", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "true", "try",
            "void", "volatile", "while"]
arithmetic_Operators = ["+", "-", "*", "/", "%"]
comparison_Operators = ["==", "!=", ">", ">=", "<", "<="]
logical_Operators = ["&&", "||", "!"]
punctuations = [",", ".", ";", "\"", "'", "(", ")", "{", "}", "[", "]", "="]

filename = input('Please enter a Java file name: ')
counter_1, counter_2, counter_3, counter_4, counter_5 = 0, 0, 0, 0, 0
avoid_duplicates = set()
file_extension = filename.split(".").pop()

if file_extension == 'java':
    with open(filename, "r") as file:
        file_data = file.read()
        lexemes = re.findall(r"\w+|[^\w\s]+|(?:!=|<=|>=|\|\||&&|==)", file_data)
        for lexeme in lexemes:
            if lexeme in keywords:
                if lexeme not in avoid_duplicates:
                    avoid_duplicates.add(lexeme)
                    print("Keyword: " + lexeme)
            if lexeme in arithmetic_Operators:
                if lexeme not in avoid_duplicates:
                    avoid_duplicates.add(lexeme)
                    print("Arithmetic Operator: " + lexeme)
            if lexeme in comparison_Operators:
                if lexeme not in avoid_duplicates:
                    avoid_duplicates.add(lexeme)
                    print("Comparison Operator: " + lexeme)
            if lexeme in logical_Operators:
                if lexeme not in avoid_duplicates:
                    avoid_duplicates.add(lexeme)
                    print("Logical Operator: " + lexeme)
            if lexeme in punctuations:
                if lexeme not in avoid_duplicates:
                    avoid_duplicates.add(lexeme)
                    print("Punctuation: " + lexeme)
else:
    print("Wrong file type.")
