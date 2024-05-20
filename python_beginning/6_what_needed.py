#!/usr/bin/python3
sentence = "There should be one-- and preferably only one --obvious way to do it. lthough that way may not be obvious at first unless you're Dutch."


sentence =sentence[sentence.index("preferably"):(sentence.index("preferably")+len("preferably "))]+ sentence[sentence.index("only"):(sentence.index("only")+len("only "))]+ sentence[sentence.index("one"):(sentence.index("one")+len("one"))]+ " "+  sentence[sentence.index("way"):(sentence.index("way")+len("way "))] + sentence[sentence.index("unless"):(sentence.index("unless")+len("unless"))]

print(sentence)
