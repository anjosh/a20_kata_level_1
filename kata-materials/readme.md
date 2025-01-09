# Submarine Puzzle Submission

## Usage
- `python main.py` will output the product of the submarine's depth and horizontal position after following the planned course.
- `python main.py --verbose` will ouput the submarine's depth and horizontal position after following each command as well as the final product.

## Assumptions
1. The submarine is located in the ocean so that it's planned course does not make it hit land, come out of water, or hit the ocean floor.

## Testing
- `python tests.py`
- Only added a basic test that should cover the happy path. We could add more tests for edge cases like possible invalid inputs but I felt that was overkill at the moment.
