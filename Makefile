default: all

all:
	python markdown_include.py README_template.md > README.md

clean:
	latexmk -C
