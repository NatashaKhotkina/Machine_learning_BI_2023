# Machine learning, Bioinformatic Institute, 2023.


## 1. K-nearest neighbour.
__K-nearest neighbour__ algorithm is a supervised learning algorithm. __KNN classifier__ learns train data and classifies test samples by finding K nearest neighbours of the sample in the training set and choosing the most prevalent class. __KNN regressor__ learns train data and predicts target by local interpolation of the targets of the nearest neighbours in the training set.
In [this homework](https://github.com/NatashaKhotkina/Machine_learning_BI_2023/tree/master/KNN), I implemented __KNN-classifier__ and __KNN-regressor__. The performance of models was evaluated with metric functions from `scikit-learn`.

## 2. Linear Regression. Gradient descend.
In [this homework](https://github.com/NatashaKhotkina/Machine_learning_BI_2023/tree/master/Linear_models), I implemented:
+ [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent);
+ [linear regression](https://en.wikipedia.org/wiki/Linear_regression);
+ [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression).

## 3. Unsupervised learning. Clustering and tSNE.
__Unsupervised learning__ is a type of machine learning that identifies patterns in data sets that are not labelled.
In [this homework](https://github.com/NatashaKhotkina/Machine_learning_BI_2023/tree/master/Unsupervised_learning) I implemented [K-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) I also selected best Agglomerative Clustering algorithm and annotated cell types with unsupervised learning.

## 4. Ensembles.
An ensemble is a combination of basic estimators that make predictions. 
[Random Forest](https://en.wikipedia.org/wiki/Random_forest) is a combination of [Decision Trees](https://en.wikipedia.org/wiki/Decision_tree). Each Decision Tree can see only a subset of data and a fraction of features ([Bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating) + [RSM](https://en.wikipedia.org/wiki/Random_subspace_method)).
[Boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning)) consists of several estimators. Each next estimator predicts the error of the previous estimator.
[Homework](https://github.com/NatashaKhotkina/Machine_learning_BI_2023/tree/master/Ensembles).

## 5. Kaggle Dota2 Competition.
[Here](https://github.com/NatashaKhotkina/Machine_learning_BI_2023/tree/master/kaggle_classical_ml) you can find a notebook for kaggle competition (data can be downloaded [here](https://www.kaggle.com/competitions/bi-ml-competition-2023/overview)). The notebook was run in Google Colab.

## 6. Neural networks.
A fully connected neural network (FC NN) is an NN where each neuron in one layer is connected to each neuron in the next layer. In [this homework](https://github.com/NatashaKhotkina/Machine_learning_BI_2023/tree/master/FC_NN), I implemented a FC NN, trained and validated it, studied the effect of normalization, activating functions, and optimizers.

## 7. Convolutional neural networks (CNN)
[Convolutional Neural Networks](https://en.wikipedia.org/wiki/Convolutional_neural_network) include convolutional layers. A convolutional layer consists of a kernel. Outputs are dot-products of kernel with fragments of input. 
![img](https://miro.medium.com/v2/resize:fit:640/format:webp/1*Fr6Umze2waDjWVHB2yzT4A.png)
