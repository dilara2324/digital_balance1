import streamlit as st
import time
import re

st.set_page_config(page_title="Digital Balance", page_icon="⏱", layout="centered")

st.sidebar.title("📱 Digital Balance")
sahifa = st.sidebar.radio(
    "Bo‘limni tanlang:",
    ["⏱ Internet limiti", "🔒 Kiberxavfsizlik", "🧠 O‘quv testlari", "💡 Tavsiyalar"]
)

# 1️⃣ INTERNET LIMITI
if sahifa == "⏱ Internet limiti":
    st.title("⏱ Internetdan foydalanish limiti")
    minutes = st.number_input("Bugun internetni necha daqiqa ishlatmoqchisiz?", min_value=1, step=1)

    if st.button("Boshlash"):
        st.success(f"⏰ Vaqt boshlandi: {minutes} daqiqa")
        with st.spinner(f"{minutes} daqiqa davomida vaqt nazorati ishlayapti...⌛"):
            time.sleep(minutes * 60)
        st.warning("⏳ Vaqt tugadi! Dam oling, real hayotga e'tibor bering ❤️")

        # 🎵 Tugaganda musiqa chalish
        st.markdown(
            """
            <script>
            setTimeout(function(){
                var audio = new Audio("https://www.soundjay.com/button/beep-07a.mp3");
                audio.play();
            }, 1000);
            </script>
            """,
            unsafe_allow_html=True
        )

# 2️⃣ KIBERXAVFSIZLIK
elif sahifa == "🔒 Kiberxavfsizlik":
    st.title("🔒 Kiberxavfsizlik tizimi")
    url = st.text_input("Shubhali havolani bu yerga kiriting:")

    if st.button("Havolani tekshirish"):
        if not url:
            st.warning("❗ Avval havolani kiriting.")
        elif not re.match(r"^https?://", url):
            st.error("⚠️ Bu havola xavfli! 'http://' yoki 'https://' bilan boshlanishi kerak.")
        elif any(x in url for x in [".exe", ".zip", ".rar", "phishing", "scam"]):
            st.error("🚫 Bu havola zararli bo‘lishi mumkin! Ehtiyot bo‘ling.")
        else:
            st.success("✅ Havola xavfsiz ko‘rinmoqda.")

# 3️⃣ TESTLAR
elif sahifa == "🧠 O‘quv testlari":
    st.title("🧠 Axborot madaniyati testi")

    savollar = [
        {
            "savol": "Internetda noma'lum havolani bosish xavflimi?",
            "variantlar": ["Ha", "Yo‘q", "Ba'zida"],
            "javob": "Ha"
        },
        {
            "savol": "Parolingizni boshqalar bilan ulashish mumkinmi?",
            "variantlar": ["Ha", "Yo‘q", "Faqat do‘stlar bilan"],
            "javob": "Yo‘q"
        },
        {
            "savol": "Kiberbulling (online haqorat)ga duch kelsangiz nima qilasiz?",
            "variantlar": ["E'tibor bermayman", "Ishonchli kattalarga aytaman", "O‘zim ham javob qaytaraman"],
            "javob": "Ishonchli kattalarga aytaman"
        }
    ]

    if "bosqich" not in st.session_state:
        st.session_state.bosqich = 0
        st.session_state.togri = 0

    if st.session_state.bosqich < len(savollar):
        s = savollar[st.session_state.bosqich]
        javob = st.radio(s["savol"], s["variantlar"])
        if st.button("Keyingi"):
            if javob == s["javob"]:
                st.session_state.togri += 1
            st.session_state.bosqich += 1
            st.rerun()
    else:
        st.success(f"Siz {len(savollar)} savoldan {st.session_state.togri} tasiga to‘g‘ri javob berdingiz 🎉")
        if st.session_state.togri == len(savollar):
            st.balloons()
        if st.button("Qayta boshlash"):
            st.session_state.bosqich = 0
            st.session_state.togri = 0
            st.rerun()

# 4️⃣ PSIXOLOGIK TAVSIYA
elif sahifa == "💡 Tavsiyalar":
    st.title("💡 Psixologik tavsiya")
    st.write("""
    - Har kuni kamida 1 soat internetdan tashqarida vaqt o‘tkazing.
    - Sport, o‘qish yoki yaqinlaringiz bilan suhbat qiling.  
    - Ekranga tikilib qolmang, tabiatni ham ko‘ring 🌿  
    ❤️ Real hayot — eng yaxshi “onlayn” tajriba!
    """)
