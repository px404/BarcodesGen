import barcode
from barcode.writer import ImageWriter
from datetime import datetime
import os

os.system('cmd /c "pip install -r libs.txt"')

def bar_gen(data,iteration):
    ts = str(datetime.now().strftime("%H-%M-%S"))
    barcode_format = barcode.get_barcode_class('code39')
    my_barcode = barcode_format(data, writer=ImageWriter())
    my_barcode.save(data+ts+"_"+"Barcode"+iteration)

n = int(input("How many barcodes would you like to generate? Integer Number Please: "))

for i in range(0,n):
    data = str(input('Enter the data: '))
    bar_gen(data,str(i))
