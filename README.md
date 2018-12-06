## For Ubuntu:  
```sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev```

Minimal Working Example
```python
import pdftotext

with open("lorem_ipsum.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Iterate over all the pages
for page in pdf:
    print(page)

# Just read the second page
print(pdf.read(2))

# Or read all the text at once
print(pdf.read_all())
```

## PDF miner  
Install it with pip install pdfminer.six. A minimal working example is here.

