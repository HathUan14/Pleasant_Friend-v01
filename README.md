# Pleasant_Friend-v01

#### Video Demo:  <URL HERE>
#### Description:
    A simple project using tkinter in Python with some usefull algorithm to help with making decisions in life

**1. Overview**
- This application simulates a smart computer where you can put some input and it will calculate and give results
- There are three options, which are 'Making decisions for your trip, by deciding on the time and value for each activity', 'Make your purchasing decision, based on price and your need', 'Divide the shares into 2 equal part among a diverse group of values'.
- Behind these options are algorithms, which are based on variables like value(the thing you obtain by your choices), weight(the thing is limited by your constraint) and W(the greatest total weight you want to calculate).
- So the possibilities of reusing the options are many, not just limited to 3 options. For example you can decide to do chores like watching movies, reading books, cooking, etc. by typing to the entry the value it brings (value), the time spent doing those chores (volume) and the maximum time you spend doing these tasks (W)

**2. Algorithm**
-  These are dynamic programing problem, I use "Backback problem" for option 1 and 2, the problem requires you to put objects, of different masses and values, into a backpack with a limited mass such that the total value is maximized. The problem requires you to put objects, of different masses and values, into a backpack with a limited weight such that the total value is maximized. The solution table F consists of n + 1 rows, W + 1 columns, F[i][j] is the greatest value by picking among item {1, 2, 3, ..., i} with limited total weight j. I consider that if the item i is not selected, assign F[i][j] = F[i-1][j], conversely, if the item i is selected then F[i][j] = val[i] + F[i-1][j-wei[i]], F[i][j] will be the larger number of the two values ​​above. Finally, F[n][W] is the total value for the answer.
- Algorithm to find subset whose sum is S is used for option 3. Considering F is a True/False matrix comprises columns with numbers from 0 to sum, rows indices are numbers from 0 to n, indicate if the list comprises 1 to i does have subset that have sum equals j. First column is True on purpose to make all F[i][s[i]] True. F[i][j] = 1 if F[i-1][j] == 1 or F[i-1][j-val[i]] == 1. I used this algorithm to find the largest possible total sum of subset for a list of value, provided that the total sum of subset is less than 1/2 of the total of all values 

**3. User interface**
- I used Tkinter module for UI development. There are entries where user can type the input, a list box to display the input data, there are 3 files store input data correspond to 3 option so user can save data for later use.
- The usage is very simple, users only need to enter the necessary data, by creating their own scale, in the value section, the scale can be 1 for 10$, 100 for 1000$, in the "weight" section and W section, the scale needs to be adjusted lower because of limited computing power, usually from 1-100. Advice: You should choose the task or item with the largest and smallest "volume" as a standard, for example 50 for the largest, 10 for the smallest for easy division.