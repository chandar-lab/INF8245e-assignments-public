OK_FORMAT = True

test = {   'name': 'question 2a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(\n'
                                               '...     design_matrix_simple(\n'
                                               '...         np.asarray([22, 23, 35], dtype=np.float64),\n'
                                               '...         np.asarray([0.1, 0.2, 0.3], dtype=np.float64)\n'
                                               '...     ),\n'
                                               '...     np.asarray([[22, 1], [23, 1], [35, 1]]))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
