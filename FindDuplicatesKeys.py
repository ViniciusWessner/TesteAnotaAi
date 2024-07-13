import os
import ruamel.yaml

def find_duplicate_keys_in_yaml_files():
    # Lista para armazenar os arquivos com chaves duplicadas
    files_with_duplicates = []

    # Percorre todos os arquivos no diretório atual e subdiretórios
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith(".yaml") or name.endswith(".yml"):
                file_path = os.path.join(root, name)
                try:
                    # Carrega o arquivo YAML
                    with open(file_path, "r", encoding="utf-8") as yaml_file:
                        yaml = ruamel.yaml.YAML(typ='safe')
                        data = yaml.load(yaml_file)

                    # Verifica se há chaves duplicadas
                    duplicate_file = _has_duplicate_keys(file_path, data)
                    if duplicate_file:
                        files_with_duplicates.append(duplicate_file)
                except Exception as e:
                    print(f"Erro ao processar {file_path}: {str(e)}")

    # Retorna a lista de arquivos com chaves duplicadas
    return files_with_duplicates

def _has_duplicate_keys(file_path, data):
    seen_keys = set()
    for key in _yaml_keys(data):
        if key in seen_keys:
            return file_path
        seen_keys.add(key)
    return None

def _yaml_keys(data):
    if isinstance(data, dict):
        for key, value in data.items():
            yield key
            yield from _yaml_keys(value)
    elif isinstance(data, list):
        for item in data:
            yield from _yaml_keys(item)

# Executa a função principal e obtém os arquivos com chaves duplicadas
files_with_duplicates = find_duplicate_keys_in_yaml_files()

# Exibe os resultados
if files_with_duplicates:
    print("Lista de arquivos que possui chaves duplicadas:")
    for file_path in files_with_duplicates:
        print(file_path)
else:
    print("Nenhum arquivo encontrado com chaves duplicadas.")
