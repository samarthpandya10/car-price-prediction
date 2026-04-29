import streamlit as st
from auth import create_db, login_user, signup_user

# Must be first Streamlit command
st.set_page_config(page_title="Car Price System", page_icon="🚗")

# Create database
create_db()

st.title("🚗 Turbo Drift")

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------- SIGNUP ----------
if choice == "Signup":
    st.subheader("Create Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Signup"):
        if new_user and new_pass:
            signup_user(new_user, new_pass)
            st.success("✅ Account created! Go to Login.")
        else:
            st.warning("⚠️ Enter username and password")

# ---------- LOGIN ----------
elif choice == "Login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(username, password):
            st.success(f"✅ Welcome {username}!")

            # small delay for UI smoothness
            st.balloons()

            # 🔥 switch page
            st.switch_page("pages/1_Predict_Price.py")

        else:
            st.error("❌ Invalid login")
