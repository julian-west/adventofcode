# # !/usr/bin/bash

# # bash solution for day 1

# Part 1

input="input.txt"
input_sorted="$(sort -n < $input)"

while IFS= read -r x_loop; do
        while IFS= read -r y_loop; do
                if [ $((x_loop+y_loop)) == 2020 ]; then
                        echo "$((x_loop*y_loop))"
                        break 2
                fi
        done <<< "$input_sorted"
done <<< "$input_sorted"


# Part 2

while IFS= read -r x_loop; do
        while IFS= read -r y_loop; do
                while IFS= read -r z_loop; do
                        if [ $((x_loop+y_loop+z_loop)) == 2020 ]; then
                                echo "$((x_loop*y_loop*z_loop))"
                                break 3
                        fi
               done <<< "$input_sorted"
        done <<< "$input_sorted"
done <<< "$input_sorted"
