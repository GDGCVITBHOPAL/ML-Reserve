

Iris Prediction ML Model Deployed on Android App

This project consists of a classiﬁcation example called the iris species prediction. The

dataset contains three classes of 50 instances each, where each class refers to the type of

iris plant.ꢀ

Attribute information:ꢀ

\1. sepal length in cmꢀ

\2. sepal width in cmꢀ

\3. petal length in cmꢀ

\4. petal width in cmꢀ


Based on the information given in the input, the Android App will predict whether the plant is

Iris Setosa, Iris Versicolor, or Iris Virginica. ꢀ

Steps to create the project:ꢀ

\1. Download the iris data set (ﬁle name: iris.data) from [https://archive.ics.uci.edu/ml/](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)ꢀ

\2. Create a new python ﬁle with a name iris in the Syder editor or Jupyter notebook. Put the iris.data ﬁle in the

same directory where model.py resides.ꢀ

\3. After executing the line open(‘iris.tﬂite’,’wb’).write(tfmodel) a new ﬁle named iris.tﬂite will

get created in the same directory where iris.data resides. ꢀ

\4. Open Android Studio. Create a new kotlin-android project.ꢀ

\5. Right-click on app > New > Other >TensorFlow Lite Model.ꢀ

\6. Click on the folder icon.ꢀ

\7. Navigate to iris.tﬂite ﬁle.ꢀ

\8. Click on OK.ꢀ

\9. Click on the ﬁnish.ꢀ

\10. Copy the generated sample code and paste it in the click listener of a button in MainActivity.kt.ꢀ

Woohoo, App is ready! ꢀ

App's Screenshots:


<img src="App's Screenshots/Iris Prediction App img1.png" width="280" height="480">
<img src="App's Screenshots/Iris Prediction App img2.png" width="280" height="480">


Contributor- Prachi Bhatt
