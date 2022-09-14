OK_FORMAT = True

test = {   'name': 'question 4b',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> _train_loss, _val_loss, _w = ridge_regression_gradient_descent(\n'
                                               '...     np.asarray([[0.5], [-0.5], [1.4]], dtype=np.float64),\n'
                                               '...     np.asarray([[-0.3, 0.1], [0.2, 1.1], [-0.45, -0.77]], dtype=np.float64),\n'
                                               '...     np.asarray([[0.76], [0.13], [-0.82]], dtype=np.float64),\n'
                                               '...     np.asarray([[1.04, -0.4], [0.9, 0.1], [-0.5, 0.47]], dtype=np.float64),\n'
                                               '...     np.asarray([[0.8], [-0.12]], dtype=np.float64),\n'
                                               '...     0.99,\n'
                                               '...     1e-7,\n'
                                               '...     1)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(_train_loss, np.asarray([1.0992692], dtype=np.float32))\n'
                                               '>>> np.testing.assert_allclose(_val_loss, np.asarray([0.40028697], dtype=np.float32))\n'
                                               '>>> np.testing.assert_allclose(_w, np.asarray([[0.79999981], [-0.12000004]], dtype=np.float32))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
