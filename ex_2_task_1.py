# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail you at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt


def is_valid_email_address(s):
    if (s.count(".") != 1 or s.count("@") != 1):
        # check for the only symbols allowed and that there's the correct number of them
        return ("1", "Exactly one @ and one . allowed.")

    atIndex = s.find("@")  # grab the indices of those symbols
    perIndex = s.find(".")
    if (atIndex > perIndex):  # if the @ is before the ., err
        return ("2", "The '@' must come before the '.'.")

    if (atIndex < 3 or atIndex > 16 or not s[0:atIndex].isalnum()):  # validate the part before the @
        return ("3", "There must be 3-16 alpha-numeric characters before the '@'")

    if (perIndex - atIndex <= 2 or perIndex - atIndex > 9 or not s[atIndex + 1:perIndex].isalnum()):
        # validate the part betwee the @ and the .
        return ("4", "There must be 2-8 alpha-numeric characters between the '@' and the '.'")

    if ((s.split(".")[1]) not in ["com", "edu", "org", "gov"]):  # validate the tld
        return ("5", "'com', 'edu', 'org', or 'gov' must follow the '.'")

    return None, "Seems legit"  # if no errs are thrown, report good email


# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = [
        "charding@iastate.edu",
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org",
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}")  # Error
