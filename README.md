# codarshians

Repositório do time codarshians para o Woman A3 Data Challenge - Hackathon de Engenharia de Dados.

## Pipeline

Para o desenvolvimento da solução utilizamos a base de dados CNPJ disponibilizada pela Receita Federal no [link](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj).

### 1. Seleção e Extração dos Dados

O primeiro passo consistiu em analisar os dados disponíveis e selecionar quais seriam necessários para responder as 6 perguntas do Hackathon. Em seguida, foi feito o download dos arquivos e tratamento dos dados.

O script [ETL.py](ETL.py) - Extract, Transform and Load - realiza a primeira parte da pipeline, onde os dados brutos são lidos e é feito o primeiro processamento. Como algumas tabelas de informações estavam disponibilizadas em diversos arquivos separados, nesta etapa os dados foram concatenados e colunas desnecessárias foram excluídas. Ao final, foram gerados novos arquivos CSVs com os dados resultados.

Durante o desenvolvimento da solução, utilizamos a biblioteca *pandas* para auxiliar na extração e processamento dos dados.

O script [salva-dados-postgresql.py](salva-dados-postgresql.py) foi implementado ainda na etapa inicial do desenvolvimento. O script lê os arquivos CVS baixados da base CNPJ da Receita Federal e salva em um banco de dados PostgreSQL.

### 2. Docker

Durante o desenvolvimento da solução, percebemos que alguns dados ainda precisavam ser tratados, como por exemplo, formatação de datas e exclusão de algumas colunas. Então foi necessário uma segunda etapa de processamento e geração de um dump do banco de dados.

Para isso, foi implementada uma arquitetura em Docker com três containers:

* App: container com imagem Python para processamento dos dados;
* PostgreSQL: container com o banco de dados;
* pgAdmin: container para gerenciamento do banco.

Mais detalhes de cada um dos serviços estão descritos no arquivo [docker-compose.yml](src/docker/docker-compose.yml).

O container Python lê os arquivos CSV da etapa anterior, faz alterações pertinentes e salva os dados no banco. Os arquivos CSV exportados foram salvos na pasta docker/src/data_csv para leitura do script.


## Perguntas do Hackathon

1. Número de indústrias ativas por mês/ano entre 2010 - 2021, discriminado por MEI
ou Simples, em cada município brasileiro
2. Número de comércios que fecharam por mês/ano entre 2010 - 2021, discriminado por MEI ou Simples, em cada município brasileiro
3. Número de CNPJ novos por mês/ano entre 2010 - 2021, discriminado por MEI ou Simples, em cada município brasileiro
4. Qual o número de CNPJ que surgiram do grupo de educação superior, entre 2015 e 2021, discriminado por ano, em cada estado brasileiro?
5. Qual a classe de CNAE com o maior capital social médio no Brasil no último ano?
6. Qual a média do capital social das empresas de pequeno porte por natureza jurídica no último ano?

### Solução

O arquivo [read_data_and_save_feather.py](read_data_and_save_feather.py) lê todos os arquivos CSV e os salva como feather (.ftr). Feather é um formato de arquivo portátil para armazenar DataFrames (de linguagens como Python ou R). Tanto a leitura dos CSVs (pd.read_csv) quanto a exportação para feather (pd.to_feather) foi feita utilizando a biblioteca pandas.

Esse tipo de arquivo foi utilizado para otimizar a leitura dos dados. Os arquivos .ftr eram significativamente menores que os CSV. Apenas na tabela estabelecimentos não foi possível utilizar esse formato.

A pasta [solução](solução) contém o script principal que vai ler os dados e resolver cada uma das questões, [load_solution.py](solução/load_solution.py). Nos demais estão as funções que resolvem cada uma das questões.

Cada método recebe os DataFrames com os dados necessários e retornam um ou dois DataFrames de resposta. Ao final de cada solução, os DataFrames resultantes são exportados para arquivos CSVs.

Esses arquivos serviram para alimentar o banco de dados, que serviu como fonte de dados para a solução final no PowerBI.

