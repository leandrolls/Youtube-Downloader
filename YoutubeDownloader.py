from pytube import YouTube, Playlist
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#-------- FUNCOES -------#

Nome_Pasta = ""
localVideo = ""

def openLocation():
    global Nome_Pasta
    Nome_Pasta = filedialog.askdirectory()
    if (len(Nome_Pasta) > 1 ):
        diretorioPasta.config(text=Nome_Pasta)
    else:
        diretorioPasta.config(text="Escolha uma pasta")

def DownloadVideo():
    global localVideo
    opcao = caixaopcoes.get()
    url = inputURL.get()
    if (len(url) > 1):
        print("")

        if opcao == opcoes[0]:
            yt = YouTube(url)
            localVideo = yt.streams.filter(progressive=True).first().download(Nome_Pasta)
        elif opcao == opcoes[1]:
            yt = YouTube(url)
            localVideo = yt.streams.filter(only_audio=True).first().download(Nome_Pasta)
        elif opcao == opcoes[2]:
            yt = Playlist(url)
            for video in yt.videos:
               localVideo = video.streams.first().download(Nome_Pasta)

    downloadconcluido = Label(janela, text="Download Concluído !")
    downloadconcluido.grid()

# ------- LAYOUT ------- #

janela = Tk()
janela.title("Youtube Downloader")
altura = 500
largura = 500
janela.resizable(True, True)
janela.configure(bg='white')
alturatela = janela.winfo_screenheight()
larguratela = janela.winfo_screenwidth()
posx = larguratela/2 - largura/2
posy = alturatela/2  - altura/2
janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
janela.columnconfigure(0,weight=1)

img = PhotoImage(file="Imagem/download.png")
label_imagem = Label(janela,image=img)
textoEndereco = Label(janela, text="\n Insira o endereço do vídeo ", bg='white')

inputURL = StringVar
inputURL =  Entry(janela, width=50, textvariable = inputURL)

diretorioPasta = Label(janela, text="\n Escolha uma pasta para armazenar o seu vídeo!", bg='white')
escolhaPasta = Button(width=10, text="Escolher ", bg='white' ,command=openLocation)
formatoDownload = Label(janela,text="\n Escolha a qualidade", bg='white')
opcoes = ["Vídeo", "Audio", "Playlist"]
caixaopcoes = ttk.Combobox(janela, value=opcoes)

botaoDownload = Button(janela, text="Download", command=DownloadVideo)

label_imagem.grid()
textoEndereco.grid()
inputURL.grid()
diretorioPasta.grid()
escolhaPasta.grid()
formatoDownload.grid()
caixaopcoes.grid()
espacamento2= Label(janela,text=" ", bg='white').grid()
botaoDownload.grid()

janela.mainloop()

