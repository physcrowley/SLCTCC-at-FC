**SLC CODING COMPETITION 2024**

After completing a problem:

- Have one team member raise their hand and wait for a judge to arrive.  
- The judge will record the current time, then provide you with an input file. After receiving the file, **ensure you update the file path in your code to open the file you were given\!**  
- Your output must match the expected output **exactly**. The expected output is explained in each problem’s output specifications.  
- You are allowed two attempts for each problem. After your first attempt, you may keep the input file from the first attempt and use it to correct your code.

Scoring:

- Your team will be awarded points for each correct line of output.  
- If you get all lines of output correct on your first attempt, you will gain bonus points.  
- You will gain some additional bonus points determined by the time you completed the problem.  
- If your code crashes partway through due to an error, any output that did not print will be counted as a zero, but you will receive points for successful output.  
  * Any errors at the end of the output caused by whitespace at the end of the file will be dismissed and you will not lose points.

Rules for solving problems:

- You may reference any code already on your device to help you solve problems.  
- You may write on paper (including these pages) to help you solve problems.  
- You may not communicate with anyone outside of your team or use the internet.

Tips:

- Read the instructions, input specifications, and output specifications fully before attempting.  
- Examine the sample input and sample output carefully\!  
- Think of edge cases that may not be covered by the sample input\!

1\)

David has started learning a new programming language called Loop. Loop is a simple programming language used to perform iterative operations. A loop program consists of a single variable *X* initially set to 0, and it repeatedly performs increments, decrements, and multiplication operations on it. Create a program that simulates the Loop language.

The language has the following syntax:

- ‘INC’: Increment *X* by 1  
- ‘DEC’: Decrement *X* by 1  
- ‘MUL *Y*’: Multiply *X* by *Y*

Input Specifications:

- Each test case contains many lines and there will be no spaces between cases.  
- The first line contains an integer *N* indicating the number of instructions in the program.  
- The next *N* lines contain the program instructions.

Output Specifications:

- For each test case, print the result of the program.

| Sample Input: 4 INC MUL 5 INC MUL 2 5 INC DEC MUL 5 INC INC 3 MUL 2 INC MUL 0 4 INC INC MUL 2 DEC | Sample Output: 12 2 0 3 |
| :---- | :---- |

2\)

Cars consume gas at different rates per hundred kilometres. In each test case, there is a destination *D* kilometres down the road, which *N* cars will attempt to reach, each starting with *G* litres of gas and consuming *L* litres per one hundred kilometres. You must determine how many cars can reach the destination.

Input Specifications:

The input is written as follows:

D  
N  
G L  
G L  
…  
G L	

- The first line contains a single integer representing the distance to the destination.  
- The second line contains a single integer *N* indicating how many cars there are.  
- The next *N* lines contain the gas and consumption rate of each car.

Output Specifications:

- Output a single number indicating how many cars are able to reach the destination.

| Sample Input: 650 3 60 9 50 7 20 4 1200 4 60 5 70 6 145 13 30 3 500 3 35 7 45 6 72 12 \-550 2 50 9 85 17 | Sample Output: 2 1 3 1 |
| :---- | :---- |

3\)

Joe is a hungry guy who loves microwaved meals. Joe starts with *N* microwaved meals and eats one at the end of every day. With every trip to the grocery store, Joe always buys enough to have *N* microwaved meals, but never more. Joe will only visit the grocery store on days where he starts with no meals, and if he does not visit the store, he will starve. The grocery store is closed on *D* days, and Joe will visit the grocery store early if he knows he will run out of food while the store is closed. You must determine how many times Joe will visit the store in a period of *X* days.

Input Specifications:

- The input is written as follows, with three lines per test case:

  N  
  X  
  D D D … D

- The first line contains a single integer *N* indicating how many meals Joe starts with.  
- The second line contains a single integer *X* indicating the number of days.  
- The third line is a list of integers representing days in the week where the store is closed, separated by spaces, with 0 representing Sunday and 6 representing Saturday.  
- For some test cases, the store may never be closed, and the third line will be blank.

Output Specifications:

