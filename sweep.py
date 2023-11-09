# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid)
def validate( block_data ):
  count = 0
  if block_data[0][0] == -1:
    count = count + 1
  else:
    count = count + 0
  if block_data[0][1] == -1:
    count = count + 1
  else:
    count = count + 0
  if block_data[0][2] == -1:
    count = count + 1
  else:
    count = count + 0
  if block_data[1][0] == -1:
    count = count + 1
  else:
    count = count + 0
  if block_data[1][1] == -1:
    count = count + 1
  else:
    count = count + 0
  if block_data[1][2] == -1:
    count = count + 1
  else:
    count = count + 0
  if block_data[2][0] == -1:
    count = count + 1
  else:
    count = count + 0
  if block_data[2][1] == -1:
    count = count + 1
  else: 
    count = count + 0
  if block_data[2][2] == -1:
    count = count + 1
  else:
    count = count + 0

  if block_data[1][1] == count:
    return "valid"
  else:
    return "invalid"

grid = [
  [-1,1,0],
  [1,1,0],
  [0,0,0]
]
print (validate(grid))
