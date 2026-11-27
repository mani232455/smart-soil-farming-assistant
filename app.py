import streamlit as st

st.set_page_config(page_title="Smart Soil Assistant", page_icon="🌱", layout="centered")

st.title("🌱 Smart Soil & Farming Assistant")
st.caption("An early-stage educational prototype")

st.warning(
    "Prototype only: this app does not provide validated agronomic advice. "
    "Do not use its output alone to choose crops, apply fertilizer, or use pesticides."
)

st.subheader("Enter soil information")
crop = st.text_input("Crop you are considering (optional)", placeholder="e.g. wheat")
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
nitrogen = st.number_input("Nitrogen (N) test value", min_value=0.0, value=0.0, help="Enter the value and unit exactly as shown on your soil-test report.")
phosphorus = st.number_input("Phosphorus (P) test value", min_value=0.0, value=0.0, help="Enter the value and unit exactly as shown on your soil-test report.")
potassium = st.number_input("Potassium (K) test value", min_value=0.0, value=0.0, help="Enter the value and unit exactly as shown on your soil-test report.")
units = st.text_input("N-P-K units / test method (if known)", placeholder="Copy from your soil-test report")
weather = st.text_area("Local weather or rainfall notes (optional)", placeholder="e.g. recent rainfall, expected dry spell")

if st.button("Review entered information", type="primary"):
    st.subheader("Your input summary")
    st.write(f"**Crop considered:** {crop or 'Not specified'}")
    st.write(f"**Soil pH:** {ph:.1f}")
    st.write(f"**N-P-K values:** N={nitrogen}, P={phosphorus}, K={potassium}")
    st.write(f"**Units / test method:** {units or 'Not specified'}")
    st.write(f"**Weather notes:** {weather or 'Not provided'}")

    st.subheader("General observations")
    if ph < 5.5:
        st.info("The entered pH is on the acidic side. Ask a local soil-testing laboratory or agriculture extension officer how this should be interpreted for your soil and crop.")
    elif ph > 8.0:
        st.info("The entered pH is on the alkaline side. Ask a local soil-testing laboratory or agriculture extension officer how this should be interpreted for your soil and crop.")
    else:
        st.info("The entered pH is within a broad middle range. This alone does not establish soil suitability for a crop.")

    st.write(
        "N-P-K values cannot be interpreted safely without their units, test method, "
        "soil context, crop, and local reference ranges. Take the original soil-test "
        "report to a qualified local agriculture expert before making input decisions."
    )

st.divider()
st.caption("Built as a learning prototype. No sensor integration, AI model, or verified field validation is included yet.")
