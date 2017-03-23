# 222 | no sorting, no neighbour selection
# solution = "EES | WSS | SEE | WNN | NWW | NWW | WNN | NEE | EES | EEN | NWW | ESS | NEE | WWN | ESS | WWN | NEE | ESS | NWW | ESS | SSE | WWN | EEN | WSS | WSS | NWW | WWN | NWW | SSE | WSS | NEE | NWW | ESS | NEE | NEE | ESS | NWW | WWS | NWW | NEE | ESS | NWW | EEN | EEN | NEE | WWN | NNW | NWW | SWW | ESS | NNE | NEE | WSS | WWN | SSW | NEE | WNN | SSW | ESS | EEN | EES | WWS | WNN | SEE"
# 240 | no sorting, 6_3 selected
# solution = "WWS | NWW | EEN | SSE | EES | ESS | NWW | ENN | ESS | NWW | EEN | WSS | SEE | WNN | NWW | NWW | WNN | NEE | EES | EEN | NWW | ESS | EES | WSS | NWW | EEN | ENN | WWN | WWS | NWW | SWW | ESS | SEE | WSS | ESS | NWW | EEN | SSW | NNW | WSS | NEE | NWW | ESS | NEE | EES | EEN | ENN | WWN | WWN | ENN | NEE | ESS | WSS | WWN | NEE | ENN | WWS | NWW | WWS | ESS | SWW | NNW | ENN | SSE | WWS | ENN | EES | SSE"
# 276 | ntns, 7_6 selected
# solution = "ESS | WWS | WWN | WSS | NEE | ENN | NWW | NNW | ENN | SSE | SSE | WWN | NNE | NEE | EES | EES | WSS | WSS | NNW | NNE | NNE | WWS | SSW | SWW | WNN | NEE | NEE | EES | ESS | WSS | ESS | SWW | NWW | WWS | ENN | EEN | ESS | EEN | SSW | WWN | NNE | NEE | WNN | WWS | WSS | EEN | SEE | SSW | SWW | NNW | WSS | NWW | WNN | SEE | WSS | NNW | EEN | NNE | EEN | EES | ENN | WWN | WWS | NWW | SSE | WWN | SSE | SEE"
# 277 | ntns, 4_3 selected
solution = "WWN | WNN | SSW | EES | WNN | NNE | SWW | ESS | NNE | NEE | EES | EES | WSS | WSS | NNW | NNE | NNE | WWS | SSW | SEE | WNN | ENN | SEE | WSS | SSW | NEE | WNN | WWS | WSS | ESS | SEE | ENN | SWW | NNW | SWW | SWW | EES | NNE | ESS | EEN | WWN | ESS | EEN | NNW | NNE | NNW | NWW | WWS | WWN | SSW | ESS | ENN | SSE | WSS | WWS | EES | NEE | WNN | SSW | NWW | ESS | NEE | WWN | WNN | EES | NEE"


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
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
BOARD_SCORES = [0, None, None, -2, -1, 0, 1, 2, 4]
STARTING_NODE = [5, 5]

steps = [[5, 5]]
scores = 0
num_minerals_landed = 0
num_total_minerals = 0


def is_mineral(step):
    if BOARD[step[0]][step[1]] == 8:
        return True
    return False

solution = solution.split(" | ")
for i in solution:
    last_step = steps[-1]
    new_step = last_step[:]
    for j in i:
        if j == "E":
            new_step[1] += 1
        elif j == "W":
            new_step[1] -= 1
        elif j == "N":
            new_step[0] -= 1
        else:
            new_step[0] += 1
        # print step
        scores += BOARD_SCORES[BOARD[new_step[0]][new_step[1]]]
        if is_mineral(new_step):
            num_total_minerals += 1
    steps.append(new_step)
    if is_mineral(new_step):
        num_minerals_landed += 1


print "Score: %i" % scores

print "Len of steps: %i" % len(steps)
print "Total steps in the provided solution: %i" % len(solution)
print "Total steps while verifying solution: %i" % (len(steps)-1)

print ""
print "Number of minerals landed: %i" % num_minerals_landed
print "Total no. of minerals passed/landed: %i" % num_total_minerals


steps = [str(i)+"_"+str(j) for i, j in steps]
print "Repetitions including base: " + str(len(steps)-len(set(steps)))



# calculate final acceptable solution from solution string
ans = []
for move in solution:
    move = "".join(",".join([i for i in move]))

    ans.append(move)

print ""
print "-----Steps-----"
print steps
print ""
print "-----Solution-----"
print " | ".join(ans)
