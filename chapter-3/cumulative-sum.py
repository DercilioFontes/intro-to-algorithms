def cumulative_sum_array(numbers):
  cumulative_sum = [0] * len(numbers)
  cumulative_sum[0] = numbers[0]
  for i in range(1, len(numbers)):
    cumulative_sum[i] = cumulative_sum[i - 1] + numbers[i]
  return cumulative_sum

# Example usage
print(cumulative_sum_array([1, 2, 3, 4, 5]))
print(cumulative_sum_array([10, 20, 30, 40, 50]))
print(cumulative_sum_array([5, 10, 15, 20, 25]))
print(cumulative_sum_array([0, 0, 0, 0, 0]))