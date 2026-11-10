# Practical Implementations: Algorithms & Data Science

This repository contains practical implementations in **Analysis and Design of Algorithms (ADA)** and **Data Science (DS)**. The algorithms are implemented in both Java and Python, and the data science modules cover foundational to advanced machine learning pipelines, feature engineering, and statistical modeling using Python.

---

## 1. Analysis and Design of Algorithms (ADA)

The ADA module encompasses classical algorithmic paradigms, including Divide and Conquer, Greedy Techniques, Dynamic Programming, and Backtracking. Implementations are provided in both Java and Python.

### 1.1 Divide and Conquer

* **Merge Sort (`MERGESORT`)**
  * **Objective:** Sort an array of elements in non-decreasing order using recursive division and merging.
  * **Task Explanation:** Divides the input array into two equal halves until single-element subproblems are reached, then merges the sorted halves into a consolidated array. Guarantees a stable sorting time complexity of $O(n \log n)$.

* **Quick Sort (`QUICKSORT`)**
  * **Objective:** In-place partitioning and sorting of an array around selected pivots.
  * **Task Explanation:** Selects a pivot element and rearranges elements such that all values smaller than the pivot precede it and all larger values succeed it. Recursively applies the partitioning to left and right subarrays, achieving an average time complexity of $O(n \log n)$.

---

### 1.2 Greedy Strategy

* **Dijkstra’s Single-Source Shortest Path**
  * **Without Priority Queue (`DIJKSTRAS_(WO_PQ)`):** Computes shortest paths from a source vertex to all other vertices in a weighted graph with non-negative weights by iteratively performing linear scans to identify the unvisited vertex with the minimum distance ($O(V^2)$).
  * **With Priority Queue (`DIJKSTRAS_(W_PQ)`):** Implements an optimized min-heap priority queue to extract minimum distance vertices, reducing traversal overhead to $O((V + E) \log V)$ for sparse graphs.

* **Prim’s Algorithm (`PRIM`)**
  * **Objective:** Construct a Minimum Spanning Tree (MST) for a connected, weighted undirected graph.
  * **Task Explanation:** Begins from an arbitrary vertex and greedily expands the spanning tree by adding the minimum-weight edge connecting a vertex within the tree to an unvisited vertex outside it, ensuring no cycles are formed.

* **Kruskal’s Algorithm (`KRUSKAL`)**
  * **Objective:** Identify the Minimum Spanning Tree (MST) using edge-based greedy selection.
  * **Task Explanation:** Sorts all edges in ascending order of edge weight and employs Disjoint Set Union (DSU / Union-Find) with path compression and union by rank to detect cycles, selecting $V - 1$ edges that span all vertices with minimal total cost.

* **Job Sequencing with Deadlines (`DEADLINES`)**
  * **Objective:** Maximize cumulative profit by scheduling unit-duration jobs with strict deadlines.
  * **Task Explanation:** Sorts available jobs in descending order of profit and assigns each job to its latest possible open slot before its deadline. If no free slot exists before the deadline, the job is discarded.

* **Fractional Knapsack (`KNAPSACK`)**
  * **Objective:** Maximize total value in a knapsack with a fixed weight capacity where items can be partitioned.
  * **Task Explanation:** Calculates the profit-to-weight ratio for each item, sorts items in descending order of ratio, and greedily loads items into the knapsack. If remaining capacity cannot accommodate a full item, the fractional portion that completely exhausts the capacity is taken.

---

### 1.3 Dynamic Programming

* **Optimal Binary Search Tree (`OBST`, `OBST2`)**
  * **Objective:** Construct a Binary Search Tree (BST) that minimizes expected total search cost given key access probabilities and dummy failure probabilities.
  * **Task Explanation:** Solves overlapping subproblems of optimal subtrees for contiguous key ranges using 2D dynamic programming tables. Evaluates every candidate key within a range as a prospective subtree root, accumulating subproblem weights and transition costs to establish both the optimal expected search cost and the optimal root matrix.

---

### 1.4 Backtracking & Graph Traversal

* **Articulation Points (`ARTICULATIONPOINTS`, `ARTICULATIONPOINTS2`)**
  * **Objective:** Detect all cut vertices (articulation points) in a connected undirected graph.
  * **Task Explanation:** Executes Tarjan’s Depth First Search (DFS) traversal to assign discovery times (`tin`) and lowest reachable ancestor times (`low`). Identifies vertices whose removal increases the number of connected components: the root if it possesses two or more DFS children, and any non-root vertex $u$ with a child $v$ satisfying $low[v] \ge tin[u]$.

