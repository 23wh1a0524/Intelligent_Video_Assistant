import streamlit as st

from app.auth import authenticate_user, create_user, initialize_database


st.set_page_config(
    page_title="Intelligent Video Assistant",
    page_icon="🎥",
)

initialize_database()


def show_login() -> None:
    st.title("Intelligent Video Assistant")
    st.subheader("Login")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        user = authenticate_user(email, password)

        if user is None:
            st.error("Invalid email or password.")
            return

        st.session_state["user"] = user
        st.success("Login successful.")
        st.rerun()


def show_registration() -> None:
    st.title("Intelligent Video Assistant")
    st.subheader("Create an account")

    with st.form("registration_form"):
        email = st.text_input("Email", key="registration_email")
        password = st.text_input(
            "Password",
            type="password",
            key="registration_password",
        )
        confirm_password = st.text_input(
            "Confirm password",
            type="password",
        )
        submitted = st.form_submit_button("Register")

    if submitted:
        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        if len(password) < 8:
            st.error("Password must contain at least 8 characters.")
            return

        if create_user(email, password):
            st.success("Account created. You can now log in.")
        else:
            st.error("That email is already registered or invalid.")


def show_dashboard() -> None:
    user = st.session_state["user"]

    st.title("Video Assistant Dashboard")
    st.write(f"Signed in as **{user['email']}**")

    if st.button("Log out"):
        st.session_state.pop("user", None)
        st.rerun()

    st.info("Video processing will be added in the next milestone.")


if "user" in st.session_state:
    show_dashboard()
else:
    login_tab, registration_tab = st.tabs(["Login", "Register"])

    with login_tab:
        show_login()

    with registration_tab:
        show_registration()