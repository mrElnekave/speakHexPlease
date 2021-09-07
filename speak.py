# After seeing Tim Babb's [article](http://www.bzarg.com/p/how-to-pronounce-hexadecimal/),
# I needed to be able to play with the script myself and converted his script into python.
# script made by Yamm Elnekave
"""
/************************************
 * hexnames.js                      *
 * (c) 2015 Tim Babb                *
 * trbabb@gmail.com                 *
 * http://bzarg.com                 *
 *                                  *
 * Use of this script is granted    *
 * for any purpose and without      *
 * warranty, provided this          *
 * attribution message is included. *
 ************************************/

"""
"""
source code:
/************************************
 * hexnames.js                      *
 * (c) 2015 Tim Babb                *
 * trbabb@gmail.com                 *
 * http://bzarg.com                 *
 *                                  *
 * Use of this script is granted    *
 * for any purpose and without      *
 * warranty, provided this          *
 * attribution message is included. *
 ************************************/

// "byte" names
byte_names = { "a"  : "atta",
           "b"  : "bibbity",
           "c"  : "city",
           "d"  : "dickety",
           "e"  : "ebbity",
           "f"  : "fleventy",
           "2"  : "twenty",
           "3"  : "thirty",
           "4"  : "forty",
           "5"  : "fifty",
           "6"  : "sixty",
           "7"  : "seventy",
           "8"  : "eighty",
           "9"  : "ninety",
           "0"  : "" };

// "digit" names
digit_names = { "0"  : "",
           "1"  : "one",
           "2"  : "two",
           "3"  : "three",
           "4"  : "four",
           "5"  : "five",
           "6"  : "six",
           "7"  : "seven",
           "8"  : "eight",
           "9"  : "nine",
           "a"  : "a",
           "b"  : "bee",
           "c"  : "cee",
           "d"  : "dee",
           "e"  : "e",
           "f"  : "eff",
           "10" : "ten",
           "11" : "eleven",
           "12" : "twelve",
           "13" : "thirteen",
           "14" : "fourteen",
           "15" : "fifteen",
           "16" : "sixteen",
           "17" : "seventeen",
           "18" : "eighteen",
           "19" : "nineteen",
           "1a" : "abteen",
           "1b" : "bibteen",
           "1c" : "cleventeen",
           "1d" : "dibbleteen",
           "1e" : "eggteen",
           "1f" : "fleventeen" };

// "power" names
power_names = ["bitey", "halfy", "worddion"];

function byteName(s, sayPlaceName) {
    if (s[0] == "1") {
       return digit_names[s.toLowerCase()];
    } else if (s.length == 1) {
        return digit_names[s[0].toLowerCase()];
    } else if (s.length == 2) {
        var s0 = byte_names[s[0].toLowerCase()];
        var s1 = digit_names[s[1].toLowerCase()];
        if (s[0] == "0" && !sayPlaceName) s0 = "oh";
        if (s[1] == "0" && s[0] == "0" && !sayPlaceName)
            return "double-oh";
        if (s0 == "" || s1 == "") return s0 + s1;
        else return s0 + "-" + s1;
    } else {
        return "";
    }
}

function bytePlaceName(i) {
    for (j = 0; j < 31; j++) {
        if (i & 1) return " " + power_names[j];
        i = i >> 1;
    }
    return "";
}  

function hexName(s, sayPlaceNames) {
    if (!/^(0x)?[a-fA-F0-9]+$/.test(s)) return "";
    sout = "";
    s = s.replace(/^0x/i,''); // trim leading "0x"
    s = s.replace(/^0*/, ''); // trim leading zeroes
    
    var place = 0;
    for (i = s.length - 1; i >= 0; i--) {
        var byte = s[i--];
        if (i >= 0) byte = s[i] + byte
        var  name = byteName(byte, sayPlaceNames);
        var pname = sayPlaceNames ? bytePlaceName(place) : "";
        var   div = (name == "" || sout == "") ? "" : " ";
        sout = name + pname + div + sout;
        place += 1;
    }
    return sout;
}

function get_hexname() {
    var inp = document.getElementById("hexnum");
    var out = document.getElementById("hexwords");
    var saynames = document.getElementById("sayPlaceNames").checked;
    var words = hexName(inp.value, saynames).trim();
    out.innerHTML = (words == "") ? "" : ("\"" + words + "\"");
}

"""

