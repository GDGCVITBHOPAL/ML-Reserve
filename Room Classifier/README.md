# Room Classifier
A part of a bigger hackathon project turned into a web-app that helps in classifying a clean and messy room.

# Dataset used
The dataset that was used to build this project was taken from Kaggle. The data set contains about 100 images of both clean and messy room and is comparitively small as compared to other data sets that we use for performing any deep learninng task.

Link to the dataset - https://www.kaggle.com/cdawn1/messy-vs-clean-room

# Tools Used
<img src="https://img.shields.io/badge/Jupyter%20-%23F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" /> <img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Keras%20-%23D00000.svg?&style=for-the-badge&logo=Keras&logoColor=white"/> <img src="https://img.shields.io/badge/TensorFlow%20-%23FF6F00.svg?&style=for-the-badge&logo=TensorFlow&logoColor=white" /> <img src="https://img.shields.io/badge/pandas%20-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" /> <img src="https://img.shields.io/badge/numpy%20-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" /> 
![image](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

# My approach

* Started off by importing the data and as i was already aware of the size of the images, i didn't have to check any image shape or anything of that sort.
* I then applied some data aygmentation as the size of our original data set was very small.
* Once i had the augmented data, i went on to create my own custom CNN architecture. 
* The custom architectures didn't help much so had to try some other pre trained models such as VGG16 and VGG19. After some experimentation, VGG19 gave some decent results.
* Once the model was ready, it was tested with a few images from the test set and then the model was exported in a .h5 file.
* This h5 file was later on used to deploy the model on the web using Streamlit and Ngrok.

# Results
The model in the end gave decent results. With validation accuracy of 95% and training accuracy of 98%, the model could have been better if we had a little bit more data. More data always helps in training better models.
