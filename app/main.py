import streamlit as st
import os.path as op
from sys import path

path.append(op.abspath(op.join(op.dirname(__file__), "..")))

from app.pages import home
from app.pages import alixpartners


# Generate sidebar elements
def generate_sidebar_elements():
    pages = {
        "Home": home,
        "AlixPartners": alixpartners
    }

    # Sidebar -- Image/Title
    st.sidebar.image(
        "docs/static/workhelix.png",
        use_column_width=True,
    )

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    st.sidebar.title("Contribute!")
    st.sidebar.info(
        "WorkHelix [Repo](https://github.com/workhelix/sample_app):"
        "\n\n:question: [Issues](https://github.com/workhelix/sample_app/issues)"
        "\n\n:handshake: [Pull Requests](https://github.com/workhelix/sample_app/pulls)"
        "\n\n:book: [Source Code](https://github.com/workhelix/sample_app/tree/main/app)"
    )

    page = pages[selection]
    page.run()


if __name__ == "__main__":
    generate_sidebar_elements()
