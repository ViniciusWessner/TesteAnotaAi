from ruamel.yaml import YAML

arquivo_yaml = '/home/anotaai/Área de trabalho/aquiteste/applications/teste1.yaml'

def removeRedisConfig(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True #ignora duplicidade

    # Chamando o arquivo
    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)  # Use 'load' em vez de 'safe_load'
        print(f"como estava o arquivo: {yamlData['redis']}")

        if 'redis' in yamlData:
            del yamlData['redis']
        if 'redisConfig' in yamlData:
            del yamlData['redisConfig']

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)
        print(yamlData)

removeRedisConfig(arquivo_yaml)
