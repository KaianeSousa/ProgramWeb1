import json
import util


def ler_arquivo(clientes):
    clientes = []
    with open("clientes.txt", "r") as file:
        clientes = json.load(file)
    return clientes
    
    
def calcular(clientes):
    idades = [clientes['idade'] for cliente in clientes]
    rendas = [clientes['renda'] for cliente in clientes]
        
    media_idade = util.calcular_media(idades)
    media_renda = util.calcular_media(rendas)
    
    return media_idade, media_renda

def main():
    clientes = ler_arquivo("clientes.txt")
    media_idade, media_renda = calcular(clientes)
    
    print(f"Média Idade: {media_idade: .2f}")
    print(f"Média Renda: R$ {media_renda: .2f}")
    
    if __name__ == "__main__":
        main()
