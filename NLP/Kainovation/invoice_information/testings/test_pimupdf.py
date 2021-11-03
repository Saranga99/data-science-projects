import fitz

abc = fitz.open("Invoice Copies/1.pdf")
print(abc.metadata)
