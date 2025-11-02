from typing import TypeAlias, Any, Final

Coeffs: TypeAlias = tuple[float | None, float | None, float | None]


class Solver:
    __slots__ = ('__a', '__b', '__c')

    def __init__(self, coeffs: Coeffs) -> None:
        if any(coeff is None for coeff in coeffs):
            raise ValueError

        self.__a: float = coeffs[0] if coeffs[0] else 0
        self.__b: float = coeffs[1] if coeffs[1] else 0
        self.__c: float = coeffs[2] if coeffs[2] else 0

    @property
    def coeffs(self) -> Coeffs:
        return (self.__a, self.__b, self.__c)

    @coeffs.setter
    def Coeffs(self, coeffs: Coeffs) -> None:
        self.__a = coeffs[0] if coeffs[0] else 0
        self.__b = coeffs[1] if coeffs[1] else 0
        self.__c = coeffs[2] if coeffs[2] else 0

    def SolveEquation(self) -> tuple[float | None, ...]:
        if self.__a == 0 and self.__b == 0 and self.__c == 0:
            raise BadSolutionsError(
                'Нет конкретных решений для этого уравнения')

        if self.__a == 0:
            return self.__SolveQuadratic()

        discr: float = self.__CalculateDiscr()
        if discr < 0:
            return (None, None, None, None)

        return Solver.__ExtractRoots(self.__CalculateRoots(discr))

    def __SolveQuadratic(self) -> tuple[float | None, ...]:
        solution: float = 0
        try:
            solution = -self.__c / self.__b
        except ZeroDivisionError:
            return (None, None, None, None)
        if solution < 0:
            return (None, None, None, None)

        return solution ** 0.5, -solution**0.5

    @staticmethod
    def __ExtractRoots(squaredRoots: tuple[float, float]) -> tuple[float | None, ...]:
        first: float | None = squaredRoots[0] ** 0.5 if squaredRoots[0] > 0 else None
        second: float | None = squaredRoots[1] ** 0.5 if squaredRoots[1] > 0 else None

        return (first, -first if first else None, second, -second if second else None)

    def __CalculateRoots(self, discr: float) -> tuple[float, float]:
        return ((-self.__b + discr**0.5) / (2 * self.__a), (-self.__b - discr**0.5) / (2 * self.__a))

    def __CalculateDiscr(self) -> float:
        return (self.__b ** 2 - 4 * self.__a * self.__c)


class BadSolutionsError(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            self.__message: Any = args[0]
        else:
            self.__message: Any = None

    def __str__(self) -> str:
        if self.__message:
            return self.__message

        return 'Bad solutions in this equation'
