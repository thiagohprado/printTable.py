def printTable(tabela):
    for i in range(len(tabela[0])):
        for n in range(len(tabela)):
            print(tabela[n][i].rjust(10), end='\t')
        print('')



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]



printTable(tableData)