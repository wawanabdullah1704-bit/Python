import streamlit as st
import numpy as np
import pandas as pd
import io

# ==============================================================================
# DFK50083 PYTHON PROGRAMMING - CASE STUDY 1 (SESSION I: 2026/2027)
# APEX LOGISTICS - WAREHOUSE INVENTORY & SALES MANAGEMENT SYSTEM
# ==============================================================================

# Tetapkan konfigurasi paparan Streamlit
st.set_page_config(
    page_title="Apex Logistics Management System",
    page_icon="📦",
    layout="wide"
)

# ------------------------------------------------------------------------------
# PART 1: OOP MODEL (TOPIC 2.0)
# ------------------------------------------------------------------------------

# Base class untuk item umum di gudang
class Item:
    def __init__(self, item_id, unit_price):
        self.item_id = str(item_id)
        self.unit_price = float(unit_price)

    # Operator Overloading: guna magic method __add__ untuk jumlahkan harga dua item
    def __add__(self, other):
        if isinstance(other, Item):
            return self.unit_price + other.unit_price
        return self.unit_price + float(other)

    # Magic method __str__ untuk paparkan maklumat ringkas item
    def __str__(self):
        return f"Item ID: {self.item_id} | Unit Price: RM{self.unit_price:.2f}"


# Subclass yang mewarisi Item dengan tambahan tarikh luput (expiry_date)
class PerishableItem(Item):
    def __init__(self, item_id, unit_price, expiry_date):
        # Panggil constructor parent class
        super().__init__(item_id, unit_price)
        self.expiry_date = expiry_date

    # Override __str__ method untuk masukkan maklumat tarikh luput
    def __str__(self):
        return f"{super().__str__()} | Expiry Date: {self.expiry_date}"


# ------------------------------------------------------------------------------
# PART 3: STREAMLIT GUI LAYOUT & NAVIGATION
# ------------------------------------------------------------------------------

st.title("📦 Apex Logistics - Warehouse Management System")
st.markdown("Sistem Pengurusan Inventori Gudang dan Analisis Jualan (DFK50083 - Case Study 1)")

# Sidebar Navigation untuk susunan antara muka yang kemas
st.sidebar.image("https://img.icons8.com/color/96/warehouse.png", width=80)
st.sidebar.title("Menu Navigasi")
menu = st.sidebar.radio(
    "Pilih Modul:",
    [
        "1. Pendaftaran Produk (OOP)",
        "2. Inventori Gudang (NumPy 5x5)",
        "3. Analisis Jualan (Pandas Pre-processing)",
        "4. Refleksi & Justifikasi Reka Bentuk (VBE5)"
    ]
)

# ------------------------------------------------------------------------------
# MODUL 1: PENDAFTARAN PRODUK & OOP (PART 1 & EXCEPTION HANDLING)
# ------------------------------------------------------------------------------
if menu == "1. Pendaftaran Produk (OOP)":
    st.header("🛒 Pendaftaran Item & Pengujian OOP Operator Overloading")
    st.write("Daftarkan dua item untuk menguji pewarisan (inheritance), method `__str__`, dan penjumlahan harga guna `__add__`.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Daftar Item 1 (Standard Item)")
        id1 = st.text_input("Item 1 ID:", value="ITM-101")
        price1_input = st.text_input("Unit Price Item 1 (RM):", value="45.50")

    with col2:
        st.subheader("Daftar Item 2 (Perishable Item)")
        id2 = st.text_input("Item 2 ID:", value="PRSH-202")
        price2_input = st.text_input("Unit Price Item 2 (RM):", value="25.00")
        expiry2 = st.date_input("Expiry Date Item 2:")

    # Butang proses dengan Exception Handling (ValueError)
    if st.button("Daftar & Kira Jumlah Harga (Test __add__)", type="primary"):
        try:
            # Uji penukaran harga kepada nombor (ValueError handling)
            price1 = float(price1_input)
            price2 = float(price2_input)

            if price1 < 0 or price2 < 0:
                raise ValueError("Harga tidak boleh bernilai negatif.")

            # Bina objek OOP
            item1 = Item(id1, price1)
            item2 = PerishableItem(id2, price2, str(expiry2))

            # Papar maklumat item menggunakan method __str__
            st.success("✅ Kedua-dua item berjaya didaftarkan tanpa ralat!")
            st.info(f"**Item 1 (__str__):** {item1}")
            st.info(f"**Item 2 (__str__):** {item2}")

            # Uji Operator Overloading __add__
            combined_price = item1 + item2
            st.metric(label="Jumlah Harga Keseluruhan (Operator Overloading: item1 + item2)", value=f"RM {combined_price:.2f}")

        except ValueError as err:
            st.error(f"❌ **ValueError Dikesan:** Sila pastikan input harga adalah angka yang sah. (Mesej: {err})")


