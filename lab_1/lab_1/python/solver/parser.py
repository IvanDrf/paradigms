import sys
from typing import TypeAlias

Coeffs :TypeAlias = tuple[float | None,float | None,float | None]

class ArgParser:
    __slots__=('__args')

    def __init__(self) -> None:
        self.__args :list[str] = sys.argv[1:]

    def ParseCoeffs(self) -> Coeffs:
        coeffs: list[float | None] =  list(ArgParser.__ConvertToNumber(value) for value in self.__args)
        while len(coeffs) < 3:
            coeffs.append(None)

        return Coeffs(coeffs[:3])


    @staticmethod
    def __ConvertToNumber(value :str) -> float | None:
        try:
            return float(value)
        except:
            return None
