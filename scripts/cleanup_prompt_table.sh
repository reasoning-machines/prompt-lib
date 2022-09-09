#!/bin/bash

# sed command that extracts the prompts from the table

# step 1: remove everthing before \begin{tabular} and after \end{tabular}, save to tmp1
sed -n '/\\begin{tabular}/, /\\end{tabular}/p' $1 > tmp1

# step 2: remove \begin{tabular} and \end{tabular}
sed -i '1d' tmp1
sed -i '$d' tmp1

# step 3: remove \pprompt{1} and \pprompt{2} and so on
sed -i 's/\\pprompt{[0-9]*}//g' tmp1

# step 4: remove all comments, \hline, and \cline{1-2}, \bottomrule, \toprule, \newline
sed -i '/^\s*%/d' tmp1
sed -i '/\s*\\hhline/d' tmp1
sed -i '/\s*\\cline{1-2}/d' tmp1
sed -i '/\s*\\bottomrule/d' tmp1
sed -i '/\s*\\toprule/d' tmp1
sed -i '/\s*\\newline/d' tmp1

# Now we are left with
# \pq{Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?}\\ \hdashline
# \tq{Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9.}\\ \hdashline
# \aq{9}\\
# Extract an Example:
# Example(
#     question = "Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
#     thought = "Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9."
#     answer = "9",
# )
sed -i 's/^.*\\pq{\(.*\)}.*$/Example(question = "\1",/g' tmp1
sed -i 's/^.*\\tq{\(.*\)}.*$/    thought = "\1",/g' tmp1
sed -i 's/^.*\\aq{\(.*\)}.*$/    answer = "\1"),/g' tmp1

# step 5: remove all escape characters for latex
sed -i 's/\\//g' tmp1

# step 6: make it a list
sed -i '1i[' tmp1
sed -i '$a]' tmp1



