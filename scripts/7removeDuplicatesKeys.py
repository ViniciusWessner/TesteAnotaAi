from ruamel.yaml import YAML
from collections import defaultdict

arquivo_yaml = '/home/anotaai/Área de trabalho/TesteAnotaAi/test/valuesTest.yaml'

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
removeDuplicateConfigurations(arquivo_yaml)
