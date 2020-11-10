print("Global print")

if(__name__ == "__main__"):
    print("When executed using the file name")
else:
    print("Being imported as module by other file")

def testFunToExport():
    print("Impl is imported")