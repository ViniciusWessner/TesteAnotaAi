from ruamel.yaml import YAML

arquivo_yaml = ''
novaVersaoApp = '2.2.1'

def updateVersionKustomization(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True 

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file) 
        print(f"como estava o arquivo {yamlData}")


        if 'helmCharts' in yamlData:
            for chart in yamlData['helmCharts']:
                if chart['name'] == 'app':
                    chart['version'] = novaVersaoApp


    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)
        print(yamlData)

updateVersionKustomization(arquivo_yaml)
