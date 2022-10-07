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
                                       'points': 2.0},
                                   {   'code': '>>> #HIDDEN\n'
                                               '>>> X = np.array([[1, 2],[1, 1]]) \n'
                                               '>>> W = np.array([[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]])\n'
                                               '>>> b = np.array([1.0,1.0,1.0])\n'
                                               '>>> target = np.array([2,0])\n'
                                               '>>> \n'
                                               '>>> batch_size = 1\n'
                                               '>>> model = LogisticRegressionModel(W)\n'
                                               '>>> model.b = b.copy()\n'
                                               '>>> \n'
                                               '>>> output = model(X)\n'
                                               '>>> expected_val_loss = negative_log_likelihood(output, target)\n'
                                               '>>> predictions = output.argmax(axis=1)\n'
                                               '>>> correct_predictions = np.equal(predictions, target).sum()\n'
                                               '>>> expected_val_accuracy = correct_predictions / 2\n'
                                               '>>> \n'
                                               '>>> \n'
                                               '>>> validation_loss, validation_accuracy = validation(model,X,target,batch_size)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_almost_equal(validation_loss, expected_val_loss)\n'
                                               '>>> np.testing.assert_almost_equal(validation_accuracy, expected_val_accuracy)\n',
                                       'hidden': True,
                                       'locked': False,
                                       'points': 4.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
