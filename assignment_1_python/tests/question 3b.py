OK_FORMAT = True

test = {   'name': 'question 3b',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> for split, ((y_train, X_train), (y_valid, X_valid)) in enumerate(cross_validation( \\\n'
                                               '...         np.asarray([[10], [20], [30]]), \\\n'
                                               '...         np.asarray([[11, 12], [21, 22], [31, 32]]), \\\n'
                                               '...         splits=3 \\\n'
                                               '...     )):\n'
                                               '...     if split == 0:\n'
                                               '...         np.testing.assert_allclose(y_train, [[10], [20]])\n'
                                               '...         np.testing.assert_allclose(X_train, [[11, 12], [21, 22]])\n'
                                               '...         np.testing.assert_allclose(y_valid, [[30]])\n'
                                               '...         np.testing.assert_allclose(X_valid, [[31, 32]])\n'
                                               '...     elif split == 1:\n'
                                               '...         np.testing.assert_allclose(y_train, [[30], [20]])\n'
                                               '...         np.testing.assert_allclose(X_train, [[31, 32], [21, 22]])\n'
                                               '...         np.testing.assert_allclose(y_valid, [[10]])\n'
                                               '...         np.testing.assert_allclose(X_valid, [[11, 12]])\n'
                                               '...     elif split == 2:\n'
                                               '...         np.testing.assert_allclose(y_train, [[30], [10]])\n'
                                               '...         np.testing.assert_allclose(X_train, [[31, 32], [11, 12]])\n'
                                               '...         np.testing.assert_allclose(y_valid, [[20]])\n'
                                               '...         np.testing.assert_allclose(X_valid, [[21, 22]])\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