* **Graph Coloring (`GRAPHCOLORING`)**
  * **Objective:** Solve the $m$-Coloring problem on an undirected graph.
  * **Task Explanation:** Assigns at most $m$ distinct colors to graph vertices such that no two adjacent vertices share the same color. Utilizes recursive backtracking to try color assignments sequentially, pruning search branches whenever an adjacency constraint is violated.

* **N-Queens Problem (`NQUEENS`)**
  * **Objective:** Place $N$ non-attacking chess queens on an $N \times N$ chessboard.
  * **Task Explanation:** Employs constraint-satisfaction backtracking to place one queen per row, verifying safety constraints across column indices and positive/negative diagonal vectors. Backtracks when no valid square remains in a row until all viable configurations are derived.

* **Sum of Subsets (`SUBSETSUM`)**
  * **Objective:** Find all distinct subsets of a given set of positive integers that sum up to a target value.
  * **Task Explanation:** Explores a state-space tree where each decision includes or excludes an element. Pruning heuristics terminate branches early if the current partial sum exceeds the target or if the remaining sum cannot bridge the remaining deficit.

---

## 2. Data Science & Machine Learning (DS)

The DS module covers exploratory data analysis, data preprocessing, regression, classification, clustering, dimensionality reduction, and feature selection pipelines.

### 2.1 Exploratory Data Analysis & Preprocessing

* **Data Preprocessing Pipeline (`datapreprocessing.py`)**
  * **Objective:** Inspect, clean, and impute tabular dataset anomalies.
  * **Task Explanation:** Assesses dataset dimensions, column datatypes, and summary statistics. Detects null values across attributes and applies targeted imputation: statistical mean imputation for continuous numerical features and modal imputation for categorical attributes.

* **Data Visualization (`datavisualisation.py`)**
  * **Objective:** Examine feature interactions and class distributions through visual exploration.
  * **Task Explanation:** Leverages Seaborn and Matplotlib to generate scatter plots across multidimensional attributes (e.g., Sepal and Petal dimensions), visualizing feature boundaries, cluster tendencies, and inter-class variance.

* **End-to-End EDA & Feature Engineering (`task1_iris_eda.py`)**
  * **Objective:** Implement an exploratory data analysis, data transformation, and encoding pipeline.
  * **Task Explanation:** Enforces automated missing value imputation, applies comparative categorical encoding strategies (One-Hot Encoding, Label Encoding, and Ordinal Encoding), standardizes numerical features with `StandardScaler`, and outputs correlation and distribution plots to disk.

---

### 2.2 Supervised Learning: Regression

* **Real Estate Price Prediction (`linearregression.py`, `linearregression2.py`)**
  * **Objective:** Model and predict continuous rental prices based on property characteristics.
  * **Task Explanation:** Preprocesses property features (e.g., bedrooms, bathrooms, carpet area), isolates numerical predictors, performs train-test splitting, trains an Ordinary Least Squares (OLS) Linear Regression model, and computes evaluation metrics including Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), $R^2$ Score, and Adjusted $R^2$.

* **Synthetic Multivariable Regression Analysis (`task3_synthetic_regression.py`)**
  * **Objective:** Analyze linear model behavior, multicollinearity, and noise sensitivity on controlled synthetic data.
  * **Task Explanation:** Synthesizes multidimensional physiological data (age, blood pressure, cholesterol, screen time) with defined collinear relationships and Gaussian noise, fits a multiple linear regression model after feature standardization, and evaluates goodness-of-fit metrics ($R^2$, MSE).

---

### 2.3 Supervised Learning: Classification

* **K-Nearest Neighbors (`knn.py`)**
  * **Objective:** Multi-class classification using non-parametric instance-based learning.
  * **Task Explanation:** Standardizes feature scales to prevent distance distortion, partitions data with stratified train-test splits, classifies query points based on majority voting among $k$ nearest Euclidean neighbors, and evaluates performance via Confusion Matrix and Classification Report (Precision, Recall, F1-Score).

* **Decision Tree Classification (`decisiontree.py`, `decisiontree2.py`)**
  * **Objective:** Non-linear rule-based multi-class classification.
  * **Task Explanation:** Encodes target classes, splits feature subsets, constructs a decision tree based on recursive feature threshold partitioning (information gain / Gini impurity), and outputs classification metrics alongside confusion matrices.

* **Random Forest Classification (`random_forest.py`)**
  * **Objective:** Ensemble classification leveraging bootstrap aggregation (bagging) and randomized feature subsets.
  * **Task Explanation:** Cleans financial/banking data by addressing infinities, imputing missing numerical values with medians and categorical values with modes, label encodes categorical variables, and fits an ensemble of randomized decision trees to assess overall predictive accuracy and robustness.

---

### 2.4 Unsupervised Learning: Clustering

