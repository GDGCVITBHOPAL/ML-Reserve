![image](https://user-images.githubusercontent.com/90418655/209568809-53613ff4-db02-4903-bafa-eac3bb0f271f.png)
![image](https://user-images.githubusercontent.com/90418655/209568834-621b63c3-882e-4dc8-a0c7-c756c6d7e102.png)

# Indian Rainfall Analysis and Prediction

## Folder Structure
Dataset - Contains the dataset and data used in the project.<br>
Models - Contains the pretrained model in pkl format.<br>
Python Script - Contains the python file of the project.<br>
Demo Video- Contains the demo video of the project.<br>

## Project Description
### Importing the module.
The modules used in the project are as follow<br>
1)numpy<br>
2)pandas<br>
3)matplotlib<br>
4)seaborn<br>
5)time<br>
6)sklearn<br>
7)os<br>

The modules can be installed using the following commands:<br>
Windows - python -m pip install somepackage<br>
Mac os - sudo easy_install pip<br>
         pip install somepackage<br>
Linux - pip install somepackage<br>

## Dataset Desription
Indian Government has undertaken many research studies to analyze the impact of global warming and climate change on rainfall pattern in India. The analyses were made using observed rainfall data from more than 3000 rain-gauge stations spread over the country for 115 years (1901-2015). The major inferences from these studies based on the 115 years of rainfall data are as follows:

The analysis of 115 years of monsoon rainfall data suggests that there is no long term change or trend in the monsoon rainfall averaged over the country. Even though, there are no changes in the all-India rainfall, there are significant changes in annual rainfall in some meteorological sub-divisions. Rainfall over Kerala, East Madhya Pradesh, Jharkhand, Arunachal Pradesh and Nagaland, Manipur, Mizoram and Tripura (NMMT) show decreasing trends. However, rainfall over coastal Karnataka, Maharashtra and Jammu and Kashmir show an increasing trend.

rainfall in india 1901-2015 - Averagge rainfall of Each state from 1901 to 2015 fron month January to December.<br>
district wise rainfall normal - District wise data of average rainfall of India.<br>

## Steps involved in the project.<br>

### Reading the dataset using pandas.<br>

### Plotting various graphs using matplotlib and seaborn based on the dataset for data analysis.<br>

### Choosing the avg_rainfall column to train the model on the year and every month data.

### Sorting the dataset based on the avg_rainfall.<br>

### Performing data analysis.<br>

### Scaling the data.<br>

### Dividing the dataset into training and testing data.<br>

### Similarly performing EDA on the second dataset.<br>

### Plotting the values of the first datset on the map of India for better data visualization.<br>

### Training the model using neural networks and polynomial regression.<br>

### The model achieved and accuracy of 98.866 using polynomial regression.<br>

### Predicting the results og the model after 2015 for a particular state chosen by the user.<br>

### Plotting the graph between the real values and the predicted values.<br>

### Saving the model.
