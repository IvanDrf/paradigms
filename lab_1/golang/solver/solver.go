package solver

import (
	"math"
	"solver/errs"
)

type Root interface {
	float64 | any
}

type Solver interface {
	SolveEquation(a, b, c float64) ([]Root, error)
}

type solver struct {
	a float64
	b float64
	c float64
}

func NewSolver() Solver {
	return solver{}
}

func (s solver) SolveEquation(a, b, c float64) ([]Root, error) {
	s.a = a
	s.b = b
	s.c = c

	if s.a == 0 && s.b == 0 && s.c == 0 {
		return nil, errs.ErrBadSolutions()
	}

	if s.a == 0 {
		return s.solveQuadratic()
	}

	discr := s.calculateDiscr()
	if discr < 0 {
		return nil, errs.ErrNoSolutions()
	}

	return s.extractRoots(s.calculateRoots(discr))

}

func (s solver) solveQuadratic() ([]Root, error) {
	if s.b == 0 {
		return nil, errs.ErrNoSolutions()
	}

	solution := -s.c / s.b
	if solution < 0 {
		return nil, errs.ErrNoSolutions()
	}

	return []Root{math.Pow(solution, 0.5), -math.Pow(solution, 0.5)}, nil
}

func (s solver) calculateDiscr() float64 {
	return s.b*s.b - 4*s.a*s.c
}

func (s solver) calculateRoots(discr float64) (float64, float64) {
	return (-s.b + math.Pow(discr, 0.5)) / (2 * s.a), (-s.b - math.Pow(discr, 0.5)) / (2 * s.a)
}

func (s solver) extractRoots(first, second float64) ([]Root, error) {
	roots := make([]Root, 4)

	if first > 0 {
		first = math.Pow(first, 0.5)
		roots[0], roots[1] = first, -first
	} else {
		roots[0], roots[1] = nil, nil
	}

	if second > 0 {
		second = math.Pow(second, 0.5)
		roots[2], roots[3] = second, -second
	} else {
		roots[2], roots[3] = nil, nil
	}

	return roots, nil
}
