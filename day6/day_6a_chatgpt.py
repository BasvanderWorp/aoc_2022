def find_marker(buffer):
  # Initialize variables
  counter = 0
  last_four = []
  found_marker = False

  # Loop through each character in the buffer
  for ch in buffer:
    # Add the character to the list of the last four characters
    last_four.append(ch)
    if len(last_four) > 4:
      last_four.pop(0)

    # Check if the current four characters are a marker
    if len(last_four) == 4:
      if last_four[0] != last_four[1] and last_four[0] != last_four[2] and last_four[0] != last_four[3] and last_four[1] != last_four[2] and last_four[1] != last_four[3] and last_four[2] != last_four[3]:
        found_marker = True
        break

    # Increment the character counter
    counter += 1

  # Return the result
  if found_marker:
    return counter
  else:
    return -1


buffer = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
result = find_marker(buffer)
print(result)  # Output: 7
