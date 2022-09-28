OK_FORMAT = True

test = {   'name': 'question 4b',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> _train_loss, _val_loss, _w = ridge_regression_gradient_descent(\n'
                                               '...     np.asarray([[0.5], [-0.5], [1.4]]),\n'
                                               '...     np.asarray([[-0.3, 0.1], [0.2, 1.1], [-0.45, -0.77]]),\n'
                                               '...     np.asarray([[0.76], [0.13], [-0.82]]),\n'
                                               '...     np.asarray([[1.04, -0.4], [0.9, 0.1], [-0.5, 0.47]]),\n'
                                               '...     np.asarray([[0.8], [-0.12]]),\n'
                                               '...     0.90,\n'
                                               '...     1e-3,\n'
                                               '...     1)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(_train_loss, np.asarray([1.0992692]), rtol=1e-6)\n'
                                               '>>> np.testing.assert_allclose(_val_loss, np.asarray([0.40028697]), rtol=1e-6)\n'
                                               '>>> np.testing.assert_allclose(_w, np.asarray([[0.79819946], [-0.12038055]]), rtol=1e-6)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2},
                                   {   'code': '>>> _train_loss, _val_loss, _w = ridge_regression_gradient_descent(\n'
                                               '...     np.asarray([[0.5], [-0.5], [1.4]]),\n'
                                               '...     np.asarray([[-0.3, 0.1], [0.2, 1.1], [-0.45, -0.77]]),\n'
                                               '...     np.asarray([[0.76], [0.13], [-0.82]]),\n'
                                               '...     np.asarray([[1.04, -0.4], [0.9, 0.1], [-0.5, 0.47]]),\n'
                                               '...     np.asarray([[0.8], [-0.12]]),\n'
                                               '...     0.90,\n'
                                               '...     1e-3,\n'
                                               '...     2)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(_train_loss, np.asarray([1.0992692, 1.0984721]), rtol=1e-6)\n'
                                               '>>> np.testing.assert_allclose(_val_loss, np.asarray([0.40028697, 0.3995371]), rtol=1e-6)\n'
                                               '>>> np.testing.assert_allclose(_w, np.asarray([[0.79640243], [-0.12075986]]), rtol=1e-6)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
