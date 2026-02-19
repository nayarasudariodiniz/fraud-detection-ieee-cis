# Detecção de Fraude em E-commerce - IEEE-CIS

Este projeto desenvolve um pipeline de Ciência de Dados para identificar transações fraudulentas em operações de e-commerce. Utilizando o dataset da IEEE Computational Intelligence Society (IEEE-CIS), o trabalho foca na superação dos desafios de dados desbalanceados e na construção de um modelo robusto para suporte à decisão em tempo real.

## 1. Problema de Negócio
O objetivo principal é distinguir transações legítimas de fraudulentas em um cenário de alta complexidade, onde apenas 3,5% dos dados representam a classe positiva (fraude). O foco está em equilibrar a captura de fraudadores (Recall) com a minimização de bloqueios indevidos de clientes bons (Precisão).

## 2. Tecnologias e Metodologia
* **Linguagem:** Python.
* **Principais Bibliotecas:** Pandas, Scikit-Learn, Imbalanced-learn, Matplotlib e Seaborn.
* **Algoritmos Testados:** Regressão Logística, Árvore de Decisão e Random Forest.
* **Técnicas de Balanceamento:** Ajuste de pesos (`class_weight`) e Random Undersampling.

## 3. Desenvolvimento e Insights Técnicos

### 3.1 Engenharia de Dados
* **Imputação de Dados:** Utilização da mediana para preenchimento de valores nulos, garantindo resistência a outliers financeiros.
* **Encoding de Variáveis:** Aplicação de One-Hot Encoding para categorias simples e Frequency Encoding para variáveis de alta cardinalidade, como domínios de e-mail.

### 3.2 Evolução de Performance
O projeto evoluiu de um modelo linear base para um modelo de ensemble otimizado via `RandomizedSearchCV`.

| Modelo | Acurácia | Precisão (Fraude) | Recall (Fraude) | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| Regressão Logística | 0.70 | 0.07 | 0.64 | 0.13 |
| Random Forest (Base) | 0.87 | 0.18 | 0.75 | 0.29 |
| **Random Forest (Final)** | **0.98** | **0.92** | **0.43** | **0.59** |

## 4. Conclusões e Resultados Finais
* **Alta Confiabilidade:** O modelo final atingiu uma **Precisão de 92%**, reduzindo significativamente o atrito com clientes legítimos e sendo ideal para sistemas de aprovação automática.
* **Aprendizado Não-linear:** A superioridade do Random Forest confirmou que os padrões de fraude neste dataset são complexos e exigem modelos baseados em árvores com profundidade otimizada.
* **Validação de Hipóteses:** Confirmou-se que variáveis de identidade e comportamento de rede (família V) possuem maior peso preditivo que o valor nominal da transação.

## 5. Como Utilizar este Repositório
1. Clone o repositório.
2. Certifique-se de baixar os dados originais no Kaggle (IEEE-CIS Fraud Detection).
3. Execute o script de pré-processamento para preparar o ambiente.
4. O notebook principal contém todos os experimentos e visualizações das métricas de performance (Matriz de Confusão e Curva ROC).