def maximize(images):
    """
    dict: {0:["tag1","tag2"], 1:["tag3","tag4"]}
    returns [[ID1, ID2, score1], [ID2, ID3, score2]]
    """
    frames = []
    l = []
    for item in dict:
        l.append(item)
    if l%2 == 1:
        del(l[-1])
    for i in range(0, len(l), 2):
        score = get_score(images, l[i], l[i+1])
        frames.append([l[i], l[i+1], score])
    return frames