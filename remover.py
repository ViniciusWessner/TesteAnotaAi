#Seu código aqui...
import os
from ruamel.yaml import YAML

def processar_kustomization_yaml(caminho_arquivo):
    yaml = YAML()
    #configurando para manter os padroes do arquivo
    yaml.preserve_quotes = True
    
    with open(caminho_arquivo, 'r') as arquivo:
        try:
            conteudo = yaml.load(arquivo)
            #retorno se foi atualizado
            atualizado = False
            if 'helmCharts' in conteudo:
                for chart in conteudo['helmCharts']:
                    if 'version' in chart:
                        chart['version'] = '2.2.1'
                        atualizado = True

            if atualizado:
                print(f"Atualizando versão em {caminho_arquivo}")

            # Escreve o conteúdo atualizado de volta no arquivo
            with open(caminho_arquivo, 'w') as arquivo_atualizado:
                yaml.dump(conteudo, arquivo_atualizado)
                
        except Exception as exc:
            print(f"Erro ao processar {caminho_arquivo}: {exc}")

def percorrer_diretorios(diretorio_raiz):
    for caminho_diretorio, nomes_diretorios, nomes_arquivos in os.walk(diretorio_raiz):
        for nome_arquivo in nomes_arquivos:
            if nome_arquivo == 'kustomization.yaml':
                caminho_arquivo = os.path.join(caminho_diretorio, nome_arquivo)
                processar_kustomization_yaml(caminho_arquivo)

if __name__ == "__main__":
    diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
    percorrer_diretorios(diretorio_raiz)
