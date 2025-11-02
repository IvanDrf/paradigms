package errs

import "fmt"

type Err struct {
	message string
}

func (e Err) Error() string {
	return fmt.Sprintf("message: %s", e.message)
}

func ErrBadSolutions() error {
	return Err{message: "нет конкретных решений для данного уравнения"}
}

func ErrNoSolutions() error {
	return Err{message: "уравнение не имеет решений"}
}
