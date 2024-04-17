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
        assert checkout_solution.checkout("BBAADDABECBBAACE") == 440

    def test_checkout5(self):
        assert checkout_solution.checkout("BBAADDABECABBAACEAAAE") == 660
        
    def test_checkout6(self):
        assert checkout_solution.checkout("EEB") == 80

    def test_checkout7(self):
        assert checkout_solution.checkout("EEEB") == 120

    def test_checkout8(self):
        assert checkout_solution.checkout("EEEEBB") == 160
        
    def test_checkout9(self):
        assert checkout_solution.checkout("FEEFEBF") == 140

    def test_checkout10(self):
        assert checkout_solution.checkout("EEFFFFEEBBFF") == 200