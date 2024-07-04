#!/usr/bin/python3

def canUnlockAll(boxes):
  """
  Determines if all the boxes in the given list can be unlocked.

  Args:
    boxes (list): A list of lists representing the lockboxes. Each inner list contains the indices of the boxes that can be unlocked.

  Returns:
    bool: True if all the boxes can be unlocked, False otherwise.
  """
  if type(boxes) is not list:
    return False
  elif (len(boxes)) == 0:
    return False
  for k in range(1, len(boxes) - 1):
    boxes_checked = False
    for idx in range(len(boxes)):
      boxes_checked = k in boxes[idx] and k != idx
      if boxes_checked:
        break
    if boxes_checked is False:
      return boxes_checked
  return True