- Output a single number showing the number of times Joe will visit the store.  
- If Joe will starve, output \-1 instead.

Notes:

- Each test case begins on Sunday.

| Sample Input: 5 14 3 21 1 2 2 7 4 5 6 4 14 1 3 5 | Sample Output: 2 8 \-1 3 |
| :---- | :---- |

4\)

In the ruins of an ancient civilization, archaeologists have discovered artifacts inscribed with encrypted messages. These messages are believed to have been secured using a cipher based on prime sequences and rotational shifts. Your task is to help decipher these messages.

The cipher used to encrypt the messages is a variant of a Caesar cipher modulated by prime number sequences. The cipher involves rotating each letter in the message by a number of positions determined by the *n*th prime number, where *n* is the position of the character in the message, starting from 0\.

Encryption Process:

- Convert each letter of the message to its position in the alphabet (A=0, B=1, …, Z=25).  
- For each letter at position *n* in the message, find the *n*th prime number.  
- Rotate the letter forward by the value of the *n*th prime number.  
- If the rotation exceeds ‘Z’, it wraps around to the beginning of the alphabet.

Decryption Process:

- Given the encrypted message, you need to reverse the encryption process using the known sequence of prime numbers.

Input Specifications:

- For each test case, a single line contains the encrypted string, consisting only of uppercase English letters.

Output Specifications:

- For each test case, output only the decrypted message.

Notes:

- 1 is not a prime number. The prime numbers start as 2, 3, 5, etcetera.

| Sample Input: CSUSP ODYO FRILNNYXAUTY | Sample Output: APPLE MATH DODECAHEDRON |
| :---- | :---- |

5\)

You have come from the future with knowledge of stock prices over a period of *N* days. To avoid suspicion, you can only buy stocks *K* times and sell *K* times. You can buy or sell multiple stocks at once, but on any day, you can only buy or sell. You can only buy whole stocks, not fractions. You start with *X* dollars. What is the maximum amount of money you can end with over a period of *N* days?

Input Specifications:

- The input is written as follows:

  N  
  …  
  K  
  X

- The first line is a single integer *N* indicating the number of days.  
- The next *N* lines contain the stock prices on each day.  
- The second last line is a single integer *K* indicating the number of times you can buy and sell (Example: If *K* \= 2, you can buy twice and sell twice).  
- The last line is a single integer *X* indicating the amount of money you start with.

Output Specifications:

- For each test case, output a single integer representing the highest amount of money you can end with.

| Sample Input: 5 1 9 3 1 2 1 100 6 5 1 3 1 3 4 2 200 2 2 1 1 100 | Sample Output: 900 2400 100 |
| :---- | :---- |

6\)

A programmer from a forgotten era recorded their work on a stone tablet. The way we use characters and letters has changed since their time, but there is a way to translate. You work in a time travel agency, and your job is to send information from this forgotten age into the far future. Given message *M*, you must perform multiple operations to translate the message.

The first step is to replace some letters in *M.* A group of adventurers has provided you with substring *S*, which appears in *M*. For every appearance of *S* in *M*, replace *S* with the reverse of *S*.

The second step is to shift the message based on *i*, where *i* is the number of words changed in the previous step. If *i* is odd, shift the position of each letter *i*\*2 positions backward. If *i* is even, shift the position of each letter *i*2 forward. Shift only letters; do not change the position of spaces\!

Input Specifications:

- The input is written as follows:

  S  
  M

- Each test case has two lines of input.  
- The first line contains a string *S* indicating the characters that must be replaced in the message.  
- The second line contains a string M indicating the message that will be translated and updated.

Output Specifications:

- For each test case, print two lines of output.  
- The first line should be a single integer indicating the number of words changed.  
- The second line should be the final message.

| Sample Input: ht htis is the text you must translate in the right way kc rokcy pakcs of pancakes lie on a patch of shamrokcs  | Sample Output: 2 hway th isi sthe tex tyou musttrans la tei nther igt 3 ackso fpanc ak eslieona pat ch o fsham ro cksrockyp |
| :---- | :---- |

