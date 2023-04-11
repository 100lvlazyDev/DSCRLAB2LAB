graph2 = [[0, 0, 7, 0, 0, 0, 46, 98],
     [0, 0, 33, 0, 0, 99, 0, 0],
     [7, 33, 0, 99, 92, 28, 0, 64],
     [0, 0, 99, 0, 15, 52, 0, 0],
     [0, 0, 92, 15, 0, 0, 0, 58],
     [0, 99, 28, 52, 0, 0, 0, 0],
     [46, 0, 0, 0, 0, 0, 0, 36],
     [98, 0, 64, 0, 58, 0, 36, 0]];

#функція знаходить суму свіх ребер графа
def sum_edges(graph):
    w_sum = 0
    l = len(graph)
    for i in range(l):
        for j in range(i, l):
            w_sum += graph[i][j]
    return w_sum

#Функція що реалізовує алгоритм дейкстри для пошуку мінімальної відстані між двома вершинами
def dijktra(graph, source, dest):
    shortest = [0 for i in range(len(graph))]
    selected = [source]
    l = len(graph)

    inf = 10000000
    min_sel = inf
    for i in range(l):
        if (i == source):
            shortest[source] = 0  # graph[source][source]
        else:
            if (graph[source][i] == 0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if (shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i

    if (source == dest):
        return 0

    selected.append(ind)
    while (ind != dest):

        for i in range(l):
            if i not in selected:
                if (graph[ind][i] != 0):

                    if ((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000


        for j in range(l):
            if j not in selected:
                if (shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)

    return shortest[dest]


# Функція що знаходить всі вершини з непарною кількістю ребер

def get_odd(graph):
    degrees = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if (graph[i][j] != 0):
                degrees[i] += 1


    odds = [i for i in range(len(degrees)) if degrees[i] % 2 != 0]

    return odds


# функція що генерує унікальні пари вершин
def gen_pairs(odds):
    pairs = []
    for i in range(len(odds) - 1):
        pairs.append([])
        for j in range(i + 1, len(odds)):
            pairs[i].append([odds[i], odds[j]])

    #print('pairs are:',pairs)
    #print('\n')
    return pairs


# Фінальна функція
def Chinese_Postman(graph):
    odds = get_odd(graph)
    if (len(odds) == 0):
        return sum_edges(graph)
    pairs = gen_pairs(odds)
    l = (len(pairs) + 1) // 2

    pairings_sum = []
    #функція яка отримує список пар що не мають спільних початкових і кінцевих вершин вершин
    def get_pairs(pairs, done=[], final=[]):

        if (pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])

            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if (i[1] not in val):
                    f.append(i)
                else:
                    continue

                if (len(f) == l):
                    pairings_sum.append(f)
                    #print(pairings_sum);
                    return
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:], val, f)

        else:
            get_pairs(pairs[1:], done, final)


    get_pairs(pairs)
    min_sums = []

    for i in pairings_sum:
        s = 0
        for j in range(len(i)):
            s += dijktra(graph, i[j][0], i[j][1])
        min_sums.append(s)

    added_dis = min(min_sums)
    chinese_dis = added_dis + sum_edges(graph)
    return chinese_dis


print('Chinese Postman Distance is:', Chinese_Postman(graph2))
