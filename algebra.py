from sympy import *
from sympy.core import symbol

x = symbols('x')
y = symbols('y')

eq1 = Eq(5*x, 15)
print(str(solve((eq1),(x))).replace(',','='))