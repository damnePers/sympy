from sympy import Basic, I
from sympy.functions import adjoint, transpose, conjugate
from sympy.matrices.expressions.matexpr import MatrixExpr


class Conjugate(MatrixExpr):
    """
    Description

    """

    def doit(self, **hints):
        arg = self.arg
        if hints.get('deep', True) and isinstance(arg, Basic):
            arg = arg.doit(**hints)
        else:
            return conjugate(self.arg)

    @property
    def arg(self):
        return self.args[0]

    @property
    def shape(self):
        return self.arg.shape[::-1]

    def _entry(self, i, j, **kwargs):
        return adjoint(self.arg._entry(j, i, **kwargs))

    def _eval_transpose(self):
        return adjoint(self)

    def _eval_adjoint(self):
        return transpose(self)

    def _eval_conjugate(self):
        return self.arg

    def _eval_trace(self):
        from sympy.matrices.expressions.trace import Trace
        return transpose(Trace(self.arg))
