import re
from ruamel.yaml import YAML

arquivo_yaml = ''

def removeLinesComments(arquivo_yaml):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.allow_duplicate_keys = True 

    new_lines = []

    with open(arquivo_yaml, 'r') as file:
        lines = file.readlines()

        for line in lines:
            #Remover comentários usando regex      
            removeComments = re.sub(r'#.*$', '', line)
            if removeComments:
                new_lines.append(removeComments)

    with open(arquivo_yaml, 'w') as file:
        for line in new_lines:
            file.write(line)


    print(f"Comentários removidos do arquivo: {arquivo_yaml}")


removeLinesComments(arquivo_yaml)