"""
The Caesar cipher is one of the earliest known and simplest ciphers. It is a type of substitution
cipher in which each letter in a plaintext message is 'shifted' a certain number of places down the
alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

One way to make a Caesar cipher a bit harder to break is to use different shifts at different
positions in the message. For example, we could shift the first character by 5, the second by 12,
the third by 7, and the fourth by 20. Then we repeat the pattern, shifting the fifth character by 5,
the sixth by 12, and so on, until we reach the end of the message we are encrypting.

Such a scheme is called a Vigenère cipher. The Vigènere cipher is about 400 years old.

Implement a function called vigenere which accepts:
    1. a message (a string)
    2. a non-empty tuple of positive integers
    3. a boolean called encode.

The vigenere function must:
 a) encrypt the message using the Vigenere cipher if the boolean encode is True
 b) decrupt the message using the Vigenere cipher if the boolean encode is False.

The vigenere function must return the shifted message. Do not shift anything that is not
a letter. Do not shift numbers. Do not shift punctuation. Just letters. Case matters. This
function must shift capital letters to capital letters, and lower case letters to lower
case letters.

Prove this function works. Write exactly enough doctests to prove it works when encoding
and decoding.
"""
