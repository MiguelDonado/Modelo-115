import re

fecha = re.compile(r"realizada\sel:\s(\d\d-\d\d-\d\d\d\d)\s")
año = re.compile(r"\.\s(\d{4})$", flags=re.MULTILINE)
periodo = re.compile(
    r"^Per.odo.*?(\d\w).*N.mero\sjustifi", flags=re.MULTILINE | re.DOTALL
)
num_perceptores = re.compile(r"\s1\s(\d+)$", flags=re.MULTILINE)
base = re.compile(r"^Base.*?\s2\s(.*?)$", flags=re.MULTILINE)
resultado = re.compile(r"Resultado.*?\s5\s(.*)$", flags=re.MULTILINE)
