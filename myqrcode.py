import qrcode

# text = input("Enter the text to convert in the qrcode= ")
# filename = input("Enter the filename to save the qrcode= ")

def generate_qr_code(filepath):
    
    
    with open(filepath,"r") as file:
        lines= file.readlines()
    
    text=lines[0].strip()
    filename = lines[1].strip()

    image_qrcode = qrcode.make(text)
    image_qrcode.save(filename)
    image_qrcode.show()

generate_qr_code('input.txt')
