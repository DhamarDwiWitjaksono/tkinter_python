import tkinter
from tkinter import messagebox
#membuat objek dari library tkinter
#objek dari library tersebut disimpan didalam variable 
bingkai=tkinter.Tk()

#membuat fungsi untuk menagkap nilai di form
def submit_form():
    nama=entry_nama.get()
    usia=entry_usia.get()
    gender=var_gender.get()
    if not nama or not usia or gender == "false":
        messagebox.showerror("kocak", "masukin dulu inputan yang bener, wooyyyyy!")
    print(f"nama: {nama}\nusia: {usia}\nkelamin: {gender}")
    entry_nama.delete(0, tkinter.END)
    entry_usia.delete(0, tkinter.END)



#mengubah ukuran bingkai
#bingkai.geometry("300x250")

#dan kita bisa pakai cara ini agar posisi tampilan seperti text langsung terpusat ditengah layar
panjang_bingkai=300 
lebar_bingkai=250

panjang_layar=bingkai.winfo_screenwidth()
lebar_layar=bingkai.winfo_screenheight()

#untuk mendapatkan posisi ditengah layar
sumbu_X=int((panjang_layar /2 ) - (panjang_layar /2))
sumbu_Y=int((lebar_layar /2) - (lebar_layar /2))
bingkai.geometry(f"{panjang_bingkai}x{lebar_bingkai}+{sumbu_X}+{sumbu_Y}")

#memberi judul pada bingkai
bingkai.title("Formulir data diri")

#untuk mengatur agar tidak bisa diubah ukurannya
#bingkai.resizable(False,False)

#label untuk nama
label_nama=tkinter.Label(bingkai,text="Nama : ")
label_nama.pack(pady=5)

#entry untuk nama
entry_nama= tkinter.Entry(bingkai)
entry_nama.pack(pady=5)

label_usia=tkinter.Label(bingkai,text=" Usia : ")
label_usia.pack(pady=5)

entry_usia=tkinter.Entry(bingkai)
entry_usia.pack(pady=5)

#membuat radio button
var_gender=tkinter.StringVar(value="false")
label_gender=tkinter.Label(bingkai,text="Jenis Kelamin : ")
label_gender.pack(pady=5)

tombol_laki=tkinter.Radiobutton(bingkai,text="Laki laki", variable=var_gender,value="laki laki")
tombol_laki.pack(pady=5)

tombol_perempuan=tkinter.Radiobutton(bingkai,text="Perempuan", variable=var_gender,value="Perempuan")
tombol_perempuan.pack(pady=5)

#membuat tombol submit
tombol_submit=tkinter.Button(bingkai,text="Submit", command=submit_form)
tombol_submit.pack(pady=5)

#memunculkan objek
#dan posisi barisan ini harus dibawah kode lainnya agar menampilkam
bingkai.mainloop()

