OK_FORMAT = True

test = {   'name': 'question 2b',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(\n'
                                               '...     linear_regression_predict(\n'
                                               '...         np.zeros([10, 2], dtype=np.float64),\n'
                                               '...         np.zeros([2, 1], dtype=np.float64)\n'
                                               '...     ),\n'
                                               '...     np.zeros([10, 1]))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
