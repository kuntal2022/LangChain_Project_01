import streamlit as st

st.set_page_config(
    page_title="AI Model Pricing Guide",
    page_icon="💰",
    layout="wide"
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .main { background: #0f0f13; }
    .block-container { padding-top: 2rem; max-width: 1400px; }

    /* Hero */
    .hero {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border: 1px solid #2a2a4a;
        border-radius: 16px;
        padding: 2rem 2.5rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    .hero h1 { font-size: 2.4rem; font-weight: 700; color: #e2e8f0; margin: 0 0 .4rem; }
    .hero p  { color: #94a3b8; font-size: 1rem; margin: 0; }

    /* Provider header */
    .provider-header {
        padding: .9rem 1.4rem;
        border-radius: 12px 12px 0 0;
        font-size: 1.15rem;
        font-weight: 700;
        letter-spacing: .03em;
        margin-top: 1.8rem;
    }
    .openai-header  { background: linear-gradient(90deg,#10a37f,#0d8a6b); color:#fff; }
    .groq-header    { background: linear-gradient(90deg,#f55036,#c73b22); color:#fff; }
    .gemini-header  { background: linear-gradient(90deg,#4285f4,#1a73e8); color:#fff; }
    .sarvam-header  { background: linear-gradient(90deg,#ff6b35,#e63e2a); color:#fff; }
    .hf-header      { background: linear-gradient(90deg,#ff9d00,#e08800); color:#fff; }

    /* Section badge */
    .section-badge {
        display: inline-block;
        padding: .25rem .75rem;
        border-radius: 20px;
        font-size: .75rem;
        font-weight: 600;
        margin: .6rem 0 .3rem;
        letter-spacing: .05em;
        text-transform: uppercase;
    }
    .badge-chat      { background:#1e3a2f; color:#4ade80; border:1px solid #2d5a3d; }
    .badge-embed     { background:#1e2a3a; color:#60a5fa; border:1px solid #2d3f5a; }
    .badge-audio     { background:#3a1e2f; color:#f472b6; border:1px solid #5a2d3f; }
    .badge-image     { background:#3a2a1e; color:#fb923c; border:1px solid #5a3d2d; }

    /* Dataframe overrides */
    .stDataFrame { border-radius: 0 0 10px 10px !important; overflow: hidden; }

    /* Note box */
    .note-box {
        background: #1e1e2e;
        border-left: 4px solid #7c3aed;
        border-radius: 0 8px 8px 0;
        padding: .7rem 1rem;
        font-size: .82rem;
        color: #94a3b8;
        margin-top: .5rem;
    }

    /* HF card */
    .hf-card {
        background: #1a1a2e;
        border: 1px solid #2a2a4a;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        margin-bottom: .8rem;
    }
    .hf-card h4 { color: #e2e8f0; font-size: .95rem; margin: 0 0 .4rem; font-family: 'JetBrains Mono', monospace; }
    .hf-card p  { color: #94a3b8; font-size: .82rem; margin: 0; line-height: 1.5; }
    .hf-tag {
        display: inline-block; background: #2a1e3a; color: #c084fc;
        border: 1px solid #4a2d6a; border-radius: 4px;
        padding: .15rem .5rem; font-size: .72rem; font-weight: 600; margin-right: .3rem;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { background: #1a1a2e; border-radius: 10px; gap: 4px; padding: 4px; }
    .stTabs [data-baseweb="tab"] { color: #94a3b8; border-radius: 8px; }
    .stTabs [aria-selected="true"] { background: #2a2a4a !important; color: #e2e8f0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Helpers ─────────────────────────────────────────────────────────────────
import pandas as pd

def show_table(df):
    st.dataframe(df, use_container_width=True, hide_index=True)

def badge(label, cls):
    st.markdown(f'<span class="section-badge {cls}">{label}</span>', unsafe_allow_html=True)

def note(text):
    st.markdown(f'<div class="note-box">ℹ️ {text}</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════════════════════════

# ── OpenAI ──────────────────────────────────────────────────────────────────
openai_chat = pd.DataFrame({
    "Model": ["GPT-4o", "GPT-4o Mini", "GPT-4.1", "GPT-4.1 Mini", "o4-mini"],
    "Model String (copy-paste)": ["gpt-4o", "gpt-4o-mini", "gpt-4.1", "gpt-4.1-mini", "o4-mini"],
    "Input ($/1M tokens)": ["$2.50", "$0.15", "$2.00", "$0.40", "$1.10"],
    "Output ($/1M tokens)": ["$10.00", "$0.60", "$8.00", "$1.60", "$4.40"],
    "Context Window": ["128K", "128K", "1M", "1M", "200K"],
    "Best For": ["Complex tasks", "Cost-effective chat", "Long context tasks", "Budget long context", "Reasoning tasks"],
})

openai_embed = pd.DataFrame({
    "Model": ["Text Embedding 3 Small", "Text Embedding 3 Large", "Text Embedding Ada 002"],
    "Model String (copy-paste)": ["text-embedding-3-small", "text-embedding-3-large", "text-embedding-ada-002"],
    "Cost ($/1M tokens)": ["$0.02", "$0.13", "$0.10"],
    "Batch Cost ($/1M tokens)": ["$0.01", "$0.065", "$0.05"],
    "Dimensions": ["1536", "3072", "1536"],
    "Notes": ["Best value ✅", "Highest quality", "Legacy – avoid"],
})

openai_audio = pd.DataFrame({
    "Model": ["Whisper", "GPT-4o Transcribe", "GPT-4o Mini Transcribe", "TTS Standard", "TTS HD", "GPT-4o Mini TTS"],
    "Model String (copy-paste)": ["whisper-1", "gpt-4o-transcribe", "gpt-4o-mini-transcribe", "tts-1", "tts-1-hd", "gpt-4o-mini-tts"],
    "Type": ["Speech-to-Text", "Speech-to-Text", "Speech-to-Text", "Text-to-Speech", "Text-to-Speech", "Text-to-Speech"],
    "Cost": ["$0.006/min", "$0.006/min", "$0.003/min", "$15/1M chars", "$30/1M chars", "$0.60 in + $12 audio out /1M tok"],
    "Notes": ["Legacy reliable model", "Best accuracy + diarization", "Budget STT", "Standard quality", "HD / Professional", "Token-based, latest model"],
})

openai_image = pd.DataFrame({
    "Model": ["DALL·E 3 (1024×1024)", "DALL·E 3 (1792×1024)", "DALL·E 2 (1024×1024)", "GPT-Image-1 (Low)", "GPT-Image-1 (Med)", "GPT-Image-1 (High)"],
    "Model String (copy-paste)": ["dall-e-3", "dall-e-3", "dall-e-2", "gpt-image-1", "gpt-image-1", "gpt-image-1"],
    "Cost per Image": ["$0.040", "$0.080", "$0.020", "$0.011", "$0.042", "$0.167"],
    "Notes": ["Standard HD", "Wide HD", "Budget option", "Fast generation", "Balanced", "Best quality"],
})

# ── Groq ────────────────────────────────────────────────────────────────────
groq_chat = pd.DataFrame({
    "Model": ["Llama 3.1 8B", "Llama 3.3 70B", "Llama 4 Scout", "Qwen3 32B", "GPT-OSS 20B", "GPT-OSS 120B"],
    "Model String (copy-paste)": ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "meta-llama/llama-4-scout-17b-16e-instruct", "qwen/qwen3-32b", "gpt-oss-20b", "gpt-oss-120b"],
    "Input ($/1M tokens)": ["$0.05", "$0.59", "$0.11", "$0.29", "$0.10", "$0.90"],
    "Output ($/1M tokens)": ["$0.08", "$0.79", "$0.34", "$0.59", "$0.40", "$0.90"],
    "Speed": ["~680 tok/s 🔥", "~330 tok/s", "~450 tok/s", "~400 tok/s", "~950 tok/s 🔥", "~200 tok/s"],
    "Best For": ["Budget + speed", "Quality + speed", "Multimodal", "Balanced", "Ultra fast", "High intelligence"],
})

groq_embed = pd.DataFrame({
    "Status": ["❌ Not Available"],
    "Notes": ["Groq is inference-only. No native embedding API. Use OpenAI / HuggingFace for embeddings."],
})

groq_audio = pd.DataFrame({
    "Model": ["Whisper Large v3", "PlayAI Dialog v1.0 (TTS)"],
    "Model String (copy-paste)": ["whisper-large-v3", "playai-tts-arabic"],
    "Type": ["Speech-to-Text", "Text-to-Speech"],
    "Cost": ["$0.111/hour audio", "$50/1M characters"],
    "Notes": ["Fast transcription on LPU", "Conversational TTS"],
})

groq_image = pd.DataFrame({
    "Status": ["❌ Not Available"],
    "Notes": ["Groq does not offer image generation. Use OpenAI DALL·E or Google Gemini Image."],
})

# ── Google Gemini ────────────────────────────────────────────────────────────
gemini_chat = pd.DataFrame({
    "Model": ["Gemini 2.5 Flash-Lite", "Gemini 2.5 Flash", "Gemini 2.5 Pro", "Gemini 3 Flash Preview", "Gemini 3 Pro Preview"],
    "Model String (copy-paste)": ["gemini-2.5-flash-lite", "gemini-2.5-flash", "gemini-2.5-pro", "gemini-3.0-flash-preview", "gemini-3.0-pro-preview"],
    "Input ($/1M tokens)": ["$0.10", "$0.30", "$1.25", "$0.50", "$2.00"],
    "Output ($/1M tokens)": ["$0.40", "$2.50", "$10.00", "$3.00", "$12.00"],
    "Context Window": ["1M", "1M", "1M (>200K costs 2x)", "1M", "1M"],
    "Best For": ["High volume / cheap", "Best value workhorse", "Complex reasoning", "Balanced next-gen", "Frontier tasks"],
})

gemini_embed = pd.DataFrame({
    "Model": ["Gemini Embedding 001", "Gemini Embedding 2 Preview"],
    "Model String (copy-paste)": ["models/embedding-001", "models/gemini-embedding-exp-03-07"],
    "Cost ($/1M tokens)": ["$0.15", "$0.20"],
    "Batch Cost ($/1M tokens)": ["$0.075", "$0.10"],
    "Notes": ["Stable production model", "Latest – image/audio support too"],
})

gemini_audio = pd.DataFrame({
    "Model": ["Gemini 2.5 Flash TTS", "Gemini 2.5 Pro TTS", "Gemini 2.5 Flash (audio input)"],
    "Model String (copy-paste)": ["gemini-2.5-flash-preview-tts", "gemini-2.5-pro-preview-tts", "gemini-2.5-flash"],
    "Type": ["Text-to-Speech", "Text-to-Speech", "Speech-to-Text (via multimodal)"],
    "Input Cost": ["$0.50/1M tok", "$1.00/1M tok", "$1.00/1M audio tok"],
    "Output Cost": ["$10.00/1M audio tok", "$20.00/1M audio tok", "—"],
    "Notes": ["Budget TTS", "High quality TTS", "25 tokens/sec of audio"],
})

gemini_image = pd.DataFrame({
    "Model": ["Gemini 3 Pro Image", "Gemini 3.1 Flash Image"],
    "Image Input": ["560 tokens/image", "1120 tokens/image"],
    "Output – 1K ($/image)": ["$0.134", "$0.067"],
    "Output – 2K ($/image)": ["$0.134", "$0.101"],
    "Output – 4K ($/image)": ["$0.240", "$0.151"],
    "Notes": ["Highest quality", "Fast & affordable"],
})

# ── Sarvam ───────────────────────────────────────────────────────────────────
sarvam_chat = pd.DataFrame({
    "Model": ["Sarvam-M", "Sarvam-2B", "Sarvam-30B", "Sarvam-105B"],
    "Model String (copy-paste)": ["sarvam-m", "sarvam-2b", "sarvam-30b", "sarvam-105b"],
    "Input ($/1M tokens)": ["~$0.20*", "~$0.10*", "~$0.40*", "~$0.70*"],
    "Context Window": ["32K", "8K", "16K", "32K"],
    "Languages": ["English + 11 Indic", "10 Indic", "10 Indic", "10 Indic"],
    "Notes": ["Best for Indian lang chat", "Lightweight", "Balanced", "Highest quality Indic"],
})

sarvam_embed = pd.DataFrame({
    "Status": ["❌ Not Available"],
    "Notes": ["Sarvam does not offer dedicated embedding models currently. Use HuggingFace multilingual models like LaBSE or paraphrase-multilingual-MiniLM for Indic language embeddings."],
})

sarvam_audio = pd.DataFrame({
    "Service": ["Saaras STT", "Saaras STT + Diarization", "Saaras STT + Translation", "Bulbul TTS v2", "Bulbul TTS v3"],
    "Model String (copy-paste)": ["saaras:v2", "saaras:v2", "saaras:v2.5", "bulbul:v2", "bulbul:v3"],
    "Type": ["STT", "STT", "STT + Translate", "TTS", "TTS"],
    "Cost": ["₹30/hr (~$0.35/hr)", "₹44/hr (~$0.53/hr)", "₹30/hr (~$0.35/hr)", "₹15/10K chars (~$0.18)", "₹30/10K chars (~$0.35)"],
    "Languages": ["10 Indic + English", "10 Indic + English", "→ English output", "6 Indian voices", "10+ Indian voices"],
})

sarvam_image = pd.DataFrame({
    "Service": ["Vision API (image understanding)"],
    "Cost": ["Rate limited; credits-based"],
    "Notes": ["Understands images with Indic language context. No image generation."],
})

# ── HuggingFace Embedding Models ────────────────────────────────────────────
hf_models = [
    {
        "model_id": "sentence-transformers/all-MiniLM-L6-v2",
        "dims": "384",
        "size": "80MB",
        "cost": "FREE (local)",
        "best_for": "Semantic search, clustering, lightweight RAG",
        "tags": ["English", "Fast", "Lightweight", "Most Popular"],
    },
    {
        "model_id": "sentence-transformers/all-mpnet-base-v2",
        "dims": "768",
        "size": "420MB",
        "cost": "FREE (local)",
        "best_for": "High quality sentence embeddings, semantic similarity",
        "tags": ["English", "High Quality", "Balanced"],
    },
    {
        "model_id": "BAAI/bge-base-en-v1.5",
        "dims": "768",
        "size": "440MB",
        "cost": "FREE (local)",
        "best_for": "Retrieval, RAG pipelines, ranking tasks",
        "tags": ["English", "RAG ✅", "MTEB Top Performer"],
    },
    {
        "model_id": "BAAI/bge-large-en-v1.5",
        "dims": "1024",
        "size": "1.3GB",
        "cost": "FREE (local)",
        "best_for": "Best English retrieval quality, production RAG",
        "tags": ["English", "Large", "Highest Accuracy"],
    },
    {
        "model_id": "BAAI/bge-m3",
        "dims": "1024",
        "size": "2.3GB",
        "cost": "FREE (local)",
        "best_for": "Multilingual retrieval (100+ languages), long documents",
        "tags": ["Multilingual 🌍", "Long Context", "Dense+Sparse"],
    },
    {
        "model_id": "intfloat/e5-base-v2",
        "dims": "768",
        "size": "440MB",
        "cost": "FREE (local)",
        "best_for": "General purpose retrieval, passage/query embedding",
        "tags": ["English", "E5 Family", "Query-optimized"],
    },
    {
        "model_id": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "dims": "384",
        "size": "470MB",
        "cost": "FREE (local)",
        "best_for": "Multilingual paraphrase, cross-lingual similarity, Indic languages",
        "tags": ["Multilingual 🌍", "Indic Support", "Lightweight"],
    },
    {
        "model_id": "nomic-ai/nomic-embed-text-v1",
        "dims": "768",
        "size": "548MB",
        "cost": "FREE (local)",
        "best_for": "Long document embedding (8192 tokens), open alternative to OpenAI ada",
        "tags": ["English", "Long Context 8K", "Open Source"],
    },
    {
        "model_id": "l3cube-pune/indic-sentence-bert-nli",
        "dims": "768",
        "size": "~440MB",
        "cost": "FREE (local)",
        "best_for": "Indian language NLI and semantic similarity tasks",
        "tags": ["Indic Languages 🇮🇳", "Hindi", "Marathi", "Bengali"],
    },
]

# ═══════════════════════════════════════════════════════════════════════════
# UI
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero">
    <h1>💰 AI Model Pricing Reference</h1>
    <p>OpenAI · Groq · Google Gemini · Sarvam AI · HuggingFace Embeddings &nbsp;|&nbsp; Prices per 1M tokens (USD) · Updated Apr 2026</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🟢 OpenAI", "🔴 Groq", "🔵 Google Gemini", "🟠 Sarvam AI", "🤗 HuggingFace Embeds"
])

# ───────────────────────────── OpenAI ───────────────────────────────────────
with tab1:
    st.markdown('<div class="provider-header openai-header">🟢 OpenAI Pricing</div>', unsafe_allow_html=True)

    badge("💬 Chat / LLM Models", "badge-chat")
    show_table(openai_chat)
    note("Pricing as of Apr 2026. Batch API gives 50% discount on most models.")

    badge("🔷 Embedding Models", "badge-embed")
    show_table(openai_embed)
    note("Embedding only charges input tokens. No output tokens billed.")

    badge("🎵 Audio Models", "badge-audio")
    show_table(openai_audio)
    note("Whisper = $0.006/min. TTS Standard = $15/1M chars. TTS HD = $30/1M chars.")

    badge("🖼️ Image Generation", "badge-image")
    show_table(openai_image)
    note("GPT-Image-1 (gpt-image-1) is newer than DALL·E 3 with better instruction following.")

# ───────────────────────────── Groq ─────────────────────────────────────────
with tab2:
    st.markdown('<div class="provider-header groq-header">🔴 Groq Pricing</div>', unsafe_allow_html=True)

    badge("💬 Chat / LLM Models", "badge-chat")
    show_table(groq_chat)
    note("Groq uses LPU (Language Processing Unit) — extremely fast inference. Batch API = 50% discount.")

    badge("🔷 Embedding Models", "badge-embed")
    show_table(groq_embed)

    badge("🎵 Audio Models", "badge-audio")
    show_table(groq_audio)
    note("Whisper Large v3 at $0.111/hr is one of the cheapest STT options available.")

    badge("🖼️ Image Generation", "badge-image")
    show_table(groq_image)

# ───────────────────────────── Gemini ───────────────────────────────────────
with tab3:
    st.markdown('<div class="provider-header gemini-header">🔵 Google Gemini Pricing</div>', unsafe_allow_html=True)

    badge("💬 Chat / LLM Models", "badge-chat")
    show_table(gemini_chat)
    note("Gemini has a generous FREE tier via AI Studio (up to 1500 req/day on Flash models). Pro models cost 2x for context > 200K tokens.")

    badge("🔷 Embedding Models", "badge-embed")
    show_table(gemini_embed)
    note("Gemini Embedding 001 = $0.15/1M tokens. Best for RAG pipelines on Google ecosystem.")

    badge("🎵 Audio Models", "badge-audio")
    show_table(gemini_audio)
    note("Audio input billed at 25 tokens/second. Audio costs 3-7x more than text depending on model.")

    badge("🖼️ Image Generation", "badge-image")
    show_table(gemini_image)
    note("Image output priced per token (1290 tokens ≈ 1024×1024 image). Gemini 3.1 Flash Image is fastest.")

# ───────────────────────────── Sarvam ───────────────────────────────────────
with tab4:
    st.markdown('<div class="provider-header sarvam-header">🟠 Sarvam AI Pricing (India-focused)</div>', unsafe_allow_html=True)

    badge("💬 Chat / LLM Models", "badge-chat")
    show_table(sarvam_chat)
    note("*Sarvam chat model pricing is credit-based (₹ credits). USD estimates are approximate. All plans start with ₹1,000 free credits.")

    badge("🔷 Embedding Models", "badge-embed")
    show_table(sarvam_embed)

    badge("🎵 Audio Models (STT + TTS)", "badge-audio")
    show_table(sarvam_audio)
    note("Sarvam excels in Indian language ASR/TTS. Bulbul TTS supports 10+ Indian voices. Saaras STT supports 10 Indic languages.")

    badge("🖼️ Vision / Image", "badge-image")
    show_table(sarvam_image)
    note("Sarvam Vision understands images with Indic context. Not a generative image model.")

# ───────────────────────────── HuggingFace ──────────────────────────────────
with tab5:
    st.markdown('<div class="provider-header hf-header">🤗 HuggingFace Embedding Models (Free / Local)</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="note-box" style="margin-bottom:1.2rem">
    📦 All models listed below are <b>FREE</b> — run locally or via HuggingFace Inference API.
    LangChain usage: <code>from langchain_huggingface import HuggingFaceEmbeddings</code>
    </div>
    """, unsafe_allow_html=True)

    # Quick comparison table
    hf_table = pd.DataFrame([{
        "Model ID": m["model_id"],
        "Dimensions": m["dims"],
        "Size": m["size"],
        "Cost": m["cost"],
        "Best For": m["best_for"],
    } for m in hf_models])

    st.markdown("#### 📊 Quick Comparison Table")
    show_table(hf_table)

    st.markdown("---")
    st.markdown("#### 📦 Detailed Cards")

    col1, col2 = st.columns(2)
    for i, m in enumerate(hf_models):
        col = col1 if i % 2 == 0 else col2
        tags_html = " ".join(f'<span class="hf-tag">{t}</span>' for t in m["tags"])
        with col:
            st.markdown(f"""
            <div class="hf-card">
                <h4>📌 {m['model_id']}</h4>
                <p>{tags_html}</p>
                <p style="margin-top:.5rem">🎯 {m['best_for']}<br>
                📐 Dims: <b>{m['dims']}</b> &nbsp;|&nbsp; 💾 Size: <b>{m['size']}</b> &nbsp;|&nbsp; 💰 <b>{m['cost']}</b></p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="note-box" style="margin-top:1rem">
    🇮🇳 <b>Recommended for Indic Language RAG:</b> <code>BAAI/bge-m3</code> (multilingual) or 
    <code>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</code> (lightweight Indic support)
    </div>
    """, unsafe_allow_html=True)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<p style="text-align:center;color:#475569;font-size:.8rem">'
    '⚠️ Prices are approximate and change frequently. Always verify on official provider websites before production use.<br>'
    '🔗 OpenAI: openai.com/api/pricing &nbsp;|&nbsp; Groq: groq.com/pricing &nbsp;|&nbsp; Gemini: ai.google.dev/gemini-api/docs/pricing &nbsp;|&nbsp; Sarvam: sarvam.ai/api-pricing'
    '</p>',
    unsafe_allow_html=True
)