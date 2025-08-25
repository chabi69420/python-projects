import os
import barcode
from barcode.writer import ImageWriter

def generate_barcode(data):
    # Select the barcode type (Code128 supports most text and numbers)
    BarcodeClass = barcode.get_barcode_class('code128')
    code = BarcodeClass(data, writer=ImageWriter())
    
    # Save as PNG
    barcode_filename = code.save("barcode")   # creates barcode.png
    print("✅ Barcode Generated:", barcode_filename)
    
    # Open the image automatically (Windows only)
    if os.name == "nt":  
        os.startfile(barcode_filename)

# Example data
data = "1234-5678-9101"
generate_barcode(data)