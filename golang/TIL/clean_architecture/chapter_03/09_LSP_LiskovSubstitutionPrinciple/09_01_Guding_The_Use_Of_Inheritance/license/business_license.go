package license

import "fmt"

type BusinessLicense struct{}

func (l BusinessLicense) CalcFee() {
	fmt.Println("Calculate Business License Fee")
}

func (l BusinessLicense) users() {
}

func NewBusinessLicense() BusinessLicense {
	return BusinessLicense{}
}
