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
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
