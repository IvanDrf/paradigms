from solver import parser, reader, solver

if __name__ == '__main__':
    argParser: parser.ArgParser = parser.ArgParser()
    coeffs: solver.Coeffs = argParser.ParseCoeffs()

    coeffReader: reader.Reader = reader.Reader(coeffs)
    coeffs = coeffReader.Read()

    solv: solver.Solver = solver.Solver(coeffs)

    try:
        print(solv.SolveEquation())
    except solver.BadSolutionsError as e:
        print(e)
