import streamlit as st

# ========== CONFIGURASI HALAMAN ==========
st.set_page_config(
    page_title="Pusat Edukasi Tani Indonesia",
    page_icon="🌾",
    layout="wide"
)

# ========== KUSTOMISASI TEMA (STYLE SAWAH NUSANTARA) ==========
st.markdown("""
    <style>
        .main {
            background-color: #F4F7F5;
        }
        .banner-sawah {
            background: linear-gradient(135deg, #1B5E20 0%, #43A047 100%);
            padding: 40px;
            border-radius: 20px;
            color: white;
            box-shadow: 0px 10px 30px rgba(27, 94, 32, 0.15);
            margin-bottom: 30px;
            text-align: center;
        }
        .premium-card-green {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.04);
            border-top: 5px solid #2E7D32;
            margin-bottom: 20px;
            min-height: 250px;
        }
        .premium-card-gold {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.04);
            border-top: 5px solid #FBC02D;
            margin-bottom: 20px;
            min-height: 250px;
        }
        .mini-box {
            background-color: #E8F5E9;
            padding: 12px;
            border-radius: 10px;
            border-left: 4px solid #2E7D32;
            margin-bottom: 10px;
            font-size: 14px;
            color: #1B5E20;
        }
    </style>
""", unsafe_allow_html=True)

# ========== INITIALIZE SESSION STATE FOR QUIZ ==========
if "pre_score" not in st.session_state:
    st.session_state.pre_score = None
if "post_score" not in st.session_state:
    st.session_state.post_score = None

# ========== SIDEBAR (NAVIGASI) ==========
with st.sidebar:
    st.markdown("<h2 style='color: #2E7D32; font-weight:700;'>🌱 Navigasi Web</h2>", unsafe_allow_html=True)
    language = st.selectbox(
        "🌍 Pilih Bahasa / Language",
        ["Bahasa Indonesia", "English", "Español"]
    )
    st.write("---")
    
    # Memperbaiki parameter radio agar kompatibel 100% dengan server cloud tanpa crash index
    menu = st.sidebar.radio(
        "📚 Select Learning Module:",
        ["🏡 Home", "🧪 Organic Fertilizer", "🌾 Weed Utilization in Rice Fields", "📝 Quiz"]
    )
    st.write("---")
    st.markdown("<div style='font-size: 12px; color: #777;'>Aplikasi Edukasi Pertanian Berkelanjutan v3.1</div>", unsafe_allow_html=True)

# ========== DEFINISI TEKS MULTI-BAHASA ==========
text = {
    "English": {
        "home_title": "INDONESIAN RICE FIELD EDUCATION HUB",
        "home_sub": "Regenerative Farming for Local Rice Production",
        "learn": "Core Learning Modules:",
        "tip": "Please use the sidebar menu on the left to explore other modules!",
        "fert_title": "Liquid & Organic Fertilizer Masterclass",
        "compost": "Aerobic Compost Making",
        "liquid": "Banana Peel Waste Fertilizer Production Using the Stacked Bucket Method",
        "weeds_title": "Weed Utilization in Rice Fields",
        "quiz_title": "Knowledge Evaluation Chamber",
        "q1": "Can fresh weeds be directly utilized as green manure or compost in rice fields?",
        "q2": "Which crucial micronutrient found in banana peels functions to prevent empty/hollow rice grains?",
        "submit_pre": "Submit Pre-Test Answers",
        "submit_post": "Submit Post-Test Answers"
    },
    "Bahasa Indonesia": {
        "home_title": "PUSAT EDUKASI SAWAH HIJAU NUSANTARA",
        "home_sub": "Modernisasi Pertanian Berkelanjutan & Mandiri untuk Petani Indonesia",
        "learn": "Materi Pembelajaran Utama:",
        "tip": "Silakan klik menu di sidebar sebelah kiri untuk melihat materi pupuk, gulma, dan kuis!",
        "fert_title": "Panduan Premium Pupuk Organik Cair",
        "compost": "Pembuatan Kompos Aerobik",
        "liquid": "Produksi Pupuk Cair dari Kulit Pisang Menggunakan Metode Keranjang Bertumpuk",
        "weeds_title": "Pemanfaatan Gulma Sawah",
        "quiz_title": "Ruang Evaluasi Kemajuan Belajar",
        "q1": "Apakah gulma segar hasil penyiangan bagus digunakan lngsung sebagai pupuk hijau di sawah?",
        "q2": "Mikronutrien esensial apa pada kulit pisang yang berfungsi mencegah bulir padi menjadi hampa (kopong)?",
        "submit_pre": "Kirim Jawaban Pre-Test",
        "submit_post": "Kirim Jawaban Post-Test"
    },
    "Español": {
        "home_title": "CENTRO DE EDUCACIÓN DE ARROZALES",
        "home_sub": "Empoderando a los agricultores locales con métodos sostenibles",
        "learn": "Módulos de Aprendizaje:",
        "tip": "¡Use el menú lateral izquierdo para comenzar a aprender!",
        "fert_title": "Guía Premium de Fertilizantes Orgánicos",
        "compost": "Producción de Compost Aeróbico",
        "liquid": "Potilizer: Fertilizante Líquido de Cáscara de Plátano",
        "weeds_title": "Ecología y Uso de Malezas en Arrozales",
        "quiz_title": "Evaluación de Conocimientos",
        "q1": "¿Se pueden usar las malezas frescas directamente como abono verde en los arrozales?",
        "q2": "¿Qué micronutriente esencial en la cáscara de plátano ayuda a prevenir granos de arroz vacíos?",
        "submit_pre": "Enviar Pre-Test",
        "submit_post": "Enviar Post-Test"
    }
}

