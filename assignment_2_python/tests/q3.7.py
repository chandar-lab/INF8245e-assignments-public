OK_FORMAT = True

test = {   'name': 'q3.7',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> X = np.array([[1, 2],[1, 1]]) \n'
                                               '>>> W = np.array([[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]])\n'
                                               '>>> b = np.array([1.0,1.0,1.0])\n'
                                               '>>> target = np.array([2,0])\n'
                                               '>>> \n'
                                               '>>> batch_size = 1\n'
                                               '>>> model = LogisticRegressionModel(W)\n'
                                               '>>> model.b = b.copy()\n'
                                               '>>> learning_rate = 0.5\n'
                                               '>>> validation_every_x_step = 1\n'
                                               '>>> \n'
                                               '>>> train_losses, train_accuracies, train_steps, \\\n'
                                               '...     val_losses, val_accuracies, val_steps = \\\n'
                                               '...         train_one_epoch(model, X, target, X, target, batch_size, learning_rate, \n'
                                               '...                         validation_every_x_step)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(len(train_losses), 2)\n'
                                               '>>> np.testing.assert_allclose(len(train_accuracies), 2)\n'
                                               '>>> np.testing.assert_allclose(train_steps, [1,2])\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 4.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
