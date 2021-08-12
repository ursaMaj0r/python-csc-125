# define variables
breadcrumb = 'x'
breadcrumb_location = {"x":0,"y":0}

# prompt for grid
grid_size = int(input('Grid size: '))

# generate grid
grid = []
for i in range(grid_size):
  row = []
  for j in range(grid_size):
    row.append('.')
  grid.append(row)
grid[0][0] = breadcrumb

# print grid
def print_grid():
  for row in grid:
    print(''.join(row))

print_grid()

# prompt for input
direction = input('Direction: ')

# prompt for directions
while direction:
  if direction == 'up':
    breadcrumb_location['y'] += -1
  elif direction == 'down':
    breadcrumb_location['y'] += +1
  elif direction == 'left':
    breadcrumb_location['x'] += -1
  elif direction == 'right':
    breadcrumb_location['x'] += 1

  # move breadcrumb
  grid[breadcrumb_location['y']][breadcrumb_location['x']] = breadcrumb
  
  #print grid
  print_grid()

  #reprompt
  direction = input('Direction: ')
