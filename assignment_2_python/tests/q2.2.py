OK_FORMAT = True

test = {   'name': 'q2.2',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> X = np.array([[1,2,3,4],\n'
                                               '...             [1,2,1,4],\n'
                                               '...             [2,3,3,3],\n'
                                               '...             [2,3,1,3]])\n'
                                               '>>> y = np.array([1,1,0,0])\n'
                                               '>>> \n'
                                               '>>> prior_probs = [0.5,0.5]\n'
                                               '>>> means = [np.array([2,3,2,3]), np.array([1,2,2,4])]\n'
                                               '>>> vars = [np.array([0.001, 0.001, 1.001, 0.001]), np.array([0.001, 0.001, 1.001, 0.001])]\n'
                                               '>>> num_classes = 2\n'
                                               '>>> preds = gnb_predict(X,prior_probs,means,vars,num_classes)\n'
                                               '>>> np.testing.assert_allclose(preds, y)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0},
                                   {   'code': '>>> #HIDDEN\n'
                                               '>>> _rng = np.random.default_rng(41)\n'
                                               '>>> X = _rng.integers(0, 10, size=(5, 4))\n'
                                               '>>> y = _rng.integers(-1, 2, size=(5))\n'
                                               '>>> \n'
                                               '>>> \n'
                                               '>>> prior_probs, means, vars = gnb_fit_classifier(X,y)\n'
                                               '>>> from sklearn.naive_bayes import GaussianNB\n'
                                               '>>> clf = GaussianNB(var_smoothing=1e-4)\n'
                                               '>>> _clf_fit = clf.fit(X,y)\n'
                                               '>>> X_t = _rng.integers(0, 10, size=(10, 4))\n'
                                               '>>> y_t = clf.predict(X_t)\n'
                                               '>>> \n'
                                               '>>> # preds = gnb_predict(X_t, clf.class_prior_, clf.theta_, clf.var_, len(clf.classes_))\n'
                                               '>>> preds = gnb_predict(X_t, _clf_fit.class_prior_, _clf_fit.theta_, _clf_fit.var_, len(_clf_fit.classes_))\n'
                                               '>>> np.testing.assert_allclose(preds, y_t)\n',
                                       'hidden': True,
                                       'locked': False,
                                       'points': 4.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
