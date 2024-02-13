#Descargar mp3 y mp4 de youtube

import pytube as pt
from pytube import YouTube

def convertidormp3 (link):
    youLink = pt.YouTube(link) #captura el link
    nombreCancion =str( youLink.title) #captura el nombre del video
    return youLink.streams.filter(abr="160kbps", progressive = False).first().download(filename= nombreCancion+".mp3") 

def convertidormp4(link):
    youLink = YouTube(link).streams.get_highest_resolution().download()
    return youLink

import tkinter

def main():
    ventana =tkinter.Tk()
    ventana.title("Downloader MP3/MP4 YouTube")
    ventana.iconbitmap("logoMacode.ico") #icono del software
    ventana.config(bg="#C6CBF6")
    ventana.resizable(0,0)
    from tkinter import font
    negrilla = font.Font(weight="bold")

    #opciones de descarga
    from tkinter import messagebox, ttk
    opciones = ttk.Combobox(state="readonly",values=["mp3", "mp4"])
    etiqueta_opciones = tkinter.Label(ventana, text = "Formato de Descarga:",bg="#C6CBF6")

    #etiquetas y entradas
    etiqueta_subtitulo = tkinter.Label(ventana, text = "DESCARGA ARCHIVOS MP3/MP4 DE YT", bg="#C6CBF6",font = negrilla)
    etiqueta_link = tkinter.Label(ventana, text = "Link de YT: ",bg="#C6CBF6")
    etiqueta_respuesta = tkinter.Label(ventana, text="",bg="#C6CBF6")
    etiqueta_desarrollador = tkinter.Label(ventana, text="By: Macode",bg="#C6CBF6")
    entrada_link = tkinter.Entry(ventana)

    #botones
    boton_descargar = tkinter.Button(ventana, text ="Descargar")
    boton_borrar = tkinter.Button(ventana, text = "Nueva Descarga")

    #ubicacion en la ventana
    etiqueta_subtitulo.grid(row=0, column =1, pady="5")
    etiqueta_link.grid(row=1, column = 0, pady="10")
    entrada_link.grid(row=1, column = 1)
    etiqueta_opciones.grid(row=2,column=0,pady="10")
    opciones.grid(row=2,column=1)
    etiqueta_respuesta.grid(row=3,column = 0, pady="5")
    boton_descargar.grid(row=7, column = 0)
    boton_borrar.grid(row=7, column = 1)
    etiqueta_desarrollador.grid(row=8, column = 3,  pady="10")

    #boton descargar
    def manejadorEventosCalcular(eventos):
        link = str(entrada_link.get())
        eleccion = opciones.get()
        if (eleccion == "mp3"):
            download = convertidormp3(link)
        else:
            download = convertidormp4(link)
        etiqueta_respuesta.config(text="Descarga Finalizada")
    boton_descargar.bind("<Button-1>", manejadorEventosCalcular)

    #boton borrar
    def manejadorEventosBorrar(eventos):
        entrada_link.delete(0,tkinter.END)
        etiqueta_respuesta.config(text="")
    boton_borrar.bind("<Button-1>",manejadorEventosBorrar)

    ventana.mainloop()

main()
        
