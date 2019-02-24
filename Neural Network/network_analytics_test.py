import analytics
import nnInterface

csvPath = 'results.csv'

majorSentiment, preds = nnInterface.runNextwork(csvPath, mode=1)

print("Major sentiment is ", majorSentiment)

analytics.plotBarGraph(preds)
analytics.plotPieChart(preds)