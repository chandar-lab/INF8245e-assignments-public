OK_FORMAT = True

test = {   'name': 'q1.3',
    'points': 8,
    'suites': [   {   'cases': [   {   'code': '>>> _x_labels = np.array([1, 2, 1, 3, 3])\n'
                                               '>>> _euclid_dists = np.array([[1, 2], [3, 1], [2, 0] , [4,5], [1,0]])\n'
                                               '>>> _nearest_labels = get_k_nearest_labels(_euclid_dists, _x_labels, 3)\n'
                                               '>>> np.testing.assert_allclose(_nearest_labels.shape, [3,2])\n'
                                               '>>> nl0 = _nearest_labels[:,0]\n'
                                               '>>> nl1 = _nearest_labels[:,1]\n'
                                               '>>> nl0.sort()\n'
                                               '>>> nl1.sort()\n'
                                               '>>> np.testing.assert_allclose(nl0, np.array([1,1,3]))\n'
                                               '>>> np.testing.assert_allclose(nl1, np.array([1,2,3]))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
