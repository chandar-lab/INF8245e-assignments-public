OK_FORMAT = True

test = {   'name': 'q1.4',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> _temp_labels = np.asarray([ [4, 1, 4, 6, 4], [7, 2, 1, 5, 4], [2, 2, 5, 6, 1] ], dtype=np.uint8)\n'
                                               '>>> np.testing.assert_allclose(\n'
                                               '...     get_prediction(_temp_labels),\n'
                                               '...     np.asarray([[2, 2, 1, 6, 4]], dtype=np.uint8))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
