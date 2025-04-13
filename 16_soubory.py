from docx import Document
import pickle

reference = open(r"prace_soubory\dovolena.txt", "wt", encoding="utf-8")
print(reference.write("Karibik\nBali\nHavaj\nThajsko\nMaldivy\nEgypt\n"))
reference.close()

reference = open(r"prace_soubory\dovolena.txt", "rt", encoding="utf-8")
print("read_lines")
for radek in reference.readlines():
    print(radek)
reference.close()

reference = open(r"prace_soubory\dovolena.txt", "at", encoding="utf-8")
print(reference.write("Tunis\nAlžírsko\n"))
reference.close()

with open(r"prace_soubory\dovolena.txt", "rt", encoding="utf-8") as reference:
    print("dovolena.txt")
    print(reference.read())

with open(r"prace_soubory\data.json", "rt", encoding="utf-8") as reference:
    print("data.json")
    print(reference.read())

with open(r"prace_soubory\data.csv", "rt", encoding="utf-8") as reference:
    print("data.csv")
    print(reference.read())
# Load the .docx file
doc = Document(r"prace_soubory\Document 1.docx")
# Extract text from paragraphs
print("docx")
for paragraph in doc.paragraphs:
    print(paragraph.text)

vizitky = [{"jmeno": "Jan", "prijmeni": "Novak", "vek": 30, "plat": 50000},
           {"jmeno": "Petr", "prijmeni": "Novy", "vek": 25, "plat": 60000},
           {"jmeno": "Eva", "prijmeni": "Novakova", "vek": 28, "plat": 70000}]

with open(r"prace_soubory\vizitky.pkl", "wb") as reference:
    pickle.dump(vizitky, reference)

with open(r"prace_soubory\vizitky.pkl", "rb") as reference:
    print(pickle.load(reference))