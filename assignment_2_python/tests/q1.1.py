OK_FORMAT = True

test = {   'name': 'q1.1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> _data = np.asarray([[0, 1, 2], [3, 3, 6], [9, 5, 7]], dtype=np.uint8)\n'
                                               '>>> np.testing.assert_allclose(min_max_normalize(_data)[0].min(), np.asarray([0.0], dtype=np.float64))\n'
                                               '>>> np.testing.assert_allclose(min_max_normalize(_data)[0].max(), np.asarray([1.0], dtype=np.float64))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> _data = np.asarray([[0, 5, 10], [10, 15, 20], [20, 25, 30]], dtype=np.uint8)\n'
                                               '>>> np.testing.assert_allclose(\n'
                                               '...     min_max_normalize(_data)[0], \n'
                                               '...     np.asarray([[0.0, 1/6, 1/3], [1/3, 0.5, 2/3], [2/3, 5/6, 1.0]], dtype=np.float64))\n',
                                       'hidden': True,
                                       'locked': False,
                                       'points': 1.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
