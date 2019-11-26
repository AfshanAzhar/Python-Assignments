{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Basic Data Types"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. CAPITALIZE(): \n",
    "The capitalize() method converts the first character of a string to capital (uppercase) letter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pakistan\n"
     ]
    }
   ],
   "source": [
    "a = \"pAkIstaN\"\n",
    "print(a.capitalize())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If the string has its first character as capital, then it returns the original string with the word in \n",
    "sentence case."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pakistan\n"
     ]
    }
   ],
   "source": [
    "a = \"PakIstaN\"\n",
    "print(a.capitalize())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. casefold():\n",
    "The casefold() method is an aggressive lower() method which convert strings to casefolded strings for caseless matching. i.e. ignores cases when comparing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pakistan\n"
     ]
    }
   ],
   "source": [
    "a = \"PakIstaN\"\n",
    "print(a.casefold()) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. center():\n",
    "The center() method creates and returns a new string which is padded with the specified character."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "******** Pakistan *******\n"
     ]
    }
   ],
   "source": [
    "a = \" Pakistan \"\n",
    "x = (a.center(25, \"*\"))\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. encode():\n",
    "The string encode() method returns encoded version of the given string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The string is: pythön!\n",
      "The encoded version is: b'pyth\\xc3\\xb6n!'\n"
     ]
    }
   ],
   "source": [
    "astring = \"pythön!\"\n",
    "#type(astring)\n",
    "\n",
    "print('The string is:', astring) # print string\n",
    "string_utf = astring.encode() # default encoding to utf-8\n",
    "\n",
    "print('The encoded version is:', string_utf) # print result"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 5. endswith():\n",
    "The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.\n",
    "\n",
    "The syntax of endswith() is: ***str.endswith(suffix[, start[, end]])***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.endswith(\"pakistan country.\",)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.endswith(\"Pakistan is my country.\",)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.endswith(\"my country.\", 12, 23)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. startswith():\n",
    "  The startswith() method returns True if a string starts with the specified prefix(string). If not, it returns False.\n",
    "  \n",
    " The syntax of startswith() is:    ***str.startswith(prefix[, start[, end]])***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.startswith(\"my country.\")\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.startswith(\"Pakistan is my country.\")\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.startswith(\"my country.\", 12, 23)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. expandtabs():\n",
    "The expandtabs() method returns a copy of string with all tab characters '\\t' replaced with whitespace characters until the next multiple of tabsize parameter.\n",
    "\n",
    "The syntax of expandtabs() method is:   ***string.expandtabs(tabsize)***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "xyz     12345   abc\n"
     ]
    }
   ],
   "source": [
    "str = 'xyz\\t12345\\tabc'\n",
    "\n",
    "# no argument is passed\n",
    "# default tabsize is 8\n",
    "result = str.expandtabs()\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "xyz   12345 abc\n"
     ]
    }
   ],
   "source": [
    "str = 'xyz\\t12345\\tabc'\n",
    "\n",
    "result = str.expandtabs(6)\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8. find():\n",
    "The find() method returns the ***index of first occurrence of the substring*** (if found). If not found, it returns -1.\n",
    "\n",
    "The syntax of find() method is:    ***str.find(sub[, start[, end]] )***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.find(\"my country.\",)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.find(\"my country.\", 10, 23)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.find(\"my country.\", 1, 20)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "result = a.find(\"country.\")\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9. format():\n",
    "The string format() method formats the given string into a nicer output in Python.\n",
    "\n",
    "The syntax of format() method is:  ***template.format(p0, p1, ..., k0=v0, k1=v1, ...)***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Adam, your balance is 230.2346.\n",
      "Hello Adam, your balance is 230.2346.\n",
      "Hello Adam, your balance is 230.2346.\n",
      "Hello Adam, your balance is 230.2346.\n"
     ]
    }
   ],
   "source": [
    "# default arguments\n",
    "print(\"Hello {}, your balance is {}.\".format(\"Adam\", 230.2346))\n",
    "\n",
    "# positional arguments\n",
    "print(\"Hello {0}, your balance is {1}.\".format(\"Adam\", 230.2346))\n",
    "\n",
    "# keyword arguments\n",
    "print(\"Hello {name}, your balance is {blc}.\".format(name=\"Adam\", blc=230.2346))\n",
    "\n",
    "# mixed arguments\n",
    "print(\"Hello {0}, your balance is {blc}.\".format(\"Adam\", blc=230.2346))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 10. format_map():\n",
    "The format_map() method is similar to str.format(******mapping) except that str.format(******mapping) creates a new dictionary whereas ****str.format_map(mapping) doesn't****.\n",
    "\n",
    "The syntax of the format_map() is:  ***str.format_map(mapping)***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 -5\n",
      "4 -5 0\n"
     ]
    }
   ],
   "source": [
    "point = {'x':4,'y':-5}\n",
    "print('{x} {y}'.format_map(point))\n",
    "\n",
    "point = {'x':4,'y':-5, 'z': 0}\n",
    "print('{x} {y} {z}'.format_map(point))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(6, y)\n",
      "(x, 5)\n",
      "(6, 5)\n"
     ]
    }
   ],
   "source": [
    "# format_map works with dict subclass\n",
    "class Coordinate(dict):\n",
    "    def __missing__(self, key):\n",
    "      return key\n",
    "\n",
    "\n",
    "print('({x}, {y})'.format_map(Coordinate(x='6')))\n",
    "print('({x}, {y})'.format_map(Coordinate(y='5')))\n",
    "print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 11. index():\n",
    "The index() method returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.   \n",
    "The index() method is similar to find() method for strings.  The only difference is that ***find() method returns -1*** if the substring is not found, whereas ***index() throws an exception.***\n",
    "\n",
    "The syntax of index() method for string is:  ***str.index(sub[, start[, end]] )***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Substring = 'my country': 12\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "substring not found",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-81-b51b9447c1c8>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Substring = 'my country':\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'India'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Substring ='India':\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: substring not found"
     ]
    }
   ],
   "source": [
    "a = \"Pakistan is my country.\"\n",
    "\n",
    "result = a.index(\"my country\")\n",
    "print(\"Substring = 'my country':\", result)\n",
    "\n",
    "result = a.index('India')\n",
    "print(\"Substring ='India':\", result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 12. isalnum():\n",
    "The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.  \n",
    "\n",
    "The syntax of isalnum() is:  ***string.isalnum()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "name = \"P234istan\"\n",
    "print(name.isalnum())\n",
    "\n",
    "# contains whitespace\n",
    "name = \"M3onica Gell22er \"\n",
    "print(name.isalnum())\n",
    "\n",
    "name = \"Mo3nicaGell22er\"\n",
    "print(name.isalnum())\n",
    "\n",
    "name = \"133\"\n",
    "print(name.isalnum())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 13. isalpha():\n",
    "The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.  \n",
    "\n",
    "The syntax of isalpha() is:  ***string.isalpha()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "name = \"Pakistan\"\n",
    "print(name.isalpha())\n",
    "\n",
    "# contains whitespace\n",
    "name = \"Pakistan Zindabad\"\n",
    "print(name.isalpha())\n",
    "\n",
    "# contains number\n",
    "name = \"Pakistanzinabad123\"\n",
    "print(name.isalpha())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 14. isascii():\n",
    "The isascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the string using \\x, \\u or \\U escapes.  \n",
    "\n",
    "This method has been newly introduced in Python version 3.7 and following is the **syntax** for it,  \n",
    "\n",
    "***string.isascii()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "my_string = '  '\n",
    "print(my_string.isascii())\n",
    "\n",
    "my_string = 'Studytonight'\n",
    "print(my_string.isascii())\n",
    "\n",
    "my_string = 'Study_ tonight'\n",
    "print(my_string.isascii())\n",
    "\n",
    "my_string = 'Studytonight @ 123'\n",
    "print(my_string.isascii())\n",
    "\n",
    "my_string = 'ö'\n",
    "print(my_string.isascii())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 15. isdecimal():\n",
    "The isdecimal() method returns True if all characters in a string are decimal characters. If not, it returns False.  \n",
    "\n",
    "The syntax of isdecimal() is:  ***string.isdecimal()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "s = \"28212\"\n",
    "print(s.isdecimal())\n",
    "\n",
    "# contains alphabets\n",
    "s = \"32ladk3\"\n",
    "print(s.isdecimal())\n",
    "\n",
    "# contains alphabets and spaces\n",
    "s = \"Mo3 nicaG el l22er\"\n",
    "print(s.isdecimal())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 16. isdigit():\n",
    "The isdigit() method returns True if all characters in a string are digits. If not, it returns False.  \n",
    "\n",
    "The syntax of isdigit() is: ***string.isdigit()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "s = \"28212\"\n",
    "print(s.isdigit())\n",
    "\n",
    "# contains alphabets and spaces\n",
    "s = \"Mo3 nicaG el l22er\"\n",
    "print(s.isdigit())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 17. isidentifier():\n",
    "The isidentifier() method returns True if the string is a valid identifier in Python. If not, it returns False.  \n",
    "The syntax of isidentifier() is: ***string.isidentifier()***\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "a = 'Pakistan'\n",
    "print(a.isidentifier())\n",
    "\n",
    "a = 'Pa kistan'\n",
    "print(a.isidentifier())\n",
    "\n",
    "a = '22Pakistan'\n",
    "print(a.isidentifier())\n",
    "\n",
    "a = ''\n",
    "print(a.isidentifier())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 18. islower():\n",
    "The islower() method returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.  \n",
    "\n",
    "The syntax of islower() is:   ***string.islower()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "s = 'this is good'\n",
    "print(s.islower())\n",
    "\n",
    "s = '@th!s is a1so g00d.'\n",
    "print(s.islower())\n",
    "\n",
    "s = 'this is Not good'\n",
    "print(s.islower())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 19. isnumeric():\n",
    "The isnumeric() method returns True if all characters in a string are numeric characters. If not, it returns False.\n",
    "\n",
    "The syntax of isnumeric() is: ***string.isnumeric()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "s = '1242323'\n",
    "print(s.isnumeric())\n",
    "\n",
    "#s = '²3455'\n",
    "s = '\\u00B23455'\n",
    "print(s.isnumeric())\n",
    "\n",
    "# s = '½'\n",
    "s = '\\u00BD'\n",
    "print(s.isnumeric())\n",
    "\n",
    "s='python12'\n",
    "print(s.isnumeric())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 20. isprintable():\n",
    "The isprintable() methods returns True if all characters in the string are printable or the string is empty. If not, it returns False.  \n",
    "\n",
    "The syntax of isprintable() is: ***string.isprintable()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Space is a printable\n",
      "True\n",
      "\n",
      "New Line is printable\n",
      "False\n",
      "\n",
      "Empty string printable? True\n"
     ]
    }
   ],
   "source": [
    "s = 'Space is a printable'\n",
    "print(s)\n",
    "print(s.isprintable())\n",
    "\n",
    "s = '\\nNew Line is printable'\n",
    "print(s)\n",
    "print(s.isprintable())\n",
    "\n",
    "s = ''\n",
    "print('\\nEmpty string printable?', s.isprintable())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 21. isspace():\n",
    "The isspace() method returns True if there are only whitespace characters in the string. If not, it return False.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 22. istitle():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 24. join():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 25. ljust():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 26. lower():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 27. lsrrip():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 28. maketrans():\n",
    "The string maketrans() method returns a mapping table for translation usable for translate() method.  \n",
    "\n",
    "The syntax of maketrans() method is: ***string.maketrans(x[, y[, z]])***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{97: '123', 98: '456', 99: '789'}\n",
      "{97: '123', 98: '456', 99: '789'}\n"
     ]
    }
   ],
   "source": [
    "# example dictionary\n",
    "dict = {\"a\": \"123\", \"b\": \"456\", \"c\": \"789\"}\n",
    "x = \"\"\n",
    "print(x.maketrans(dict))\n",
    "\n",
    "# example dictionary\n",
    "dict = {97: \"123\", 98: \"456\", 99: \"789\"}\n",
    "x = \"abc\"\n",
    "print(x.maketrans(dict))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 29. partition():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 30. replace():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 31. rfind():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 32. rindex():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 33. rjust():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 34. rpartition():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 35.  isupper():\n",
    "The string isupper() method returns whether or not all characters in a string are uppercased or not.  \n",
    "\n",
    "The syntax of isupper() method is: ***string.isupper()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# example string\n",
    "string = \"THIS IS GOOD!\"\n",
    "print(string.isupper());\n",
    "\n",
    "# numbers in place of alphabets\n",
    "string = \"THIS IS ALSO G00D!\"\n",
    "print(string.isupper());\n",
    "\n",
    "# lowercase string\n",
    "string = \"THIS IS not GOOD!\"\n",
    "print(string.isupper());"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 36. split():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 37. rsplit():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 38. splitliness():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 39. strip():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 40. rstrip():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 41. swapcase():\n",
    "The string swapcase() method converts all uppercase characters to lowercase and all lowercase characters to uppercase characters of the given string, and returns it.  \n",
    "\n",
    "The format of swapcase() method is: ***string.swapcase()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this should all be lowercase.\n",
      "THIS SHOULD ALL BE UPPERCASE.\n",
      "tHiS sHoUlD bE mIxEd CaSeD.\n"
     ]
    }
   ],
   "source": [
    "# example string\n",
    "string = \"THIS SHOULD ALL BE LOWERCASE.\"\n",
    "print(string.swapcase())\n",
    "\n",
    "string = \"this should all be uppercase.\"\n",
    "print(string.swapcase())\n",
    "\n",
    "string = \"ThIs ShOuLd Be MiXeD cAsEd.\"\n",
    "print(string.swapcase())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 42. title():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 43. translate():"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 44. upper():\n",
    "The string upper() method converts all lowercase characters in a string into uppercase characters and returns it.  \n",
    "\n",
    "The syntax of upper() method is:   ***string.upper()***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "THIS SHOULD BE UPPERCASE!\n",
      "TH!S SH0ULD B3 UPP3RCAS3!\n"
     ]
    }
   ],
   "source": [
    "# example string\n",
    "string = \"this should be uppercase!\"\n",
    "print(string.upper())\n",
    "\n",
    "# string with numbers\n",
    "# If no lowercase characters exist, it returns the original string.\n",
    "string = \"Th!s Sh0uLd B3 uPp3rCas3!\"\n",
    "print(string.upper())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 45. zfill():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
