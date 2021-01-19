In this problem, three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, that the missionaries present on the bank cannot be outnumbered by cannibals. The boat cannot cross the river by itself with no people on board. 

Here lets represent state as (c, m, b)

Here,
c = number of cannibals on the left side of the river
possible values = [0, 1, 2, 3]

m = number of missionaries on the left side of the river
possible values = [0, 1, 2, 3]

b = side where the boat currently is
0 means right, 1 means left

Task is to find all the possible ways to reach from Start state to End state and display them as output.