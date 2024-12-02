import requests
from time import sleep
from loguru import logger
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import messagebox, simpledialog

URL = 'https://api.adviceslip.com/advice'

# Funções existentes no código
def busca_conselho(URL):
    try:
        resposta_conselho = requests.get(URL)
        id_conselho = resposta_conselho.json()['slip']['id']
        texto_conselho = resposta_conselho.json()['slip']['advice']
        if id_conselho and texto_conselho:
            return id_conselho, texto_conselho
        else:
            logger.error('\nID ou texto do conselho não foram encontrados.')
            return None
    except requests.exceptions.RequestException as bug:
        logger.error(f'\nErro ao acessar a API: {bug}')
        return None

def traduzir_conselho(advice):
    try:
        return GoogleTranslator(source='english', target='portuguese').translate(advice)
    except Exception as bug:
        logger.error(f'\nErro ao traduzir o conselho: {bug}')
        return None

def salvar_txt_conselho(conselhos, nome_txt='conselhos.txt'):
    try:
        with open(nome_txt, 'a', encoding='utf-8') as txt:
            for conselho in conselhos:
                txt.write(f'ID {conselho[0]}: {conselho[1]}\n')
        messagebox.showinfo("Conselhos Salvos", f'Estes conselhos foram salvos como "{nome_txt}"!')
    except Exception as bug:
        logger.error(f'\nErro ao salvar o arquivo: {bug}')
        messagebox.showerror("Erro", "Erro ao salvar os conselhos.")

def ler_ultimas_linhas(nome_txt='conselhos.txt', n_linhas=10):
    try:
        with open(nome_txt, 'r', encoding='utf-8') as txt:
            todas_as_linhas = txt.readlines()
            return todas_as_linhas[-n_linhas:]
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado.")
        return None
    except Exception as bug:
        logger.error(f'\nErro ao ler o arquivo: {bug}')
        messagebox.showerror("Erro", "Erro ao ler o arquivo.")
        return None

# Funções adicionais para a interface gráfica
def receber_conselhos():
    conselhos_recebidos.clear()
    try:
        n_conselhos = simpledialog.askinteger("Conselhos", "Quantos conselhos você quer receber?")
        if n_conselhos is None or n_conselhos <= 0:
            messagebox.showinfo("Aviso", "Número inválido ou operação cancelada.")
            return

        for i in range(n_conselhos):
            logger.info(f'Ciclo {i + 1} de chamada de API iniciado')
            conselho = busca_conselho(URL)
            if conselho:
                conselhos_recebidos.append(conselho)
            else:
                messagebox.showwarning("Aviso", f"Conselho {i + 1}: Não foi possível obter o conselho.")
            sleep(1)
        messagebox.showinfo("Conselhos", "Conselhos recebidos com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Número inválido.")

def ver_conselhos_recebidos():
    if conselhos_recebidos:
        conselhos_traduzidos = [
            f"ID {id_conselho}: {traduzir_conselho(texto_conselho)}"
            for id_conselho, texto_conselho in conselhos_recebidos
        ]
        messagebox.showinfo("Conselhos Recebidos", "\n".join(conselhos_traduzidos))
    else:
        messagebox.showinfo("Aviso", "Nenhum conselho recebido ainda.")

def salvar_conselhos():
    if conselhos_recebidos:
        conselhos_traduzidos = [
            (id_conselho, traduzir_conselho(texto_conselho)) 
            for id_conselho, texto_conselho in conselhos_recebidos
        ]
        salvar_txt_conselho(conselhos_traduzidos)
    else:
        messagebox.showinfo("Aviso", "Nenhum conselho recebido para salvar!")

def ver_conselhos_salvos():
    conselhos_salvos = ler_ultimas_linhas()
    if conselhos_salvos:
        messagebox.showinfo("Conselhos Salvos", "\n".join([linha.strip() for linha in conselhos_salvos]))

def mostrar_conselhos_ingles():
    if conselhos_recebidos:
        conselhos_ingles = [
            f"ID {id_conselho}: {texto_conselho}"
            for id_conselho, texto_conselho in conselhos_recebidos
        ]
        messagebox.showinfo("Conselhos em Inglês", "\n".join(conselhos_ingles))
    else:
        messagebox.showinfo("Aviso", "Nenhum conselho recebido ainda.")

def sair():
    root.destroy()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Seu Zé - Conselhos")
root.geometry("450x350")


conselhos_recebidos = []

label_titulo = tk.Label(root, text="Bem-vindo, Seu Zé! Quer alguns conselhos?", font=("Garamond", 16), wraplength=300, justify="center")
label_titulo.pack(pady=10)

btn_receber_conselhos = tk.Button(root, text="1. Quero receber novos conselhos!", command=receber_conselhos, font=("Garamond", 12), bg='lightblue', fg='black')
btn_receber_conselhos.pack(fill="x", pady=5)

btn_ver_conselhos = tk.Button(root, text="2. Quero ver os conselhos recebidos!", command=ver_conselhos_recebidos, font=("Garamond", 12), bg='lightblue', fg='black')
btn_ver_conselhos.pack(fill="x", pady=5)

btn_salvar_conselhos = tk.Button(root, text="3. Quero salvar estes conselhos em um arquivo!", command=salvar_conselhos, font=("Garamond", 12), bg='lightblue', fg='black')
btn_salvar_conselhos.pack(fill="x", pady=5)

btn_ver_salvos = tk.Button(root, text="4. Quero ver os conselhos que acabei de salvar no arquivo!", command=ver_conselhos_salvos, font=("Garamond", 12), bg='lightblue', fg='black')
btn_ver_salvos.pack(fill="x", pady=5)

btn_conselhos_ingles = tk.Button(root, text="5. Quero mostrar estes conselhos em inglês para um gringo!", command=mostrar_conselhos_ingles, font=("Garamond", 12), bg='lightblue', fg='black')
btn_conselhos_ingles.pack(fill="x", pady=5)

btn_sair = tk.Button(root, text="6. Pronto, estou satisfeito! Vou 'mimbora'!", command=sair, font=("Garamond", 12), bg='lightblue', fg='black')
btn_sair.pack(fill="x", pady=5)

root.mainloop()
