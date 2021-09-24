# codarshians

Repositório do time codarshians para o Woman A3 Data Challenge - Hackathon de Engenharia de Dados.

## Pipeline

Para o desenvolvimento da solução utilizamos a base de dados CNPJ disponibilizada pela Receita Federal no [link](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj).

### 1. Seleção e Extração dos Dados

O primeiro passo consistiu em analisar os dados disponíveis e selecionar quais seriam necessários para responder as 6 perguntas do Hackathon. Em seguida, foi feito o download dos arquivos e tratamento dos dados.

O script [ETL.py](ETL.py) realiza a primeira parte da pipeline, onde os dados brutos são lidos e é feito o primeiro processamento. Como algumas tabelas de informações estavam disponibilizadas em diversos arquivos separados, nesta etapa os dados foram concatenados e colunas desnecessárias foram excluídas. Ao final, foram gerados novos arquivos CSVs com os dados resultados.

Durante o desenvolvimento da solução, utilizamos a biblioteca *pandas* para auxiliar na extração e processamento dos dados.

O script [salva-bd-postgresql3.py](salva-bd-postgresql3.py) foi implementado ainda na etapa inicial do desenvolvimento. O script lê os arquivos CVS obtidos na etapa anterior e salva em um banco de dados PostgreSQL.

### 2. Docker

Durante o desenvolvimento da solução, percebemos que alguns dados ainda precisavam ser tratados, como por exemplo, formatação de datas e exclusão de algumas colunas. Então foi necessário uma segunda etapa de processamento e geração de um dump do banco de dados.

Para isso, foi implementada uma arquitetura em Docker com três containers:

* App: container com imagem Python para processamento dos dados;
* PostgreSQL: container com o banco de dados;
* pgAdmin: container para gerenciamento do banco.

Mais detalhes de cada um dos serviços estão descritos no arquivo [docker-compose.yml](docker-compose.yml).

O container Python lê os arquivos CSV da etapa anterior, faz alterações pertinentes quando necessário e salva os dados no banco.
