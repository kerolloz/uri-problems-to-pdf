import pdfkit

def download_problem_pdf(url, name):
    options = {
        'margin-top': '3px',
        'margin-right': '8px',
        'margin-left': '8px',
        'margin-bottom': '3px',
    }
    pdfkit.from_url(url, name, options=options)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide the problem link and the pdf name")
        exit(1)
    link = sys.argv[1]
    out_name = sys.argv[2]
    pdf_name = "original_problem.pdf"
    download_problem_pdf(link, pdf_name)
    cut_problem_pdf(pdf_name, out_name)
