import streamlit as st
from PIL import Image

st.title("🍎 Klasifikasi Kematangan Buah Berdasarkan Warna")
st.write("Aplikasi ini memprediksi tingkat kematangan buah berdasarkan warna dominan (RGB).")

# ======== FUNGSI KLASIFIKASI MANUAL =========
def classify_fruit_color(r, g, b):
    # Warna merah → matang
    if r > 180 and g < 100 and b < 100:
        return "Matang"

    # Warna oranye/kuning → setengah matang
    if r > 180 and g > 120 and b < 100:
        return "Setengah Matang"

    # Warna hijau → mentah
    if g > r and g > b:
        return "Mentah"

    return "Tidak diketahui (warna di luar pola umum)"

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

