package main

import (
	"fmt"
	r "solver/reader"
	s "solver/solver"
)

const (
	A = iota
	B
	C
)

func main() {
	reader := r.NewReader()
	coeffs := reader.ReadInputCoeffs(reader.ReadCmdArgs())

	solver := s.NewSolver()
	roots, err := solver.SolveEquation(coeffs[A], coeffs[B], coeffs[C])
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(roots)
	}
}
