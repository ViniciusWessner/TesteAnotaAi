from ruamel.yaml import YAML

arquivo_yaml = ''

def removeRedisConfig(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True 

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)  
        print(f"como estava o arquivo: {yamlData['redis']}")

        if 'redis' in yamlData:
            del yamlData['redis']
        if 'redisConfig' in yamlData:
            del yamlData['redisConfig']

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)
        print(yamlData)

removeRedisConfig(arquivo_yaml)
