import tkinter
window=tkinter.Tk()
window.title("Ceaser Cipher Converter")
l=tkinter.Label(window, text="Enter your text")
e=tkinter.Entry(window, width=50, borderwidth=2)
plain_upper=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
ceaser_upper=('D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C')
plain_lower=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
ceaser_lower=('d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c')
plain_number=('0','1','2','3','4','5','6','7','8','9')
ceaser_number=('3','4','5','6','7','8','9','0','1','2')
def encrypter():
    text=e.get()
    length=len(text)
    final="" 
    if(length==0):
        l3=tkinter.Label(window, text="Please enter text!", foreground="Red")
        l3.pack()
    else:
        for i in range(0,length):
            character=text[i]
            if(character in plain_upper):
                for j in range(0,26):
                    if(character==plain_upper[j]):
                        final=final+ceaser_upper[j]
            elif(character in plain_lower):
                for k in range(0,26):
                    if(character==plain_lower[k]):
                        final=final+ceaser_lower[k]
            elif(character in plain_number):
                for l in range(0,10):
                    if(character==plain_number[l]):
                        final=final+ceaser_number[l]
            else:
                final=final+character
        l1=tkinter.Label(window, text="Encrypted text: "+str(final), foreground="Green")
        l1.pack()
        print(final)
def decrypter():
    text=e.get()
    length=len(text)
    final=""
    if(length==0):
        l4=tkinter.Label(window, text="Please enter text!", foreground="Red")
        l4.pack()
    else:
        for i in range(0,length):
            character=text[i]
            if(character in ceaser_upper):
                for j in range(0,26):
                    if(character==ceaser_upper[j]):
                        final=final+plain_upper[j]
            elif(character in ceaser_lower):
                for k in range(0,26):
                    if(character==ceaser_lower[k]):
                         final=final+plain_lower[k]
            elif(character in ceaser_number):
                for l in range(0,10):
                    if(character==ceaser_number[l]):
                        final=final+plain_number[l]
            else:
                final=final+character
        l2=tkinter.Label(window, text="Decrypted text: "+str(final), foreground="Green")
        l2.pack()
        print(final) 
b1=tkinter.Button(window, text="Encrypt", command=encrypter)
b2=tkinter.Button(window, text="Decrypt", command=decrypter)
l.pack()
e.pack()
b1.pack()
b2.pack()
window.mainloop()






