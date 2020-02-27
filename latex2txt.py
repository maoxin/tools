"""
trasfer latex text to plain text.
we get the plain text from paper latex before feed it into grammarly to check grammer erros and typos

use:
    * copy the documents from abstract to the conclusion as "latex"
    * txt = to_txt(latex)
"""

import re

def latex_replace1(matchobj):
    if matchobj.group(1) == 'cite':
        return ''
    elif matchobj.group(1) == 'ref':
        return " 1"
    else:
        return f" {matchobj.group(2)}"

def latex_replace1_1(matchobj):
    if matchobj.group(1) == 'cite':
        return ''
    elif matchobj.group(1) == 'ref':
        return "1"
    else:
        return f"{matchobj.group(2)}"

def to_txt(latex):
    latex = latex.encode('unicode-escape').decode().replace('\\\\', '\\')

    pattern_ftd = r"\\x08egin{figure}.*?\\end{figure}|\\x08egin{table}.*?\\end{table}|\\x08egin{dmath}.*?\\end{dmath}"
    # remove figure, table, and dmath

    txt = re.sub(pattern_ftd, "", latex, flags=re.DOTALL)

    pattern1 = r" \\(\w+?){(.+?)}"
    txt = re.sub(pattern1, latex_replace1, txt)

    pattern1_1 = r"\\(\w+?){(.+?)}"
    txt = re.sub(pattern1_1, latex_replace1_1, txt)

    pattern2 = r"\$.*?\$"
    txt = re.sub(pattern2, "A", txt)

    pattern3 = r"\\item "
    txt = re.sub(pattern3, "", txt)

    return txt.encode().decode('unicode-escape')