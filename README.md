# Udacity ud120 Projects v2: python3 + jupyter + conda env

The aim of this fork is to improve original starter project code for students taking
[Intro to Machine Learning](https://classroom.udacity.com/courses/ud120) on Udacity with
python 3.8, conda managing and jupyter notebooks.

## Mini-Projects

- [Lesson 2: Naive Bayes](./02-naive-bayes/nb_author_id.ipynb)
- [Lesson 3: SVM](./03-svm/svm_author_id.ipynb)
- [Lesson 4: Decision Trees](./04-decision-tree/dt_author_id.ipynb)
- [Lesson 5: Choose Your own Algorithm](./05-choose-your-own/your_algorithm.ipynb)
- [Lesson 6: Datasets and Questions](./06-datasets-questions/explore_enron_data.ipynb)
- [Lesson 7: Regressions](./07-regression/finance_regression.ipynb)
- [Lesson 8: Outliers](./08-outliers/outlier_removal_regression.ipynb)
- [Lesson 9: Clustering](09-10-k-means/k_means_cluster.ipynb)
- [Lesson 10: Feature Scaling](09-10-k-means/k_means_cluster.ipynb)
- [Lesson 11: Text Learning](11-text-learning/vectorize_text.ipynb)
- [Lesson 12: Feature Selection](12-feature-selection/find_signature.ipynb)
- [Lesson 13: PCA](13-pca/eigenfaces.ipynb)
- [Lesson 14: Validation](14-validation/validate_poi.ipynb)
- [Lesson 15: Evaluation Metrics](15-evaluation/evaluate_poi_identifier.ipynb)
- [Lesson 17: Final Project](17-final-project/poi_id.ipynb)

## Important Notes

### Lesson 3: SVM

In this repo newer version of `scikit-learn` is used. Thus, to get the results expected by the course grader
you need to use `SVC` with `gamma='auto'`, since the default value of gamma changed, see `sklearn.svm.SVC` [docs](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html):
> Changed in version 0.22: The default value of gamma changed from 'auto' to 'scale'.

For example:

```python
clf = SVC(kernel='linear', gamma='auto')
```

### Lesson 7: Regressions

To get the correct (acceptable by grader) results set `sort_keys='../utils/python2_lesson06_keys.pkl'` for
`feature_format` function:

```python
...
data = feature_format(dictionary, features_list, remove_any_zeroes=True, sort_keys='../utils/python2_lesson06_keys.pkl')
...
```

> [...] This will open up a file in the tools folder with the Python 2 key order.

 See [this](https://classroom.udacity.com/courses/ud120/lessons/2301748537/concepts/30416086000923) for detailed explanation.


## Initial Setup

### 1. Clone the repo

```bash
$ git clone https://github.com/trsvchn/ud120-projects-py3-jupyter.git
$ cd ud120-projects-v2
```

### 2. Set up conda environment

#### 2.1. Download and install anaconda

[link](https://www.anaconda.com/distribution/)

#### 2.2. Create environment

```bash
$ conda env create -f environment.yml
```

#### 2.3. Activate environment via

```bash
$ conda activate ud120
```

### 3. Run starter script to check env and download required data

```bash
$ python ./utils/starter.py
```
