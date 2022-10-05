OK_FORMAT = True

test = {   'name': 'q2.2',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> X = np.array([[1,2,3,4],\n'
                                               '...             [1,2,1,4],\n'
                                               '...             [2,3,3,3],\n'
                                               '...             [2,3,1,3]])\n'
                                               '>>> y = np.array([1,1,0,0])\n'
                                               '>>> \n'
                                               '>>> prior_probs = [0.5,0.5]\n'
                                               '>>> means = [[2,3,2,3],[1,2,2,4]]\n'
                                               '>>> vars = [[0.001, 0.001, 1.001, 0.001], \n'
                                               '...         [0.001, 0.001, 1.001, 0.001]]\n'
                                               '>>> num_classes = 2\n'
                                               '>>> preds = gnb_predict(X,prior_probs,means,vars,num_classes)\n'
                                               '>>> np.testing.assert_allclose(preds, y)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
