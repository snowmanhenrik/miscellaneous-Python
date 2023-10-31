def pearsonSpecterLitt(candidates:dict):
    gpatuple = ()
    gpalist = []
    report = []
    
    for entity in candidates:
        gpatuple = (candidates[entity][0],entity)
        gpalist.append(gpatuple)

    gpalist.sort()
    gpalist = gpalist[::-1]
    
    for i in range(len(gpalist)):
        report.append(gpalist[i][1])

    if len(report) != 0:
        return report
    else:
        print("Sorry, No Suitable Candidates!")
        return report
