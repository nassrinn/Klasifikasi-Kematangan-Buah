import streamlit as st
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# ============================
#  MODEL SEDERHANA KNN
# ============================

# Dataset warna buah (contoh sederhana)
# format: [R, G, B]
X = np.array([
    [255, 0, 0],      # merah cerah - matang
    [200, 30, 30],    # merah gelap - matang
    [255, 165, 0],    # oranye - setengah matang
    [255, 220, 100],  # kuning - setengah matang
    [0, 255, 0],      # hijau - mentah
    [50, 180, 50],    # hijau tua - mentah
])

# Label
y = np.array([
    "Matang",
    "Matang",
    "Setengah Matang",
    "Setengah Matang",
    "Mentah",
    "Mentah",
])

# Train Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# ============================
#  STREAMLIT APP
# ============================

st.title("🍎 Klasifikasi Kematangan Buah Berdasarkan Warna")
st.write("Upload gambar atau pilih warna untuk memprediksi tingkat kematangan buah.")

# --- Pilihan Input ---
mode = st.radio("Pilih metode input:", ["Upload Gambar", "Input Warna Manual"])

# --------------------------
#  INPUT 1 — UPLOAD GAMBAR
# --------------------------
if mode == "Upload Gambar":
    file = st.file_uploader("Upload foto buah", type=["jpg", "jpeg", "png"])

    if file:
        import cv2
        from PIL import Image

        img = Image.open(file)
        st.image(img, caption="Gambar yang diupload", width=300)

        # Convert ke numpy + ambil warna dominan sederhana
        img_np = np.array(img)
        avg_color = img_np.reshape(-1, 3).mean(axis=0).astype(int)

        st.write(f"Rata-rata warna (RGB): {avg_color}")

        prediction = model.predict([avg_color])[0]

        st.subheader("📌 Hasil Prediksi")
        st.write(f"**Buah diprediksi:** {prediction}")

# --------------------------
#  INPUT 2 — PILIH WARNA MANUAL
# --------------------------
else:
    color = st.color_picker("Pilih warna buah")

    # Convert hex ke RGB
    rgb = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
    st.write(f"RGB: {rgb}")

    prediction = model.predict([list(rgb)])[0]

    st.subheader("📌 Hasil Prediksi")
    st.write(f"**Buah diprediksi:** {prediction}")

# ============================
#  Footer
# ============================
st.markdown("---")
st.caption("Aplikasi klasifikasi kematangan buah — Streamlit + KNN ML Model")
