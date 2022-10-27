from otter.test_files import test_case

OK_FORMAT = False

name = "q4.2"
points = 2

@test_case(points=2.0, hidden=False)
def test_q4_2_public_1(numpy, gaussian_naive_bayes):
    _tmp_sample = numpy.array([[0.5, 0.1]])
    _tmp_label = numpy.array([1])
    _f1_train_bnb_bow, _f1_val_bnb_bow, _f1_test_bnb_bow = gaussian_naive_bayes(_tmp_sample, _tmp_label, _tmp_sample, _tmp_label, _tmp_sample, _tmp_label)
    numpy.testing.assert_allclose(_f1_train_bnb_bow, 1.0)
    numpy.testing.assert_allclose(_f1_val_bnb_bow, 1.0)
    numpy.testing.assert_allclose(_f1_test_bnb_bow, 1.0)

