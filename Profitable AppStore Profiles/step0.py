def csv2lol(csvFile,trim_headers=0):
    opFile = open(csvFile, encoding="utf8")
    from csv import reader
    rFile = reader(opFile)
    lol = list(rFile)
    if trim_headers:
        return lol[1:]
    else:
        return lol
        

apps_data = csv2lol("googleplaystore.csv")

for x in apps_data:
    if x[0] == 'Subway Surfers':
        print(apps_data.index(x))
