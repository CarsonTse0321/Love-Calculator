name1 = input("enter your name:")
name2 = input("enter your name:")

name1 = name1.lower()
name2 = name2.lower()

T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")
E = name1.count("e") + name2.count("e")
first_digit = str(T + R + U + E)
L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")
second_digit = str(L + O + V + E)
Love_Score = int(first_digit + second_digit)
if Love_Score < 10 or Love_Score > 90:
  print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score > 40 and Love_Score < 50:
  print(f"Your score is {Love_Score}, you are alright together.")
else:
  print(f"Your score is {Love_Score}.")