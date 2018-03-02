#coding=utf8
def levenshtein_distance(str1, str2):
    dp = [[0] * 1000 for row in range(1000)]

    for i in range(1, 1000):
        dp[i][0] = i

    for j in range(1, 1000):
        dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
            
    return dp[len(str1)][len(str2)]

def levenshtein_similarity(str1, str2):
    s = []
    similarity = 1.0 * (max(len(str1), len(str2)) - levenshtein_distance(str1, str2)) / max(len(str1), len(str2)) 
    if similarity > 0.25:
        s.append(similarity)
    a = 0
    for each in s:
        a = a + each 
    try:
        result = 1.0 * a / len(s)
    except:
        result = 0
    return result

def similarity_list(str1, str2):
    s = []
    for i in str1:
        # for j in str2:
        similarity = 1.0 * (max(len(i), len(str2)) - levenshtein_distance(i, str2)) / max(len(i), len(str2)) 
        print similarity
        if similarity > 0:
            s.append(similarity)
    a = 0
    for each in s:
        a = a + each 

    try:
        result = str(1.0 * a / len(s))
    except:
        result = 0

    print 'similarity: ' + str(result)
