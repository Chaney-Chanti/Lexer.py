import re
operators = { '=': 'Assig_Op','+': 'Add_Op', '<=': 'GTOE_Op'}
optr_keys = operators.keys()

comments = {r'//' : 'Single Line Comment'}
comment_keys = comments.keys()

datatype = {'int': 'Integer', 'char': 'Character'}
datatype_keys = datatype.keys()

keyword = {'return' : 'keyword that returns a value from a block'}
keyword_keys = keyword.keys()

delimiter = {';':'terminator symbol semicolon (;)'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'Blocked Statement Body Open', '}':'Blocked Statement Body Closed'}
block_keys = blocks.keys()

token = ['keyword', 'identifier', 'symbol', 'operator', '']

non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

numerals = ['0','1','2','3','4','5','6','7','8','9','10']

# Flags
dataFlag = False
output = open("output_tokens_887111342.txt","w")
output.write("tokens               lexemes\n_____________________________\n")

def lexer(f, program):   
    f = open("input_sourcetext-1.txt", "r")
    count = 0
    dataFlag = False

    for line in program:
        count = count+1
        print ("Line #",count,"\n",line)
        
        
        lexemes = line.split()
        print ("Lexemes are", lexemes)
        print ("Line #", count, 'properties \n')
        for token in lexemes:
            if '\r' in token:
                position = token.find('\r')
                token=token[:position]
            if token in block_keys:
                print(blocks[token])
                # output.write("symbol               " + blocks[token])
            if token in optr_keys:
                print("Operator is: ", operators[token])
                output.write("Operator               " + operators[token] + '\n')
            if '()' in token:
                print("Function named", token)
            if token in comment_keys:
                print ("Comment Type: ", comments[token])

            if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
                print("Identifier: ", token)
                output.write("Identifier               " + token + '\n')
            if token in datatype_keys:
                print("type is: ", datatype[token])
                output.write("Keyword               " + datatype[token] + '\n')
                dataFlag = True

            if token in keyword_keys:
                print(keyword[token])   

            if token in delimiter:
                print("Delimiter" , delimiter[token])
            if '#' in token:
                match = f.search(r'#\w+', token)
                print("Header", match.group())
            if token in numerals:
                print(token,type(int(token)))

        dataFlag = False   
        f.close()


def main():
    f = open("input_sourcetext-1.txt", "r")
    i = f.read()
    program = i.split('\n')
    lexer(f, program)

if __name__ == "__main__":
    main()

