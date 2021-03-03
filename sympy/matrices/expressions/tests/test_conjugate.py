from sympy.core import symbols, S
from sympy.functions import adjoint, conjugate, transpose
from sympy.matrices.expressions import MatrixSymbol, Adjoint, trace, Transpose, Conjugate
from sympy.matrices import eye, Matrix

n, m, l, k, p = symbols('n m l k p', integer=True)
A = MatrixSymbol('A', n, m)
B = MatrixSymbol('B', m, l)
C = MatrixSymbol('C', n, n)

def test_conjugate():
    Sq = MatrixSymbol('Sq', n, n)

    assert Conjugate(A) == conjugate(A)
