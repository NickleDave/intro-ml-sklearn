# Frankenstein's monster-like combination of:
# https://github.com/jakevdp/sklearn_pycon2015/blob/master/notebooks/fig_code/sgd_separator.py
# and http://scikit-learn.org/stable/_downloads/plot_separating_hyperplane.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets.samples_generator import make_blobs

def plot_svm_separator():
    # we create 50 separable points
    X, Y = make_blobs(n_samples=50, centers=2,
                      random_state=0, cluster_std=0.60)

    # fit the model
    clf = SVC(kernel='linear')
    clf.fit(X, Y)

    # get the separating hyperplane
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-1, 5, 10)
    yy = a * xx - (clf.intercept_[0]) / w[1]

    # get parallels to separating hyperplane that pass through support vectors
    b = clf.support_vectors_[0]
    yy_down = a * xx + (b[1] - a * b[0])
    b = clf.support_vectors_[-1]
    yy_up = a * xx + (b[1] - a * b[0])

    # plot the line, the points, and the nearest vectors to the plane
    plt.figure(figsize=(7.5,7.5))
    plt.plot(xx, yy, 'k-')
    plt.plot(xx, yy_down, 'k--')
    plt.plot(xx, yy_up, 'k--')
    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[: ,1],
                s=320, c="none", linewidths=1, edgecolors='k' )
    plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, s=180)
    plt.axis('tight')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

if __name__ == '__main__':
    plot_svm_separator()
    plt.show()
