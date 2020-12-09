# !/usr/bin/env bash

# Bash script solution to week 5
# Based on Primagen solution - see YouTube

# ------------------------------------------------------
## Part 1
# ------------------------------------------------------

# read input line by line from file
# convert FBLR to binary using the tr command
# note that the 2# command will evaluate a series of 0s and 1s as binary!
# next, pass the result into sort to get smallest number on top
seat_ids=$(
        while IFS= read -r line; do
                echo "$((2#`echo $line | tr FBLR 0101`))";
        done < input.txt | sort -rn
        )

# the answer to the problem is the final value in the list!
high=$(echo "${seat_ids[@]}" | head -1)
echo $high

# also store the lowest seat id to use in part 2
low=$(echo "${seat_ids[@]}" | tail -1)

# ------------------------------------------------------
# Part 2
# ------------------------------------------------------

# read file again but save sorted list of seat ids
val=$(
        while IFS= read -r line; do
                echo "$((2#`echo $line | tr FBLR 0101`))";
        done < input.txt | sort -rn
)
# calculate theoretical sum of all seat ids (if none were missing)
theoretical_sum=$(seq $low $high | paste -sd + - | bc)
actual_sum=$(echo "${val[@]}" | paste -sd + - | bc)

# your seat id is theoretical sum minus actual sum (as there are no missing seats)
echo `expr $theoretical_sum - $actual_sum`

