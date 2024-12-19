func minPathSum(grid [][]int) int {
    rows := len(grid)
    if rows == 0 {
        return 0
    }
    cols := len(grid[0])


    for i:=rows-1; i>=0; i-- {
        for j:= cols-1; j>=0; j-- {
            if (i==rows-1 && j==cols-1) {
                continue
            } else if (i== rows-1){
                grid[i][j] += grid[i][j+1]
            } else if (j == cols-1){
                grid[i][j] += grid[i+1][j]
            } else {
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
            }
        }
    }
    return grid[0][0]
}

func min(a, b int) int{
    if a<b {
        return a
    }
    return b
}
