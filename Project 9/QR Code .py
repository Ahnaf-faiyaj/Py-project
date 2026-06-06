import qrcode as qr
from PIL import Image   


Qr = qr.QRCode(version = 1,
               error_correction = qr.constants.ERROR_CORRECT_H,
                box_size = 20 , border = 8 )


Qr.add_data("https://www.figma.com/files/team/1311259104046683524/drafts?fuid=1311259101774277508")
Qr.make(fit = True)

# img = Qr.make_image(fill_color = "#e17055" , back_color = "#34495e" )
# img = Qr.make_image(fill_color = "#f368e0" , back_color = "#5f27cd" )
img = Qr.make_image(fill_color = "#227093" , back_color = "#ff5252" )
img.save("Ahnaf_Figma.png")