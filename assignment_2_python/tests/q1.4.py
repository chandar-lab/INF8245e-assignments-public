OK_FORMAT = True

test = {   'name': 'q1.4',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> _temp_labels = np.asarray([ [4, 1, 4, 6, 4], [7, 2, 1, 5, 4], [2, 2, 5, 6, 1] ], dtype=np.uint8)\n'
                                               '>>> np.testing.assert_allclose(\n'
                                               '...     get_prediction(_temp_labels),\n'
                                               '...     np.asarray([[2, 2, 1, 6, 4]], dtype=np.uint8))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> # HIDDEN\n'
                                               '>>> _rng = np.random.default_rng(41)\n'
                                               '>>> _temp_labels = _rng.integers(0, 10, size=(5, 1000))\n'
                                               '>>> _pred_sol = scipy.stats.mode(_temp_labels)[0]\n'
                                               '>>> np.testing.assert_allclose(\n'
                                               '...     get_prediction(_temp_labels),\n'
                                               '...     _pred_sol)\n',
                                       'hidden': True,
                                       'locked': False,
                                       'points': 2.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
