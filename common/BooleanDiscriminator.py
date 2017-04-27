import re

def BooleanDiscriminator(equation):
	threeMarkFormat = re.sub(r"([0-9]+) *([<|>|=]+) *([0-9]+) *([<|>|=]+) *([0-9]+)",r"\1\2\3and\3\4\5",equation)
	spaceFormat = re.sub(" +","",threeMarkFormat)
	bracketFormat = re.sub(r"([0-9]+[<|>|=]+[0-9]+)",r"(\1)",spaceFormat)
	andFormat = bracketFormat.replace('and','&')
	orFormat = andFormat.replace('or','|')
	baseBracketFormat = re.sub(r"^(.*)$",r"(\1)",orFormat) 
	formatText = baseBracketFormat

	maxNest = 0
	nestLevel = 0
	colLevel = 0
	nestColCount = [0]
	result = [[[]]]
	formatText = list(formatText)
	textCount = formatText
	forCount = 1

	for i in formatText:
		if maxNest < nestLevel:
			maxNest = nestLevel
			nestColCount.append(0)
			result.append([[]])
		if i == "(":
			if len(textCount) > forCount:
				if textCount[forCount] == "(":
					nestLevel = nestLevel + 1
		elif i == ")":
			if len(textCount) > forCount:
				if textCount[forCount] == ")":
					result[nestLevel-1][nestColCount[nestLevel-1]].append( str(nestLevel) + "-" + str(nestColCount[nestLevel]) )
					nestColCount[nestLevel] = nestColCount[nestLevel] + 1
					result[nestLevel].append([])
					nestLevel = nestLevel - 1
				else :
					result[nestLevel].append([])
					result[nestLevel-1][nestColCount[nestLevel-1]].append( str(nestLevel) + "-" + str(nestColCount[nestLevel]) )
					nestColCount[nestLevel] = nestColCount[nestLevel] + 1
		elif i == "&" or i == "|":
			result[nestLevel][nestColCount[nestLevel]].append(i)
			result[nestLevel-1][nestColCount[nestLevel-1]].append( str(nestLevel) + "-" + str(nestColCount[nestLevel]) )
			result[nestLevel].append([])
			nestColCount[nestLevel] = nestColCount[nestLevel] + 1
		else:
			result[nestLevel][nestColCount[nestLevel]].append(i)
		forCount = forCount + 1

	print(result)

if __name__ == "__main__":
	BooleanDiscriminator("( 6 >10 ) or ( ( 0 < 4 <= 100) and 6> 10  )")
	#BooleanDiscriminator("( ( 0 < 4 <= 100) and 6> 10  )")