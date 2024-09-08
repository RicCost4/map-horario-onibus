# Banco de Dados
criar uma pasta 'data' dentro do diretorio 'db', pois nele é que vai ser mapeado a pasta do banco de dados. postgres do seu compose.

Rodar o docker engina na maquina, se estiver usando o windows, instalar o docker-desktop e executar.

```Powershell
cd .\db\
docker-compose -f docker-compose.yaml up -d
```

ao criar pela primeira vez o banco, concetar no banco, e criar o esquema 'online' dentro do banco 'cardapio'.

# Migration
como rodar a migration

```Powershell
cd .\db\
npm i
npx knex migrate:latest --env development
```