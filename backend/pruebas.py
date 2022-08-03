from interprete.extra.Ast import Ast
from interprete.analizador.parser import parser

prueba = 'let xdsaf : i64 = 5.5*5; let mut x = true;';
resultado: Ast = parser.parse(prueba);