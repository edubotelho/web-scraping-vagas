import requests
import csv
from bs4 import BeautifulSoup

link = "https://realpython.github.io/fake-jobs/"

requisiscao = requests.get(link)
soup = BeautifulSoup(requisiscao.text, "html.parser")


''' localizando os elementos que contem as informações das vagas'''

tituloVaga = soup.find_all("h2", class_="title")
company = soup.find_all("h3", class_="subtitle")
Location = soup.find_all("p", class_="location")
Descricao = soup.find_all("a", string="Apply")  

contando = len(tituloVaga)

print(f"Total de vagas: {contando}")

''' função para requisitar a página da vaga e pegar a descrição da vaga'''
def pagerequest(url):
    response = requests.get(url)
    soup2 = BeautifulSoup(response.text, "html.parser")
    return soup2

vagas = []

''' iterando sobre as vagas e pegando as informações de cada vaga'''
for i in range(contando):

    objectos = {
        "titulo": tituloVaga[i].text,
        "empresa": company[i].text,
        "localizacao": Location[i].text,
        "link2" : Descricao[i]["href"]
    }

    soup2 = pagerequest(objectos["link2"])
    divPg = soup2.find("div", class_="content")
    descP = divPg.find("p")
    descricaovaga = descP.text.strip()

    print(i + 1, "º Vaga ---")
    print(objectos["titulo"])
    print(objectos["empresa"])
    print(objectos["localizacao"])
    print("Descrição da vaga: ", descricaovaga)

    print("---------------------------------------------------")

    objectos["descricao"] = descricaovaga
    vagas.append(objectos)

''' salvando as informações das vagas em um arquivo CSV'''

with open("vagas.csv", "w", newline="", encoding="utf-8") as arquivo:
    campos = ["titulo", "empresa", "localizacao", "link2", "descricao"]

    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(vagas)