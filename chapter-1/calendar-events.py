def has_overlap(events):
  events.sort(key=lambda x: x['start'])

  for i in range(len(events) - 1):
    if events[i]['end'] > events[i + 1]['start']:
      return True
  return False

# Example usage
events = [
    {'start': 1, 'end': 3},
    {'start': 4, 'end': 6},
    {'start': 5, 'end': 7},
]
print(has_overlap(events))  # Output: True
events = [
    {'start': 1, 'end': 3},
    {'start': 4, 'end': 6},
    {'start': 7, 'end': 9},
]
print(has_overlap(events))  # Output: False
events = [
    {'start': 1, 'end': 3},
    {'start': 2, 'end': 4},
    {'start': 5, 'end': 7},
]
print(has_overlap(events))  # Output: True
events = [
    {'start': 1, 'end': 3},
    {'start': 4, 'end': 6},
    {'start': 7, 'end': 9},
]
print(has_overlap(events))  # Output: False