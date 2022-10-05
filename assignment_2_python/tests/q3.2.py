OK_FORMAT = True

test = {   'name': 'q3.2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> \n'
                                               '>>> _X = np.array([[1, 0.5, 0.2, 3],\n'
                                               '...               [1,  -1,   7, 3],\n'
                                               '...               [2,  12,  13, 3]])\n'
                                               '>>> _smx = softmax(_X)\n'
                                               '>>> np.testing.assert_allclose(_smx.sum(axis=1), [1,1,1])\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
