from otter.test_files import test_case

OK_FORMAT = False

name = "q1.3"
points = 2

@test_case(points=1.0, hidden=False)
def test_q1_3_public_1(numpy, binary_bow):
    _tmp = binary_bow(numpy.array(["this is is a randomword", "randomword1 randomword2", "is"]), vocab = ["this", "is", "a"])
    numpy.testing.assert_allclose(isinstance(_tmp, (numpy.ndarray, numpy.generic)), 1)
    numpy.testing.assert_allclose(_tmp.dtype == int, 1)
    numpy.testing.assert_allclose(_tmp, numpy.array([[1, 1, 1], [0, 0, 0], [0, 1, 0]], dtype=int))

