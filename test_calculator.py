import Calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == Calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == Calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)