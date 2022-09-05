OK_FORMAT = True

test = {   'name': 'question 1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_equal(problem_1([1,2]), True)\n'
                                               '>>> np.testing.assert_equal(problem_1([2,1]), True)\n'
                                               '>>> np.testing.assert_equal(problem_1([1,1]), True)\n'
                                               '>>> np.testing.assert_equal(problem_1([1,2,0]), False)\n'
                                               '>>> np.testing.assert_equal(problem_1([1,2,3,4,5]), True)\n'
                                               '>>> np.testing.assert_equal(problem_1([5,4,3,2,1]), True)\n'
                                               '>>> np.testing.assert_equal(problem_1([5,3,4,1,2]), False)\n'
                                               '>>> np.testing.assert_equal(problem_1([1,1,1,1,1]), True)\n'
                                               '>>> np.testing.assert_equal(problem_1([1]), True)\n'
                                               '>>> np.testing.assert_equal(problem_1([]), True)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
