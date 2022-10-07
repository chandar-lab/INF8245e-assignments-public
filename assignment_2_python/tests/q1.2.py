OK_FORMAT = True

test = {   'name': 'q1.2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(\n...     get_euclidean_distance(np.ones((10, 4)), np.ones((5, 4))),\n...     np.zeros((10, 5)))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> _Xa = np.ones((5,3))\n>>> np.testing.assert_allclose(\n...     get_euclidean_distance(_Xa, _Xa), np.zeros((5, 5)))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> # HIDDEN\n'
                                               '>>> _rng = np.random.default_rng(41)\n'
                                               '>>> _Xa = _rng.random((500, 96))\n'
                                               '>>> _Xb = _rng.random((100, 96))\n'
                                               '>>> _euclid_dists = scipy.spatial.distance.cdist(_Xa, _Xb)\n'
                                               '>>> np.testing.assert_allclose(\n'
                                               '...     get_euclidean_distance(_Xa, _Xb), \n'
                                               '...     _euclid_dists)\n'
                                               '>>> \n',
                                       'hidden': True,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
