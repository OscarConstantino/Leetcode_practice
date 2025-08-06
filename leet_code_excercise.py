def longestCommonPrefix(strs):
    if not strs[0] == "":
        substring = ""
        for pos,char in enumerate(strs[0]):
            substring+=char
            for string in strs[1:]:
                if pos < len(string):
                    if not string[pos] == char:
                        return substring[:-1]
                else:
                    return substring[:-1]
        return substring
    else:
        return ""

#strs = ["flower","flow","flight"]
#strs2 = ["dog","racecar","car"]
#strs3 = ["c","acc","ccc"]
#strs4 = ["ab","a"]
#strs5 = [""]

#strsLists = [strs, strs2, strs3, strs4, strs5]

#for list in strsLists:
#    print("RES: ",longestCommonPrefix(list))