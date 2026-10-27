import streamlit as st
import requests


col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("GitHub Profile Finder")
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    username = st.text_input("Enter Github username")

col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    search = st.button("search", use_container_width=False)


if search:
    if username.strip() == "":
        st.warning("please enter a username")

    else:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            col1, col2, col3 = st.columns([1, 1, 3])

            with col2:
                st.image(data["avatar_url"], width=150)
            with col3:
                st.subheader(data["name"] or data["login"])
                st.write("Bio:", data["bio"] or "no bio available")

                st.metric("Public Repos:", data["public_repos"])
                st.metric("Followers", data["followers"])

        elif response.status_code == 404:
            st.error("Github user not found")
        else:
            st.error("something wrong, try agion")
