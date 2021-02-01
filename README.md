# Context-Free-Grammer-Total-Free
Total free is term of Automata theory.

<h3>Definition</h3>
<p>For a given CFG we define a tree with the start symbol S as its root and
whose nodes are working strings of terminals and nonterminals. The descendants of each node are all the possible results of applying every production
to the working string, one at a time. A string of all terminals is a terminal
node in the tree. The resultant tree is called the total language tree of the
CFG. </p>

<h3>Example</h3>
<p>For the CFG </p>

                                            S --> aa | bX | aXX
                                            X --> ab | b
<p>The total language tree is :</p>
