import pytest
from python.solver import Solver,  Coeffs, BadSolutionsError


@pytest.fixture
def EmptyCoeffs() -> Coeffs:
    return (0, 0, 0)


@pytest.fixture
def NoSolutionsCoeffs() -> Coeffs:
    return (0, 0, 1)


@pytest.fixture
def NormalCoeffs() -> Coeffs:
    return (5, -3, -5)


def test_Solver(EmptyCoeffs, NoSolutionsCoeffs, NormalCoeffs):
    slv: Solver = Solver(EmptyCoeffs)
    try:
        slv.SolveEquation()
    except BadSolutionsError as e:
        assert e.__str__() == 'Нет конкретных решений для этого уравнения'

    slv.Coeffs = NoSolutionsCoeffs
    assert slv.SolveEquation() == (None, None, None, None)

    slv.Coeffs = NormalCoeffs
    assert slv.SolveEquation() == (1.1593233590724614, -1.1593233590724614, None, None)
