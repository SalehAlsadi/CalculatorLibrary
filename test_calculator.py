import Calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == Calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == Calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == Calculator.multiply(10, 10)

    def test_division(self):
        assert 50 == Calculator.division(500, 10)