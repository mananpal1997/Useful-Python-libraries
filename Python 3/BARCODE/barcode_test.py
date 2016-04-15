import barcode
from barcode.writer import ImageWriter
from barcode import generate

#print(barcode.PROVIDED_BARCODES)
EAN = barcode.get_barcode_class('ean13')
ean = EAN(u'5901234123457')
fullname = ean.save('ean13_barcode') #creates barcode svg

'''
ean = EAN(u'5901234123457', writer=ImageWriter()) #creates barcode image
fullname = ean.save('ean13_barcode')
'''
'''
fp = open('a.txt','wb')
ean.write(fp)
'''
'''
name = generate('EAN13', u'5901234123457', output='barcode_svg')
'''
