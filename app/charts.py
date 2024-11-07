import matplotlib.pyplot as plt

def generateBarChart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()
    
    
def generatePieChart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie.png')
    plt.close()
    
if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [10, 40, 800]
    generateBarChart(labels, values)
    generatePieChart(labels, values)