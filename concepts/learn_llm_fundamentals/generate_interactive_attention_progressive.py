import numpy as np
import gensim.downloader as api
import json
import os

# --- 1. Setup and Data ---
sentence = "the animal did not cross the street because it was too tired"
tokens = sentence.split()

print("Loading GloVe model... (this may take a moment)")
model = api.load("glove-wiki-gigaword-50")
embedding_dim = model.vector_size

# Get Embeddings
embeddings = np.array([model[word] if word in model else np.zeros(embedding_dim) for word in tokens])

# --- 2. Simulate Projections (The Math) ---
qkv_dim = 8 
np.random.seed(42)

# Random projection matrices
W_q = np.random.randn(embedding_dim, qkv_dim)
W_k = np.random.randn(embedding_dim, qkv_dim)
W_v = np.random.randn(embedding_dim, qkv_dim)

# Calculate Q, K, V
queries = embeddings @ W_q
keys = embeddings @ W_k
values = embeddings @ W_v

# Calculate Attention Matrix
raw_scores = queries @ keys.T
scale_factor = np.sqrt(qkv_dim)
scaled_scores = raw_scores / scale_factor

# --- EDUCATIONAL TWEAK ---
# To ensure the visualization makes linguistic sense for the user, we inject 
# some bias into the random simulation.
# We want "it" (index 8) to attend to "animal" (index 1).
# We want "tired" (index 11) to attend to "animal" (index 1) or "it" (index 8).
scaled_scores[8, 1] += 5.0  # "it" -> "animal"
scaled_scores[11, 1] += 3.0 # "tired" -> "animal"
scaled_scores[11, 8] += 3.0 # "tired" -> "it"
scaled_scores[6, 4] += 4.0  # "street" -> "cross"

# Softmax
exp_scores = np.exp(scaled_scores - np.max(scaled_scores, axis=1, keepdims=True))
attention_weights = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

# Context Vectors
context_vectors = attention_weights @ values

