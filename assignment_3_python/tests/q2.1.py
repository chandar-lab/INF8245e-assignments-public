from otter.test_files import test_case

OK_FORMAT = False

name = "q2.1"
points = 3

@test_case(points=1.5, hidden=False)
def test_q2_1_public_1(numpy, frequency_bow):
    _tmp = frequency_bow(numpy.array(["this is is a randomword", "randomword1 randomword2", "is"]), vocab = ["this", "is", "a"])
    numpy.testing.assert_allclose(isinstance(_tmp, (numpy.ndarray, numpy.generic)), 1)
    numpy.testing.assert_allclose(_tmp.dtype == float, 1)
    numpy.testing.assert_allclose(_tmp, numpy.array([[0.25, 0.5, 0.25], [0, 0, 0], [0, 1, 0]], dtype=float))

