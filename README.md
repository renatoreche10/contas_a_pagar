Gerenciador de Contas a Pagar
Este é um sistema de gestão financeira pessoal desenvolvido para facilitar o controle de despesas. O projeto permite o cadastro, edição e exclusão de contas, organizando-as automaticamente por categorias e apresentando resumos financeiros em tempo real.
Funcionalidades
Cadastro de Despesas: Inclusão de descrição, valor, data de vencimento e categoria.
Organização por Categorias: Separação visual automática em blocos como Contas Básicas, Saúde, Cartão e Gerais.
Cálculos Automatizados: O sistema calcula o Total Geral e o total gasto por cada categoria no servidor.
Gestão de Registros: Interface interativa para editar informações ou excluir contas com confirmação via modal [Conversation].
Formatação Inteligente: Datas formatadas no padrão brasileiro (DD/MM/YYYY) utilizando a biblioteca Day.js.
Tecnologias Utilizadas
Back-end: Python com o framework Flask.
Banco de Dados: MySQL para persistência dos dados.
Front-end: HTML5, CSS3 (Layout com Flexbox) e JavaScript puro
.
Bibliotecas Externas: Day.js para manipulação de datas.
Pré-requisitos
Para rodar o projeto localmente, você precisará de:
Python 3.x instalado.
WampServer ou similar para gerenciar o servidor MySQL.
As seguintes bibliotecas Python: pip install flask mysql-connector-python
Configuração do Banco de Dados
Crie um banco de dados chamado sistemacontas e uma tabela despesas com a seguinte estrutura:
CREATE DATABASE sistemacontas; USE sistemacontas;
CREATE TABLE despesas ( id INT AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR(100) NOT NULL, valor DECIMAL(10,2) NOT NULL, categoria ENUM('contasBasicas', 'saude', 'cartao', 'gerais') NOT NULL, dataVencimento DATE NOT NULL );
