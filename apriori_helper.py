# For Network Gragh
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def draw_plot(support,confidence,lift):
    plt.figure(figsize=(12,8))
    points=plt.scatter(support, confidence, alpha=0.8,s=500,c=lift,cmap="RdBu",edgecolors='black')
    cb=plt.colorbar(points)
    cb.set_label(label='Lift',size=15)
    plt.title('22 Association Rules',fontsize=20)
    plt.xlabel('Support',fontsize=15)
    plt.ylabel('Confidence',fontsize=15)
    plt.tick_params(labelsize=15)
    plt.show()

def draw_graph(rules, rules_to_show, metric=None):
    if metric=='lift':
        plt.figure(figsize=(12,8))
        G1 = nx.DiGraph()
        color_map=[]
        colors = 0.14035943    
        for i in range (rules_to_show):
            for a in rules.iloc[i]['antecedents']:        
                G1.add_nodes_from(nodes_for_adding=[a])
                for c in rules.iloc[i]['consequents']:     
                    G1.add_nodes_from(nodes_for_adding=[c])
                    G1.add_edge(a, c, color=colors,  weight= rules.iloc[i,6])
        for node in G1:
            color_map.append('turquoise')
        edges = G1.edges()
        colors = [G1[u][v]['color'] for u,v in edges]
        weights = [G1[u][v]['weight'] for u,v in edges]
        pos = nx.spring_layout(G1, k=16, scale=1)
        nx.draw(G1, pos, edges=edges, node_color = color_map, edge_color=colors, width=weights, font_size=16, with_labels=False)            
        for p in pos:  # raise text positions
            pos[p][1] += 0.1
        nx.draw_networkx_labels(G1, pos,font_size=16)
        plt.title('Network visualizing association rules',fontsize=20)
        plt.show()
        
    elif metric=='conviction':
        plt.figure(figsize=(12,8))
        G1 = nx.DiGraph()
        color_map=[]
        colors = 0.14035943    
        for i in range (rules_to_show):
            for a in rules.iloc[i]['antecedents']:        
                G1.add_nodes_from(nodes_for_adding=[a])
                for c in rules.iloc[i]['consequents']:     
                    G1.add_nodes_from(nodes_for_adding=[c])
                    G1.add_edge(a, c, color=colors,  weight= rules.iloc[i,-1])
        for node in G1:
            color_map.append('turquoise')
        edges = G1.edges()
        colors = [G1[u][v]['color'] for u,v in edges]
        weights = [G1[u][v]['weight'] for u,v in edges]
        pos = nx.spring_layout(G1, k=16, scale=1)
        nx.draw(G1, pos, edges=edges, node_color = color_map, edge_color=colors, width=weights, font_size=16, with_labels=False)            
        for p in pos:  # raise text positions
            pos[p][1] += 0.1
        nx.draw_networkx_labels(G1, pos,font_size=16)
        plt.title('Network visualizing association rules',fontsize=20)
        plt.show()

    elif metric=='confidence':
        plt.figure(figsize=(12,8))
        G1 = nx.DiGraph()
        color_map=[]
        colors = 0.14035943    
        for i in range (rules_to_show):
            for a in rules.iloc[i]['antecedents']:        
                G1.add_nodes_from(nodes_for_adding=[a])
                for c in rules.iloc[i]['consequents']:     
                    G1.add_nodes_from(nodes_for_adding=[c])
                    G1.add_edge(a, c, color=colors,  weight= (1+rules.iloc[i,5]))
        for node in G1:
            color_map.append('turquoise')
        edges = G1.edges()
        colors = [G1[u][v]['color'] for u,v in edges]
        weights = [G1[u][v]['weight'] for u,v in edges]
        pos = nx.spring_layout(G1, k=16, scale=1)
        nx.draw(G1, pos, edges=edges, node_color = color_map, edge_color=colors, width=weights, font_size=16, with_labels=False)            
        for p in pos:  # raise text positions
            pos[p][1] += 0.1
        nx.draw_networkx_labels(G1, pos,font_size=16)
        plt.title('Network visualizing association rules',fontsize=20)
        plt.show()

    elif metric=='support':
        plt.figure(figsize=(12,8))
        G1 = nx.DiGraph()
        color_map=[]
        colors = 0.14035943    
        for i in range (rules_to_show):
            for a in rules.iloc[i]['antecedents']:        
                G1.add_nodes_from(nodes_for_adding=[a])
                for c in rules.iloc[i]['consequents']:     
                    G1.add_nodes_from(nodes_for_adding=[c])
                    G1.add_edge(a, c, color=colors,  weight= (1+rules.iloc[i,4]))
        for node in G1:
            color_map.append('turquoise')
        edges = G1.edges()
        colors = [G1[u][v]['color'] for u,v in edges]
        weights = [G1[u][v]['weight'] for u,v in edges]
        pos = nx.spring_layout(G1, k=16, scale=1)
        nx.draw(G1, pos, edges=edges, node_color = color_map, edge_color=colors, width=weights, font_size=16, with_labels=False)            
        for p in pos:  # raise text positions
            pos[p][1] += 0.1
        nx.draw_networkx_labels(G1, pos,font_size=16)
        plt.title('Network visualizing association rules',fontsize=20)
        plt.show()

    else:
        plt.figure(figsize=(12,8))
        G1 = nx.DiGraph()
        color_map=[]
        colors = 0.14035943    
        for i in range (rules_to_show):
            for a in rules.iloc[i]['antecedents']:        
                G1.add_nodes_from(nodes_for_adding=[a])
                for c in rules.iloc[i]['consequents']:     
                    G1.add_nodes_from(nodes_for_adding=[c])
                    G1.add_edge(a, c, color=colors,  weight= 2)
        for node in G1:
            color_map.append('turquoise')
        edges = G1.edges()
        colors = [G1[u][v]['color'] for u,v in edges]
        weights = [G1[u][v]['weight'] for u,v in edges]
        pos = nx.spring_layout(G1, k=16, scale=1)
        nx.draw(G1, pos, edges=edges, node_color = color_map, edge_color=colors, width=weights, font_size=16, with_labels=False)            
        for p in pos:  # raise text positions
            pos[p][1] += 0.1
        nx.draw_networkx_labels(G1, pos,font_size=16)
        plt.title('Network visualizing association rules',fontsize=20)
        plt.show()