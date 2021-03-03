from sympy import Basic
from sympy.matrices.expressions import funcmatrix

from sympy.matrices.expressions.matexpr import MatrixExpr

class Conjugate(MatrixExpr):

    is_Conjugate = True

    def doit(self, **hints):
        arg = self.arg
        if hints.get('deep', True) and isinstance(arg, Basic):
            return conjugate(arg.doit(**hints))
        else:
            return conjugate(self.arg)


    @property
    def arg(self):
        return self.args[0]

    def _eval_conjugate(self):
        return self.arg

    def _eval_complex_conjugate(self):
        z = as_real_imag(self) #func in funcmatrix.py
        return complex(z[0], -z[1])

    def conjugate(self):
        return self.map(_eval_complex_conjugate(self.arg))

##Failing tests
##sympy/core/tests/test_args.py[973]
