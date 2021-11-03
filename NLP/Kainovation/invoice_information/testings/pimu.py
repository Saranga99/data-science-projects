import fitz

file = fitz.open(
    "C:/Users/Saranga/Desktop/data-science-projects/NLP/Kainovation/invoice_information/Invoice Copies/2.pdf")

for pagenumber, page in enumerate(file.pages(), start=1):
    text = page.get_text()
    txt = open(f"report_page_{pagenumber}.txt", "a")
    txt.writelines(text)
    txt.close()


# class EXTRACTOR:
#     def extract_text(self, file_path: str):
#         doc = fitz.open(file_path)

#         for i in range(doc.pageCount):
#             page = doc.load_page(i)
#             pagetext = page.get_text("text")
