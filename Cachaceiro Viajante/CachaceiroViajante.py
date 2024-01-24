import pulp
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def criar_dados_excel(caminho_arquivo):
    dados = {
        'Origem': ['Bartatal', 'Bartatal', 'Bartatal', 'Berola', 'Berola', 'Amendoim', 'Amendoim', 'Santo Grau', 'Santo Grau', 'Artevale', 'Baiuca', 'Bar do Goreco', 'Casa do Patrocinio'],
        'Destino': ['Berola', 'Amendoim', 'Santo Grau', 'Santo Grau', 'Artevale', 'Baiuca', 'Fernandao', 'Bar do Goreco', 'Casa do Patrocinio', 'Capistrana', 'Fernandao', 'Capistrana', 'Capistrana'],
        'Distância (km)': [10, 15, 5, 14, 12, 7, 9, 6, 11, 13, 8, 4, 9, 1],
        'Nível de Intoxicação': [2, 3, 1, 2, 3, 2, 2, 1, 2, 3, 2, 2, 1, 0]
    }
    
    # Garante que todas as listas tenham o mesmo comprimento
    comprimento_maximo = max(len(v) for v in dados.values())
    for chave, valor in dados.items():
        dados[chave] = valor + [None] * (comprimento_maximo - len(valor))
    
    df = pd.DataFrame(dados)
    df.to_excel(caminho_arquivo, index=False)

def ler_dados(caminho_arquivo):
    dados = pd.read_excel(caminho_arquivo)
    return dados

def criar_grafo(dados):
    G = nx.DiGraph()
    for _, linha in dados.iterrows():
        origem, destino, distancia, intox = linha['Origem'], linha['Destino'], linha['Distância (km)'], linha['Nível de Intoxicação']
        G.add_node(origem, intoxication=intox)  # Adiciona 'intoxication' ao nó
        G.add_edge(origem, destino, distance=float(distancia), intoxication=float(intox))
    
    # Adiciona 'intoxication' com valor padrão zero para nós que não têm essa chave
    for no in G.nodes():
        if 'intoxication' not in G.nodes[no]:
            G.nodes[no]['intoxication'] = 0
    
    return G

def resolver_problema(G, alpha=0.5, limite_intoxicacao=10):
    modelo = pulp.LpProblem("Cachaceiro_Viajante", pulp.LpMinimize)

    x = pulp.LpVariable.dicts("rota", G.edges(), 0, 1, pulp.LpBinary)
    y = pulp.LpVariable.dicts("ordem", G.nodes(), 0, len(G.nodes()) - 1, pulp.LpInteger)

    modelo += alpha * pulp.lpSum(G[u][v]['distance'] * x[u, v] for u, v in G.edges()) + \
             (1 - alpha) * pulp.lpSum(G[u][v]['intoxication'] * x[u, v] for u, v in G.edges())

    for no in G.nodes():
        modelo += pulp.lpSum(x[u, v] for u, v in G.out_edges(no)) == 1
    for aresta in G.edges():
        modelo += y[aresta[0]] - y[aresta[1]] + len(G.nodes()) * x[aresta] <= len(G.nodes()) - 2
        modelo += y[aresta[1]] - y[aresta[0]] + len(G.nodes()) * (1 - x[aresta]) <= len(G.nodes()) - 2

    modelo += pulp.lpSum(G[u][v]['intoxication'] * x[u, v] for u, v in G.edges()) <= limite_intoxicacao

    # Restrição para não passar por bares já visitados
    for aresta in G.edges():
        modelo += x[aresta] <= pulp.lpSum(x[u, v] for u, v in G.in_edges(aresta[1]))

    modelo.solve()

    rota = [(u, v) for u, v in G.edges() if pulp.value(x[u, v]) == 1]
    distancia = pulp.value(modelo.objective)
    intoxicacao = {v: G.nodes[v]['intoxication'] + sum(G[u][v]['intoxication'] * pulp.value(x[u, v]) for u in G.predecessors(v)) for v in G.nodes()}
    intoxicacao_total = pulp.value(pulp.lpSum(intoxicacao.values()))

    return rota, distancia, intoxicacao, intoxicacao_total

def desenhar_grafo(G, rota):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8)
    nx.draw_networkx_edges(G, pos, edgelist=rota, edge_color="red", width=2)
    plt.show()

if __name__ == "__main__":
    caminho_arquivo_excel = "cachaceiro_dados.xlsx"  # Caminho para a planilha Excel
    criar_dados_excel(caminho_arquivo_excel)

    dados = ler_dados(caminho_arquivo_excel)
    G = criar_grafo(dados)

    print("-" * 30)
    print("TABELA".center(30, '-'))
    print(dados.to_string(index=False))

    rota, distancia, intoxicacao, intoxicacao_total = resolver_problema(G, limite_intoxicacao=15)
    
    print("-" * 30)
    print("Rota:", rota)
    print("-" * 30)
    print("Distância percorrida:", distancia, "km")
    print("-" * 30)
    print("Intoxicação por bar:", intoxicacao)
    print("-" * 30)
    print("Intoxicação total:", intoxicacao_total)

    desenhar_grafo(G, rota)
