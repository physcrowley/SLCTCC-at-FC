# SLC CODING COMPETITION 2025

After completing a problem:

- Have on team member raise their hand and wait for a judge to arrive.  
- The judge will record the current time, then provide you with an input file. After receiving the file, **ensure you update the file path in your code to open the file you were given\!**  
- Your output must match the expected output **exactly**. The expected output is explained in each problem’s output specifications.  
- You are allowed two attempts for each problem. After your first attempt, you may keep the input file from the first attempt and use it to correct your code.

Scoring:

- Your team will be awarded points for each correct line of output.  
- If you get all lines of outputs correct on your first attempt, you will gain bonus points.  
- You will gain some additional bonus points determined by the time you completed the problem.  
- If your code crashes partway through due to an error, any output that did not print will be counted as zero, but you will receive points for successful output.  
  * Any errors at the *end* of the output caused by whitespace at the end of the file will be dismissed and you will not lose points.

Rules for solving problems:

- You may reference any code or documentation already on your device to help you solve problems.  
  * You may *not* use generative AI to solve problems.  
- You may write on paper (including these pages) to help you solve problems.  
- You may *not* communicate with anyone outside of your team or use the internet.

Tips:

- Read the instructions, input specifications, and output specifications fully before attempting.  
- Examine the sample input and sample output carefully\!  
- Think of edge cases that may not be covered by the sample input\!  
- Ensure your output matches the format of the expected output **exactly**\! 

1) **Word Flip**

You are helping a librarian organize special books that have mirrored text\! She needs your help flipping words. Given a list of words, output each word in reverse. 

Input Specifications:

- Each test case is a series of words split across multiple lines.  
- Some lines will include more than one word, separated by spaces. In these cases, the words should be reversed but the order of words should be kept.  
- The final line of the test case will be “STOP”, which should not be included in the output.

Output Specifications:

- For each test case, output a single line containing all words separated by spaces in the order they appeared in the input.

| Sample Input: apple banana tree STOP red orange yellow green blue STOP one two-three four five six STOP | Sample Output: elppa ananab eert der egnaro wolley neerg eulb eno eerht-owt ruof evif xis |
| :---- | :---- |

2) **Number Sort**

You have been asked to assist with sorting a scrambled list of numbers. These numbers will be sorted by two factors: value and parity (even or odd). Given a series of numbers, organize them into a list where all odd numbers appear first in ascending order, then all even numbers appear in descending order.

Input Specifications:

- Each test case contains one line of input.  
- Each line of input is a series of numbers separated by commas and spaces.

Output Specifications:

- For each test case, output a single line containing the sorted list of numbers separated by commas and spaces.

| Sample Input: 1, 5, 2, 4, 6, 3 3, 8, 9, 2, 5, 0, 2, 8 11, 2, 300, 5, 2, 2, 3, 10, 0 | Sample Output: 1, 3, 5, 6, 4, 2 3, 5, 9, 8, 8, 2, 2, 0 3, 5, 11, 300, 10, 2, 2, 2, 0 |
| :---- | :---- |

3) **Encrypted Dispatch**

You are a secret agent working for an elite organization. To protect sensitive information, all messages must be encrypted before being transmitted. Messages are encrypted with a variant of a Caesar cipher, where the rotation of each letter is determined by its first appearance in the message (counting from 1). 

Encryption Process:

- Each letter in the message is shifted forward in the alphabet by a number determined by its position in the message.  
- If a letter appears multiple times, its shift is determined by the first appearance.  
- Only letters should be shifted, and capitalization should be preserved.  
- If the rotation exceeds ‘Z’, it wraps around to the beginning of the alphabet.

Input Specifications:

- Each test case is a single line containing the secret code.  
- Each line will contain at least one letter.

Output Specifications:

- For each test case, output a single line containing the encrypted message.

| Sample Input: hello a a a Secret Code | Sample Output: igoot b b b Tgfvgz Fxmg |
| :---- | :---- |

4) **Melody Transposition**

A music teacher has asked for your help transposing melodies for her students. To successfully transpose a melody, you must shift the *pitch* of each *note* up or down a specified number of *semitones*.

In music, notes are assigned letter names (letters *A* through *G*), which correspond to their *pitch*. The pitch of a note is measured in *semitones*. Each pitch must be raised or lowered by two semitones to reach the next letter. A pitch that is raised by only one semitone becomes *sharp*, represented by *\#* (hashtag), and a pitch lowered by only one semitone becomes *flat*, represented by *b* (lowercase B). Sharps and flats are collectively called *accidentals*, and notes without accidentals are called *naturals*. Exceptions to these rules include *B* and *E* which only need to be raised by one semitone to reach *C* and *F* respectively, and vice versa. **These notes will never have accidentals applied**, and should always be written as naturals.

