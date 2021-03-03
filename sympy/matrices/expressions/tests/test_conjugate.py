from sympy.functions import conjugate, conjugate, transpose
from sympy.matrices.expressions import MatrixSymbol, trace, Transpose
from sympy.matrices import eye, Matrix
from sympy import symbols, S
from sympy import refine, Q

n, m, l, k, p = symbols('n m l k p', integer=True)
A = MatrixSymbol('A', n, m)
B = MatrixSymbol('B', m, l)
C = MatrixSymbol('C', n, n)


def test_conjugate():
    Sq = MatrixSymbol('Sq', n, n)

    assert Conjugate(A).shape == (m, n)
    assert Conjugate(A*B).shape == (l, n)
    assert conjugate(Conjugate(A)) == A
    assert isinstance(Conjugate(Conjugate(A)), Conjugate)

    # assert conjugate(Conjugate(A)) == Transpose(A)
    # assert transpose(Conjugate(A)) == Conjugate(Transpose(A))

    assert Conjugate(eye(3)).doit() == eye(3)

    assert Conjugate(S(5)).doit() == S(5)

    assert Conjugate(Matrix([[1, 2], [3, 4]])).doit() == Matrix([[1, 3], [2, 4]])

    assert conjugate(trace(Sq)) == conjugate(trace(Sq))
    assert trace(conjugate(Sq)) == conjugate(trace(Sq))

    assert Conjugate(Sq)[0, 1] == conjugate(Sq[1, 0])

    assert Conjugate(A*B).doit() == Conjugate(B) * Conjugate(A)
