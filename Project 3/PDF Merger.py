import PyPDF2

pdfiles = ["cosmos_by_carl_sagan_p1.pdf","cosmos_by_carl_sagan_p2.pdf" ]
merger =  PyPDF2.PdfMerger()

for filename in pdfiles:
    with open(filename, 'rb') as pdffile :
     merger.append(pdffile)

merger.write('merger.pdf')
merger.close()


