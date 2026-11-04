import ply.lex as lex
#resultado del analisis
resultado_lexema = []
reservadas = (
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
    'GET',
    'RETURN',
    'VOID',
    'INT',
    'FLOAT_KW',  
    'ENDL',
)
tokens = reservadas + (
    'IDENTIFICADOR',
    'FLOAT',
    'ENTERO',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',
    #CONDICIONALES
    'SI',
    'SINO',
    #CICLOS
    'MIENTRAS',
    'PARA',
    #LOGICA
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    #SIMBOLOS
    'NUMERAL',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    #OTROS
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', #>
    'MAYORIZQ',
)

t_ignore = ' \t'

#REGLAS DE EXPRESION REGULARES
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MINUSMINUS = r'\-\-'
#t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2}|\^)'
t_ASIGNAR = r'='
#EXPRESIONES LOGICAS
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = r';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'
#
def t_INCLUDE(t):
    r'include'
    return t
def t_USING(t):
    r'using'
    return t
def t_NAMESPACE(t):
    r'namespace'
    return t
def t_STD(t):
    r'std'
    return t
def t_COUT(t):
    r'cout'
    return t
def t_CIN(t):
    r'cin'
    return t
def t_GET(t):
    r'get'
    return t
def t_ENDL(t):
    r'endl'
    return t
def t_SINO(t):
    r'sino'
    return t
def t_SI(t):
    r'si'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_VOID(t):
    r'void'
    return t
def t_MIENTRAS(t):
    r'while'
    return t
def t_INT(t):
    r'int'
    return t
def t_FLOAT_KW(t):
    r'float'
    return t
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_]\w*'
    return t
def t_FLOAT(t):
    r'\d+\.\d+'    # Para números decimales como 10.5
    t.value = float(t.value)
    return t
def t_ENTERO(t):
    r'\d+' 
    t.value = int(t.value)
    return t
def t_CADENA(t):
    r'\"([^\"\n]|(\"))*\"'  
    return t
def t_NUMERAL(t):
    r'\#'
    return t
def t_PLUSPLUS(t):
    r'\+\+'
    return t
def t_MENORIGUAL(t):
    r'\<='
    return t
def t_MAYORIGUAL(t):
    r'\>='
    return t
def t_IGUAL(t):
    r'=='
    return t
def t_MAYORDER(t):
    r'<<'
    return t
def t_MAYORIZQ(t):
    r'>>'
    return t
def t_DISTINTO(t):
    r'!='
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("comentario de multiples lineas")


def t_comments_ONELine(t):
    r'\/\/.*'
    print("comentario de una linea")
def t_error(t):
    global resultado_lexema
    estado = "** Token no valido en la linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value), str (t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)
#prueba de ingreso
def prueba(data):
    global resultado_lexema
    analizador = lex.lex()
    analizador.input(data)
    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)    
    return resultado_lexema
#instanciar el analizador
analizador = lex.lex()
    
if __name__ == '__main__':
    print("Hola mundo")
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)