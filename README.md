# Checkout System

## Overview
This is a simple checkout system for a computer store that implements flexible pricing rules for various products. The system supports promotions like bulk discounts and special offers.

## Features
- Scans items in any order.
- Applies special pricing rules:
  - **3 for 2** deal on Apple TVs.
  - **Bulk discount** on Super iPads (price drops if more than 4 are purchased).
  - **Free VGA adapter** with every MacBook Pro purchased.

## Products
| SKU | Name          | Price      |
|-----|---------------|------------|
| ipd | Super iPad   | $549.99    |
| mbp | MacBook Pro  | $1399.99   |
| atv | Apple TV     | $109.50    |
| vga | VGA adapter   | $30.00     |

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
