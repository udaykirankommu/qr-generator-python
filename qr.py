import qrcode
print("******* QR Code Generated *******")
d = input("Enter text or URL: ")
img=qrcode.make(d)

file=input("Enter file name(without .png): ")

img.save(file + ".png")

print(f"\n QR Code generated successfully!")
print(f"saved as: {file}.png")