# ------------------------------------------------------------------------------
# MODUL 2: INVENTORI GUDANG (NUMPY 5x5 MATRIX PROCESSING)
# ------------------------------------------------------------------------------
elif menu == "2. Inventori Gudang (NumPy 5x5)":
    st.header("📊 Analisis Stok Gudang (NumPy 5x5 Matrix)")
    st.write("Matriks 5x5 mewakili paras stok barang merentasi 5 Seksyen Gudang (A hingga E) dan 5 Zon Rak.")

    # 5x5 NumPy Matrix stok gudang
    stock_matrix = np.array([
        [45, 12, 60, 30, 8],    # Seksyen A
        [15, 5, 20, 10, 2],     # Seksyen B (Stok Rendah)
        [80, 95, 70, 85, 90],   # Seksyen C (Stok Tinggi)
        [25, 18, 40, 30, 22],   # Seksyen D
        [8, 12, 14, 6, 9]       # Seksyen E (Stok Rendah)
    ])

    sections = ["Seksyen A", "Seksyen B", "Seksyen C", "Seksyen D", "Seksyen E"]
    zones = ["Zon 1", "Zon 2", "Zon 3", "Zon 4", "Zon 5"]

    # Papar matriks dalam bentuk DataFrame untuk GUI yang kemas
    df_matrix = pd.DataFrame(stock_matrix, index=sections, columns=zones)
    st.dataframe(df_matrix, use_container_width=True)

    # Pengiraan Matematik Menggunakan Fungsi NumPy
    total_warehouse_stock = np.sum(stock_matrix)
    section_totals = np.sum(stock_matrix, axis=1)  # Row-wise sum
    average_per_section = np.mean(stock_matrix, axis=1)

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Jumlah Keseluruhan Stok (np.sum)", f"{total_warehouse_stock} Unit")
    with col_b:
        st.metric("Purata Stok Seunit Rak", f"{np.mean(stock_matrix):.1f} Unit")

    st.subheader("Pengesanan Seksyen Paras Stok Rendah")
    # Kenal pasti seksyen yang mempunyai jumlah stok rendah (< 60 unit)
    low_stock_threshold = 60
    low_sections = [sections[i] for i, total in enumerate(section_totals) if total < low_stock_threshold]

    # Feature Tambahan: Automated Low-Stock Alert (Part 4)
    if low_sections:
        st.warning(f"⚠️ **AMARAN STOK RENDAH:** Seksyen berikut mempunyai stok di bawah paras minimum {low_stock_threshold} unit: **{', '.join(low_sections)}**.")
    else:
        st.success("Semua seksyen mempunyai stok yang mencukupi.")

    # Visualisasi Carta Bar untuk Stok Setiap Seksyen (Part 4)
    st.subheader("Carta Paras Stok Mengikut Seksyen")
    chart_data = pd.DataFrame({"Seksyen": sections, "Jumlah Stok": section_totals}).set_index("Seksyen")
    st.bar_chart(chart_data)

    # Ujian Kestabilan: ZeroDivisionError Handling (Part 3)
    st.divider()
    st.subheader("Kira Purata Agihan Stok Seunit (ZeroDivisionError Test)")
    divisor_input = st.number_input("Masukkan bilangan kontena untuk agihan stok:", min_value=0, value=0, step=1)

    if st.button("Kira Agihan Stok"):
        try:
            if divisor_input == 0:
                raise ZeroDivisionError("Pembahagi bernilai sifar.")
            stock_per_container = total_warehouse_stock / divisor_input
            st.success(f"Purata stok bagi setiap kontena: **{stock_per_container:.2f} unit**")
        except ZeroDivisionError as err:
            st.error(f"❌ **ZeroDivisionError Dikesan:** Tidak boleh membahagi stok dengan 0 kontena. (Mesej: {err})")


