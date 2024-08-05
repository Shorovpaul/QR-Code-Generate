import qrcode as QC  # Import the qrcode library and alias it as QC for convenience.

data = "https://github.com/Shorovpaul"  # Define the data (URL) you want to encode into the QR code.

img = QC.make(data)  # Create a QR code image from the data using the qrcode library.

img  # Display the generated QR code image object (this line itself does not display the image but returns the object).

img.save("MY github link_QC.png")  # Save the QR code image to a file named "M Y_QC.png".
