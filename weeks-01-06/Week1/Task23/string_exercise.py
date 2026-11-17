# Task 23 - String data type
s = "  Artificial Intelligence and Machine Learning  "
print(repr(s))
print("strip:", repr(s.strip()))
t = s.strip()
print("upper/lower/title:", t.upper(), "|", t.lower(), "|", t.title())
print("length:", len(t), "| first/last char:", t[0], t[-1])
print("slicing:", t[0:10], "| reversed:", t[::-1])
print("find/count:", t.find("Intelligence"), t.count("n"))
print("replace:", t.replace("Machine", "Deep"))
print("split:", t.split())
print("join:", "-".join(["a", "b", "c"]))
print("startswith/endswith:", t.startswith("Art"), t.endswith("ing"))
print("isdigit/isalpha:", "123".isdigit(), "abc".isalpha(), "abc123".isalnum())

name, marks = "Sara", 91.456
print("f-string: %s scored %.1f" % (name, marks), "|", f"{name} scored {marks:.2f}")
print("format():", "{} scored {:>8.2f}".format(name, marks))
print("center/zfill:", "hi".center(10, "*"), "42".zfill(5))

# Palindrome and vowel count
word = "Level"
print(word, "is palindrome:", word.lower() == word.lower()[::-1])
print("vowels in 'education':", sum(1 for c in "education" if c in "aeiou"))
print("Escape: tab\\t newline\\n -> raw:", r"C:\new\table")
