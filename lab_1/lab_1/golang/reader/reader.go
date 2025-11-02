package reader

import (
	"fmt"
	"os"
	"strconv"
)

type Coeff interface {
	interface{} | float64
}

type Reader interface {
	ReadCmdArgs() []Coeff
	ReadInputCoeffs(coeffs []Coeff) []float64
}

type reader struct {
}

func NewReader() Reader {
	return reader{}
}

func (r reader) ReadCmdArgs() []Coeff {
	if len(os.Args) < 2 {
		return []Coeff{nil, nil, nil}
	}

	args := os.Args[1:]

	coeffs := make([]Coeff, 0, 3)
	for _, str := range args {
		coeff, err := strconv.ParseFloat(str, 64)
		if err != nil {
			coeffs = append(coeffs, nil)
		} else {
			coeffs = append(coeffs, coeff)
		}
	}

	for len(coeffs) < 3 {
		coeffs = append(coeffs, nil)
	}

	return coeffs

}

func (r reader) ReadInputCoeffs(coeffs []Coeff) []float64 {
	res := make([]float64, 0, 3)

	for i, val := range coeffs {
		if val == nil {
			res = append(res, inputCoeff(val, i))
		} else {
			res = append(res, val.(float64))
		}
	}

	return res
}

func inputCoeff(val Coeff, i int) float64 {
	if val != nil {
		return val.(float64)
	}

	input := createInputStr(i)
	number := 0.0

	for val == nil {
		fmt.Print(input)
		_, err := fmt.Scan(&number)
		if err != nil {
			continue
		}

		val = number
	}

	return val.(float64)

}

const (
	a = iota
	b
	c
)

func createInputStr(i int) string {
	switch i {
	case a:
		return "Введите коэффициент A: "

	case b:
		return "Введите коэффициент B: "

	case c:
		return "Введите коэффициент C: "
	}

	return ""
}