# ------------------------------------------------------------------------------
# MODUL 3: ANALISIS JUALAN (PANDAS DATA PRE-PROCESSING)
# ------------------------------------------------------------------------------
elif menu == "3. Analisis Jualan (Pandas Pre-processing)":
    st.header("📈 Pemprosesan Data Rekod Jualan (Pandas)")
    st.write("Muat naik fail CSV untuk menjalankan pembersihan data (Duplicate removal, Imputation, Filtering).")

    # File uploader (Part 3)
    uploaded_file = st.file_uploader("Muat Naik Fail Rekod Jualan (CSV):", type=["csv"])

    # Semak dan proses fail dengan Exception Handling tambahan (Part 4 Robustness)
    df = None
    try:
        if uploaded_file is not None:
            # Tangkap ralat jika fail kosong atau format tidak sah
            if uploaded_file.size == 0:
                raise pd.errors.EmptyDataError("Fail yang dimuat naik adalah kosong.")
            df = pd.read_csv(uploaded_file)
        else:
            st.info("💡 Memuatkan data sampel lalai (`sales_records.csv`) untuk tujuan demonstrasi.")
            # Data sampel berdasarkan silibus Week 11
            default_data = {
                'Order_ID': [101, 102, 103, 102, 104, 105, 106, 107, 108, 109],
                'Category': ['Electronics', 'Clothing', 'Perishable', 'Clothing', 'Home', 'Electronics', 'Perishable', 'Clothing', 'Home', 'Perishable'],
                'Price': [299.99, 45.00, 15.50, 45.00, 75.00, np.nan, 12.50, 35.00, 80.00, 20.00],
                'Units_Sold': [12, 25, 50, 25, 8, 18, np.nan, 30, 5, 45]
            }
            df = pd.DataFrame(default_data)

    except pd.errors.EmptyDataError as empty_err:
        st.error(f"❌ **EmptyDataError Dikesan:** {empty_err}")
    except Exception as general_err:
        st.error(f"❌ **File Processing Error:** Gagal memproses fail CSV. ({general_err})")

    # Sekiranya dataframe sah diperolehi, jalankan pra-pemprosesan
    if df is not None:
        st.subheader("1. Data Asal (Sebelum Pembersihan)")
        st.write(f"Jumlah rekod asal: **{len(df)} baris** (Termasuk duplikasi & data hilang)")
        st.dataframe(df, use_container_width=True)

        # A. Dismantle and remove Duplicates
        initial_count = len(df)
        df_cleaned = df.drop_duplicates(keep='first').copy()
        duplicates_removed = initial_count - len(df_cleaned)

        # B. Fix missing data (NaN) by replacing them with average value (Mean Imputation)
        avg_price = df_cleaned['Price'].mean()
        avg_units = df_cleaned['Units_Sold'].mean()
        df_cleaned['Price'] = df_cleaned['Price'].fillna(avg_price)
        df_cleaned['Units_Sold'] = df_cleaned['Units_Sold'].fillna(avg_units)

        # Tambah lajur Total Sales
        df_cleaned['Total_Sales'] = df_cleaned['Price'] * df_cleaned['Units_Sold']

        st.subheader("2. Data Selepas Pembersihan (Cleaned Data)")
        st.success(f"✅ {duplicates_removed} rekod duplikasi telah dihapuskan. Nilai NaN telah digantikan dengan nilai purata (Mean).")
        st.dataframe(df_cleaned, use_container_width=True)

        # C. Filter data to display only high sales volume
        threshold_units = st.slider("Tetapkan Had Minimum Jualan Tinggi (Units Sold):", min_value=1, max_value=60, value=20)
        high_sales_df = df_cleaned[df_cleaned['Units_Sold'] >= threshold_units]

        st.subheader(f"3. Rekod Jualan Tinggi (Units Sold >= {threshold_units})")
        st.dataframe(high_sales_df, use_container_width=True)

        # Feature Tambahan: Export/Download Processed Data (Part 4)
        csv_buffer = io.StringIO()
        df_cleaned.to_csv(csv_buffer, index=False)
        st.download_button(
            label="📥 Muat Turun Data Bersih (Download Processed CSV)",
            data=csv_buffer.getvalue(),
            file_name="apex_cleaned_sales.csv",
            mime="text/csv"
        )


