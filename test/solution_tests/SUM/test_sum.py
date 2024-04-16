from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum2(self):
        assert sum_solution.compute(100, 100) == 200

    def test_sum3(self):
        assert sum_solution.compute(0, 0) == 0

    def test_sum4(self):
        assert sum_solution.compute(99, 0) == 99
