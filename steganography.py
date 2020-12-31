# coded by varshini

# Encryption is the process of translating plain text data (plaintext) into something that appears to be random and meaningless (ciphertext)
# Decryption is the process of converting meaningless message (Ciphertext) into its original form (Plaintext).
# HINT : there is a slight difference between original image and encrypted image
# that's the encrypted image has yellow lines at the top left corner.....Indicates the image is encrypted
# whereas the original image does'nt

# importing powerful opencv library
# importing os
import cv2
import os

# creating dictionaries
d = {}
c = {}

# loop over alphabets
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# reading the image
x = cv2.imread("bharath.jpg")

# displaying the height and width of the given image
i = x.shape[0]
j = x.shape[1]
print(i,j)

# asking for user security key
key=input("enter the security key to edit:")
# entering the text to hide
text=input("enter the text to hide:")

# initialising keylength as 0
key_length = 0
# initializing text lenght as len(text)
text_length = len(text)
z = 0
n = 0
m = 0

l=len(text)

for i in range(l):
    x[n,m,z] = d[text[i]]^d[key[key_length]]
    n = n+1
    m = m+1
    m = (m+1)%3
    key_length = (key_length+1)%len(key)

cv2.imwrite("encrypted_img.jpg",x)
os.startfile("encrypted_img.jpg")
print("Data hiding in image completed successfully")

key_length = 0
key_length = len(text)
z = 0
n = 0
m = 0

ch=int(input("\nenter 1 to extract data from image:"))
# checks whether the character is same as the above mentioned charater(just want to check) 
if ch==1:
    # user to enter the same key
    key1=input("\n\nre enter key to extract text:")
    decrypt=""
    
    # checking for the same key
    if key==key1:
        # decrypting the image
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[kl]]]
            n = n+1
            m = m+1
            m = (m+1)%3
            key_length = (key_length+1)%len(key)
        # prints the encrypted text    
        print("Encrypted text was:",decrypt)
    else:
        print("Key doesn't matched")
else:
    print("Thankyou.....Exiting.......")
    
    
    
