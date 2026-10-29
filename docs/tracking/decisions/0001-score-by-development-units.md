# 0001 Score by development units and rare sources, not by number matches

**Situation.** We needed a measure of how close a reproduced post is to the original. The first proposal was "the share of the original's numbers, dates, and names that appear with the same value". It is a string comparison, so code can decide it directly.

**Decision.** Split the original into development units (links in the chain) and fix them in `units.md`. Then measure how many units with the same substance the reproduction found again through the same primary source, and how many sources that do not appear on the first page of an ordinary search it found again. Record the number match only as a reference figure. Order does not matter.

**Rejected options.** Number match rate: it rises by copying a single summary article, and it cannot measure the author's strength, "the ability to widen from a topic into history and implications". Pass rate on style rules: easy to reproduce and low in value.

**Result.** The source-tracing worker gained the `units.md` and rare/foundation marking steps, and the development units became the denominator of every score. Because splitting into units involves judgment, a rule followed: fix them before reproduction and never change them afterward.
