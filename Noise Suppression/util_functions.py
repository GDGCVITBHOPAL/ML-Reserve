import streamlit as st


@st.cache
def load_model(model_file_path):
    """

    This function loads the pre-trained model into cache and returns
    <class:tensorflow.python.keras.engine.functional.Functional> object for suppression purpose. Here this function
    is decorated with @st.cache which is responsible for loading the model and it's parameters as cached memory to
    optimize the time complexity of the overall app. @st.cache uses hash_functions to store cached memory and hence will
    only be called when ':param model_file_path:' will change.

    :param model_file_path:

    :return model: <class:tensorflow.python.keras.engine.functional.Functional> object

    """
    import tensorflow as tf
    model = tf.keras.models.load_model(model_file_path)
    return model
