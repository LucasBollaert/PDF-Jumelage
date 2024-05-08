import os
from PyPDF3 import PdfFileReader, PdfFileWriter

# Chemin du dossier contenant les fichiers PDF
dossier_pdf = "."

# Créer un objet PdfFileWriter pour le fichier final
pdf_writer = PdfFileWriter()

# Parcourir tous les fichiers du dossier
for fichier in os.listdir(dossier_pdf):
    if fichier.endswith(".pdf"):
        chemin_complet = os.path.join(dossier_pdf, fichier)

        # Ouvrir le fichier PDF actuel
        pdf_reader = PdfFileReader(chemin_complet)

        # Ajouter toutes les pages du fichier PDF actuel au fichier final
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

# Chemin du fichier PDF final
chemin_final = os.path.join(dossier_pdf, "impression_file.pdf")

# Écrire le contenu cumulé dans le nouveau fichier PDF
with open(chemin_final, "wb") as out:
    pdf_writer.write(out)

print(f"Tous les fichiers PDF ont été fusionnés dans {chemin_final}")
