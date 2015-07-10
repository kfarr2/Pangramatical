.PHONY: run clean

# run the traaaaap
run:
	python genetic.py

# remove that .pyc garbage
clean:
	find -iname "*.pyc" -delete
	find -iname "__pycache__" -delete
