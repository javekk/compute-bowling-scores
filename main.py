# Compute bowling score
#
# @author: Raffaele Perini
#
# Input: an array with scores of each roll
#
# Output: total score
#



scoresMatrix = [
    [9,0,  1,2,  10,   2,8,  1,3,  0,2,  7,1,  8,2,  5,5,  4,2],
    [1,4,  4,5,  6,4,  5,5,  10,   0,1,  7,3,  6,4,  10,   2,8,6],
    [9,1,  0,10, 10,   10,   6,2,  7,3,  8,2,  10,   9,0,  9,1,10],
    [10,   10,   10,   10,   10,   10,   10,   10,   10,   10,10,10],
    [10,   10,   10,   10,   10,   10,   10,   10,   10,   10,10,1],
    [8,2,  10,   10,   10,   10,   10,   10,   10,   10,   10,10,7],
    [9,0,  10,   10,   10,   10,   10,   10,   10,   10,   10,10,2],
    [8,0,  7,0,  5,3,  9,1,  9,1,  10,   8,0,  5,1,  3,7,  9,0],
    [8,2,  9,0,  4,4,  7,2,  9,0,  10,   10,   8,0,  3,5,  9,1,7]
]

scoresResult = [92, 133, 168, 300, 291, 287, 271, 122, 133]

def main():

    # Iterate through every scores
    for j, scorez in enumerate(scoresMatrix):

        finalScore = 0
        i = 0

        for frame in range(10): 
            
            if scorez[i] + scorez[i+1] < 10:
                finalScore += scorez[i] + scorez[i+1]
                i += 2
            elif scorez[i] == 10:
                finalScore += 10 + scorez[i+1] + scorez[i+2]
                i += 1
            elif scorez[i] + scorez[i+1] == 10:
                finalScore += 10 + scorez[i+2]
                i += 2
            
            #print(finalScore)

        print("Computed score: " + str(finalScore) + ", true score: " + str(scoresResult[j]))


if __name__ == "__main__":
    main()


