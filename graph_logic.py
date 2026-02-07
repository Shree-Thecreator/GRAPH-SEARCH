import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def generate_math_plot(search_term):
    search_term = search_term.lower()
    fig, ax = plt.subplots(figsize=(6, 4))
    
    
    x = np.linspace(-10, 10, 400)
    
    # 1. Trigonometric Functions
    if any(t in search_term for t in ["sin", "cos", "tan", "sec", "cosec", "cot"]):
        x_trig = np.linspace(0, 2 * np.pi, 500)
        if "sin" in search_term: y = np.sin(x_trig)
        elif "cos" in search_term: y = np.cos(x_trig)
        elif "tan" in search_term: y = np.tan(x_trig)
        elif "sec" in search_term: y = 1/np.cos(x_trig)
        elif "cosec" in search_term: y = 1/np.sin(x_trig)
        elif "cot" in search_term: y = 1/np.tan(x_trig)
        
       
        y[np.abs(y) > 10] = np.nan
        ax.plot(x_trig, y, label=f"y = {search_term}")
        ax.set_ylim(-10, 10)

   
    elif "quadratic" in search_term or "x^2" in search_term:
        ax.plot(x, x**2, label="y = x²")
    elif "cubic" in search_term or "x^3" in search_term:
        ax.plot(x, x**3, label="y = x³")
    elif "exp" in search_term:
        ax.plot(x, np.exp(x), label="y = e^x")
        ax.set_ylim(0, 50)
    elif "log" in search_term:
        x_log = np.linspace(0.1, 10, 400)
        ax.plot(x_log, np.log(x_log), label="y = ln(x)")
    elif "sigmoid" in search_term:
        y = 1 / (1 + np.exp(-x))
        ax.plot(x, y, label="Sigmoid")
    elif "bell" in search_term or "normal" in search_term:
        y = (1/np.sqrt(2*np.pi)) * np.exp(-0.5*x**2)
        ax.plot(x, y, label="Normal Distribution")

    
    elif "o(n log n)" in search_term:
        x_dsa = np.linspace(1, 20, 100)
        ax.plot(x_dsa, x_dsa * np.log2(x_dsa), label="O(n log n)")
    elif "o(log n)" in search_term:
        x_dsa = np.linspace(1, 20, 100)
        ax.plot(x_dsa, np.log2(x_dsa), label="O(log n)")

    else:
        return None

    ax.grid(True, linestyle='--', alpha=0.7)
    ax.axhline(y=0, color='black', linewidth=1)
    ax.axvline(x=0, color='black', linewidth=1)
    ax.legend()
    return fig

def generate_graph(search_term):
    """Generates the interactive Node graph based on the curve."""
    
    G = nx.Graph()
    points = 25
    x_vals = np.linspace(-5, 5, points)
    
   
    for i, x in enumerate(x_vals):
       
        label_val = f"{x:.1f}"
        G.add_node(i, label=label_val, title=f"Point {i}")
        if i > 0:
            G.add_edge(i, i-1)
    return G