# 222 | no sorting, no neighbour selection
# solution = "EES | WSS | SEE | WNN | NWW | NWW | WNN | NEE | EES | EEN | NWW | ESS | NEE | WWN | ESS | WWN | NEE | ESS | NWW | ESS | SSE | WWN | EEN | WSS | WSS | NWW | WWN | NWW | SSE | WSS | NEE | NWW | ESS | NEE | NEE | ESS | NWW | WWS | NWW | NEE | ESS | NWW | EEN | EEN | NEE | WWN | NNW | NWW | SWW | ESS | NNE | NEE | WSS | WWN | SSW | NEE | WNN | SSW | ESS | EEN | EES | WWS | WNN | SEE"
# 240 | no sorting, 6_3 selected
# solution = "WWS | NWW | EEN | SSE | EES | ESS | NWW | ENN | ESS | NWW | EEN | WSS | SEE | WNN | NWW | NWW | WNN | NEE | EES | EEN | NWW | ESS | EES | WSS | NWW | EEN | ENN | WWN | WWS | NWW | SWW | ESS | SEE | WSS | ESS | NWW | EEN | SSW | NNW | WSS | NEE | NWW | ESS | NEE | EES | EEN | ENN | WWN | WWN | ENN | NEE | ESS | WSS | WWN | NEE | ENN | WWS | NWW | WWS | ESS | SWW | NNW | ENN | SSE | WWS | ENN | EES | SSE"
# 276 | ntns, 7_6 selected
# solution = "ESS | WWS | WWN | WSS | NEE | ENN | NWW | NNW | ENN | SSE | SSE | WWN | NNE | NEE | EES | EES | WSS | WSS | NNW | NNE | NNE | WWS | SSW | SWW | WNN | NEE | NEE | EES | ESS | WSS | ESS | SWW | NWW | WWS | ENN | EEN | ESS | EEN | SSW | WWN | NNE | NEE | WNN | WWS | WSS | EEN | SEE | SSW | SWW | NNW | WSS | NWW | WNN | SEE | WSS | NNW | EEN | NNE | EEN | EES | ENN | WWN | WWS | NWW | SSE | WWN | SSE | SEE"
# 277 | ntns, 4_3 selected
# solution = "WWN | WNN | SSW | EES | WNN | NNE | SWW | ESS | NNE | NEE | EES | EES | WSS | WSS | NNW | NNE | NNE | WWS | SSW | SEE | WNN | ENN | SEE | WSS | SSW | NEE | WNN | WWS | WSS | ESS | SEE | ENN | SWW | NNW | SWW | SWW | EES | NNE | ESS | EEN | WWN | ESS | EEN | NNW | NNE | NNW | NWW | WWS | WWN | SSW | ESS | ENN | SSE | WSS | WWS | EES | NEE | WNN | SSW | NWW | ESS | NEE | WWN | WNN | EES | NEE"
# 283 | ntns, 4_3 selected
# solution = "WWN | WNN | SSW | EES | WNN | NNE | SWW | ESS | NNE | NEE | EES | EES | WSS | WSS | NNW | NNE | NNE | WWS | SSW | SEE | WNN | ENN | SEE | WSS | SSE | SSW | SWW | NNW | WSS | NWW | EEN | EEN | ESS | EEN | SSW | WWN | NNW | NNW | SWW | NNW | ENN | SEE | NEE | EES | ESS | WSS | ESS | SWW | NNW | WWS | WWS | NNW | EEN | NWW | SSE | WSS | NEE | ENN | SSE | WWS | NWW | NEE | NNE | WNN | NEE | ESS | NEE | SSE | WWS | NWW"
# 283 | ntns, 7_6 selected
# solution = "ESS | WWS | WWN | WSS | NEE | ENN | NWW | NNW | ENN | SSE | SSE | WWN | NNE | NEE | EES | EES | WSS | WSS | NNW | NNE | NNE | WWS | SSW | SWW | NWW | ENN | SSE | SWW | EES | SWW | ESS | NNE | WWS | EES | NEE | EES | EEN | NNW | NNE | NNW | NWW | WWS | WWS | NNE | EES | NEE | SEE | WSS | NWW | SWW | ESS | EEN | SEE | SSW | SWW | NNW | WSS | NWW | EEN | EEN | ESS | EEN | SSW | WWN | NNE | NEE | WNN | WWS | WWN | SSE"
# 286 | ntns, 7_6 selected
# solution = "ESS | WWS | WWN | WSS | NEE | ENN | NWW | NNW | ENN | SSE | SSE | WWN | NNE | NEE | EES | EES | WSS | WSS | NNW | NNE | NNE | WWS | SSW | SWW | NWW | ENN | EES | SEE | NEE | SSE | WWS | WSS | SEE | ENN | SWW | NNW | SWW | SWW | EES | NNE | ESS | EEN | ENN | WWN | SWW | NNW | EEN | EES | ENN | WWN | WWS | NWW | WSS | NEE | NEE | EES | ESS | WSS | ESS | SWW | NWW | WWS | NWW | NEE | WSS | NNW | EEN | NWW | EEN | SEE"
# 287 exp, ntns, 4_3 selected, removed <=0 weighted edges
solution = "WWN | WNN | SSW | EES | WNN | NNE | SWW | ESS | NNE | NEE | EES | EES | WSS | WSS | NNW | NNE | NNE | WWS | SSW | ESS | ESS | EEN | SSW | WWN | WWN | SWW | EES | NNE | ESS | EEN | ENN | WNN | ENN | WWN | SSW | SWW | WSS | SWW | ESS | NEE | WWN | WSS | NEE | ENN | SSE | WWS | NWW | NEE | NNE | WNN | WSS | NNW | ENN | SEE | NEE | EES | ESS | WSS | ESS | SWW | NNW | ENN | SWW | NNE | NEE | SSE | WWS | NWW"

from main import BOARD, BOARD_SCORES

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
        new_step_score = BOARD_SCORES[BOARD[new_step[0]][new_step[1]]]
        scores += new_step_score
        # print "Intermediate action, step, score added, cum score: {}, {}, {}, {}".format(j, new_step, new_step_score, scores)
        if is_mineral(new_step):
            num_total_minerals += 1
    # print "Landed step: {}".format(new_step)
    steps.append(new_step)
    if is_mineral(new_step):
        num_minerals_landed += 1


print "Score: %i" % scores

print "No. of landing zones including starting point: %i" % len(steps)
print "Total no. of steps in the provided solution: %i" % len(solution)
print "Total no. of steps while verifying solution: %i" % (len(steps)-1)

print ""
print "Number of times landed on minerals: %i" % num_minerals_landed
print "Total no. of times passed/landed on minerals: %i" % num_total_minerals


steps = [str(i)+"_"+str(j) for i, j in steps]
print "Repetitions including starting position: %i" % (len(steps)-len(set(steps)))

# calculate final acceptable solution from solution string
ans = []
for move in solution:
    move = "".join(",".join([i for i in move]))

    ans.append(move)

print ""
print "-----Steps-----"
print [(i, j) for i, j in enumerate(steps)]
print ""
print "-----Solution-----"
print " | ".join(ans)
