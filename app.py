import streamlit as st
import time
import random

st.set_page_config(page_title="Digital Balance", page_icon="🌐", layout="centered")
st.title("🌐 Digital Balance")
st.subheader("Internet va real hayot muvozanatini saqlang 💡")

menu = st.sidebar.radio("Bo‘limni tanlang:", [
    "⏱ Internet vaqtini nazorat qilish",
    "🔒 Kiberxavfsizlik tekshiruvi",
    "🧠 O‘quv testlari",
    "❤️ Psixologik tavsiyalar"
])

if menu == "⏱ Internet vaqtini nazorat qilish":
    vaqt = st.number_input("Necha daqiqa foydalanmoqchisiz?", 1, 180)
    if st.button("Boshlash"):
        with st.spinner(f"{vaqt} daqiqa davomida vaqt nazorati ishlayabdi...⌛")
            time.sleep(vaqt * 60) # daqiqani soniyaga o'giradi
        st.success(f"✅ {vaqt} daqiqa tugadi! Endi dam oling 🌿")

elif menu == "🔒 Kiberxavfsizlik tekshiruvi":
    link = st.text_input("Havolani kiriting:")
    zararli = ["phishing", "spam", "malware", "virus", "apk"]
    if st.button("Tekshirish"):
        if any(s in link.lower() for s in zararli):
            st.error("⚠️ Xavfli havola topildi!")
        elif link.strip() == "":
            st.warning("Havola kiritilmadi.")
        else:
            st.success("✅ Havola xavfsizdek ko‘rinadi.")

elif menu == "🧠 O‘quv testlari":
    st.write("Axborot madaniyati testi")
    savollar = {
        "Internetda shaxsiy ma’lumotlarni kimga berish mumkin?": "Hech kimga",
        "Parol qanday bo‘lishi kerak?": "Uzoq, murakkab va maxfiy",
        "Internetdagi yolg‘on xabarlar nima deb ataladi?": "Fake news",
    }

    ball = 0
   elif menu == "🧠 O‘quv testlari":
    st.write("Axborot madaniyati testi")

    savollar = [
        {
            "savol": "Internetda shaxsiy ma’lumotlarni kimga berish mumkin?",
            "variantlar": ["Hech kimga", "Har kimga", "Do‘stlarimga", "Ijtimoiy tarmoqlarga"],
            "javob": "Hech kimga"
        },
        {
            "savol": "Parol qanday bo‘lishi kerak?",
            "variantlar": ["Uzoq, murakkab va maxfiy", "Qisqa va esda qoladigan", "Faqat ismim", "Telefon raqamim"],
            "javob": "Uzoq, murakkab va maxfiy"
        },
        {
            "savol": "Internetdagi yolg‘on xabarlar nima deb ataladi?",
            "variantlar": ["Trend", "Fake news", "Promo", "Spam"],
            "javob": "Fake news"
        }
    ]

    ball = 0
    for i, item in enumerate(savollar):
        javob = st.radio(item["savol"], item["variantlar"], key=f"savol_{i}")
        if javob == item["javob"]:
            ball += 1

    if st.button("Natija"):
        st.success(f"Siz {ball}/{len(savollar)} ball to‘pladingiz 🎯")
        if ball == len(savollar):
            st.balloons()
            st.info("Ajoyib! Siz axborot madaniyatini juda yaxshi bilasiz 👏")
        elif ball >= 2:
            st.warning("Yaxshi, lekin biroz ehtiyot bo‘lish kerak 💡")
        else:
            st.error("Ko‘proq o‘rganish tavsiya qilinadi 📘")
    if st.button("Natija"):
        st.success(f"Siz {ball}/{len(savollar)} ball to‘pladingiz 🎯")

elif menu == "❤️ Psixologik tavsiyalar":
    tavsiyalar = [
        "Bugun internetdan keyin 30 daqiqa sayr qiling 🌿",
        "Har 1 soatda 10 daqiqa tanaffus qiling ☕",
        "Telefonni uxlaganda yotoqxonadan uzoqda saqlang 📵",
        "Do‘stlaringiz bilan yuzma-yuz suhbatlashing 🤝",
    ]
    if st.button("Bugungi tavsiyani ko‘rish"):
        st.info(random.choice(tavsiyalar))
