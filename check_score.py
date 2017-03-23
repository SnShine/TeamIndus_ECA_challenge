BOARD = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 2, 6, 7, 4, 8, 6, 8, 7, 3, 1],
         [1, 3, 8, 6, 5, 3, 4, 5, 6, 7, 1],
         [1, 6, 7, 4, 6, 2, 8, 7, 4, 6, 1],
         [1, 5, 7, 5, 3, 7, 6, 2, 7, 4, 1],
         [1, 3, 6, 8, 6, 0, 4, 8, 6, 3, 1],
         [1, 4, 2, 6, 4, 5, 6, 7, 3, 5, 1],
         [1, 7, 8, 3, 6, 5, 7, 4, 2, 7, 1],
         [1, 6, 5, 7, 8, 4, 3, 6, 5, 6, 1],
         [1, 5, 3, 4, 6, 2, 6, 7, 4, 8, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

BOARD_SCORES = [0, None, None, -2, -1, 0, 1, 2, 4]

STARTING_NODE = [5, 5]

solution = "EES | WSS | SEE | WNN | NWW | NWW | WNN | NEE | EES | EEN | NWW | ESS | NEE | WWN | ESS | WWN | NEE | ESS | NWW | ESS | SSE | WWN | EEN | WSS | WSS | NWW | WWN | NWW | SSE | WSS | NEE | NWW | ESS | NEE | NEE | ESS | NWW | WWS | NWW | NEE | ESS | NWW | EEN | EEN | NEE | WWN | NNW | NWW | SWW | ESS | NNE | NEE | WSS | WWN | SSW | NEE | WNN | SSW | ESS | EEN | EES | WWS | WNN | SEE"
solution = "WWS | NWW | EEN | SSE | EES | ESS | NWW | ENN | ESS | NWW | EEN | WSS | SEE | WNN | NWW | NWW | WNN | NEE | EES | EEN | NWW | ESS | NEE | WWN | WWS | NWW | SWW | ESS | SEE | WSS | ESS | NWW | EEN | SSW | NNW | WSS | NEE | NWW | ESS | NEE | EES | EEN | ENN | WNN | SWW | EES | NNE | SWW | WWN | ENN | NEE | ESS | WSS | WWN | NEE | ENN | WWS | NWW | WWS | ESS | SWW | NNW | ENN | SSE | WWS | ENN | EES | SSE"
solution = "WWS | NWW | EEN | SSE | EES | ESS | NWW | ENN | ESS | NWW | EEN | WSS | SEE | WNN | NWW | NWW | WNN | NEE | EES | EEN | NWW | ESS | EES | WSS | NWW | EEN | ENN | WWN | WWS | NWW | SWW | ESS | SEE | WSS | ESS | NWW | EEN | SSW | NNW | WSS | NEE | NWW | ESS | NEE | EES | EEN | ENN | WWN | WWN | ENN | NEE | ESS | WSS | WWN | NEE | ENN | WWS | NWW | WWS | ESS | SWW | NNW | ENN | SSE | WWS | ENN | EES | SSE"
solution = solution.split(" | ")
# print solution

steps = [[5, 5]]
scores = 0


for i in solution:
    step = steps[-1]
    for j in i:
        if j == "E":
            step[1] += 1
        elif j == "W":
            step[1] -= 1
        elif j == "N":
            step[0] -= 1
        else:
            step[0] += 1
        # print step
        scores += BOARD_SCORES[BOARD[step[0]][step[1]]]
    steps.append(step)
    print step

print scores
steps = [str(i)+"_"+str(j) for i, j in steps]
