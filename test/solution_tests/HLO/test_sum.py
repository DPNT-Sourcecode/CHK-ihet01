from solutions.HLO import sum_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello("John") == "Hello, John!"

    def test_hello2(self):
        assert hello_solution.hello("Chris") == "Hello, Chris!"