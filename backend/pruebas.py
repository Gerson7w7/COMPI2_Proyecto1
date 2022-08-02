from interprete.extra.Ast import Ast
from interprete.analizador.parser import parser

prueba = 'let mut x = 5*5;';
resultado: Ast = parser.parse(prueba);