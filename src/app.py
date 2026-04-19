import streamlit as st
import requests
import base64

# --- Base64 Image Loader ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

hero_bg_path = r"C:\Users\devan\.gemini\antigravity\brain\9f3a143b-df66-4d07-9a71-81d1cda2e72b\futuristic_zomato_hero_1776550012013.png"
hero_bg_b64 = get_base64_of_bin_file(hero_bg_path)

food_img_paths = [
    r"C:\Users\devan\.gemini\antigravity\brain\9f3a143b-df66-4d07-9a71-81d1cda2e72b\golden_dragon_food_1776545832984.png",
    r"C:\Users\devan\.gemini\antigravity\brain\9f3a143b-df66-4d07-9a71-81d1cda2e72b\chilli_spice_food_1776546004893.png",
    r"C:\Users\devan\.gemini\antigravity\brain\9f3a143b-df66-4d07-9a71-81d1cda2e72b\the_wok_food_1776546019547.png"
]
food_imgs_b64 = [get_base64_of_bin_file(p) for p in food_img_paths]

food_imgs_b64 = [get_base64_of_bin_file(p) for p in food_img_paths]

st.set_page_config(page_title="Zomato AI Recommender", page_icon="🍔", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.cdnfonts.com/css/metropolis-2');

:root {
  --red: #E23744;
  --red-neon: #FF4D5A;
  --green: #3AB44A;
  --gold: #F5A623;
  --dark-bg: #09090C;
  --sidebar-bg: #121217;
  --card-bg: #1A1A24;
  --text-main: #FFFFFF;
  --text-muted: #9E9EA7;
  --border-glass: rgba(255, 255, 255, 0.08);
  --shadow-neon: 0 0 20px rgba(226, 55, 68, 0.5);
  --shadow-ambient: 0 10px 30px rgba(0, 0, 0, 0.5);
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-xl: 28px;
}

/* Global Background and Fonts */
[data-testid="stAppViewContainer"] {
    background-color: var(--dark-bg);
    background-image: radial-gradient(circle at top right, rgba(226, 55, 68, 0.05), transparent 40%),
                      radial-gradient(circle at bottom left, rgba(245, 166, 35, 0.05), transparent 40%);
    font-family: 'Metropolis', sans-serif !important;
    color: var(--text-main);
}
p, label, span, div {
    font-family: 'Metropolis', sans-serif;
}

/* Fix Streamlit Material Icons */
.material-symbols-rounded, .material-icons, [data-testid="stIconMaterial"] {
    font-family: "Material Symbols Rounded" !important;
}

/* Header */
[data-testid="stHeader"] {
    background: rgba(9, 9, 12, 0.8) !important;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-glass);
    height: 70px !important;
}
/* Logo injected via dynamic f-string CSS below */

/* Animations */
@keyframes panBg {
    0% { background-position: 0% 50%; }
    100% { background-position: 100% 50%; }
}
@keyframes pulseNeon {
    0% { box-shadow: 0 0 15px rgba(226, 55, 68, 0.4); }
    50% { box-shadow: 0 0 25px rgba(226, 55, 68, 0.8); }
    100% { box-shadow: 0 0 15px rgba(226, 55, 68, 0.4); }
}
@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(5deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

/* Hero Section */
.hero-wrapper {
    padding: 80px 50px;
    border-radius: var(--radius-lg);
    margin-top: -10px;
    margin-bottom: 50px;
    position: relative;
    overflow: hidden;
    color: white;
    box-shadow: var(--shadow-ambient), inset 0 0 100px rgba(0,0,0,0.8);
    border: 1px solid rgba(255,255,255,0.1);
}
.hero-glass-content {
    position: relative;
    z-index: 2;
    background: rgba(10, 10, 15, 0.45);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 50px;
    border-radius: var(--radius-lg);
    display: inline-block;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6), inset 0 0 20px rgba(255,255,255,0.05);
}

