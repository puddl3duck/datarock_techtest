import pytest
import pandas as pd
from typing import List
from shopping_cart import Checkout

pricing_rules = {
    'ipd': 549.99,
    'mbp': 1399.99,
    'atv': 109.50,
    'vga': 30.00
}

@pytest.fixture
def checkout_data() -> pd.DataFrame:
    # Create a DataFrame with the test cases
    data = {
        'skus': [
            ['atv', 'atv', 'atv', 'vga'],  # Scenario 1
            ['atv', 'ipd', 'ipd', 'atv', 'ipd', 'ipd', 'ipd'],  # Scenario 2
            ['mbp', 'vga', 'ipd']  # Scenario 3
        ],
        'expected_total': [
            249.00,  # Expected total for Scenario 1
            2718.95,  # Expected total for Scenario 2
            1949.98   # Expected total for Scenario 3
        ]
    }
    return pd.DataFrame(data)


def test_checkout(checkout_data: pd.DataFrame) -> None:
    for index, row in checkout_data.iterrows():
        co = Checkout(pricing_rules)
        for sku in row['skus']:
            co.scan(sku)
        assert co.total() == pytest.approx(row['expected_total'], rel=1e-2)