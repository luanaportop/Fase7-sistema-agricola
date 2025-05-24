import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier



# 1. Coletar e carregar dados
dados = pd.read_csv('dados_irrigacao_aumentados.csv')  # Exemplo: histórico de dados
# Colunas: ['umidade_solo', 'temperatura', 'luminosidade', 'nutrientes_P', 'nutrientes_K', 'irrigacao']

# 2. Pré-processamento - irrigação = target
X = dados.drop('irrigacao', axis=1)
y = dados['irrigacao']

# 3. Divisão de dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinamento do modelo
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)
accuracy = modelo.score(X_test,y_test)
print(f"Acurácia: {accuracy:.2f}")


#Arvore
#modeloTree = DecisionTreeClassifier(max_depth=5) 
#modeloTree.fit(X_train, y_train)
#accuracy = modeloTree.score(X_test,y_test)
#print(f"Acurácia (Decision Tree): {accuracy:.2f}")



#Linear
#modeloLog = LogisticRegression()
#modeloLog.fit(X_train, y_train)
#accuracy = modeloLog.score(X_test,y_test)
#print(f"Acurácia (Logistic Regression): {accuracy:.2f}")


#KNN

#modeloknn = KNeighborsClassifier(n_neighbors=5)  # Ajuste n_neighbors conforme necessário
#modeloknn.fit(X_train, y_train)
#accuracy_knn = modeloknn.score(X_test,y_test)
#print(f"Acurácia (KNN): {accuracy_knn:.2f}")



# 6. Previsão futura
novo_dado = pd.DataFrame([[40, 30, 800, 1, 0]], columns=X.columns)
previsao = modelo.predict(novo_dado)
print("Necessidade de irrigação:", "Sim" if previsao[0] else "Não")
