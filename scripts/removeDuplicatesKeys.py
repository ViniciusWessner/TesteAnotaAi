from ruamel.yaml import YAML
from collections import defaultdict

arquivo_yaml = ''

def remove_duplicate_configurations(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True  
    yaml.allow_duplicate_keys = True  

    with open(arquivo_yaml, 'r') as file:
        yaml_data = yaml.load(file)

        def remove_duplicates(yamlFile):
            if isinstance(yamlFile, dict):
                key_count = defaultdict(int)

                duplicate_keys = []

                for key in list(yamlFile.keys()):
                    key_count[key] += 1
                    if key_count[key] > 1:
                        duplicate_keys.append(key)
                        

                for key in duplicate_keys:
                   del yamlFile[key]

                for key, value in yamlFile.items():
                    remove_duplicates(value)
            elif isinstance(yamlFile, list):

                for item in yamlFile:
                    remove_duplicates(item)

        remove_duplicates(yaml_data)

    with open(arquivo_yaml, 'w') as file:
        yaml.dump(yaml_data, file)
        print(f"As configurações duplicadas foram removidas no arquivo '{arquivo_yaml}'.")

remove_duplicate_configurations(arquivo_yaml)
