OK_FORMAT = True

test = {   'name': 'q3.4',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> prediction = np.array([[0.1,0.9], [0.4,0.6]])\n'
                                               '>>> target = np.array([1,0])\n'
                                               '>>> np.testing.assert_allclose(negative_log_likelihood(prediction,target), 0.5108256237659906)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
