package solver_test

import (
	"slices"
	"solver/errs"
	"solver/solver"
	"testing"
)

type equation struct {
	a float64
	b float64
	c float64

	roots []solver.Root
	err   error
}

var testTable = []equation{
	{a: 0, b: 0, c: 0, roots: nil, err: errs.ErrBadSolutions()},
	{a: 5, b: -3, c: -5, roots: []solver.Root{1.1593233590724614, -1.1593233590724614, nil, nil}, err: nil},
	{a: 0, b: 0, c: 1, roots: nil, err: errs.ErrNoSolutions()},
}

func TestSolver(t *testing.T) {
	for _, val := range testTable {
		roots, err := solver.NewSolver().SolveEquation(val.a, val.b, val.c)

		if !slices.Equal(roots, val.roots) || err != val.err {
			t.Errorf("TEST FAILED: %v != %v or %v != %v\n", roots, val.roots, err, val.err)
		}
	}
}
