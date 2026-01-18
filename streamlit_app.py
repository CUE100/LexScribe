import streamlit as st

def main():
    st.title("LexScribe")
    st.write("This is the LexScribe Streamlit app entrypoint.")

    name = st.text_input("Your name")
    if st.button("Greet"):
        st.success(f"Hello, {name or 'there'}!")


if __name__ == "__main__":
    main()