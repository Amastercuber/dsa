# Adjacent Digit Sum

You are given a string `s` consisting of numerical characters and a target sum `target`.

Write a function to find if there is a pair of adjacent numbers in the string that add up to `target`. The function should return a boolean value:

- `True` if such a pair exists
- `False` otherwise

Use the two-pointer technique to solve this problem without converting the entire string into a list of numbers.

> **Note:** Each character in the string `s` should be treated as a separate digit. For example, `"56"` in the string should be considered as `5` and `6`.

## Example 1

```text
Input: s = "1234", target = 5
Output: True
```

**Explanation:** The digits `2` and `3` are adjacent and add up to `5`.

## Example 2

```text
Input: s = "1112", target = 4
Output: False
```

**Explanation:** There are no two adjacent digits that add up to `4`.

## Function Template

```python
def has_adjacent_sum(s, target):
    pass
```
