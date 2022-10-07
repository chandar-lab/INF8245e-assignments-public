OK_FORMAT = True

test = {   'name': 'q3.3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> _X = np.array([[1, 2],[1, 1], [2, 1], [2, 2]])\n'
                                               '>>> _W = np.array([[1, 1], [2, 2], [3, 3]])\n'
                                               '>>> _b = np.array([1,1,1])\n'
                                               '>>> LR_model = LogisticRegressionModel(_W)\n'
                                               '>>> LR_model.b = _b\n'
                                               '>>> np.testing.assert_allclose(LR_model(_X).sum(axis=1), [1,1,1,1])\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> #HIDDEN\n'
                                               '>>> _X = np.array([[1, 2],[1, 1], [2, 1], [2, 2]])\n'
                                               '>>> _W = np.array([[1, 1], [2, 2], [3, 3]])\n'
                                               '>>> _b = np.array([1,1,1])\n'
                                               '>>> _wx = np.array([[3,6,9],[2,4,6],[3,6,9],[4,8,12]])\n'
                                               '>>> _wxb = np.array([[4,7,10],[3,5,7],[4,7,10],[5,9,13]])\n'
                                               '>>> model = LogisticRegressionModel(_W)\n'
                                               '>>> model.b = _b\n'
                                               '>>> np.testing.assert_allclose(model(_X), scipy.special.softmax(_wxb, axis=1))\n',
                                       'hidden': True,
                                       'locked': False,
                                       'points': 1.0},
                                   {   'code': '>>> #HIDDEN\n'
                                               '>>> \n'
                                               '>>> _rng = np.random.default_rng(41)\n'
                                               '>>> _X = _rng.integers(0, 10, size=(5, 4))\n'
                                               '>>> _W = np.random.normal(0.5, 0.1, (10, 4))\n'
                                               '>>> model = LogisticRegressionModel(_W)\n'
                                               '>>> model.b = np.ones(_W.shape[0])\n'
                                               '>>> wx = np.matmul(_W, _X[:, :, None]) \n'
                                               '>>> wx = np.resize(wx, wx.shape[:2])\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(model(_X), scipy.special.softmax(wx, axis=1))\n',
                                       'hidden': True,
                                       'locked': False,
                                       'points': 1.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
