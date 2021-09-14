operators = { '=': '=','+': '+', '<=': '<=', '==': '==', '<<': '<<', '>>': '>>'}
optr_keys = operators.keys()

keyword = {'return' : 'return', 'using': 'using', 'namespace': 'namespace', 'std': 'std', 'for': 'for', 'while': 'while', 'cout': 'cout', 'int': 'int', 'char': 'char'}
keyword_keys = keyword.keys()

delimiter = {';':';'}
delimiter_keys = delimiter.keys()

non_identifiers = {'_','`','~','!','@','#','$','%','^','&','*','(',')','|','"',':',';','{'
,'}','[',']','?'}

# Flags
dataFlag = False
output = open("output_tokens_887111342.txt","w")
output.write("token               lexemes\n_____________________________\n")

def lexer(f, program):   
    f = open("input_sourcetext-1.txt", "r")
    count = 0
    dataFlag = False

    for line in program:
        count = count+1
        print ("Line #",count,"\n",line)
        
        lexemes = line.split()
        # list_cycle = itertools.cycle(lexemes)
        # next(list_cycle)
        print ("Lexemes are: ", lexemes, "\n" )
        print ("Line #", count, 'properties: ')
        for index, lexeme in enumerate(lexemes):
            if '\n' in lexeme:
                position = lexeme.find('\n')
                lexeme=lexeme[:position]
            if lexeme in optr_keys:
                print("Operator is: ", operators[lexeme])
                output.write("Operator                " + operators[lexeme] + '\n')
            if lexeme in keyword_keys:
                print("Keyword is: ", keyword[lexeme])
                output.write("Keyword               " + keyword[lexeme] + '\n')
            if lexeme[-1] == ';':
                if(lexeme.split(';')[0].isnumeric()):
                    print("Number is: ", int(lexeme.split(';')[0]))
                    output.write("Number                  " + (lexeme.split(';')[0]) + '\n')
                    print("Symbol is: ", lexeme[-1])
                    output.write("Symbol                  " + lexeme[-1] + '\n')
            if lexeme in non_identifiers:
                print("Symbol is: ", lexeme)
                output.write("Symbol                  " + lexeme + '\n')

            if len(lexeme) == 1:
                if lexeme.isalpha():
                    print("Identifier is: ", lexeme)
                    output.write("Identifier              " + lexeme + '\n')
                    
            if lexeme[0] == '"':
                string = ''
                while(lexeme[-2] != '"'):
                    print(lexeme)
                    print(lexeme[index+1])
                    string = string + lexeme
                    string = string + ' ' + lexemes[index+1]
                    lexeme = lexemes[index+1]
                print("String is: ", string.split(";"))
                output.write("String              " + string + '\n')
                print("Symbol is: ", lexeme[-1])
                output.write("Symbol                  " + lexeme[-1] + '\n')

        f.close()

def main():
    f = open("input_sourcetext-1.txt", "r")
    i = f.read()
    program = i.split('\n')
    lexer(f, program)

if __name__ == "__main__":
    main()

