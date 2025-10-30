import streamlit as st
import time

st.set_page_config(page_title="Digital Balance", page_icon="⏱", layout="centered")

st.title("🌐 Digital Balance")
st.subheader("Internetdan foydalanish vaqtini nazorat qiluvchi va o‘rgatuvchi tizim")

# 1️⃣ Foydalanish vaqti limiti
st.header("⏱ Internetdan foydalanish limiti")
minutes = st.number_input("Bugun internetni necha daqiqa ishlatmoqchisiz?", min_value=1, step=1)

if st.button("Boshlash"):
    st.success(f"⏰ Vaqt boshlandi: {minutes} daqiqa")
    with st.spinner(f"{minutes} daqiqa davomida vaqt nazorati ishlayapti...⌛"):  # shu joy to‘g‘rilandi
        time.sleep(minutes * 60)  # haqiqiy daqiqa asosida ishlaydi
    st.warning("⏳ Vaqt tugadi! Dam oling, real hayotga e’tibor bering ❤️")

# 2️⃣ O‘quv testi
st.header("🧠 Axborot madaniyati testi")
st.write("Quyidagi savollarga javob bering:")

savollar = {
    "Internetda noma’lum havolani bosish xavflimi?": ["Ha", "Yo‘q", "Ba’zida"],
    "Parolingizni boshqalar bilan ulashish mumkinmi?": ["Ha", "Yo‘q", "Faqat do‘stlar bilan"],
    "Kiberbulling (online haqorat)ga duch kelsangiz nima qilasiz?": [
        "E’tibor bermayman",
        "Ishonchli kattalarga aytaman",
        "O‘zim ham javob qaytaraman"
    ]
}

javoblar = {
    "Internetda noma’lum havolani bosish xavflimi?": "Ha",
    "Parolingizni boshqalar bilan ulashish mumkinmi?": "Yo‘q",
    "Kiberbulling (online haqorat)ga duch kelsangiz nima qilasiz?": "Ishonchli kattalarga aytaman"
}

foydalanuvchi_javoblari = {}
for savol, variantlar in savollar.items():
    javob = st.radio(savol, variantlar)
    foydalanuvchi_javoblari[savol] = javob

if st.button("Natijani ko‘rish"):
    to‘g‘ri = sum(foydalanuvchi_javoblari[s] == javoblar[s] for s in savollar)
    st.success(f"Siz {len(savollar)} savoldan {to‘g‘ri} tasiga to‘g‘ri javob berdingiz 🎉")
    if to‘g‘ri == len(savollar):
        st.balloons()
    else:
        st.info("Yaxshi harakat! Qayta urinib ko‘rishingiz mumkin 🧠")

# 3️⃣ Psixologik tavsiya
st.header("💡 Psixologik tavsiya")
st.write("Har kuni kamida 1 soat internetdan tashqarida vaqt o‘tkazing — sport, o‘qish yoki yaqinlaringiz bilan suhbat ❤️")

