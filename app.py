import streamlit as st

st.set_page_config(
    page_title="Farmer Education Hub",
    page_icon="🌱",
    layout="wide"
)

# ========== INITIALIZE SESSION STATE FOR QUIZ ==========
# Menyimpan skor pre-test dan post-test agar bisa dibandingkan
if "pre_score" not in st.session_state:
    st.session_state.pre_score = None
if "post_score" not in st.session_state:
    st.session_state.post_score = None

# ========== LANGUAGE ==========
language = st.sidebar.selectbox(
    "🌍 Language / Bahasa",
    ["English", "Bahasa Indonesia", "Español"]
)

menu = st.sidebar.radio(
    "📚 Menu",
    ["Home", "Fertilizer", "Weeds", "Quiz"]
)

# ========== TEXT DEFINITION ==========
text = {
    "English": {
        "home_title": "Farmer Education Hub",
        "home_sub": "Simple learning for sustainable farming",
        "fert_title": "Organic Fertilizer Guide",
        "compost": "Compost Making",
        "liquid": "Liquid Banana Peel Fertilizer (Potilizer)",
        "weeds_title": "Weed Utilization",
        "quiz_title": "Knowledge Evaluation (Pre-Test & Post-Test)",
        "q1": "Can weeds be used as green manure or compost for rice fields?",
        "q2": "What essential micronutrient in banana peels helps prevent empty rice grains and aids flowering?",
        "submit_pre": "Submit Pre-Test",
        "submit_post": "Submit Post-Test"
    },
    "Bahasa Indonesia": {
        "home_title": "Pusat Edukasi Petani",
        "home_sub": "Pembelajaran sederhana untuk pertanian berkelanjutan",
        "fert_title": "Panduan Pupuk Organik",
        "compost": "Pembuatan Kompos",
        "liquid": "Pupuk Cair Kulit Pisang (Potilizer)",
        "weeds_title": "Pemanfaatan Gulma",
        "quiz_title": "Evaluasi Pengetahuan (Pre-Test & Post-Test)",
        "q1": "Apakah gulma dapat digunakan sebagai pupuk hijau atau kompos di sawah?",
        "q2": "Mikronutrien esensial apa pada kulit pisang yang membantu mencegah bulir padi hampa dan membantu pembungaan?",
        "submit_pre": "Kirim Jawaban Pre-Test",
        "submit_post": "Kirim Jawaban Post-Test"
    },
    "Español": {
        "home_title": "Centro de Educación Agrícola",
        "home_sub": "Aprendizaje simple para agricultura sostenible",
        "fert_title": "Guía de Fertilizantes Orgánicos",
        "compost": "Producción de Compost",
        "liquid": "Fertilizante Líquido de Plátano (Potilizer)",
        "weeds_title": "Uso de Malezas",
        "quiz_title": "Evaluación de Conocimiento (Pre-Test y Post-Test)",
        "q1": "¿Se pueden usar las malezas como abono verde o compost para los arrozales?",
        "q2": "¿Qué micronutriente esencial en las cáscaras de plátano ayuda a prevenir granos vacíos y ayuda a la floración?",
        "submit_pre": "Enviar Pre-Test",
        "submit_post": "Enviar Post-Test"
    }
}

t = text[language]

# ========== HOME MODULE ==========
if menu == "Home":
    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.title("🌾 " + t["home_title"])
        st.write(t["home_sub"])
        st.info("💡 Use the sidebar to navigate through the modules / Gunakan menu di sidebar untuk belajar.")
    with col2:
        st.image("padi.jpg", use_container_width=True, caption="Sustainable Rice Farming")

# ========== FERTILIZER MODULE (JOURNAL COMPLIANT) ==========
elif menu == "Fertilizer":
    st.title("🌿 " + t["fert_title"])
    st.write("---")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.subheader("🍂 " + t["compost"])
        st.write("**🇬🇧 English:** Collect dry leaves ➔ add green waste ➔ turn weekly.")
        st.write("**🇮🇩 Bahasa Indonesia:** Kumpulkan daun kering ➔ tambah sampah hijau ➔ balik mingguan.")

    with col2:
        st.subheader("🪣 " + t["liquid"])
        st.write("**Closed Vessel Fermentation (Method according to Journal):**")
        st.write("**🇬🇧 English:** Dice ripe banana peels (2 cm). Mix with water, sugar, and EM4 in a sealed container. Ferment for 7–14 days. Open daily to release gas.")
        st.write("**🇮🇩 Bahasa Indonesia:** Potong kulit pisang matang (2 cm). Campur dengan air, gula, dan EM4 di wadah tertutup. Fermentasikan selama 7–14 hari. Buka tutupnya setiap hari untuk buang gas.")

    st.write("---")
    st.subheader("🧪 Nutrient Composition / Komposisi Nutrisi Kulit Pisang")
    st.write("Data source: *IKONOMIKA Jurnal Ekonomi dan Bisnis Islam (2020)*")

    if language == "English":
        nutrient_data = {
            "Nutrient Type": ["Macronutrient", "Macronutrient", "Macronutrient", "Macronutrient", "Micronutrient", "Micronutrient", "Micronutrient"],
            "Mineral Element": ["Potassium (K)", "Phosphorus (P)", "Calcium (Ca)", "Magnesium (Mg)", "Boron (B)", "Iron (Fe)", "Sodium (Na)"],
            "Concentration (mg/100g)": ["Very High / Active", "211.30 ± 1.24", "59.10 ± 0.85", "44.50 ± 0.08", "Essential Trace", "47.00 ± 1.26", "115.10 ± 0.26"],
            "Main Plant Function": [
                "Sugar transport and stomata control.",
                "Cellular division and energy formation.",
                "Builds strong plant cell walls.",
                "Core part of chlorophyll for photosynthesis.",
                "Crucial for flowering, carbohydrate transport, and grain filling (prevents empty grains).",
                "Chlorophyll synthesis.",
                "Maintains cellular osmotic balance."
            ]
        }
    else:
        nutrient_data = {
            "Jenis Unsur Hara": ["Makronutrien", "Makronutrien", "Makronutrien", "Makronutrien", "Mikronutrien Esensial", "Mikronutrien Esensial", "Mikronutrien Esensial"],
            "Unsur / Mineral": ["Kalium (K)", "Fosfor (P)", "Kalsium (Ca)", "Magnesium (Mg)", "Boron (B)", "Zat Besi (Fe)", "Natrium (Na)"],
            "Konsentrasi (mg/100g)": ["Sangat Tinggi / Aktif", "211.30 ± 1.24", "59.10 ± 0.85", "44.50 ± 0.08", "Tersedia / Dibutuhkan", "47.00 ± 1.26", "115.10 ± 0.26"],
            "Fungsi Utama bagi Tanaman": [
                "Transportasi gula dan kontrol stomata.",
                "Pembelahan sel dan energi.",
                "Memperkuat struktur dinding sel tanaman.",
                "Inti pusat molekul klorofil untuk fotosintesis.",
                "Sangat penting untuk pembungaan, transportasi karbohidrat, dan pengisian bulir padi (mencegah hampa).",
                "Sintesis hijau daun (klorofil).",
                "Menjaga keseimbangan osmotik sel."
            ]
        }
    st.table(nutrient_data)

