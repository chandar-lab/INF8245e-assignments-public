OK_FORMAT = True

test = {   'name': 'question 3a',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(\n'
                                               '...     ridge_regression_optimize(\n'
                                               '...         np.zeros([2, 5], dtype=np.float64),\n'
                                               '...         np.zeros([2, 1], dtype=np.float64),\n'
                                               '...         hyperparameter=1\n'
                                               '...     ),\n'
                                               '...     np.zeros([1, 5]))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
