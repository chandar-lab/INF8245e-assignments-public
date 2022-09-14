OK_FORMAT = True

test = {   'name': 'question 2b',
    'points': [0.5, 2.25, 2.25],
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(\n'
                                               '...     linear_regression_predict(\n'
                                               '...         np.zeros([10, 2], dtype=np.float64),\n'
                                               '...         np.zeros([2, 1], dtype=np.float64)\n'
                                               '...     ),\n'
                                               '...     np.zeros([10, 1]))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
