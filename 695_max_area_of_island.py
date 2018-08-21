# Max Area of Island
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)


def solution(grid):
    visited = set([])
    max_area = 0

    for index_r, row in enumerate(grid):
        for index_c, column in enumerate(row):
            a = calculateArea(index_r, index_c, grid, visited)
            max_area = a if a > max_area else max_area

    return max_area

def calculateArea(ri, rc, grid, visited):
    area = 0
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    if ri in range(0, grid_rows) and rc in range(0, grid_cols):
        # print("Visiting: ", (ri, rc), grid[ri][rc])
        if grid[ri][rc] == 1 and (ri, rc) not in visited:
            # print("True for: ", ri, rc)
            visited.add((ri, rc))
            area = 1 \
                + calculateArea(ri+1, rc, grid, visited)\
                + calculateArea(ri-1, rc, grid, visited)\
                + calculateArea(ri, rc+1, grid, visited)\
                + calculateArea(ri, rc-1, grid, visited)
    return area

if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print("Max area is: ", solution(grid))