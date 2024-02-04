# Modelo 115 Data Extraction

This project is designed to extract specific information from Modelo 115 tax documents in Spain. The extracted data is then written to an Excel file for further analysis.

## Project Structure

The project consists of several Python scripts and a CSV file:

- `definitive.py`: This is the main script that orchestrates the data extraction and writing to an Excel file.
- `intro_func.py`: This script contains functions for reading PDF files and extracting data from them.
- `output.py`: This script contains functions for writing the extracted data to an Excel file.
- `support_regex.py`: This script contains regular expressions used for data extraction.
- `cabeceras.csv`: This CSV file contains the headers for the Excel file.

## How It Works

The `extract_data_file(file)` function in `intro_func.py` reads each PDF file and extracts the desired data from each page using the `extract_data_page(page)` function.

The `write_to_xlsx(rows)` function in `output.py` writes the extracted data to an Excel file, using the headers from `cabeceras.csv`.

## Running the Project

To run the project, execute the `definitive.py` script:

```bash
python definitive.py
```
This will create an Excel file named Modelo 115.xlsx in the project directory.