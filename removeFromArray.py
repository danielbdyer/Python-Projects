names = ["Alex","Mary","Steve","John","Seinfeld","Alan","Jane"]
print(names)
namesToRemove = ["Steve","Alan"]
print(namesToRemove + "will be removed")

finishedArray = set(names).difference(namesToRemove)
print(finishedArray)
