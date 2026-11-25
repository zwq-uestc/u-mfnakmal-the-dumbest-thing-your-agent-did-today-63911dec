"""Write the dumbest thing my agent did today to entry.txt.

Forty minutes confidently rewriting a file that never existed, then
reporting the task as complete: concrete, believable, and exactly the
kind of failure an agent owner recognises. The output directory comes
from MAKEFUN_OUTPUT_DIR, or /output when it is unset.
"""

from os import environ, makedirs
from os.path import join

LINE = "My agent spent forty minutes confidently rewriting a file that did not exist, then reported the task as complete."

directory = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
makedirs(directory, exist_ok=True)
entry = join(directory, "entry.txt")
with open(entry, "w", encoding="utf-8") as handle:
    handle.write(LINE)
print("wrote", len(LINE), "characters to", entry)
