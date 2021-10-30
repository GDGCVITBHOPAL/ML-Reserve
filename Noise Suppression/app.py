# Importing project dependencies

import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
import util_functions as ufs
import time

# Setting config option for deployment

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Noise-Suppressor')
st.subheader('Removes background-noise from audio samples')

# UI design

nav_choice = st.sidebar.radio('Navigation', ['Home'], index=0)

_param_dict = {}  # Used for getting plot related information
_path_to_model = 'utils/models/auto_encoders_for_noise_removal_production.h5'  # Path to pre-trained model
_targe_file = 'utils/outputs/preds.wav'  # target file for storing model.output

if nav_choice == 'Home':
    st.image('utils/images/header.jpg', width=450, height=500)

    st.info('Upload your audio sample below')
    audio_sample = st.file_uploader('Audio Sample', ['wav'])  # Get audio sample as an input from users
    if audio_sample:
        try:
            prog = st.progress(0)
            model = ufs.load_model(_path_to_model)  # call to the utility module to cache the model
            audio = tf.audio.decode_wav(audio_sample.read(), desired_channels=1)
            # decoding audio waveform by using  tf.audio.decode_wav as a mono sound wave
            _param_dict.update({'audio_sample': audio.audio})
            flag = 1
            for i in range(100):
                time.sleep(0.001)
                prog.progress(i + 1)
            st.info('Uploaded audio sample')
            st.audio(audio_sample)
            with st.spinner('Wait for it...'):
                time.sleep(1)
                preds = model.predict(tf.expand_dims(audio.audio, 0))  # using this EagerTensor to suppress te noie
                preds = tf.reshape(preds, (-1, 1))
                _param_dict.update({'predicted_outcomes': preds})
                preds = np.array(preds)
                write(_targe_file, 44100, preds)  # writing the output file to play
            st.success('Audio after noise removal')
            st.audio(_targe_file)

            # Visual Representation of model's prediction using sync plots

            prediction_stats = st.checkbox('Prediction Plots')
            noise_rem = st.checkbox('Noise Removal Plots')
            if noise_rem:
                fig, axes = plt.subplots(2, 1, figsize=(10, 6))
                axes[0].plot(np.arange(len(_param_dict['audio_sample'])), _param_dict['audio_sample'], c='r')
                axes[0].set_title('Original audio sample')
                axes[1].plot(np.arange(len(_param_dict['predicted_outcomes'])), _param_dict['predicted_outcomes'],
                             c='b')
                axes[1].set_title('Noise suppressed audio output')
                st.pyplot()

            if prediction_stats:
                plt.figure(figsize=(10, 6))
                plt.plot(np.arange(len(_param_dict['audio_sample'])), _param_dict['audio_sample'], c='r',
                         label='Original audio sample')
                plt.plot(np.arange(len(_param_dict['predicted_outcomes'])), _param_dict['predicted_outcomes'], c='b',
                         label='Noise suppressed audio output')
                plt.legend()
                st.pyplot()

        except Exception as e:
            print(e, type(e))
