from tkinter import*
from PIL import Image, ImageTk

def every(text):
    var = ""
    for i in range(0, len(text)):
        var += text[i]
    if i%100==0 and i!=0:
        var +="\n"
    return var


shubham_root = Tk()

shubham_root.geometry("1200x600")
shubham_root.title("NEWSPAPER")
shubham_root.configure(bg="light blue")

texts = []
photo = [] 

for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every(text))

    image = Image.open(f"{i+1}.png")
    # photo.append(ImageTk.PhotoImages(image))
    photo.append(ImageTk.PhotoImage(image))

f1 = Frame(shubham_root, width=800, height=80)
Label(f1,text="SST News \n IPL \"MUMBAI INDIAN\" ACTION PLAYER DEBUE IN 2025",font="Luchida 20 bold").pack()
Label(f1,text="DATE : \"APRIL\" 2025", font="Luchida 10 bold",).pack()
f1.pack()

f2 = Frame(shubham_root, width=900, height= 300)
Label(f2, text=texts[0],padx=30, pady=30,).pack(side=LEFT)
Label(f2, image=photo[0],anchor="e").pack(padx=200)
f2.pack(anchor="w")

f3 = Frame(shubham_root, width=900, height= 300)
Label(f3, text=texts[1],padx=30, pady=30,).pack(side=RIGHT)
Label(f3, image=photo[1],anchor="e").pack(padx=120)
f3.pack(anchor="e")

f4 = Frame(shubham_root, width=900, height= 300)
Label(f4, text=texts[2],padx=30, pady=30,).pack(side=LEFT)
Label(f4, image=photo[2],anchor="e").pack(padx=120)
f4.pack(anchor="w")

# GUI logic here

shubham_root.mainloop()

