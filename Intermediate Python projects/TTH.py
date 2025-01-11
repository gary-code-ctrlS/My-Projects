import pywhatkit as pw

txt="""This program will convert the given text to a handwritten format.
Which can be useful if you are lazy like me"""

pw.text_to_handwriting(txt, "tempHW.png", [0,0,138])
print(" END ")