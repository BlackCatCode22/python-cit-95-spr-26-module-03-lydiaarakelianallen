text = "X-DSPAM-Confidence:    0.8475"
# this locates the colon (the number occures after the colon)
ipos=text.find(':')
# this cuts the string starting one space after the colon and ends at the end of the string
piece=text[ipos+1:]
# this turns the string into a float and automatically removes the white space at the beginning of the string
value=float(piece)
# this prints the float number
print(value)