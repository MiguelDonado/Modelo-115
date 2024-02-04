import os
import pdfplumber
from support_regex import fecha, año, periodo, base, resultado, num_perceptores


def get_pdf_files():
    pdf_files = [f for f in os.listdir(".") if f.endswith(".pdf")]
    return pdf_files


def read_pdf(file):
    # It'll return the text from the PDF file as one string
    with pdfplumber.open(file) as pdf:
        text_file = [page.extract_text() for page in pdf.pages]
    return text_file


def to_number(number):
    return float(number.replace(".", "").replace(",", "."))


def extract_data_page(page):
    if "realizada" in page:
        fecha_field = fecha.search(page).group(1)
        return [fecha_field]
    elif "SUBARRENDAMIENTO" in page:
        año_field = año.search(page).group(1)
        periodo_field = periodo.search(page).group(1)
        num_perceptores_field = num_perceptores.search(page).group(1)
        base_field = base.search(page).group(1)
        resultado_field = resultado.search(page).group(1)
        if not base_field:
            return None
        return [
            año_field,
            periodo_field,
            num_perceptores_field,
            to_number(base_field),
            to_number(resultado_field),
        ]
    else:
        return None


def extract_data_file(file):
    text_file = read_pdf(file)
    row = []
    rows = []
    for page in text_file:
        if provisional_row := extract_data_page(page):
            row.extend(provisional_row)
        else:
            row.append("ERROR")
        if len(row) == 6:
            rows.append(row)
            row = []
        if "ERROR" in row:
            row = ["ERROR"] * 6
            rows.append(row)
            row = []
    return rows
