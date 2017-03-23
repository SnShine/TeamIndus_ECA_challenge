s = "WWS | NWW | EEN | SSE | EES | ESS | NWW | ENN | ESS | NWW | EEN | WSS | SEE | WNN | NWW | NWW | WNN | NEE | EES | EEN | NWW | ESS | EES | WSS | NWW | EEN | ENN | WWN | WWS | NWW | SWW | ESS | SEE | WSS | ESS | NWW | EEN | SSW | NNW | WSS | NEE | NWW | ESS | NEE | EES | EEN | ENN | WWN | WWN | ENN | NEE | ESS | WSS | WWN | NEE | ENN | WWS | NWW | WWS | ESS | SWW | NNW | ENN | SSE | WWS | ENN | EES | SSE"

s = s.split(" | ")
ans = []

for move in s:
    move = "".join(",".join([i for i in move]))

    ans.append(move)

print " | ".join(ans)
