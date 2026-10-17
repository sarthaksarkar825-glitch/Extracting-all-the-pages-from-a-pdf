import os
import fitz  # PyMuPDF

pdf_filename = "Basisc Electrical Book.pdf"
output_folder = "all_book_pages"

os.makedirs(output_folder, exist_ok=True)

doc = fitz.open(pdf_filename)
total_pages = len(doc)
print(f"Total pages: {total_pages}")

# 1.5 zoom yields crisp text and circuits without blowing up storage
zoom = fitz.Matrix(1.5, 1.5)

for page_idx in range(total_pages):
    page = doc[page_idx]
    pix = page.get_pixmap(matrix=zoom, alpha=False)
    
    # 4-digit zero-padding ensures proper sorting (page_0001.jpg)
    filename = f"page_{page_idx + 1:04d}.jpg"
    pix.save(os.path.join(output_folder, filename))
    
    if (page_idx + 1) % 50 == 0 or (page_idx + 1) == total_pages:
        print(f"Saved {page_idx + 1}/{total_pages} pages...")

print("\nAll pages successfully extracted!")
#complete