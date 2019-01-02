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
    if len(sys.argv) < 2:
        print("Please provide the problem link")
        exit(1)
    link = sys.argv[1]
    link = problem_link_checker(link)
    if link == None:
        print("Please provide a valid problem link")
    out_name = "problem.pdf"
    download_problem_pdf(link, out_name)
