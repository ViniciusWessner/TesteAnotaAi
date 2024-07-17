import os
import re
from ruamel.yaml import YAML
from collections import defaultdict

novaVersaoApp = '2.2.1'

def removeRedisConfig(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)

        if 'redis' in yamlData:
            del yamlData['redis']
            print("Removendo Redis")
        if 'redisConfig' in yamlData:
            del yamlData['redisConfig']
            print("Removendo Redisconfig")

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)

def removeAnnotation(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)

        if 'ingress' in yamlData and 'annotations' in yamlData['ingress']:
            if 'nginx.ingress.kubernetes.io/ssl-redirect' in yamlData['ingress']['annotations']:
                del yamlData['ingress']['annotations']['nginx.ingress.kubernetes.io/ssl-redirect']
                print("Removendo Annotation")

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)

def removeLinesComments(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True

    new_lines = []

    with open(arquivo_yaml, 'r') as file:
        lines = file.readlines()

        for line in lines:
            removeComments = re.sub(r'#.*$', '', line)
            if removeComments:
                new_lines.append(removeComments)

    with open(arquivo_yaml, 'w') as file:
        for line in new_lines:
            file.write(line)

def removeDuplicateConfigurations(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True

    with open(arquivo_yaml, 'r') as file:
        yaml_data = yaml.load(file)

        def remove_duplicates(yaml_file):
            if isinstance(yaml_file, dict):
                key_count = defaultdict(int)
                duplicate_keys = []

                for key in list(yaml_file.keys()):
                    key_count[key] += 1
                    if key_count[key] > 1:
                        duplicate_keys.append(key)

                for key in duplicate_keys:
                    del yaml_file[key]
                    

                for key, value in yaml_file.items():
                    remove_duplicates(value)
            elif isinstance(yaml_file, list):
                for item in yaml_file:
                    remove_duplicates(item)

        remove_duplicates(yaml_data)

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yaml_data, file)

def updateVersionKustomization(arquivo_yaml, novaVersaoApp):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)

        if 'helmCharts' in yamlData:
            for chart in yamlData['helmCharts']:
                if chart['name'] == 'app':
                    chart['version'] = novaVersaoApp
                    print("Atualizando versão para 2.2.1")

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)

def addEnv(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)

        if 'env' not in yamlData or yamlData['env'] == 'null' or yamlData['env'] is None:
            yamlData['env'] = 'dev'
            print("Adicionando Env")

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)

def updateContainerPort(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)

        if 'ports' in yamlData:
            for ports in yamlData['ports']:
                if ports['name'] == 'http':
                    ports['containerPort'] = '$PORT'
                    print("atualizando Container port")
                    break

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)

def requestAndLimitCPU(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True

    with open(arquivo_yaml, 'r') as file:
        yamlData = yaml.load(file)

        if 'resources' in yamlData and 'limits' in yamlData['resources']:
            yamlData['resources']['limits']['cpu'] = '10m'
            yamlData['resources']['requests']['cpu'] = '100m'
            print("Alterando CPU")

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yamlData, file)

def percorreDiretorios(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                removeRedisConfig(file_path)
                removeAnnotation(file_path)
                removeDuplicateConfigurations(file_path)
                removeLinesComments(file_path)
                if file == 'values.yaml':
                    addEnv(file_path)
                updateContainerPort(file_path)
                requestAndLimitCPU(file_path)
                if file == 'kustomization.yaml':
                    updateVersionKustomization(file_path, novaVersaoApp)

if __name__ == "__main__":
    diretosioRaiz = "../applications" 
    percorreDiretorios(diretosioRaiz)
