import threading
from tkinter import *
import client

def janelaLogin():

    janela = Tk()

    labelIP = Label(janela, text='Server IP: ')
    labelIP.pack()
    caixaIP = Entry()
    caixaIP.pack()    

    labelPORT = Label(janela, text='PORT: ')
    labelPORT.pack()
    caixaPORT = Entry()
    caixaPORT.pack()

    labelUSER = Label(janela, text='USERNAME: ')
    labelUSER.pack()
    caixaUSER = Entry()
    caixaUSER.pack()


    def login(): 
        caixaIP.pack()
        client.ServerIP = caixaIP.get()
        client.PORT =  int(caixaPORT.get())
        client.username = caixaUSER.get()
        print(f'{client.ServerIP} : {client.PORT} : {client.username}!')
        client.conectar()
        janela.destroy()       

    botaoLogin = Button(janela, text='Login', command=login)
    botaoLogin.pack()
    janela.mainloop()

janelaLogin()

def janelaChat():
    client.thread1.start()
    client.thread2.start()

    janela = Tk()
    janela.title('CHATING...')

    labelDigite = Label(text="Digite:")
    labelDigite.grid(column=1, row=1)
    entrada = Entry()
    entrada.grid(column=1, row=2)

    caixaTexto = Text(janela, width=30, height=15, state=DISABLED)
    caixaTexto.grid(column=1, row=0, padx=10, pady=10)

    def enviarMenssagem():
        client.messegeSend = entrada.get()
        client.sendMessage()
        entrada.delete(0, END)

    botaoEnviar = Button(janela, text='Enviar', command=enviarMenssagem)
    botaoEnviar.grid(column=1, row=3) 
    
    def receberMenssagem():
        texto = ''
        while True:
            if (client.messageRecv != texto):
                texto = client.messageRecv
                caixaTexto.config(state=NORMAL)
                caixaTexto.insert(INSERT, texto+'\n')
                caixaTexto.config(state=DISABLED)
            
    thread0 = threading.Thread(target=receberMenssagem,args=()) 
    thread0.start()

    janela.mainloop()
             
janelaChat()



