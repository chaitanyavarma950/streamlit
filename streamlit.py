import streamlit as st

# -------------------------------
# Session State for Login
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -------------------------------
# Fake user database
# -------------------------------
USER_CREDENTIALS = {
    "admin": "admin123",
    "devops": "deploy2025"
}


# -------------------------------
# Login Page
# -------------------------------
def login_page():
    st.title("🔐 Login Page")
    st.write("Enter your credentials to continue:")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")


# -------------------------------
# Dashboard Page
# -------------------------------
def dashboard_page():
    st.title(f"🚀 Deployment Dashboard - Welcome {st.session_state.username}")
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Overview", "Deploy", "Logs", "Logout"])

    if choice == "Overview":
        st.subheader("📊 System Overview")
        st.metric("Active Deployments", 5)
        st.metric("Failed Deployments", 1)
        st.metric("Last Deployed", "2 hours ago")

    elif choice == "Deploy":
        st.subheader("⚙️ New Deployment")
        service = st.selectbox("Select Service", ["UI", "Node", "Flask", "MongoDB", "Python Crons"])
        version = st.text_input("Enter version tag (e.g. v1.2.3)")
        if st.button("Deploy Now"):
            if version:
                st.success(f"Deployment triggered for {service} with version {version}")
            else:
                st.warning("Please enter a version tag before deploying.")

    elif choice == "Logs":
        st.subheader("📜 Deployment Logs")
        st.text_area("Logs", value="Deployment started...\nPulling image...\nDeploy complete ✅", height=200)

    elif choice == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()


# -------------------------------
# Main App
# -------------------------------
if not st.session_state.logged_in:
    login_page()
else:
    dashboard_page()
