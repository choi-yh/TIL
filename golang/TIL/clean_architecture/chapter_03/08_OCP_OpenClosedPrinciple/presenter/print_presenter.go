package presenter

import (
	"github.com/choi-yh/TIL/golang/TIL/clean_architecture/chapter_03/08_OCP_OpenClosedPrinciple/view"
)

type PrintPresenter struct {
	pdfView view.PDFView
}

func (p PrintPresenter) PrintView() {
	p.pdfView.ViewFinancialReportOnPDF()
}
