import os
import barcode
from barcode.writer import ImageWriter

def generate_barcode(data):
    
    BarcodeClass = barcode.get_barcode_class('code128')
    code = BarcodeClass(data, writer=ImageWriter())
    
    barcode_filename = code.save("barcode")   
    print("✅ Barcode Generated:", barcode_filename)
    
    if os.name == "nt":  
        os.startfile(barcode_filename)

data = "1234-5678-9101"

generate_barcode(data)
