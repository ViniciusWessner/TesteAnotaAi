from ruamel.yaml import YAML

arquivo_yaml = ''

def updateContainerPort(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True 

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file) 
        print(f"como estava o arquivo {yamlData}")

        if 'ports' in yamlData:
            for ports in yamlData['ports']:
                if ports['name'] == 'http':
                    ports['containerPort'] = '$PORT'
                    print("Porta http encontrada e alterada")
                    break
                else:
                    print("Porta 'htttp' nao encontrada")
        else:
            print("opcao 'ports' nao encontrada")


    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)
        print(yamlData)

updateContainerPort(arquivo_yaml)
