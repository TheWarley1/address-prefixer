# Address Prefixer

Bulk-prefix a URL onto addresses in a CSV file. Built for on-chain analysis workflows (e.g. turning a plain address list into gmgn-style profile links).

## Requirements

- Python 3.8+
- pandas (`pip install -r requirements.txt`)

## Usage

```python
from prefixer import add_prefix_to_addresses

add_prefix_to_addresses(
    input_csv="addresses.csv",
    output_csv="prefixed_addresses.csv",
    prefix_url="https://gmgn.ai/base/address/",
    address_column="Address",
)
```

Or run directly:

```bash
python3 prefixer.py
```

## Behavior

- Prefixes every value in the target column with the given URL
- Handles empty/NaN cells (left empty)
- Collapses accidental double slashes (`https://x//y` -> `https://x/y`)