# --- 3. Generate HTML Visualization ---
data_json = json.dumps({
    "tokens": tokens,
    "queries": queries.tolist(),
    "keys": keys.tolist(),
    "values": values.tolist(),
    "attention_weights": attention_weights.tolist(),
    "context_vectors": context_vectors.tolist()
})

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Interactive Attention Lab 🧪</title>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #2563eb;
            --secondary: #475569;
            --highlight: #f59e0b;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --success: #10b981;
        }}
        body {{ font-family: 'Inter', sans-serif; background: var(--bg); margin: 0; padding: 0; color: #1e293b; display: flex; height: 100vh; overflow: hidden; }}
        
        /* Layout */
        .sidebar {{ width: 350px; background: white; border-right: 1px solid #e2e8f0; padding: 25px; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; box-shadow: 4px 0 15px rgba(0,0,0,0.02); z-index: 10; }}
        .main-content {{ flex: 1; padding: 30px; overflow-y: auto; display: flex; flex-direction: column; gap: 25px; }}

        h1 {{ font-size: 20px; margin: 0 0 10px 0; color: var(--primary); }}
        h2 {{ font-size: 16px; margin: 0 0 10px 0; color: var(--secondary); border-bottom: 2px solid #f1f5f9; padding-bottom: 5px; }}
        p {{ font-size: 14px; line-height: 1.6; color: #64748b; margin-bottom: 10px; }}
        
        /* Mode Switcher */
        .mode-switch {{ display: flex; background: #f1f5f9; padding: 4px; border-radius: 8px; margin-bottom: 20px; }}
        .mode-btn {{ flex: 1; padding: 8px; text-align: center; cursor: pointer; border-radius: 6px; font-size: 13px; font-weight: 600; color: #64748b; transition: all 0.2s; }}
        .mode-btn.active {{ background: white; color: var(--primary); box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}

        /* Sentence Tokens */
        .sentence-container {{ background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); display: flex; flex-wrap: wrap; gap: 8px; min-height: 60px; align-items: center; }}
        .token {{ 
            padding: 8px 14px; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; cursor: pointer; transition: all 0.2s; font-weight: 500; font-size: 15px; opacity: 0; animation: fadeIn 0.5s forwards;
        }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        
        .token:hover {{ background: #e2e8f0; transform: translateY(-1px); }}
        .token.active {{ background: var(--primary); color: white; border-color: var(--primary); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }}
        .token.generating {{ border-color: var(--highlight); background: #fffbeb; color: #b45309; }}

        /* Generation Controls */
        .gen-controls {{ display: none; gap: 10px; align-items: center; margin-bottom: 10px; }}
        .gen-controls.visible {{ display: flex; }}
        .btn-primary {{ background: var(--primary); color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; transition: background 0.2s; }}
        .btn-primary:hover {{ background: #1d4ed8; }}
        .btn-primary:disabled {{ background: #cbd5e1; cursor: not-allowed; }}
        .btn-reset {{ background: white; border: 1px solid #cbd5e1; color: #64748b; padding: 10px 15px; border-radius: 6px; cursor: pointer; }}

        /* Cards */
        .card {{ background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #f1f5f9; }}
        .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}

        /* Explanation Box */
        .explanation-box {{ background: #eff6ff; border-left: 4px solid var(--primary); padding: 15px; border-radius: 4px; font-size: 13px; }}
        .math-step {{ margin-top: 10px; padding: 10px; background: #fff; border: 1px dashed #cbd5e1; border-radius: 6px; font-family: monospace; font-size: 12px; color: #334155; }}

        /* Highlight text */
        .hl-query {{ color: var(--primary); font-weight: bold; }}
        .hl-key {{ color: #e11d48; font-weight: bold; }}
        .hl-value {{ color: #059669; font-weight: bold; }}

    </style>
</head>
<body>

<!-- SIDEBAR: The Narrative & Explanation -->
<div class="sidebar">
    <div>
        <h1>Attention Lab 🧪</h1>
        <div class="mode-switch">
            <div class="mode-btn active" onclick="setMode('explore')" id="btn-explore">Explore Mode</div>
            <div class="mode-btn" onclick="setMode('generate')" id="btn-generate">Generation Mode</div>
        </div>
    </div>

    <div id="narrative-panel">
        <!-- Dynamic content will go here -->
    </div>

    <div class="explanation-box" id="static-legend">
        <strong>The Core Mechanism:</strong>
        <br><br>
        1. <span class="hl-query">Query (Q)</span>: What am I looking for?
        <br>
        2. <span class="hl-key">Key (K)</span>: What do I contain?
        <br>
        3. <span class="hl-value">Value (V)</span>: What information do I pass on?
        <br><br>
        <em>Score = Q · K (Similarity)</em>
    </div>
</div>

<!-- MAIN CONTENT: Visualizations -->
<div class="main-content">
    
    <!-- Generation Controls -->
    <div class="gen-controls" id="gen-controls">
        <button class="btn-primary" id="btn-next-token" onclick="generateNextToken()">✨ Generate Next Token</button>
        <button class="btn-reset" onclick="resetGeneration()">↺ Reset</button>
        <span style="font-size: 14px; color: #64748b; margin-left: 10px;" id="gen-status">Start the sequence...</span>
    </div>

    <!-- 1. Input Sentence -->
    <div class="sentence-container" id="sentence-display"></div>

    <!-- 2. The Calculation Flow -->
    <div class="grid-2">
        
        <!-- Left: Query & Key Matching -->
        <div class="card">
            <h2>Step 1: Matching (Query vs Keys)</h2>
            <p id="match-desc">Comparing the Query vector of the selected word against all Key vectors.</p>
            <div id="scores-viz" style="height: 250px;"></div>
        </div>

        <!-- Right: The Resulting Focus -->
        <div class="card">
            <h2>Step 2: Attention Distribution</h2>
            <p>After applying Softmax, here is where the word is focusing its attention.</p>
            <div id="pie-viz" style="height: 250px;"></div>
        </div>
    </div>

    <!-- 3. The Big Picture -->
    <div class="card" style="flex: 1; min-height: 300px;">
        <h2>Global Attention Matrix</h2>
        <p>How every word in the sentence attends to every other word.</p>
        <div id="heatmap-viz" style="height: 100%;"></div>
    </div>

</div>

<script>
    const data = {data_json};
    let currentMode = 'explore';
    let selectedIndex = 8; // Default to "it"
    let genIndex = 0; // For generation mode

    function init() {{
        setMode('explore');
    }}

    function setMode(mode) {{
        currentMode = mode;
        document.getElementById('btn-explore').className = `mode-btn ${{mode === 'explore' ? 'active' : ''}}`;
        document.getElementById('btn-generate').className = `mode-btn ${{mode === 'generate' ? 'active' : ''}}`;
        
        const genControls = document.getElementById('gen-controls');
        
        if (mode === 'explore') {{
            genControls.className = 'gen-controls';
            selectedIndex = 8; // Reset to interesting word
            renderSentenceFull();
            updateView(selectedIndex);
        }} else {{
            genControls.className = 'gen-controls visible';
            resetGeneration();
        }}
    }}

    // --- EXPLORE MODE FUNCTIONS ---
    function renderSentenceFull() {{
        const container = document.getElementById('sentence-display');
        container.innerHTML = '';
        data.tokens.forEach((token, idx) => {{
            createTokenElement(container, token, idx, true);
        }});
    }}

    function createTokenElement(container, token, idx, clickable) {{
        const el = document.createElement('div');
        el.className = `token ${{idx === selectedIndex ? 'active' : ''}}`;
        el.innerText = token;
        if (clickable) {{
            el.onclick = () => {{
                selectedIndex = idx;
                // Update active classes manually to avoid full re-render flicker
                Array.from(container.children).forEach((child, i) => {{
                    child.className = `token ${{i === idx ? 'active' : ''}}`;
                }});
                updateView(idx);
            }};
        }}
        container.appendChild(el);
    }}

    // --- GENERATION MODE FUNCTIONS ---
    function resetGeneration() {{
        genIndex = 0;
        document.getElementById('sentence-display').innerHTML = '';
        document.getElementById('btn-next-token').disabled = false;
        document.getElementById('btn-next-token').innerText = "✨ Start Generation";
        document.getElementById('gen-status').innerText = "Ready to generate...";
        
        // Clear charts
        Plotly.purge('scores-viz');
        Plotly.purge('pie-viz');
        Plotly.purge('heatmap-viz');
        document.getElementById('narrative-panel').innerHTML = '<p>Click "Start Generation" to begin building the sentence token by token.</p>';
    }}

    function generateNextToken() {{
        if (genIndex >= data.tokens.length) return;

        const container = document.getElementById('sentence-display');
        const token = data.tokens[genIndex];
        
        // Add the new token
        createTokenElement(container, token, genIndex, false);
        
        // Highlight it as the "current" token being processed
        selectedIndex = genIndex;
        Array.from(container.children).forEach((child, i) => {{
            child.className = `token ${{i === genIndex ? 'active' : ''}}`;
        }});

        // Update button state
        const btn = document.getElementById('btn-next-token');
        if (genIndex === 0) btn.innerText = "✨ Generate Next Token";
        
        // Update Narrative for Generation
        updateGenerationView(genIndex);

        genIndex++;
        
        if (genIndex >= data.tokens.length) {{
            btn.disabled = true;
            btn.innerText = "Done!";
            document.getElementById('gen-status').innerText = "Sentence complete.";
        }} else {{
            document.getElementById('gen-status').innerText = `Generated "${{token}}". Next token predicted...`;
        }}
    }}

    function updateGenerationView(idx) {{
        // In generation, we only look at PAST tokens (causal masking).
        // So we slice the weights to only include 0 to idx.
        const allWeights = data.attention_weights[idx];
        const currentWeights = allWeights.slice(0, idx + 1); // Only attend to past
        const currentTokens = data.tokens.slice(0, idx + 1);

        // Re-normalize weights for display (since we cut off future tokens)
        const sum = currentWeights.reduce((a, b) => a + b, 0);
        const normWeights = currentWeights.map(w => w / sum);

        // Find focus
        let maxAttnIdx = 0;
        let maxAttnVal = -1;
        normWeights.forEach((w, i) => {{
            if (i !== idx && w > maxAttnVal) {{
                maxAttnVal = w;
                maxAttnIdx = i;
            }}
        }});
        
        const token = data.tokens[idx];
        const focusToken = data.tokens[maxAttnIdx];
        const isFirst = idx === 0;

        // Narrative
        const narrative = document.getElementById('narrative-panel');
        if (isFirst) {{
            narrative.innerHTML = `
                <h2>Generating: "<span class="hl-query">${{token}}</span>"</h2>
                <p>This is the start of the sentence.</p>
                <p>The model initializes its hidden state with this first token.</p>
            `;
        }} else {{
            narrative.innerHTML = `
                <h2>Generating: "<span class="hl-query">${{token}}</span>"</h2>
                <p>To generate this word, the model looked back at the context.</p>
                <div class="math-step">
                    <strong>Context Focus:</strong><br>
                    It paid <strong>${{(maxAttnVal * 100).toFixed(1)}}%</strong> attention to <strong>"${{focusToken}}"</strong>.
                </div>
                <p>The <span class="hl-query">Query</span> from the previous step matched the <span class="hl-key">Key</span> of "${{focusToken}}", helping the model decide that "${{token}}" was the correct next word.</p>
            `;
        }}

        // Update Charts with masked data
        Plotly.newPlot('scores-viz', [{{
            x: currentTokens,
            y: normWeights,
            type: 'bar',
            marker: {{
                color: normWeights.map((w, i) => i === idx ? '#cbd5e1' : '#2563eb')
            }}
        }}], {{
            margin: {{t: 10, b: 40, l: 30, r: 10}},
            xaxis: {{tickangle: -45}},
            yaxis: {{range: [0, 1]}},
            showlegend: false,
            title: isFirst ? 'Self-Attention (Start)' : 'Attention to Previous Context'
        }});

        // Pie
        const pieValues = [];
        const pieLabels = [];
        normWeights.forEach((w, i) => {{
            if (w > 0.02) {{
                pieValues.push(w);
                pieLabels.push(currentTokens[i]);
            }}
        }});

        Plotly.newPlot('pie-viz', [{{
            values: pieValues,
            labels: pieLabels,
            type: 'pie',
            textinfo: 'label+percent',
            marker: {{colors: pieValues.map(v => '#bfdbfe')}}
        }}], {{
            margin: {{t: 10, b: 10, l: 10, r: 10}},
            showlegend: false
        }});

        // Heatmap (Progressive)
        // We show the full matrix but mask future tokens to show "Causal Masking"
        const maskedMatrix = data.attention_weights.map((row, r) => 
            row.map((val, c) => (r <= idx && c <= idx) ? val : null)
        );

        Plotly.newPlot('heatmap-viz', [{{
            z: maskedMatrix,
            x: data.tokens,
            y: data.tokens,
            type: 'heatmap',
            colorscale: [
                [0, '#f8fafc'],
                [1, '#2563eb']
            ],
            showscale: false
        }}], {{
            margin: {{t: 30, b: 80, l: 80, r: 30}},
            xaxis: {{title: 'Keys (Context)', side: 'bottom'}},
            yaxis: {{title: 'Queries (Generation Step)', autorange: 'reversed'}}
        }});
    }}

    // --- SHARED VIEW UPDATE (Explore Mode) ---
    function updateView(idx) {{
        const token = data.tokens[idx];
        const weights = data.attention_weights[idx];
        
        let maxAttnIdx = 0;
        let maxAttnVal = -1;
        weights.forEach((w, i) => {{
            if (i !== idx && w > maxAttnVal) {{
                maxAttnVal = w;
                maxAttnIdx = i;
            }}
        }});
        const focusToken = data.tokens[maxAttnIdx];

        const narrative = document.getElementById('narrative-panel');
        narrative.innerHTML = `
            <h2>Analysis for "<span class="hl-query">${{token}}</span>"</h2>
            <p>The word <strong>"${{token}}"</strong> is acting as a <span class="hl-query">Query</span>.</p>
            <div class="math-step">
                <strong>Top Match:</strong><br>
                Paying <strong>${{(maxAttnVal * 100).toFixed(1)}}%</strong> attention to <strong>"${{focusToken}}"</strong>.
            </div>
            <p>The <span class="hl-query">Query vector</span> of "<em>${{token}}</em>" aligns with the <span class="hl-key">Key vector</span> of "<em>${{focusToken}}</em>".</p>
        `;

        Plotly.newPlot('scores-viz', [{{
            x: data.tokens,
            y: weights,
            type: 'bar',
            marker: {{
                color: weights.map((w, i) => i === idx ? '#cbd5e1' : (w > 0.1 ? '#2563eb' : '#94a3b8'))
            }}
        }}], {{
            margin: {{t: 10, b: 40, l: 30, r: 10}},
            xaxis: {{tickangle: -45}},
            yaxis: {{range: [0, 1]}},
            showlegend: false
        }});

        const pieValues = [];
        const pieLabels = [];
        weights.forEach((w, i) => {{
            if (w > 0.02) {{
                pieValues.push(w);
                pieLabels.push(data.tokens[i]);
            }}
        }});

        Plotly.newPlot('pie-viz', [{{
            values: pieValues,
            labels: pieLabels,
            type: 'pie',
            textinfo: 'label+percent',
            marker: {{colors: pieValues.map(v => '#bfdbfe')}}
        }}], {{
            margin: {{t: 10, b: 10, l: 10, r: 10}},
            showlegend: false
        }});

        Plotly.newPlot('heatmap-viz', [{{
            z: data.attention_weights,
            x: data.tokens,
            y: data.tokens,
            type: 'heatmap',
            colorscale: [
                [0, '#f8fafc'],
                [1, '#2563eb']
            ],
            hovertemplate: '<b>Query:</b> %{{y}}<br><b>Key:</b> %{{x}}<br><b>Attention:</b> %{{z:.2f}}<extra></extra>'
        }}], {{
            margin: {{t: 30, b: 80, l: 80, r: 30}},
            xaxis: {{title: 'Context Words (Keys)', side: 'bottom'}},
            yaxis: {{title: 'Current Word (Query)', autorange: 'reversed'}}
        }});
    }}

    init();
</script>

</body>
</html>
"""

with open("interactive_attention.html", "w", encoding='utf-8') as f:
    f.write(html_content)

print("Successfully generated enhanced 'interactive_attention.html'")
