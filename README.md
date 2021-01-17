# Image_decipherment
# Created by Varshini

## Steganography
Steganography is the art of hiding the fact that communication is taking place, by hiding information in other information. This project is developed for hiding information in any image file. The scope of the project is implementation of steganography tools for hiding information includes any type of information file and image files and the path where the user wants to save Image and extruded file. .
It is one of the technique of hiding secret data within an ordinary, non-secret, file or message in order to avoid detection; the secret data is then extracted at its destination.

## Application of Image Steganography
Steganography is employed in various useful applications, e.g. secret communication among agencies / people, copyright control of materials, enhancing robustness of image search engines and smart IDs (identity cards) where individuals’ details are embedded in their photographs. Other applications are video-audio synchronization, companies’ safe circulation of secret data, TV broadcasting, TCP/IP packets (for instance a unique ID can be embedded into an image to analyze the network traffic of particular users). In steganography many different carrier file formats can be used, but digital images are the most popular because of their frequency on the Internet.

## Explanation
Let the first few pixels of the original image (24bit color) be-

10101011.10001011.010101000, 10101001.00001100.01011110, 10100111.11001101.01011001

Let the secret message be 'A'.
'A' translates to '01000001' in (8 bit) ASCII.

To conceal the secret message inside the image, we change the last bits of the image like so-

A = 0 1 0 0 0 0 0 1

10101010.10001011.010101000, 10101000.00001100.01011110, 10100110.11001101.01011001

(Bold digits show changed bits)

The LSB Method does not require a key to be shared prior to the message being transferred between the sender and the recipient.

In addition, a delimiter needs to be used to stop decoding after the message length has been reached. An alternate approach is to specify the size of the message before the actual message.


## Encoding
* Replace image.png with the image you want to use.
* Execute the script with PATH having the corresponding directory.
* This would produce encoded image which is the new image with the hidden secret text.

## Decoding
* With  encoded image existing, execute the script with PATH having the corresponding directory.
* The secret text is displayed in the command window.
