
# Start position should be smaller than end position in slicing (-5 < -2) when the step is 0 or positive
s = "abcdefgh"
print('s[-5:-2] :', s[-5:-2])

# Step 2 : move by starting index 0
s = "Python"
print('s[::2] :', s[::2])

# Start position should be greater than end position in slicing (5 > 1) when the step is negative
s = "Python"
print('s[5:1:-1] :',s[5:1:-1])

# Returns Empty string
s = "abcdef"
print(f"Starting position is higher than end position with 0 step:{s[4:1]}")

# Returns Empty string
s = "abcdef"
print(f"Starting position is higher than end position with 0 step:{s[-1:-4]}")

# Returns string
s = "abcdef"
print(f"Starting position is higher than end position with -1 step:{s[-1:-4:-1]}")
#here -1 indicates reversing

s = "abcdef"
print("Full reverse with no indexing and with a -2 step:", s[::-2])

s = "abcdef"
print("Start > end but negative step:",s[1:4:-1])

s = "abcdefghij"
print("Mixed Indices:", s[-8:8:2])

s = "abcdef"
print(s[:: -1][1:4])
#fedcba
#edc

s = "abcdefghij"
print("Advanced indexing 1 s[8:2:-2]:", s[8:2:-2])
# step 1: reverse:  ihgfed
# step 2: Apply the step: ige

s = "abcdefghij"
print("Advanced indexing 2 (tricky one) s[2:8:-1]:", s[2:8:-1])
# slicing always starts with step and then start and stop position
# for negative slicing, start position should be higher than end position, otherwise empty string will be returned

s = "abcdefghij"
print("Advanced indexing 3 (nested Slicing) s[::-1][2:7]:", s[::-1][2:7])
#step 1: reverse
# find 2-6
#cdefgh (reverse this)

s = "abcdefghij"
print("Advanced indexing 4 (Reverse + step combo) s[-2:-9:-2]:", s[-2:-9:-2])
#cdefghi
#igec

s = "abcdefgh"
print("Advanced indexing 5 s[:: -3] :", s[:: -3])
#heb

s = "abcdef"
print("Advanced indexing 6 s[10:2:-1] (Out-of-range indices) :",s[10:2:-1])
#fedcba
#fed

s = "abcdefghij"
a = s[1:9:2]
#bcdefghi
#bdfh
print("Advanced indexing 7 (Chained slicing madness) a[::-1] :", a[::-1])

s = "abcdef"
print("Advanced indexing 8  s[-2:-5] :", s[-2:-5] )
# Step 0. Hence, expected to have smalled number as starting position than end position
# Returns empty string

s = "abcdef"
print("Advanced indexing 9 (Same start and end) s[3:3:-1]: ", s[3:3])
print("Advanced indexing 9 (Same start and end with step) s[3:3:-1]: ", s[3:3:1])
print("Advanced indexing 9 (Same start and end with step) s[3:3:-1]: ", s[3:3:-1])

s = "abcdefghij"
print("Advanced indexing 10 s[7:1:-3]:", s[7:1:-3])

# Sub indexing
s = "PythonIsFun"
print("Advanced indexing 10 s[::-1][::2][1:5] :", s[::-1][::2][1:5])
#nuFsInohtyP
#nFIotP
#FIot