# ------------------------------------------------------------------------------
# MODUL 4: REFLEKSI & JUSTIFIKASI REKA BENTUK (PART 4 - VBE5: COURAGE)
# ------------------------------------------------------------------------------
elif menu == "4. Refleksi & Justifikasi Reka Bentuk (VBE5)":
    st.header("📝 Refleksi & Justifikasi Reka Bentuk (VBE5: Courage)")
    st.write("Dokumentasi dan justifikasi cabaran penyahpepijatan (*debugging*) serta ciri-ciri penambahbaikan sistem.")

    with st.expander("📌 1. Integrasi Ciri-Ciri Tambahan Melangkaui Keperluan (Beyond Requirements)", expanded=True):
        st.markdown("""
        * **Automated Low-Stock Alert:** Sistem memantau matriks 5x5 secara dinamik dan memaparkan amaran visual segera (`st.warning`) apabila mana-mana seksyen gudang berada di bawah paras 60 unit.
        * **Eksport Data Dinamik (`st.download_button`):** Membolehkan pihak pengurusan memuat turun data jualan yang telah siap diproses ke dalam format CSV untuk kegunaan audit syarikat.
        * **Visualisasi Visual Automatik:** Menukar pengiraan matriks NumPy kepada carta bar Streamlit (`st.bar_chart`) bagi memudahkan pembacaan trend stok.
        """)

    with st.expander("🛡️ 2. Penyahpepijatan Bebas & Edge-Case Error Handling", expanded=True):
        st.markdown("""
        * **Pengendalian Fail Kosong (`pd.errors.EmptyDataError`):** Menangani isu apabila pengguna memuat naik fail CSV bersaiz 0 bait atau rosak tanpa menyebabkan Streamlit memaparkan *raw exception stack trace*.
        * **Keteguhan Input Harga (`ValueError`):** Input harga menggunakan medan teks yang disahkan sebelum ditukar kepada nombor, mengelakkan kemasukan simbol atau abjad.
        * **Pembahagian Sifar (`ZeroDivisionError`):** Pengiraan agihan stok dijamin selamat daripada pembahagi sifar dengan maklum balas mesra pengguna.
        """)

    with st.expander("💡 3. Justifikasi Reka Bentuk Sistem (Design Decisions)", expanded=True):
        st.markdown("""
        * **Modulariti OOP:** Menggunakan `Item` dan `PerishableItem` memastikan struktur data gudang boleh diskalakan pada masa hadapan (contohnya menambah kategori item baharu).
        * **Kecekapan NumPy & Pandas:** Operasi vektor NumPy memproses matriks 5x5 secara pantas tanpa memerlukan gelung (*for loop*) yang berat, manakala Pandas membolehkan teknik pembersihan data *mean imputation* dijalankan dengan tepat.
        """)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Politeknik Mukah Malaysia | DFK50083 Session I: 2026/2027")