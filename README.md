# Project Data Pipeline - Store Nutrition

## 📌 Sobre o Projeto

Este projeto tem como objetivo simular e desenvolver um **pipeline de análise e engenharia de dados**
voltado para o segmento de **nutrição esportiva (suplementos)**.

A proposta é trabalhar desde o **tratamento e limpeza de dados brutos**, passando pela **exploração (EDA)**,
até a **geração de insights de negócio**, como:

- Produtos mais vendidos;
- Marcas com maior participação no faturamento;
- Comparação entre lojas (Loja 1, Loja 2, Filial);
- Comportamento de clientes e ticket médio.

Este projeto serve tanto como **portfólio** quanto como **exercício prático** de boas práticas em Engenharia de Dados.

---

## 📂 Estrutura de Pastas

```
project-data-pipeline-store-nutrition/
│
├── data/                  # datasets brutos e tratados
│   └── DT_Store_Suplements.csv
│
├── notebooks/             # Jupyter notebooks para exploração (EDA, testes)
│
├── scripts/               # scripts Python com funções reutilizáveis
│
├── docs/                  # relatórios, imagens, documentação complementar
│
├── README.md              # documentação principal do projeto
└── requirements.txt       # bibliotecas necessárias
```

---

## ⚙️ Como Rodar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/project-data-pipeline-store-nutrition.git
   cd project-data-pipeline-store-nutrition
   ```

2. Crie e ative um ambiente virtual (Python 3.10+ recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o Jupyter Notebook (se for explorar):
   ```bash
   jupyter notebook
   ```

---

## 🚀 Próximos Passos

- [ ] Exploração inicial do dataset (`/notebooks`)
- [ ] Tratamento de dados inconsistentes
- [ ] Criação de scripts de limpeza em `/scripts`
- [ ] Análises de vendas, marcas e clientes
- [ ] Dashboard de visualização (Power BI ou Python)

---

## ✨ Autor

Projeto desenvolvido por **Vanthuir Maia**  
Especialista em Engenharia de Dados & Analytics
