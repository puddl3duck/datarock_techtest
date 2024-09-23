class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.scanned_items = []

    def scan(self, item):
        self.scanned_items.append(item)

    def total(self):
        total_price = 0
        item_counts = {sku: self.scanned_items.count(sku) for sku in self.pricing_rules.keys()}

        # Apply special rules
        if item_counts.get('atv', 0) >= 3:
            total_price += (item_counts['atv'] // 3) * 2 * self.pricing_rules['atv'] + \
                           (item_counts['atv'] % 3) * self.pricing_rules['atv']
        else:
            total_price += item_counts.get('atv', 0) * self.pricing_rules['atv']

        if item_counts.get('ipd', 0) > 4:
            total_price += item_counts['ipd'] * 499.99
        else:
            total_price += item_counts.get('ipd', 0) * self.pricing_rules['ipd']

        # Free VGA adapter for each MacBook Pro
        total_price += item_counts.get('mbp', 0) * self.pricing_rules['mbp']
        total_price += item_counts.get('vga', 0) * self.pricing_rules['vga']

        return total_price
