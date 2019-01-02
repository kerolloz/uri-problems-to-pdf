import pdfkit
import re
import sys

def download_problem_pdf(url, name):
    options = {
        'margin-top': '3px',
        'margin-right': '8px',
        'margin-left': '8px',
        'margin-bottom': '3px',
    }
    pdfkit.from_url(url, name, options=options)


def problem_link_checker(url):
    link_format = 'https://www.urionlinejudge.com.br/repository/UOJ_{number}_en.html'
    number = re.findall("[0-9]\d+", url)
    if len(number) == 1:
        return link_format.format(number=''.join(number))
    return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide the problem link and the pdf name")
        exit(1)
    link = sys.argv[1]
    out_name = sys.argv[2]
    pdf_name = "original_problem.pdf"
    download_problem_pdf(link, pdf_name)
