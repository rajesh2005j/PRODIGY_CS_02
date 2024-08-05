try:
    # Taking path of image as input 
    path = r"C:\Users\engin\OneDrive\Desktop\inc\hello.jpg"

    # Taking decryption key as input
    key = int(input('Enter Key for decryption of image: '))

    # Print path of image file and decryption key that we are using
    print('The path of file:', path)
    print('Key for decryption:', key)

    # Open file for reading purpose
    with open(path, 'rb') as fin:
        # Storing image data in variable "image"
        image = fin.read()

    # Converting image into byte array to perform decryption easily on numeric data
    image = bytearray(image)

    # Perform XOR operation on each value of bytearray
    for index, value in enumerate(image):
        image[index] = value ^ key

    # Open file for writing purpose
    with open(path, "wb") as fin:
        # Writing decrypted data in image
        fin.write(image)

    print("Decryption done!!")

except Exception as e:
    print("Error caught:", e)
