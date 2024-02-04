from output import write_to_xlsx
from intro_func import get_pdf_files, extract_data_file


def main():
    pdf_files = get_pdf_files()
    row = []  # List that will contain the data of each row
    rows = []  # List that will contain the data of all rows (list of lists)
    for file in pdf_files:
        text_file = extract_data_file(file)
        # Variable that will be used to know which page we are in
        for row in text_file:
            rows.append(row)
    write_to_xlsx(rows)


if __name__ == "__main__":
    main()
