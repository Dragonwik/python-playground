
#Integers
intBasic = 10
intFromBinary = 0b11 # 3
intFromOctal = 0o170 # 120
intFromHex = 0x1C # 28
intFromString = int("17")
intFromRounding = int(9.562) #Rounds to Zero
intFromRoundingUp = int(-9.562) #Rounds to Zero
intFromBase5 = int("44", 5) #24
intIntegerFromIntegerDivision = 100//7 #14
intFromBitShift = 5 << 3 #40

print([intBasic,intFromBinary,intFromOctal,
    intFromHex,intFromString,intFromRounding,
    intFromRoundingUp,intFromBase5,intIntegerFromIntegerDivision,
    intFromBitShift])
    
#Floats
floatBasic = 3.1459
floatFromIntegerDivision = 7.15//2.22
floatFromSciNoteation = 3.12e6
floatPlankConstant = 1.616e-35
floatFromInt = float(1)
floatFromString = float("3.159")
floatNotANumber = float("nan")
floatInfinity = float("inf")
floatNegativeInfinity = float("-inf")
floatFromIntegerFloatMath = 80/1.0
print([floatBasic,floatFromIntegerDivision,floatFromSciNoteation,floatPlankConstant,
    floatFromInt,floatFromString, floatNotANumber,floatInfinity,
    floatNegativeInfinity,floatFromIntegerFloatMath])

#None
noneValue = None #This is like a Null but Absence of a value
noneValueisNone = noneValue is None

#Bool
trueValue = True
falseValue = False
falseIsZero = False == 0
trueIsOne = True == 1
truthlyAllValuesBut0AreTruthly = bool(3.215) #Including Negatives
falsyEmptyListsAreFalsy = bool([]) == False
truthyStringsAreTruthly = bool("Penguin")
falsyEmptyStringsAreFalsy = bool("") == False
truthyFalseStringIsTruthly = bool("False") == True #!! Watch Out !!