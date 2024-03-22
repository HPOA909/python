import unittest

def pascal_triangle(n):
  """
  Generates Pascal's triangle up to n rows.

  Args:
      n: The number of rows.

  Returns:
      A list representing the Pascal's triangle.
  """
  if n <= 0:
    return []
  triangle = [[1]]
  for i in range(1, n):
    row = [1]  # Start with 1 for each row
    for j in range(1, i):
      row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)  # End with 1 for each row
    triangle.append(row)
  return triangle

class TestPascalTriangle(unittest.TestCase):

  def test_empty_triangle(self):
    """Tests if an empty triangle is returned for n <= 0"""
    self.assertEqual(pascal_triangle(0), [])
    self.assertEqual(pascal_triangle(-2), [])

  def test_first_two_rows(self):
    """Tests if the first two rows are generated correctly"""
    self.assertEqual(pascal_triangle(1), [[1]])
    self.assertEqual(pascal_triangle(2), [[1], [1, 1]])

  def test_larger_triangle(self):
    """Tests if a larger triangle is generated correctly"""
    expected_triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    self.assertEqual(pascal_triangle(4), expected_triangle)

if __name__ == '__main__':
  unittest.main()
