from ruamel.yaml import YAML

arquivo_yaml = '/home/anotaai/Área de trabalho/aquiteste/applications/teste1.yaml'

def addEnv(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True #ignora duplicidade

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)
        #print(f"Como estava meu arquivo antes de alterar, {yamlData}")

        if 'env' not in yamlData or yamlData['env'] == 'null' or yamlData['env'] is None:
            if 'env' in yamlData:
               print(f"O arquivo env estava setado como: {yamlData['env']}")
               yamlData['env'] = 'dev'
            else:
               yamlData['env'] = 'dev'
               print(f"Adicionando env agora ficou {yamlData['env']}")

    
    with open(arquivo_yaml, 'w') as file: 
     yaml.dump(yamlData, file)
     print(yamlData)

addEnv(arquivo_yaml)