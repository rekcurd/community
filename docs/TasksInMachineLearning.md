# Tasks in Machine Learning
There are two main tasks in machine learning (ML) as a service.

1. Building ML model
1. Serving ML service (Drucker's target)

## Tasks in Building ML model
1. Data
    1. Collection (e.g. supervised learning, unsupervised learning, distant supervision)
    1. Cleaning/Cleansing (e.g. outlier filtering, data completion)
1. Features
    1. Preprocessing (e.g. morphological analysis, syntactic analysis)
    1. Dictionary (e.g. wordnet)
1. Training
    1. Algorithms (e.g. regression, SVM, deep learning)
    1. Parameter tuning (e.g. grid search, Coarse-to-Fine search, early stopping strategy)
    1. Evaluation (e.g. cross validation, ROC curve)
1. Others
    1. Server setup
    1. Versioning (data, parameters, model and performance)

Because of the recent ML popularity, there are many useful tools/frameworks to handle the tasks above. [kubeflow](https://github.com/kubeflow/kubeflow) is one of the best options for building a ML development environment.

## Tasks in Serving ML service
1. High Availability
1. Management
    1. Uploading the latest model
    1. Switching a model without stopping services
    1. Versioning models
1. Monitor
    1. Load balancing
    1. Auto healing
    1. Auto scaling
    1. Performance/Results check
1. Others
    1. Server setup
    1. Managing the service level (e.g. development/staging/production)
    1. Integrate into the existing services
    1. AB testing
    1. Managing all ML services
    1. Logging

Since there are few tools available for the tasks above, we are developing Drucker to solve these tasks. In Drucker, any ML framework (e.g. scikit-learn, gensim, Chainer, PyTorch, TensorFlow) is serveable. Drucker can comprehensively manage the ML model and the service level.