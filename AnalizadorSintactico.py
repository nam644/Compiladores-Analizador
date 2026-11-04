import ply.yacc as yacc
from AnalizadorLexico import tokens
from AnalizadorLexico import analizador
resultado_gramatica = []
precedence = (
    ('right', 'ASIGNAR'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'IGUAL', 'DISTINTO'),
    ('left', 'MENORQUE', 'MAYORQUE', 'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV', 'MODULO'),
    ('right', 'POTENCIA'),
    ('right', 'UMINUS'),
)
nombres = {}
def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    t[0] = t[3]
def p_declaracion_expresion(t):
    'declaracion : expresion'
    t[0] = t[1]
def p_expresiones_operaciones(t):
    """
    expresion : expresion SUMA expresion
              | expresion RESTA expresion
              | expresion MULT expresion
              | expresion DIV expresion
              | expresion POTENCIA expresion
              | expresion MODULO expresion
    """
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        t[0] = t[1] ** t[3]
def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]
def p_expresion_grupo(t):
    """
    expresion : PARIZQ expresion PARDER
              | LLAIZQ expresion LLADER
              | CORIZQ expresion CORDER
    """
    t[0] = t[2]
def p_expresion_logicas(t):
    """
    expresion : expresion MENORQUE expresion
              | expresion MAYORQUE expresion
              | expresion MENORIGUAL expresion
              | expresion MAYORIGUAL expresion
              | expresion IGUAL expresion
              | expresion DISTINTO expresion
    """
    if t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '<=':
        t[0] = t[1] <= t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]
    elif t[2] == '==':
        t[0] = t[1] == t[3]
    elif t[2] == '!=':
        t[0] = t[1] != t[3]
def p_expresion_booleana(t):
    """
    expresion : expresion AND expresion
              | expresion OR expresion
    """
    if t[2] == '&&':
        t[0] = t[1] and t[3]
    elif t[2] == '||':
        t[0] = t[1] or t[3]
def p_expresion_not(t):
    'expresion : NOT expresion %prec NOT'
    t[0] = not t[2]
def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]
def p_expresion_cadena(t):
    'expresion : COMDOB expresion COMDOB'
    t[0] = t[2]
def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("nombre desconocido", t[1])
        t[0] = 0
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "error sintactico de tipo {} en el valor {}".format(
            str(t.type),
            str(t.value)
        )
        print(resultado)
    else:
        resultado = "error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)
parser = yacc.yacc()
def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    for item in data.splitlines():
        if item:
            gram = parser.parse(item, lexer=analizador)
            if gram is not None:
                resultado_gramatica.append(str(gram))
        else:
            print("data vacia")
    print("result: ", resultado_gramatica)
    return resultado_gramatica
if __name__ == '__main__':
    while True:
        try:
            s = input('ingresa datos >>')
        except EOFError:
            break 
        if not s: continue




        prueba_sintactica(s)