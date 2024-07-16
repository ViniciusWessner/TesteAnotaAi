from ruamel.yaml import YAML

arquivo_yaml = ''

def removeAnnotation(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True 

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file) 
        print(f"como estava o arquivo /n {yamlData}")

        if 'ingress' in yamlData and 'annotations' in yamlData['ingress']:
            if 'nginx.ingress.kubernetes.io/ssl-redirect' in yamlData['ingress']['annotations']:
                del yamlData['ingress']['annotations']['nginx.ingress.kubernetes.io/ssl-redirect']
                print("Remivo o ingress")
            else: 
                print("Arquivo não possui annotation do ingress")

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)
        print(yamlData)

removeAnnotation(arquivo_yaml)
