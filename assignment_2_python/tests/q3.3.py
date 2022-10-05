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
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
