OK_FORMAT = True

test = {   'name': 'q2.1',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> X = np.array([[1,2,3,4],\n'
                                               '...             [1,2,1,4],\n'
                                               '...             [2,3,3,3],\n'
                                               '...             [2,3,1,3]])\n'
                                               '>>> y = np.array([1,1,0,0])\n'
                                               '>>> \n'
                                               '>>> prior_probs, means, vars = gnb_fit_classifier(X,y)\n'
                                               '>>> np.testing.assert_allclose(\n'
                                               '...     prior_probs,\n'
                                               '...     [0.5,0.5])\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(\n'
                                               '...     means,\n'
                                               '...     [np.array([2., 3., 2., 3.]), np.array([1., 2., 2., 4.])])\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(\n'
                                               '...     vars,\n'
                                               '...     [np.array([0.001, 0.001, 1.001, 0.001]), np.array([0.001, 0.001, 1.001, 0.001])])\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
