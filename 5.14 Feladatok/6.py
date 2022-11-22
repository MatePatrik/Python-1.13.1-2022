xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
def napok(Jegy):
    for i in xs:
        if i>=90:
            osztályzat="jeles"
        elif i>=80 and i<90:
            osztályzat="jó"
        elif i>=70 and i<80:
            osztályzat="közepes"
        elif i>=60 and i<70:
            osztályzat="elégséges"
        elif i>60:
            osztályzat="elégtelen"
        print("A kapott jegyed: ",osztályzat)
napok(xs)
