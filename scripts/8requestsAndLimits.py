from ruamel.yaml import YAML

arquivo_yaml = '/home/anotaai/Área de trabalho/aquiteste/applications/teste1.yaml'

def requestAndLimitCPU(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True #ignora duplicidade

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)
        print(yamlData)

        if 'resources' in yamlData:
            print("Alterando dados")
            yamlData['resources']['limits']['cpu'] = '10m'
            yamlData['resources']['requests']['cpu'] = '100m'
        else:
            print("Nao encontrado resources and requests")
        
    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)
        print(yamlData)

requestAndLimitCPU(arquivo_yaml)