.hero-blob-1 { position: absolute; top: -10%; right: 5%; width: 400px; height: 400px; background: rgba(226,55,68,0.2); border-radius: 50%; filter: blur(60px); animation: float 10s ease-in-out infinite; z-index: 1;}
.hero-blob-2 { position: absolute; bottom: -20%; right: 25%; width: 500px; height: 500px; background: rgba(245,166,35,0.1); border-radius: 50%; filter: blur(80px); animation: float 15s ease-in-out infinite reverse; z-index: 1;}

.eyebrow {
    display: inline-flex;
    align-items: center;
    background: rgba(255,255,255,0.05);
    border: 1px solid var(--border-glass);
    color: var(--text-main);
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 50px;
    padding: 8px 18px;
    margin-bottom: 25px;
}
.gold-dot { width: 8px; height: 8px; background: var(--gold); border-radius: 50%; margin-right: 10px; box-shadow: 0 0 12px var(--gold); }

.hero-title { font-weight: 900; font-size: 64px; line-height: 1.1; margin: 0; color: white; text-shadow: 0 0 20px rgba(0,0,0,0.8); letter-spacing: -1px; }
.hero-subtitle { font-weight: 300; font-style: italic; font-size: 52px; color: rgba(255,255,255,0.8); margin: 0 0 40px 0; text-shadow: 0 0 20px rgba(0,0,0,0.8); }

.stats-row { display: flex; gap: 40px; margin-top: 40px; }
.stat-item { border-left: 1px solid rgba(255,255,255,0.15); padding-left: 20px; }
.stat-item:first-child { border-left: none; padding-left: 0; }
.stat-num { font-size: 28px; font-weight: 800; color: white; text-shadow: 0 0 15px rgba(255,255,255,0.4); }
.stat-label { font-size: 12px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1.5px; font-weight: 700; margin-top: 4px;}

/* Sidebar Overrides for Dark Cyberpunk */
section[data-testid="stSidebar"] > div {
    background-color: var(--sidebar-bg) !important;
}
section[data-testid="stSidebar"] {
    box-shadow: 10px 0 30px rgba(0,0,0,0.5) !important;
    border-right: 1px solid var(--border-glass) !important;
}
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: var(--text-main) !important;
    font-weight: 800 !important;
    font-size: 24px !important;
    margin-top: 15px;
    margin-bottom: 30px;
    text-shadow: 0 0 10px rgba(255,255,255,0.1);
}
[data-testid="stSidebar"] label p, [data-testid="stWidgetLabel"] p {
    font-size: 12px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    color: var(--text-muted) !important;
    margin-bottom: 8px !important;
}
[data-testid="stSidebar"] input[type="text"], 
[data-testid="stSidebar"] textarea {
    padding: 14px 18px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    color: var(--text-main) !important;
    background-color: var(--card-bg) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}

[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    background-color: var(--card-bg) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}

[data-testid="stSidebar"] input[type="text"]:focus, 
[data-testid="stSidebar"] div[data-baseweb="select"] > div:focus-within, 
[data-testid="stSidebar"] textarea:focus {
    border-color: var(--red-neon) !important;
    box-shadow: 0 0 15px rgba(226, 55, 68, 0.4), inset 0 0 5px rgba(226, 55, 68, 0.2) !important;
    background-color: #1a1a24 !important;
}

