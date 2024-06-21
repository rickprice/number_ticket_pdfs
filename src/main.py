from pypdf import PaperSize, PdfReader, PdfWriter, Transformation

# Read source file
reader = PdfReader("TestBusinessCard.pdf")
sourcepage = reader.pages[0]

# Create a destination file, and add a blank page to it
writer = PdfWriter()
destpage = writer.add_blank_page(width=PaperSize.A4.height, height=PaperSize.A4.width)

# Copy source page to destination page, several times
for y in range(4):
    destpage.merge_transformed_page(
        sourcepage,
        Transformation().translate(
            0,
            (y+1) * sourcepage.mediabox.height,
        ),
    )

# Write file
with open("DuplicatedBusinessCard.pdf", "wb") as fp:
    writer.write(fp)

