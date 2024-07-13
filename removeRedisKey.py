import os
from ruamel.yaml import YAML

def remover_chaves_redis(caminho_arquivo):
    yaml = YAML()
    
    with open(caminho_arquivo, 'r') as arquivo:
        try:
            conteudo = yaml.load(arquivo)
            alterado = False
            
            # Verifica e remove a chave 'redis'
            if 'redis' in conteudo:
                del conteudo['redis']
                alterado = True
                print(f"Chave 'redis' removida em {caminho_arquivo}")
            
            # Verifica e remove a chave 'redisConfig'
            if 'redisConfig' in conteudo:
                del conteudo['redisConfig']
                alterado = True
                print(f"Chave 'redisConfig' removida em {caminho_arquivo}")
            
            # Se houve alterações, escreve o conteúdo atualizado de volta no arquivo
            if alterado:
                with open(caminho_arquivo, 'w') as arquivo_atualizado:
                    yaml.dump(conteudo, arquivo_atualizado)
                    
        except Exception as exc:
            print(f"Erro ao processar {caminho_arquivo}: {exc}")

def percorrer_diretorios_com_remocao_chaves_redis(diretorio_raiz):
    for caminho_diretorio, _, nomes_arquivos in os.walk(diretorio_raiz):
        for nome_arquivo in nomes_arquivos:
            if nome_arquivo.endswith('.yaml') or nome_arquivo.endswith('.yml'):
                caminho_arquivo = os.path.join(caminho_diretorio, nome_arquivo)
                remover_chaves_redis(caminho_arquivo)

if __name__ == "__main__":
    diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
    percorrer_diretorios_com_remocao_chaves_redis(diretorio_raiz)
