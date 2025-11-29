import streamlit as st
from PIL import Image

st.title("🍎 Klasifikasi Kematangan Buah Berdasarkan Warna")
st.write("Aplikasi ini memprediksi tingkat kematangan buah berdasarkan warna dominan (RGB).")

# ======== FUNGSI KLASIFIKASI MANUAL =========
def classify_fruit_color(r, g, b):
   def classify_fruit_color(r, g, b):
    # ----- Matang (merah / merah gelap / kemerahan) -----
    if (r > 150 and g < 120 and b < 120) or (r > 180 and g < 150):
        return "Matang"

    # ----- Setengah matang (oranye / kuning) -----
    if (r > 170 and g > 140 and b < 120) or (r > 200 and g > 160):
        return "Setengah Matang"

    # ----- Mentah (hijau / hijau kekuningan) -----
    if (g > 120 and g > r and g > b) or (g > 150 and r < 120):
        return "Mentah"

    # ----- Kecoklatan (sering buah terlalu matang atau busuk) -----
    if r > 100 and g < 80 and b < 60:
        return "Cenderung Terlalu Matang / Coklat"

    # Jika tidak masuk semua kategori
    return "Tidak diketahui (warna unik / campuran)"

# ============================================
#            PILIH MODE INPUT
# ============================================
mode = st.radio("Pilih metode input warna:", ["Upload Gambar", "Input Warna Manual"])

# ============================================
#            MODE 1: UPLOAD GAMBAR
# ============================================
if mode == "Upload Gambar":
    uploaded_file = st.file_uploader("Upload gambar buah", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, width=300, caption="Gambar yang diupload")

        # Ambil warna rata-rata dengan mengecilkan gambar jadi 1x1 pixel
        small_img = img.resize((1, 1))
        dominant_color = small_img.getpixel((0, 0))  # (R, G, B)

        r, g, b = dominant_color

        st.write(f"### 🎨 Warna Dominan Gambar (RGB): {dominant_color}")

        prediction = classify_fruit_color(r, g, b)

        st.subheader("📌 Hasil Prediksi")
        st.write(f"**Buah diprediksi:** {prediction}")

# ============================================
#            MODE 2: INPUT WARNA MANUAL
# ============================================
else:
    color = st.color_picker("Pilih warna buah")
    
    # Convert HEX → RGB
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)

    st.write(f"RGB: {(r, g, b)}")

    prediction = classify_fruit_color(r, g, b)

    st.subheader("📌 Hasil Prediksi")
    st.write(f"**Buah diprediksi:** {prediction}")

# Footer
st.markdown("---")
st.caption("Aplikasi klasifikasi kematangan buah — Tanpa library ML, cocok untuk hosting Streamlit Cloud.")