# ========== WEEDS MODULE ==========
elif menu == "Weeds":
    st.title("🌾 " + t["weeds_title"])
    st.write("---")
    
    col_img1, col_img2 = st.columns(2) 
    with col_img1:
        st.image("teki.jpg", use_container_width=True, caption="Rumput Teki - C:N ~12:1")
    with col_img2:
        st.image("eceng.jpg", use_container_width=True, caption="Eceng Gondok - C:N ~15:1")

    col_img3, col_img4 = st.columns(2) 
    with col_img3:
        st.image("jajagoan.jpg", use_container_width=True, caption="Jajagoan - C:N ~18:1")
    with col_img4:
        st.image("semanggi.jpg", use_container_width=True, caption="Semanggi Air - C:N ~11:1")

# ========== QUIZ MODULE (PRE-TEST & POST-TEST COMPARISON) ==========
elif menu == "Quiz":
    st.title("🧪 " + t["quiz_title"])
    st.write("---")

    # Membuat dua tab visual untuk memisahkan ujian
    tab1, tab2, tab3 = st.tabs(["📋 1. Pre-Test", "📝 2. Post-Test", "📊 3. Result Comparison"])

    # --- TAB 1: PRE-TEST ---
    with tab1:
        st.markdown("### Take this test BEFORE reading the fertilizer and weeds modules")
        pre_ans1 = st.radio(t["q1"], ["-", "Yes / Ya", "No / Tidak"], key="pre_q1")
        pre_ans2 = st.radio(t["q2"], ["-", "Nitrogen (N)", "Boron (B)", "Phosphorus (P)"], key="pre_q2")
        
        if st.button(t["submit_pre"]):
            score = 0
            if pre_ans1 == "Yes / Ya": score += 50
            if pre_ans2 == "Boron (B)": score += 50
            st.session_state.pre_score = score
            st.success(f"Pre-Test submitted! Your score: **{score}/100**")

    # --- TAB 2: POST-TEST ---
    with tab2:
        st.markdown("### Take this test AFTER reading and analyzing all the modules")
        post_ans1 = st.radio(t["q1"], ["-", "Yes / Ya", "No / Tidak"], key="post_q1")
        post_ans2 = st.radio(t["q2"], ["-", "Nitrogen (N)", "Boron (B)", "Phosphorus (P)"], key="post_q2")
        
        if st.button(t["submit_post"]):
            score = 0
            if post_ans1 == "Yes / Ya": score += 50
            if post_ans2 == "Boron (B)": score += 50
            st.session_state.post_score = score
            st.success(f"Post-Test submitted! Your score: **{score}/100**")
            if score == 100:
                st.balloons()

    # --- TAB 3: COMPARISON RESULT ---
    with tab3:
        st.markdown("### 📊 Performance Analysis")
        
        col_pre, col_post = st.columns(2)
        with col_pre:
            if st.session_state.pre_score is not None:
                st.metric(label="Pre-Test Score", value=f"{st.session_state.pre_score} / 100")
            else:
                st.info("Pre-Test not taken yet.")
                
        with col_post:
            if st.session_state.post_score is not None:
                st.metric(label="Post-Test Score", value=f"{st.session_state.post_score} / 100")
            else:
                st.info("Post-Test not taken yet.")

        # Logika perbandingan skor kemajuan belajar
        if st.session_state.pre_score is not None and st.session_state.post_score is not None:
            st.write("---")
            improvement = st.session_state.post_score - st.session_state.pre_score
            if improvement > 0:
                st.success(f"📈 Great job! Your score improved by **{improvement} points**! The learning modules were effective!")
            elif improvement == 0 and st.session_state.post_score == 100:
                st.success("🌟 Perfect score on both tests! You have mastered the sustainable farming topics thoroughly.")
            elif improvement == 0:
                st.warning("🔄 Your score remained the same. Consider re-reading the fertilizer data or weed ratio information.")
            else:
                st.error("📉 Your post-test score was lower than your pre-test score. We recommend reviewing the guide material.")