import yaml
import os

def remove_redis_config(diretorioArquivos):
    with open(diretorioArquivos, 'r') as file:
        yaml_data = yaml.safe_load(file)

        print (yaml_data)

        if 'redis' in yaml_data:
            del yaml_data['redis']
        # Remover outros campos relacionados ao redis conforme necessário

        print(yaml_data)

    with open(diretorioArquivos, 'w') as file:
        yaml.safe_dump(yaml_data, file)




