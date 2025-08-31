import json

# --- Core Collatz and Automaton Functions ---
def v2(n):
    if n == 0: return 0
    return (n & -n).bit_length() - 1

def f(n):
    if n is None or n % 2 == 0 or n <= 0: return None
    val = 3 * n + 1
    return val // (2 ** v2(val))

def phi(j):
    if j % 4 != 3: return None
    return v2(j + 1)

def get_state_classification(j, k):
    if j % 4 == 1: return "contractive"
    if j == 2**k - 1: return "highest"
    if j % 4 == 3: return "transitional"
    return "unknown"

def get_successor_state(j, m_parity, k):
    mod = 2**k
    n = mod * m_parity + j
    next_n = f(n)
    if next_n is None: return None
    return next_n % mod

def generate_data_for_k(k):
    """Generates all nodes and edges for a given k-bit automaton."""
    mod = 2**k
    nodes = []
    edges = []
    
    all_states = range(1, mod, 2)
    
    for j in all_states:
        # Node Data
        node_data = {
            'id': str(j),
            'label': f"S_{j}",
            'class': get_state_classification(j, k),
            'phi': phi(j) if get_state_classification(j, k) != "contractive" else None
        }
        nodes.append({'data': node_data})
        
        # Edge Data
        for m_parity in [0, 1]:
            j_prime = get_successor_state(j, m_parity, k)
            if j_prime is not None:
                edge_data = {
                    'source': str(j),
                    'target': str(j_prime),
                    'm_parity': 'even' if m_parity == 0 else 'odd'
                }
                edges.append({'data': edge_data})
                
    return {'nodes': nodes, 'edges': edges}

def main():
    """Main function to generate data for all k and save to a JS file."""
    print("Generating graph data for k=2 to k=12...")
    
    all_graph_data = {}
    for k in range(2, 13):
        print(f"  - Processing k={k}...")
        all_graph_data[k] = generate_data_for_k(k)
        
    # Write to a JavaScript file to be easily included in the HTML
    with open('graph_data.js', 'w') as f:
        f.write('const graphData = ')
        json.dump(all_graph_data, f, indent=2)
        f.write(';')
        
    print("\n✅ Success! Data saved to 'graph_data.js'")

if __name__ == '__main__':
    main()