Example:

- *D*, raised by one semitone, becomes *D\#*, then *E* if raised again. If *E* is lowered by one semitone, it becomes *Eb*. *E* only needs to be raised by one semitone to become *F*.

When writing accidentals, **a sharp *or* a flat can be used to refer to the same note**. For example, both *D\#* and *Eb* refer to the note that lies between *D* and *E*. Melodies will not be written with both sharps *and* flats, and will only use one symbol when denoting accidentals. When transposing melodies, you must determine which symbol to use for accidentals. If the provided melody already uses one of the symbols, use that symbol for the transposed melody, otherwise default to *sharps* if transposing up and *flats* if transposing down.

Input Specifications:

- Each test case consists of two lines of input.  
- The first line contains a single integer indicating the number of semitones to transpose the melody by.  
- The second line contains the melody itself, a series of letter names (with or without accidentals) each separated by spaces.

Output Specifications:

- Output a single line containing the transposed melody.

Notes:

- In the real-world, notes *E\#*, *Fb*, *B\#*, and *Cb* are commonly used for a variety of reasons. For this problem, **pretend they do not exist**; you will be marked incorrect if they appear in your output.

| Sample Input: 2 C D E F G \-3 A C E 1 D D D A G\# G F D F G | Sample Output: D E F\# G A Gb A Db D\# D\# D\# A\# A G\# F\# D\# F\# G\# |
| :---- | :---- |

5) **Treasure Hunting**

You and your favourite band of dungeon-delvers have, well, delved into the nearest dungeon in search of treasure. The treasure you are looking for changes with each dungeon.

Given a map of the dungeon, return the number of “steps” needed to reach the desired treasure. The dungeon map is made of multiple lines of text, with each line representing one floor of the dungeon. Each floor requires one step by default, but certain shortcuts or obstacles may reduce or increase the number of steps needed.

If you reach a shortcut, ignore everything else on the same floor. If you reach the treasure before anything else on the same floor, ignore anything after the treasure. Everything that is not a shortcut, obstacle, or desired treasure should be ignored. You may assume that a shortcut will never occur before the treasure on the same floor as it, that the desired treasure exists, and that the desired treasure will not share the name of a shortcut or obstacle.

**Shortcuts**: Ladder (- 2 steps), Chute (- 5 steps) | **Obstacles**: Spikes (+ 2 steps), Lava (+ 5 steps)

Input Specifications:

- The first line of every test case contains the desired treasure.  
- The rest is a multi-line string where each line represents a floor of the dungeon. The beginning and end of each floor will be denoted with a \# character.  
- An empty line will be placed between each test case to separate them.

Output Specifications:

- For each test case, output the number of steps, written in the format “*N* steps”, where *N* is the number of steps taken.  
  * Note that if only one step is needed, output “1 step”.

| Sample Input: Gold \#    Spikes               \# \#     Spikes              \# \#                         \# \#           Merchant      \# \#   Jester          Spikes\# \#                         \# \#           Gold          \# \#             Lava        \# Chalice \#Chest          \# \# Chute Lava    \# \#Traitorous Elf \# \# Lava   Ladder \# \# Spikes Chalice\# \#               \# | Sample Output: 13 steps 5 steps |
| :---- | :---- |

6) **Colour Variance**

A paint factory has tasked you with checking the quality of their paint colours. They have sent you a series of tests to perform, including an expected colour and a colour to compare to it. For each pair of colours, they want you to provide a percentage representing how accurate the second colour is to matching the first. For example, two colours that are identical will have an accuracy of 100%, while pure black and pure white will have an accuracy of 0%.

Input Specifications:

- Each test case consists of a single line of input, containing two rgb colours separated by commas.  
- RGB colours are written in the format *rgb(r,g,b)*, where *r*, *g*, and *b* are integers.  
- R, G, and B values will never be less than 0 and will never exceed 255\.

Output Specifications:

- Output a percentage (rounded to one decimal point) showing the accuracy of the two colours.  
- If a percentage ends with a zero after the decimal, include the zero anyway.

| Sample Input: rgb(128,122,0), rgb(95,128,0) rgb(50,50,50), rgb(50,50,50) rgb(78,4,54), rgb(20,87,237) |
| :---- |
| Sample Output: 92.4% 100.0% 52.6% |

Hint: To find the accuracy of the colours, try thinking of each RGB colour as 3D coordinates and measure the distance between colours. The greatest distance between colours occurs with rgb(255,255,255) and rgb(0,0,0).