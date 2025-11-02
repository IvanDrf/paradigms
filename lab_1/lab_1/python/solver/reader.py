from typing import Final, TypeAlias
Coeffs :TypeAlias = tuple[float | None,float | None,float | None]

class Const:
    A: Final = 0
    B: Final = 1
    C: Final = 2

class Reader:
    __slots__=('__coeffs')

    def __init__(self, coeffs :Coeffs) -> None:
        self.__coeffs :Coeffs = coeffs

    def Read(self) -> Coeffs:
        coeffs :list[float] = [0,0,0]

        for i, coeff in enumerate(self.__coeffs):
            coeffs[i] = Reader.__InputCoeff(coeff=coeff, index=i)

        return Coeffs(coeffs)

    @staticmethod
    def __InputCoeff(*,coeff : float | None, index: int) -> float:
        inputStr :str = Reader.__CreateInputStr(index=index)

        while coeff is None:
            try:
                coeff = float(input(inputStr))
            except:
                print('Коэффициент должен быть числом')

        return coeff

    @staticmethod
    def __CreateInputStr(*, index : int) -> str:
        match index:
            case Const.A:
                return 'Введите коэффициент A: '
            case Const.B:
                return 'Введите коэффициент B: '
            case Const.C:
                return 'Введите коэффициент C: '

        return ''
