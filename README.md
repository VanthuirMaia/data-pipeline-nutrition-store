# Project Data Pipeline - Store Nutrition

## 📌 Sobre o Projeto

Este projeto tem como objetivo simular e desenvolver um **pipeline de análise e engenharia de dados**
voltado para o segmento de **nutrição esportiva (suplementos)**.

A proposta é trabalhar desde o **tratamento e limpeza de dados brutos**, passando pela **exploração (EDA)**,
até a **geração de insights de negócio** e finalização com um **dashboard interativo em Streamlit**, incluindo:

- Produtos mais vendidos;
- Marcas com maior participação no faturamento;
- Comparação entre lojas (Loja 1, Loja 2, Filial);
- Visualizações executivas (KPIs, gráficos organizados em grid).

Este projeto serve tanto como **portfólio** quanto como **exercício prático** de boas práticas em Engenharia de Dados,
utilizando o método **Aprendizagem Baseada em Projetos (Project-Based Learning)**.

---

## 📂 Estrutura de Pastas

```
project-data-pipeline-store-nutrition/
│
├── data/                  # datasets brutos e tratados
│   ├── DT_Store_Suplements.csv
│   └── DT_Store_Suplements_final.csv
│
├── notebooks/             # Jupyter notebooks para exploração (EDA, testes, relatórios)
│   ├── 01_exploracao_inicial.ipynb
│   ├── 02_tratamento_dados.ipynb
│   ├── 03_padronizacao.ipynb
│   ├── 04_analise_exploratoria.ipynb
│   └── 05_relatorio.ipynb
│
├── scripts/               # scripts Python com funções reutilizáveis
│
├── docs/                  # relatórios, imagens, documentação complementar
│
├── app.py                 # dashboard interativo em Streamlit
│
├── README.md              # documentação principal do projeto
└── requirements.txt       # bibliotecas necessárias
```

---

## ⚙️ Como Rodar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/VanthuirMaia/data-pipeline-nutrition-store
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

4. Inicie o Jupyter Notebook (se for explorar os notebooks):

   ```bash
   jupyter notebook
   ```

5. Execute o dashboard no Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## 🚀 Próximos Passos

- [x] Exploração inicial do dataset (`/notebooks`)
- [x] Tratamento de dados inconsistentes
- [x] Padronização de colunas (produtos, marcas, categorias)
- [x] Criação de KPIs e métricas de negócio
- [x] Dashboard interativo com Streamlit
- [ ] Versão em Power BI para maior interatividade
- [ ] Inclusão de métricas avançadas (CLV, CAC, LTV)
- [ ] Aplicação de modelos de Machine Learning (recomendação e previsão)

---

## ✨ Autor

Projeto desenvolvido por **Vanthuir Maia**  
Especialista em Engenharia de Dados & Analytics
