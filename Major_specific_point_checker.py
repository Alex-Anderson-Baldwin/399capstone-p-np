
## CHECKS the user is taking enough 300 level points within their specific major
def major_specific_points_check(Subject,Subject_number,Major):
    a = self.__cursor.execute("""select 300_LEVEL_POINTS_MAJOR_SPECIFIC from majorRequirements WHERE majorNAME=?""", (Major))
    points = a.fethall()
    paper = points / 15  # assuming paper worth 15 points
    paper_count = 0

    for i in len(Subject):
        if(Subject[i]==Major):
            if(Subject_number[i]>299 AND(Subject_number[i]<399 ):
                paper_count = paper_count+1
    if(paper_count<paper):
        print("Not enough 300 level papers within the users major")
        return 0

    return 1
