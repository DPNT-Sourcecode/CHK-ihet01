from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_fail(self):
        assert checkout_solution.checkout(32) == -1

    def test_checkout_fail2(self):
        assert checkout_solution.checkout("ABACADX") == -1

    def test_checkout(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout2(self):
        assert checkout_solution.checkout("ABACAD") == 195

    def test_checkout3(self):
        assert checkout_solution.checkout("BBAADDABCBBAAC") == 390
        
    def test_checkout4(self):
        assert checkout_solution.checkout("BBAADDABECBBAACE") == 470

    def test_checkout5(self):
        assert checkout_solution.checkout("BBAADDABECABBAACEAAAE") == 690