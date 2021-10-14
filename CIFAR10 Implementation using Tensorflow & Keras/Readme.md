<h1 align="left">Implementation Of CIFAR10 <br>using TensorFlow & Keras Sequential API </h1>

The CIFAR-10 dataset is useful for developing and practicing a methodology for solving  ***Image Classification*** problems using convolutional neural networks.  
For this project, I have created an Image Classifier that classifies every object in the CIFAR10 dataset, CNN model with several layers. 



## Tools Used:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)

## Install the necessary packages:
### Run the following commands in Terminal

```bash
pip install tensorflow
```
  
```bash
pip install matplotlib
```

```bash
pip install keras
```

## Dataset:
### CIFAR10 
#### The dataset is comprised of 60,000 32×32 pixel color photographs of objects from 10 classes, such as frogs, birds, cats, ships, etc.There are 6,000 images of each class. The class labels and their standard associated integer values are listed below

<ul style="list-style-type:none">
  
  <li>0: airplane</li>
  <li>1: automobile</li>
  <li>2: bird</li>
  <li>3: cat</li>
  <li>4: deer</li>
  <li>5: dog</li>
  <li>6: frog</li>
  <li>7: horse</li>
  <li>8: ship</li>
  <li>9: truck</li>
  </ul>
  
#### The dataset is divided into 50,000 training images and 10,000 testing images

#### (The dataset already exists in the keras.datasets library and can be easily used)

