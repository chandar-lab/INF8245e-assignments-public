OK_FORMAT = True

test = {   'name': 'q3.5',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> X = np.array([[1, 2],[1, 1]]) \n'
                                               '>>> prediction = np.array([[0.3,0.2,0.5], [0.5,0.1,0.4]])\n'
                                               '>>> target = np.array([2,0])\n'
                                               '>>> received_grad_w, received_grad_b = compute_gradients(X, prediction,target)\n'
                                               '>>> np.testing.assert_allclose(received_grad_w.shape, [3,2])\n'
                                               '>>> np.testing.assert_allclose(received_grad_b.shape, [3])\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
