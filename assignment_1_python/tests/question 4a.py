OK_FORMAT = True

test = {   'name': 'question 4a',
    'points': [1, 9],
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(\n'
                                               '...     ridge_regression_gradient(\n'
                                               '...         np.asarray([[0.5], [-0.5], [1.4]], dtype=np.float64),\n'
                                               '...         np.asarray([[-0.3, 0.1], [0.2, 1.1], [-0.45, -0.77]], dtype=np.float64),\n'
                                               '...         np.asarray([[0.8], [-0.12]], dtype=np.float64),\n'
                                               '...         0.99\n'
                                               '...     ),\n'
                                               '...     np.asarray([[1.94454], [0.35895067]], dtype=np.float64)\n'
                                               '>>> )\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
