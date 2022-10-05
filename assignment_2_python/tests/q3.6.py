OK_FORMAT = True

test = {   'name': 'q3.6',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> X = np.array([[1, 2],[1, 1]]) \n'
                                               '>>> W = np.array([[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]])\n'
                                               '>>> b = np.array([1.0,1.0,1.0])\n'
                                               '>>> target = np.array([2,0])\n'
                                               '>>> \n'
                                               '>>> batch_size = 1\n'
                                               '>>> model = LogisticRegressionModel(W)\n'
                                               '>>> model.b = b.copy()\n'
                                               '>>> \n'
                                               '>>> validation_loss, validation_accuracy = validation(model,X,target,batch_size)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_array_less(0,validation_loss)\n'
                                               '>>> np.testing.assert_array_less(validation_accuracy,1.0)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
