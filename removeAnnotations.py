import os
from ruamel.yaml import YAML

def remover_ssl_redirect_em_ingress(caminho_arquivo):
    yaml = YAML()
    yaml.preserve_quotes = True
    
    with open(caminho_arquivo, 'r') as arquivo:
        try:
            conteudo = yaml.load(arquivo)
            alterado = False
            
            if 'ingress' in conteudo:
                if 'annotations' in conteudo['ingress']:
                    if 'nginx.ingress.kubernetes.io/ssl-redirect' in conteudo['ingress']['annotations']:
                        del conteudo['ingress']['annotations']['nginx.ingress.kubernetes.io/ssl-redirect']
                        alterado = True
            
            if alterado:
                print(f"Removida a annotation ssl-redirect em {caminho_arquivo}")
                
                # Escreve o conteúdo atualizado de volta no arquivo
                with open(caminho_arquivo, 'w') as arquivo_atualizado:
                    yaml.dump(conteudo, arquivo_atualizado)
                    
        except Exception as exc:
            print(f"Erro ao processar {caminho_arquivo}: {exc}")

def percorrer_diretorios_com_remocao_ssl_redirect(diretorio_raiz):
    for caminho_diretorio, _, nomes_arquivos in os.walk(diretorio_raiz):
        for nome_arquivo in nomes_arquivos:
            if nome_arquivo.endswith('.yaml') or nome_arquivo.endswith('.yml'):
                caminho_arquivo = os.path.join(caminho_diretorio, nome_arquivo)
                remover_ssl_redirect_em_ingress(caminho_arquivo)

if __name__ == "__main__":
    diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
    percorrer_diretorios_com_remocao_ssl_redirect(diretorio_raiz)
