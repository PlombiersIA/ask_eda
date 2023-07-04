import streamlit as st


def main():
   # Use the full page instead of a narrow central column
   st.set_page_config(layout="wide")

   path_to_gwenn_ha_du = "images/Gwenn_ha_du.png"
   st.sidebar.image(path_to_gwenn_ha_du, use_column_width=False, width=100)

   st.title("ML-Ops.bzh")
   st.subheader("Machine learning operations (MLOps) is the discipline of AI model delivery. It focuses on the ML model's development, deployment, monitoring, and lifecycle management. MLOps enables data scientists and IT operations teams to collaborate and increase the pace of model development and deployment via monitoring, validation, and governance of machine learning models.")

   st.image("images/mlops_pipeline.jpg")

   col1, col2, col3 = st.columns(3)

   with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")

   with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")

   with col3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")


if __name__ == "__main__":
    main()