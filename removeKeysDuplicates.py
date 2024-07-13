import os
import ruamel.yaml

def remover_chaves_duplicadas_em_arquivos_yaml():
    # Percorre todos os arquivos no diretório atual e subdiretórios
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith(".yaml") or name.endswith(".yml"):
                file_path = os.path.join(root, name)
                try:
                    # Carrega o arquivo YAML
                    with open(file_path, "r", encoding="utf-8") as yaml_file:
                        yaml = ruamel.yaml.YAML(typ='rt')
                        data = yaml.load(yaml_file)

                    # Remove chaves duplicadas
                    _remover_chaves_duplicadas(data)

                    # Salva o arquivo modificado
                    with open(file_path, "w", encoding="utf-8") as yaml_file:
                        yaml.dump(data, yaml_file)

                    print(f"Chaves duplicadas removidas em {file_path}")
                except Exception as e:
                    print(f"Erro ao processar {file_path}: {str(e)}")

def _remover_chaves_duplicadas(data):
    chaves_vistas = set()
    _remover_chaves_duplicadas_recursivo(data, chaves_vistas)

def _remover_chaves_duplicadas_recursivo(data, chaves_vistas):
    if isinstance(data, dict):
        for chave, valor in list(data.items()):
            if chave in chaves_vistas:
                del data[chave]
            else:
                chaves_vistas.add(chave)
                _remover_chaves_duplicadas_recursivo(valor, chaves_vistas)
    elif isinstance(data, list):
        for item in data:
            _remover_chaves_duplicadas_recursivo(item, chaves_vistas)

# Executa a função principal para remover chaves duplicadas nos arquivos YAML
remover_chaves_duplicadas_em_arquivos_yaml()
