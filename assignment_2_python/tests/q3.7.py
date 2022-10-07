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
                                       'points': 4.0},
                                   {   'code': '>>> #HIDDEN\n'
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
                                               '>>> batch_x = []\n'
                                               '>>> batch_y = []\n'
                                               '>>> for x,y in iterate_samples(batch_size, X, target, True):\n'
                                               '...     batch_x.append(x)\n'
                                               '...     batch_y.append(y)\n'
                                               '>>> \n'
                                               '>>> expected_train_losses = []\n'
                                               '>>> expected_train_accuracies = []\n'
                                               '>>> expected_train_steps = []\n'
                                               '>>> expected_val_losses = []\n'
                                               '>>> expected_val_accuracies = []\n'
                                               '>>> expected_val_steps = []\n'
                                               '>>> expected_step_count = 0\n'
                                               '>>> \n'
                                               '>>> \n'
                                               '>>> output_0 = model(batch_x[0])\n'
                                               '>>> received_loss_0 = negative_log_likelihood(output_0, batch_y[0])\n'
                                               '>>> received_grad_w, received_grad_b = compute_gradients(batch_x[0], \n'
                                               '...                                                     output_0, batch_y[0])\n'
                                               '>>> model.W -= learning_rate * received_grad_w\n'
                                               '>>> model.b -= learning_rate * received_grad_b\n'
                                               '>>> expected_train_losses.append(received_loss_0.item())\n'
                                               '>>> predicted_label = output_0.argmax(axis=1)\n'
                                               '>>> expected_train_accuracies.append(np.equal(predicted_label, batch_y[0]).item())\n'
                                               '>>> expected_train_steps.append(1)\n'
                                               '>>> \n'
                                               '>>> output_1 = model(batch_x[1])\n'
                                               '>>> received_loss_1 = negative_log_likelihood(output_1, batch_y[1])\n'
                                               '>>> \n'
                                               '>>> expected_train_losses.append(received_loss_1.item())\n'
                                               '>>> predicted_label = output_1.argmax(axis=1)\n'
                                               '>>> expected_train_accuracies.append(np.equal(predicted_label, batch_y[1]).item())\n'
                                               '>>> expected_train_steps.append(2)\n'
                                               '>>> \n'
                                               '>>> model.W = W\n'
                                               '>>> model.b = b.copy()\n'
                                               '>>> train_losses, train_accuracies, train_steps, \\\n'
                                               '...     val_losses, val_accuracies, val_steps = \\\n'
                                               '...         train_one_epoch(model, X, target, X, target, batch_size, learning_rate, \n'
                                               '...                         validation_every_x_step)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(train_losses, expected_train_losses)\n'
                                               '>>> np.testing.assert_allclose(train_accuracies, expected_train_accuracies)\n'
                                               '>>> np.testing.assert_allclose(train_steps, expected_train_steps)\n',
                                       'hidden': True,
                                       'locked': False,
                                       'points': 6.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