/* Fix Selectbox Text Colors */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: var(--card-bg) !important;
    color: white !important;
}
.stSelectbox div[data-baseweb="select"] * {
    color: white !important;
    -webkit-text-fill-color: white !important;
}
::placeholder { color: #888888 !important; opacity: 1 !important; -webkit-text-fill-color: #888888 !important; }

/* Fix Dropdown Popover Menu (attached to body) */
div[data-baseweb="popover"] > div {
    background-color: var(--card-bg) !important;
    border: 1px solid var(--border-glass) !important;
}
div[data-baseweb="popover"] ul {
    background-color: var(--card-bg) !important;
}
div[data-baseweb="popover"] li {
    color: var(--text-main) !important;
}
div[data-baseweb="popover"] li:hover {
    background-color: var(--red-neon) !important;
    color: white !important;
}
/* Sliders */
.stSlider div[data-baseweb="slider"] {
    accent-color: var(--red-neon) !important;
}
.stSlider div[role="slider"] {
    box-shadow: 0 0 12px var(--red-neon) !important;
    background-color: var(--text-main) !important;
}
.stSlider [data-testid="stTickBarMin"], 
.stSlider [data-testid="stTickBarMax"], 
.stSlider [data-testid="stThumbValue"] { 
    color: var(--text-muted) !important; 
    font-family: 'Metropolis', sans-serif !important;
}

/* Button overrides - Zomato Authentic */
.stButton button {
    background-color: #E23744 !important;
    background-image: none !important;
    border-radius: 8px !important;
    padding: 16px !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    color: white !important;
    border: none !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 14px rgba(226, 55, 68, 0.4) !important;
    text-transform: none !important;
    letter-spacing: normal !important;
}
.stButton button:hover {
    background-color: #C0392B !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(226, 55, 68, 0.6) !important;
    animation: none !important;
}

/* Status Bar overrides */
.stAlert[data-baseweb="notification"] {
    border: 1px solid var(--border-glass) !important;
    border-radius: var(--radius-md) !important;
    padding: 18px !important;
    background: rgba(20, 20, 25, 0.8) !important;
    backdrop-filter: blur(10px);
}
.stAlert[data-baseweb="notification"] p {
    font-weight: 600 !important;
    font-size: 15px !important;
}
/* Success */
.stAlert[data-baseweb="notification"]:has(svg[data-testid="stIconSuccess"]) { border-left: 4px solid var(--green) !important; }
.stAlert[data-baseweb="notification"]:has(svg[data-testid="stIconSuccess"]) p { color: #A5D6A7 !important; }
/* Error */
.stAlert[data-baseweb="notification"]:has(svg[data-testid="stIconError"]) { border-left: 4px solid var(--red-neon) !important; }
.stAlert[data-baseweb="notification"]:has(svg[data-testid="stIconError"]) p { color: #FFCDD2 !important; }
/* Warning */
.stAlert[data-baseweb="notification"]:has(svg[data-testid="stIconWarning"]) { border-left: 4px solid var(--gold) !important; }
.stAlert[data-baseweb="notification"]:has(svg[data-testid="stIconWarning"]) p { color: #FFE082 !important; }

/* AI Results Cards (Futuristic Glass) */
@keyframes slideUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
.ai-card {
    background: rgba(26, 26, 36, 0.6);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: var(--radius-lg);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 30px;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    animation: slideUp 0.6s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    position: relative;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    display: flex;
    overflow: hidden;
    min-height: 240px;
}
.ai-card:hover {
    transform: translateY(-8px) scale(1.01);
    box-shadow: 0 20px 40px rgba(0,0,0,0.8), 0 0 20px rgba(226, 55, 68, 0.15);
    border-color: rgba(255,255,255,0.2);
}
.ai-card-image {
    width: 320px;
    background-size: cover;
    background-position: center;
    position: relative;
}
.ai-card-image-gradient {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(to right, transparent 0%, rgba(26, 26, 36, 0.6) 50%, rgba(26, 26, 36, 1) 100%);
}
.ai-card-content {
    padding: 30px 40px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.rank-badge {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    font-size: 18px;
    color: #1C1C1C;
    box-shadow: 0 0 20px rgba(0,0,0,0.8);
    z-index: 2;
    border: 2px solid rgba(255,255,255,0.2);
}
.rank-1 { background-color: var(--gold); box-shadow: 0 0 20px rgba(245, 166, 35, 0.6); }
.rank-2 { background-color: #E0E0E0; box-shadow: 0 0 20px rgba(224, 224, 224, 0.4); }
.rank-3 { background-color: #CD7F32; box-shadow: 0 0 20px rgba(205, 127, 50, 0.5); }
.rank-other { display: none; }

.ai-card-title { font-size: 26px; font-weight: 800; color: white; display: flex; align-items: center; gap: 15px; margin-bottom: 15px; text-shadow: 0 2px 10px rgba(0,0,0,0.5);}
.ai-rating { background-color: var(--green); color: white; padding: 6px 14px; border-radius: 50px; font-size: 14px; font-weight: 800; box-shadow: 0 0 15px rgba(58, 180, 74, 0.4); }

.ai-tags-row { display: flex; gap: 15px; margin-bottom: 25px; }
.ai-cuisine-tag { font-size: 13px; font-weight: 600; color: rgba(255,255,255,0.9); background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.05); backdrop-filter: blur(8px); }
.ai-budget-pill { font-size: 13px; font-weight: 800; color: var(--gold); background: rgba(245,166,35,0.15); padding: 8px 16px; border-radius: 50px; border: 1px solid rgba(245,166,35,0.2); }

.ai-says-block {
    background: rgba(0,0,0,0.3);
    border-radius: var(--radius-sm);
    border-left: 4px solid var(--red-neon);
    padding: 20px 24px;
    margin-top: auto;
    box-shadow: inset 0 0 30px rgba(0,0,0,0.5);
    border-top: 1px solid rgba(255,255,255,0.05);
    border-right: 1px solid rgba(255,255,255,0.05);
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.ai-says-label { font-size: 12px; font-weight: 900; text-transform: uppercase; color: var(--red-neon); margin-bottom: 10px; letter-spacing: 1px; text-shadow: 0 0 10px rgba(255, 77, 90, 0.4);}
.ai-says-text { font-size: 15px; color: rgba(255,255,255,0.85); line-height: 1.7; font-weight: 400;}

/* Hide default streamlit title */
[data-testid="stMarkdownContainer"] h1 { display: none !important; }

/* Pure CSS Zomato Logo (100% Reliable) */
[data-testid="stHeader"]::before {
    content: "zomato";
    font-family: 'Metropolis', sans-serif !important;
    font-weight: 900 !important;
    font-style: italic !important;
    font-size: 38px !important;
    color: #E23744 !important;
    letter-spacing: -2px !important;
    margin-left: 20px;
    margin-top: 10px;
    display: block;
    text-shadow: 0 0 15px rgba(226, 55, 68, 0.4);
}

/* Hide Deploy Button */
.stAppDeployButton { 
    display: none !important; 
}

/* Custom Top Navigation */
.top-nav {
    position: fixed;
    top: 15px;
    right: 70px;
    z-index: 999999;
    display: flex;
    gap: 25px;
    align-items: center;
}
.nav-link {
    color: white !important;
    text-decoration: none !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    transition: color 0.2s ease !important;
    font-family: 'Metropolis', sans-serif !important;
}
.nav-link:hover {
    color: var(--red-neon) !important;
}
.user-avatar {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: url('https://ui-avatars.com/api/?name=Zomato+User&background=E23744&color=fff') center/cover;
    border: 2px solid rgba(255,255,255,0.2);
    cursor: pointer;
    transition: border-color 0.2s ease, transform 0.2s ease;
    box-shadow: 0 0 10px rgba(226, 55, 68, 0.3);
}
.user-avatar:hover {
    border-color: var(--red-neon);
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# Inject Custom Top Navigation
st.markdown("""
<div class="top-nav">
    <a href="#" class="nav-link">Log in</a>
    <a href="#" class="nav-link">Sign up</a>
    <div class="user-avatar"></div>
</div>
""", unsafe_allow_html=True)

# Dynamic Hero Section with embedded Base64 image
st.markdown(f"""
<div class="hero-wrapper" style="background: linear-gradient(rgba(9, 9, 12, 0.6), rgba(9, 9, 12, 0.9)), url('data:image/png;base64,{hero_bg_b64}'); background-size: cover; background-position: center; animation: panBg 60s infinite alternate linear;">
    <div class="hero-blob-1"></div>
    <div class="hero-blob-2"></div>
    <div class="hero-glass-content">
        <div class="eyebrow"><div class="gold-dot"></div>Zomato AI Engine</div>
        <h1 class="hero-title">Find Your Perfect Meal</h1>
        <h2 class="hero-subtitle">curated just for you.</h2>
        <div class="stats-row">
            <div class="stat-item"><div class="stat-num">50k+</div><div class="stat-label">Restaurants</div></div>
            <div class="stat-item"><div class="stat-num">98%</div><div class="stat-label">Match Rate</div></div>
            <div class="stat-item"><div class="stat-num">24/7</div><div class="stat-label">AI Concierge</div></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Fetch locations from API
@st.cache_data(ttl=600)
def get_locations():
    try:
        res = requests.get("http://127.0.0.1:8000/api/locations", timeout=5)
        if res.status_code == 200:
            return res.json().get("locations", ["Any"])
    except:
        pass
    return ["Any"]

available_locations = get_locations()

with st.sidebar:
    st.header("Your Preferences")
    
    location = st.selectbox("Location", options=available_locations)
    cuisine = st.text_input("Cuisine", placeholder="e.g., Italian, Chinese, Cafe")
    max_budget = st.slider("Max Budget (for two)", min_value=100, max_value=5000, value=1500, step=100)
    min_rating = st.slider("Minimum Rating", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
    
    st.markdown("---")
    st.subheader("AI Personalization")
    additional_prefs = st.text_area(
        "Additional Preferences", 
        placeholder="e.g., Must have a great view, family friendly..."
    )
    
    submit_btn = st.button("Find Restaurants", type="primary", use_container_width=True)

if submit_btn:
    with st.spinner("Analyzing thousands of restaurants and generating personalized recommendations..."):
        payload = {
            "location": location if location != "Any" else None,
            "cuisine": cuisine if cuisine else None,
            "max_budget": max_budget,
            "min_rating": min_rating,
            "additional_preferences": additional_prefs if additional_prefs else None
        }
        
        try:
            res = requests.post("http://127.0.0.1:8000/api/recommend", json=payload)
            res.raise_for_status()
            data = res.json()
            
            recs = data.get("recommendations", [])
            total_filtered = data.get("total_matches_filtered", 0)
            
            if not recs:
                st.warning("No restaurants found matching your exact criteria. Try broadening your filters.")
            else:
                st.success(f"Successfully filtered {total_filtered} restaurants down to the Top {len(recs)} matches!")
                for idx, r in enumerate(recs):
                    rank = idx + 1
                    rank_class = f"rank-{rank}" if rank <= 3 else "rank-other"
                    
                    name = r.get("restaurant_name", "Unknown")
                    cuis = r.get("cuisine", "Unknown")
                    rate = r.get("rating", "N/A")
                    cost = r.get("estimated_cost", "N/A")
                    url = r.get("url", "#")
                    ai_exp = r.get("ai_explanation", "No explanation provided.")
                    
                    # Cycle through the available food images safely
                    img_b64 = food_imgs_b64[idx % len(food_imgs_b64)] if food_imgs_b64 else ""
                    bg_style = f"background-image: url('data:image/png;base64,{img_b64}');" if img_b64 else "background-color: #333;"
                    
                    st.markdown(f"""
                    <div class="ai-card" style="animation-delay: {idx * 80}ms;">
                        <div class="rank-badge {rank_class}">{rank}</div>
                        <div class="ai-card-image" style="{bg_style}">
                            <div class="ai-card-image-gradient"></div>
                        </div>
                        <div class="ai-card-content">
                            <div class="ai-card-title">
                                <a href="{url}" target="_blank" style="color: white; text-decoration: none;">{name}</a>
                                <span class="ai-rating">★ {rate}</span>
                            </div>
                            <div class="ai-tags-row">
                                <div class="ai-cuisine-tag">{cuis[:35]}{'...' if len(cuis)>35 else ''}</div>
                                <div class="ai-budget-pill">₹{cost} for two</div>
                            </div>
                            <div class="ai-says-block">
                                <div class="ai-says-label">✦ AI SAYS</div>
                                <div class="ai-says-text">{ai_exp}</div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Make sure the FastAPI server is running on port 8000!")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.info("👈 Please set your preferences in the sidebar and click 'Find Restaurants'.")