* **K-Means Clustering (`kmeans.py`)**
  * **Objective:** Partition unlabeled data into $k$ distinct, non-overlapping spherical clusters.
  * **Task Explanation:** Scales input features to zero mean and unit variance, initializes cluster centroids, iteratively refines assignments to minimize within-cluster sum of squares (inertia), extracts final centroids, and quantitatively evaluates cluster cohesion and separation using Silhouette Score and Adjusted Rand Index (ARI).

* **Hierarchical Agglomerative Clustering (`hierarchialclustering.py`)**
  * **Objective:** Group multidimensional observations using bottom-up linkage hierarchies.
  * **Task Explanation:** Normalizes continuous weather/sensor variables, computes pair-wise distance matrices using Ward's minimum variance criterion, constructs and plots a hierarchical dendrogram, fits Agglomerative Clustering into discrete clusters, and scores separation via Silhouette analysis.

---

### 2.5 Dimensionality Reduction & Feature Selection

* **Principal Component Analysis (`pca.py`)**
  * **Objective:** Project high-dimensional data onto orthogonal axes of maximum variance.
  * **Task Explanation:** Centers and scales feature vectors, performs eigen-decomposition of the covariance matrix to extract principal components, projects samples onto the top two principal components ($PC_1, PC_2$), and provides comparative visualizations between raw feature coordinates and transformed principal subspaces.

* **Recursive Feature Elimination (`rfedimensional.py`, `task2_feature_selection.py`)**
  * **Objective:** Isolate optimal feature subsets and minimize dimensional redundancy.
  * **Task Explanation:** Trains a baseline Logistic Regression classifier on all available diagnostic features (e.g., Breast Cancer dataset), iteratively prunes the least important features according to model weights using RFE down to a target subset, and contrasts classification accuracy, precision, recall, and F1-score before and after reduction.

* **PCA Impact on Regression Performance (`task4_gpa_pca_impact.py`)**
  * **Objective:** Assess the effect of linear subspace projection on predictive regression models.
  * **Task Explanation:** Evaluates a Linear Regression model predicting continuous academic outcomes (GPA) first using full standardized feature sets, then compresses the predictor space to orthogonal principal components via PCA, directly measuring variance preservation, MSE, and $R^2$ trade-offs.

* **Clustering Analysis Before and After PCA (`task6_kmeans_pca.py`)**
  * **Objective:** Investigate how dimensionality reduction impacts cluster formation and quality.
  * **Task Explanation:** Applies K-Means clustering to full-dimensional feature sets and evaluates Silhouette Score and Adjusted Rand Index against known class partitions; subsequently projects the dataset to a 2D PCA representation and reapplies K-Means to contrast cluster boundary quality and noise filtering.

---

## Repository Structure

```
adads_prac/
│
├── ADA/
│   ├── JAVA/
│   │   ├── ARTICULATIONPOINTS.java
│   │   ├── ARTICULATIONPOINTS2.java
│   │   ├── DEADLINES.java
│   │   ├── DIJKSTRAS_(WO_PQ).java
│   │   ├── DIJKSTRAS_(W_PQ).java
│   │   ├── GRAPHCOLORING.java
│   │   ├── KNAPSACK.java
│   │   ├── KRUSKAL.java
│   │   ├── MERGESORT.java
│   │   ├── NQUEENS.java
│   │   ├── OBST.java
│   │   ├── OBST2.JAVA
│   │   ├── PRIM.java
│   │   ├── QUICKSORT.java
│   │   └── SUBSETSUM.java
│   │
│   ├── PYTHON/
│   │   ├── ARTICULATIONPOINTS.py
│   │   ├── DEADLINES.py
│   │   ├── DIJKSTRAS_(WO_PQ).py
│   │   ├── DIJKSTRAS_(W_PQ).py
│   │   ├── GRAPHCOLORING.py
│   │   ├── KNAPSACK.py
│   │   ├── KRUSKAL.py
│   │   ├── MERGESORT.py
│   │   ├── NQUEENS.py
│   │   ├── OBST.py
│   │   ├── PRIM.py
│   │   ├── QUICKSORT.py
│   │   └── SUBSETSUM.py
│   │
│   └── graph_input.txt
│
└── DS/
    ├── datapreprocessing.py
    ├── datavisualisation.py
    ├── decisiontree.py
    ├── decisiontree2.py
    ├── hierarchialclustering.py
    ├── kmeans.py
    ├── knn.py
    ├── linearregression.py
    ├── linearregression2.py
    ├── pca.py
    ├── random_forest.py
    ├── rfedimensional.py
    ├── task1_iris_eda.py
    ├── task2_feature_selection.py
    ├── task3_synthetic_regression.py
    ├── task4_gpa_pca_impact.py
    └── task6_kmeans_pca.py
```