import re
import os
from gtts import gTTS


byte_names = {"a": "atta",
          "b": "bibbity",
          "c": "city",
          "d": "dickety",
          "e": "ebbity",
          "f": "fleventy",
          "2": "twenty",
          "3": "thirty",
          "4": "forty",
          "5": "fifty",
          "6": "sixty",
          "7": "seventy",
          "8": "eighty",
          "9": "ninety",
          "0": ""}

digit_names = {"0": "",
          "1": "one",
          "2": "two",
          "3": "three",
          "4": "four",
          "5": "five",
          "6": "six",
          "7": "seven",
          "8": "eight",
          "9": "nine",
          "a": "a",
          "b": "bee",
          "c": "cee",
          "d": "dee",
          "e": "e",
          "f": "eff",
          "10": "ten",
          "11": "eleven",
          "12": "twelve",
          "13": "thirteen",
          "14": "fourteen",
          "15": "fifteen",
          "16": "sixteen",
          "17": "seventeen",
          "18": "eighteen",
          "19": "nineteen",
          "1a": "abteen",
          "1b": "bibteen",
          "1c": "cleventeen",
          "1d": "dibbleteen",
          "1e": "eggteen",
          "1f": "fleventeen"}

power_names = ["bitey", "halfy", "worddion"]


def byteName(s, sayPlaceName):
    if s[0] == "1":
        return digit_names[s.lower()]
    elif len(s) == 1:
        return digit_names[s[0].lower()]
    elif len(s) == 2:
        s0 = byte_names[s[0].lower()]
        s1 = digit_names[s[1].lower()]
        if s[0] == "0" and not sayPlaceName: s0 = "oh"
        if s[1] == "0" and s[0] == "0" and not sayPlaceName: return "double-oh"
        if s0 == "" or s1 == "":
            return s0 + s1
        else:
            return s0 + "-" + s1
    else:
        return ""


def bytePlaceName(place):
    if place == 0:
        return ""
    i = place
    # 5 or 101 has its 1 byte turned on and will be bitey
    # 4 or 100 has its 1 and 2 bytes turned off. But the 4 byte is turned on. Therefore it will be worddion
    for j in range(len(power_names)):
        if (i & 1): return " " + power_names[j]
        i = i >> 1
    return " placemarker"


def hexName(s: str, sayPlaceNames):
    s = s.strip()
    if not re.compile("^(0x)?[a-fA-F0-9]+$").match(s): return "Must be hexadecimal"
    sout = ""
    s = re.sub("^0x", '', s)  # trim leading "0x"
    s = re.sub("^0*", '', s)  # trim leading zeroes
    place = 0
    i = len(s)
    while True:
        i -= 1
        if i < 0:
            break
        byte = s[i]
        i -= 1

        if i >= 0: byte = s[i] + byte
        name = byteName(byte, sayPlaceNames)
        pname = bytePlaceName(place) if sayPlaceNames else ""
        div = "" if (name == "" or sout == "") else " "
        sout = name + pname + div + sout
        place += 1

    return sout


def get_hexname(inp, sayPlaceNames=True):
    words = hexName(inp, sayPlaceNames).strip()
    out = "" if (words == "") else f"\"{words}\""
    return out

testing = False
inputs = [
    "0xDEADBEEF",
    "0xDEADBEE"
]
outputs = [
    "\"dickety-e bitey atta-dee halfy bibbity-e bitey ebbity-eff\"",
    "\"dee bitey ebbity-a halfy dickety-bee bitey ebbity-e\""

]
if __name__ == "__main__":
    if testing:
        for i in range(len(inputs)):
            temp = get_hexname(inputs[i], True)
            if outputs[i] != temp:
                print(f"{inputs[i]} should result in the following: {outputs[i]}\n ----> instead of: {temp}")

    while True:
        inp = input("write your hex here:")
        out = get_hexname(inp)
        print(out)

        language = 'en'
        out = re.sub("(?:(?<=worddion)|(?<=bitey)|(?<=halfy)|(?<=placemarker))[ ]", ', ', out)  # trim leading "0x"
        myobj = gTTS(text=out, lang=language, slow=False)

        myobj.save("output.mp3")
        os.system("mp3player output.mp3")
        os.remove("output.mp3")
