OK_FORMAT = True

test = {   'name': 'question 2c',
    'points': [1, 9],
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(\n'
                                               '...     linear_regression_optimize(\n'
                                               '...         np.asarray([[1], [2], [3]], dtype=np.float64),\n'
                                               '...         np.asarray([[0, 1], [0.5, 1], [1, 1]], dtype=np.float64)\n'
                                               '...     ),\n'
                                               '...     np.asarray([[2], [1]]))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
