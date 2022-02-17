# Pattern Extractor
We want you to build a function that will analyze each character in a given code and determine its nature. The goal is simple, extract a pattern from codes.

## Pattern Translation
Create a function ``extract(code)`` to provide information regarding the nature of each element contained in the code:
* For example, when given the code ``'AeB7'`` as input the function should produce ``'vowel-up vowel-low consonant-up number'`` as output.

In general :
* Add ``number`` to the answer if the element of the code is a digit.
* Add ``vowel`` to the answer if the element of the code is a vowel.
* Add ``consonant`` to the answer if the element of the code is a consonant.
* Follow it by ``-up`` if the vowel or consonant is in upper case.
* Follow it by ``-low`` if the vowel or consonant is in lower case.

*Example*:

With the code ``'65AeBc7'`` the function would output ``number number vowel-up vowel-low consonant-up consonant-up number``.

<details><summary markdown="span">Hint
</summary>
Don't forget to use string functions to identify specific attributes of your characters.
</details>

<details><summary markdown="span">View solution
</summary>

```python
def extract(code):
    pattern = ""
    for c in code:
        if c.isdigit(): pattern += "number "
        elif c in "aeiouy":
            if c.isupper(): pattern += "vowel-up "
            else: pattern += "vowel-low "
        else:
            if c.isupper(): pattern += "consonant-up "
            else: pattern += "consonant-low "
    return pattern.strip()
```
</details>

## Pattern Grouping
We would like now to treat the data you've been providing.
We want you to build a a function that will transform your precedent ouput into something easier and quicker to process.
It is up to you to transform the data into an usable pattern!

Create a function ``treatment(data)`` to transform the data you previously returned into a pattern:
Each suite of common elements should be indicated by the nature of the element followed by '*' and its occurence without other elements in between.

*Example*:

With the code ``'66AeB7'`` your precedent function would output ``'number number vowel-up vowel-low consonant-up number'``.
With this output as input ``treatment`` would output the string ``'number*2 vowel-up*1 vowel-low*1 consonant-up*1 number*1'``.

<details><summary markdown="span">Hint
</summary>
Use a for loop on the string.
</details>

<details><summary markdown="span">View solution
</summary>

```python
def treatment(data):
    pattern = ""
    current = data[0]
    count = 0
    for c in data.split():
        if c == current:
            count += 1
        else:
            pattern += f'{current}*{count} '
            count = 1
            current = c
    return pattern + f'{current}*{count}'
```
</details>