t = text[language]

# ========== MODUL 1: BERANDA (HOME) ==========
if menu == "🏡 Home":
    st.markdown(f"""
    <div class="banner-sawah">
        <h1 style="margin: 0; font-size: 34px; font-weight: 800; letter-spacing: 1px;">🌾 {t['home_title']}</h1>
        <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">{t['home_sub']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_kiri, col_kanan = st.columns([7, 5], gap="large")
    
    with col_kiri:
        st.markdown(f"### 🎯 {t['learn']}")
        st.markdown("""
        <div class="premium-card-green">
            <h4 style="color: #2E7D32; margin-top:0; font-weight:700;">Banana Peel Fertilizer Innovation 🌿</h4>
            <p style="color: #555; font-size:14px; line-height:1.6;">
                Learn how banana peels can be transformed into eco-friendly liquid organic fertilizer through a simple and sustainable process. This project uses a simple modified system called the  <b>stacked bucked method,</b> where two buckets are arranged as a fertilizer reactor to maximize mineral release from banana peels. The goal is to improve nutrient availability for rice production through sustainable organic innovation. Key nutrients released from banana peels include:            </p>
            <div class="mini-box"><b>High Potassium (K):</b> Helps regulate the opening and closing of rice leaf stomata and strengthens plant immnunity.</div>
            <div class="mini-box"><b>Essential Micronutrient Boron (B):</b> Supports carbohydrate transport for better grain filling and helps prevent empty rice grains.</div>
        </div>
        
        <div class="premium-card-gold">
            <h4 style="color: #E65100; margin-top:0; font-weight:700;">Optimization of Indigenous Rice Field Weeds 🌾</h4>
            <p style="color: #555; font-size:14px; line-height:1.6;">
                Fresh weeds such as water clover and nut grass have a low C/N ratio (10:1–20:1), allowing them to decompose rapidly in paddy soil and release natural Nitrogen (N) within a short period of time. This process supports sustainable nutrient cycling and can help improve soil fertility naturally in rice cultivation systems.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_kanan:
        st.write("#### 📸 Rice Field Visualization")
        st.image("padi.jpg", use_container_width=True, caption="Traditional rice field tillage with water buffalo")
        st.info(f"💡 **Tip:** {t['tip']}")

# ========== MODUL 2: PUPUK ORGANIK ==========
elif menu == "🧪 Organic Fertilizer":
    st.markdown(f"<h1 style='color:#1B5E20;'>🧪 {t['fert_title']}</h1>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(f"""
        <div class="premium-card-gold" style="min-height:220px;">
            <h3 style="color: #E65100; margin-top:0; font-weight:700;">🍂 {t['compost']}</h3>
            <p style='color:#444; line-height:1.6; font-size:14.5px;'>
                <b>📋 Step-by-Step Rice Straw Composting Process:</b><br>
                Chop the rice straw, mix with husk and EM4 bioactivator, then pack inside an airtight sack for 3 to 4 weeks until mature.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Gambar ditaruh tepat di bawah sini dengan indentasi (spasi maju) yang sejajar
        st.image("flowchart.png", caption="Rice Straw Composting Flowchart", use_container_width=True)
    with col2:
        st.markdown(f"""
        <div class="premium-card-green" style="min-height:220px;">
            <h3 style="color: #2E7D32; margin-top:0; font-weight:700;">🪣 {t['liquid']}</h3>
            <p style='color:#444; line-height:1.5; font-size:14px;'>
                <b>📺 Watch the Tutorial Video:</b><br>
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=w-e5Nds3w4U")

    st.write("---")
    st.markdown("### 🔬 Mineral Content of Banana Peels")
    st.image("table.png", use_container_width=True)
    st.write("---")
    

    st.markdown("## 🧮 Fermentation Calculator (Kalkulator Fermentasi Pupuk Cair)")

    material_weight = st.number_input(
        "Organic material weight (kg)",
        min_value=1.0,
        value=10.0
    )

    water_ratio = st.slider(
        "Water ratio (L per kg material)",
        min_value=0.5,
        max_value=5.0,
        value=2.0,
        step=0.1
    )

    temperature = st.slider(
        "Fermentation temperature (°C)",
        min_value=15,
        max_value=50,
        value=30
    )

    # ===== CALCULATION =====
    water_needed = material_weight * water_ratio
    molasses_needed = water_needed * 0.05

    if temperature < 20:
        fermentation_days = 21
    elif temperature <= 30:
        fermentation_days = 14
    else:
        fermentation_days = 7

    # ===== OUTPUT =====
    st.subheader("📊 Results")

    st.success(f"💧 Water needed: {water_needed:.1f} L")
    st.success(f"🍯 Molasses needed: {molasses_needed:.1f} L")
    st.success(f"⏳ Fermentation time: {fermentation_days} days")

    # optional progress
    st.progress(int(min((temperature - 15) / 30 * 100, 100)))

# ========== MODUL 3: GULMA =========
elif menu == "🌾 Weed Utilization in Rice Fields":
    st.markdown(f"<h1 style='color:#1B5E20;'>🌾 {t['weeds_title']}</h1>", unsafe_allow_html=True)
    st.write("---")

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.image("teki.jpg", use_container_width=True, caption="1. Rumput Teki - Rasio C/N ~12:1")
        st.image("jajagoan.jpg", use_container_width=True, caption="3. Jajagoan - Rasio C/N ~18:1")
    with c2:
        st.image("eceng.jpg", use_container_width=True, caption="2. Eceng Gondok - Rasio C/N ~15:1")
        st.image("semanggi.jpg", use_container_width=True, caption="4. Semanggi Air - Rasio C/N ~11:1")

    st.write("---")
    st.markdown("### Utilization of Weeds in Rice Fields")
    
    st.image("decomposition.png", use_container_width=True)
# ========== MODUL 4: KUIS ==========
elif menu == "📝 Quiz":
    st.markdown(f"<h1 style='color:#1B5E20;'>📝 {t['quiz_title']}</h1>", unsafe_allow_html=True)
    st.write("---")
 
    tab1, tab2, tab3 = st.tabs(["📋 1. Pre-Test", "🎯 2. Post-Test", "📊 3. Hasil Analisis"])
 
    with tab1:
        st.markdown("#### Initial Assessment (Pre-Test) - Complete before reading the material")
        
        # Pre-test quiz questions in English
        p_ans1 = st.radio("1. Is EM4 the correct name of the bioactivator used to make compost fertilizer?", ["-", "Yes / Ya", "No / Tidak"], key="p_q1")
        p_ans2 = st.radio("2. Which essential micronutrient found in banana peels functions to prevent empty or hollow rice grains?", ["-", "Nitrogen (N)", "Boron (B)", "Phosphorus (P)"], key="p_q2")
        p_ans3 = st.radio("3. Is fresh weed with a low C/N ratio from weeding excellent to be used directly as green manure in rice fields?", ["-", "Yes / Ya", "No / Tidak"], key="p_q3")
        p_ans4 = st.radio("4. Is the optimal incubation temperature for composting strictly between 40°C and 50°C?", ["-", "Yes / Ya", "No / Tidak"], key="p_q4")
        p_ans5 = st.radio("5. Can the 'Stacked Bucket' method be utilized to produce liquid organic fertilizer?", ["-", "Yes / Ya", "No / Tidak"], key="p_q5")
        
        if st.button(t["submit_pre"]):
            sc = 0
            if p_ans1 == "Yes / Ya": sc += 20
            if p_ans2 == "Boron (B)": sc += 20
            if p_ans3 == "Yes / Ya": sc += 20
            if p_ans4 == "Yes / Ya": sc += 20
            if p_ans5 == "Yes / Ya": sc += 20
            st.session_state.pre_score = sc
            st.success(f"Pre-Test saved! Your score: **{sc}/100**")
 
    with tab2:
        st.markdown("#### Final Evaluation (Post-Test) - Complete after reading the material")
        
        # Post-test quiz questions in English
        po_ans1 = st.radio("1. Is EM4 the correct name of the bioactivator used to make compost fertilizer?", ["-", "Yes / Ya", "No / Tidak"], key="po_q1")
        po_ans2 = st.radio("2. Which essential micronutrient found in banana peels functions to prevent empty or hollow rice grains?", ["-", "Nitrogen (N)", "Boron (B)", "Phosphorus (P)"], key="po_q2")
        po_ans3 = st.radio("3. Is fresh weed with a low C/N ratio from weeding excellent to be used directly as green manure in rice fields?", ["-", "Yes / Ya", "No / Tidak"], key="po_q3")
        po_ans4 = st.radio("4. Is the optimal incubation temperature for composting strictly between 40°C and 50°C?", ["-", "Yes / Ya", "No / Tidak"], key="po_q4")
        po_ans5 = st.radio("5. Can the 'Stacked Bucket' method be utilized to produce liquid organic fertilizer?", ["-", "Yes / Ya", "No / Tidak"], key="po_q5")
        
        if st.button(t["submit_post"]):
            sc = 0
            if po_ans1 == "Yes / Ya": sc += 20
            if po_ans2 == "Boron (B)": sc += 20
            if po_ans3 == "Yes / Ya": sc += 20
            if po_ans4 == "Yes / Ya": sc += 20
            if po_ans5 == "Yes / Ya": sc += 20
            st.session_state.post_score = sc
            st.success(f"Post-Test saved! Your score: **{sc}/100**")
            if sc == 100:
                st.balloons()
 
    with tab3:
        st.markdown("### 📊 Learning Outcome Comparison Results")
        c_pre, c_post = st.columns(2)
        with c_pre:
            if st.session_state.pre_score is not None:
                st.metric(label="Pre-Test Score", value=f"{st.session_state.pre_score} / 100")
            else:
                st.info("Pre-Test has not been taken yet.")
        with c_post:
            if st.session_state.post_score is not None:
                st.metric(label="Post-Test Score", value=f"{st.session_state.post_score} / 100")
            else:
                st.info("Post-Test has not been taken yet.")
 
        if st.session_state.pre_score is not None and st.session_state.post_score is not None:
            st.write("---")
            diff = st.session_state.post_score - st.session_state.pre_score
            if diff > 0:
                st.success(f"📈 Congratulations! Your understanding has improved by **{diff} points**!")
            elif diff == 0 and st.session_state.post_score == 100:
                st.success("🌟 Perfect! You have mastered the sustainable rice farm organic fertilizer material beautifully!")
            else:
                st.warning("🔄 Your score remains unchanged or is not yet optimal. We highly recommend reviewing the chapters on Micronutrients, Composting Temperature, and C/N Ratios.")