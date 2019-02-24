import matplotlib.pyplot as plt
import numpy as np

# Returns an array with 13 indexes each with the number of predictions of that class
def getCountList(preds):
    counts = []
    for i in range(0, 13):
        counts.append(0)

    for pred in preds:
        counts[pred] += 1

    return counts

# Returns an array with 3 indexes each with the number of counts for neutral, pos, and neg
def getPosNegCounts(preds):
    counts = []
    for i in range(0, 3):
        counts.append(0)

    for pred in preds:
        if pred == 0 or pred == 2 or pred == 3:
            counts[0] += 1
        if pred == 1 or pred == 6 or pred == 7 or pred == 8 or pred == 9 or pred == 11:
            counts[1] += 1
        if pred == 4 or pred == 5 or pred == 10 or pred == 12:
            counts[2] += 1
    return counts


preds = []
preds.append(10)
preds.append(2)
preds.append(8)
preds.append(8)
preds.append(4)
preds.append(11)
preds.append(1)
preds.append(3)
preds.append(7)
preds.append(6)
preds.append(5)
preds.append(3)
preds.append(1)
preds.append(4)
preds.append(8)
preds.append(6)
preds.append(3)
preds.append(6)
preds.append(4)
preds.append(0)
preds.append(1)
preds.append(8)
preds.append(3)
preds.append(5)
preds.append(7)
preds.append(3)
preds.append(12)
preds.append(7)
preds.append(4)
preds.append(3)
preds.append(11)
preds.append(10)
preds.append(5)
preds.append(3)
preds.append(7)
preds.append(4)
preds.append(2)

def plotBarGraph(preds):

    counts = getCountList(preds)

    ind = np.arange(len(counts))
    width = 0.5

    fig, ax = plt.subplots(figsize=(15, 10))
    rects1 = ax.bar(ind, counts, width)


    ax.set_ylabel('# of Tweets')
    ax.set_title('Tweets by Emotional Sentiment')
    ax.set_xticks(ind)
    ax.set_xticklabels(('empty', 'relief', 'neutral', 'boredom', 'anger', 'hate', 'enthusiasm', 'fun', 'happiness', 'love', 'sadness', 'surprise', 'worry'))
    ax.legend()

    plt.show()


def plotPieChart(preds):
    labels = 'Neutral', 'Positive', 'Negative'
    counts = getPosNegCounts(preds)
    print(counts)

    fig, ax = plt.subplots()
    ax.pie(counts, explode=None, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax.axis('equal')

    plt.show()