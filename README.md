## Desafio

Quais ações deverão ser executadas?

- [x] Remover a configuração `redis` e `redisConfig`;

- [x] Remover a annotations do ingress `nginx.ingress.kubernetes.io/ssl-redirect`;

- Caso uma configuração esteja com `enable: false` remover os demais campos dela;

- Remover configurações duplicadas;

- [x] Remover linhas comentadas;

- [x] Atualizar a versão de todos Kustomization para `2.2.1`;

- [x] Deixar as configurações na mesma ordem;

- [x] Adicionar a env `ENV:dev`;

- [x] Alterar a configuração `containerPort:$PORT` para:

```yml
ports:
  - name: http
    containerPort: $PORT
    protocol: TCP
```

- [x] Alterar o `requests` e `limits` de CPU para `10m` e `100m`, respectivamente.

# Orientações

O desafio deverá retornar com os scripts utilizados para executar as ações e quais comandos devem ser usados para testá-los. 

Podendo ser utilizada qualquer linguagem, desde que seja possível testar seguindo as orientações fornecidas.

Não esquecer da importância dos logs nos scripts. 
