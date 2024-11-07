import matplotlib.pyplot as plt

def generatePiechart():
    labels = ['A', 'B', 'C']
    values = [200, 65, 120]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie.png')
    plt.close()