import random as rm


def create_list_from_freq(freq, size=16):
    num = round(freq * size)
    ones = [1 if i < num else 0 for i in range(size)]
    rm.shuffle(ones)
    return ones


d = {'nolinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 'y': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                 'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
     'onelink': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 'y': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]},
     'twolinks': {'x': [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                  'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
     'collider': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  'y': [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                  'z': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}}


def check_dependencies(dictionary: dict):
    '''The idea is if [(z=1xn\z=0xn)|y=1]==[(z=1xn\z=0xn)|y=0] => z_||_y (z & y  are independed)
       returns list of "answers"'''
    depd = {"x & y": "are INDEPENDED",
            "x & z": "are INDEPENDED",
            "y & z": "are INDEPENDED", }

    iwx0 = indexes_where_x_is_0 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[0]]) if x == 0}
    iwx1 = indexes_where_x_is_1 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[0]]) if x == 1}
    iwy0 = indexes_where_y_is_0 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 0}
    iwy1 = indexes_where_y_is_1 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 1}
    iwz0 = indexes_where_z_is_0 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[2]]) if x == 0}
    iwz1 = indexes_where_z_is_1 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[2]]) if x == 1}

    try:
        '''
        if len(iwx1 & iwy1) / len(iwx0 & iwy1) != len(iwx1 & iwy0) / len(iwx0 & iwy0) or len(iwy1 & iwx1) / len(
                iwy0 & iwx1) != len(iwy1 & iwx0) / len(
            iwy0 & iwx0):  # if [(X=1xN/X=0xN) | Y=1] != [(X=1xN/X=0xN) | Y=0] or [(Y=1xN/Y=0xN) | X=1] != [(Y=1xN/Y=0xN) | X=0]
            depd["x & y"] = "are DEPENDED"
        if len(iwx1 & iwz1) / len(iwx0 & iwz1) != len(iwx1 & iwz0) / len(iwx0 & iwz0) or len(iwz1 & iwx1) / len(
                iwz0 & iwx1) != len(iwz1 & iwx0) / len(
            iwz0 & iwx0):  # if [(X=1xN/X=0xN) | Z=1] != [(X=1xN/X=0xN) | Z=0] or [(Z=1xN/Z=0xN) | X=1] != [(Z=1xN/Z=0xN) | X=0]
            depd["x & z"] = "are DEPENDED"
        if len(iwy1 & iwz1) / len(iwy0 & iwz1) != len(iwy1 & iwz0) / len(iwy0 & iwz0) or len(iwz1 & iwy1) / len(
                iwz0 & iwy1) != len(iwz1 & iwy0) / len(
            iwz0 & iwy0):  # if [(Y=1xN/Y=0xN) | Z=1] != [(Y=1xN/Y=0xN) | Z=0] or [(Z=1xN/Z=0xN) | Y=1] != [(Z=1xN/Z=0xN) | Y=0]
            depd["y & z"] = "are DEPENDED"
        print("x & y ", depd["x & y"], "\n", "x & z ", depd["x & z"], "\n", "y & z ", depd["y & z"], sep="")

    except ZeroDivisionError:

        if len(iwx0 & iwy1) / len(iwx1 & iwy1) != len(iwx0 & iwy0) / len(iwx1 & iwy0) or len(iwy0 & iwx1) / len(
                iwy1 & iwx1) != len(iwy0 & iwx0) / len(iwy1 & iwx0):  # if [(X=0xN/X=1xN) | Y=1] != [(X=0xN/X=1xN) | Y=0] or [(Y=0xN/Y=1xN) | X=1] != [(Y=0xN/Y=1xN) | X=0]
            depd["x & y"] = "are DEPENDED"
        if len(iwx0 & iwz1) / len(iwx1 & iwz1) != len(iwx0 & iwz0) / len(iwx1 & iwz0) or len(iwz0 & iwx1) / len(
                iwz1 & iwx1) != len(iwz0 & iwx0) / len(iwz1 & iwx0):  # if [(X=0xN/X=1xN) | Z=1] != [(X=0xN/X=1xN) | Z=0] or [(Z=0xN/Z=1xN) | X=1] != [(Z=0xN/Z=1xN) | X=0]
            depd["x & z"] = "are DEPENDED"
        if len(iwy0 & iwz1) / len(iwy1 & iwz1) != len(iwy0 & iwz0) / len(iwy1 & iwz0) or len(iwz0 & iwy1) / len(
                iwz1 & iwy1) != len(iwz0 & iwy0) / len(iwz1 & iwy0):  # if [(Y=0xN/Y=1xN) | Z=1] != [(Y=0xN/Y=1xN) | Z=0] or [(Z=0xN/Z=1xN) | Y=1] != [(Z=0xN/Z=1xN) | Y=0]
            depd["y & z"] = "are DEPENDED"
        print("x & y ", depd["x & y"], "\n", "x & z ", depd["x & z"], "\n", "y & z ", depd["y & z"], sep="")
        '''
        if (check_coop_frequencies(dictionary)[0] != check_frequencies(dictionary)[0] * check_frequencies(dictionary)[
            1]  # if P(x=1 & y=1) != P(x=1)*P(y=1)
                or
                check_coop_frequencies(dictionary, (1, 0))[0] != check_frequencies(dictionary, (1, 0, 1))[0] *
                check_frequencies(dictionary, (1, 0, 1))[1] or  # if P(x=1 & y=0) != P(x=1)*P(y=0)
                check_coop_frequencies(dictionary, (0, 1))[0] != check_frequencies(dictionary, (0, 1, 1))[0] *
                check_frequencies(dictionary, (1, 0, 1))[1] or  # if P(x=0 & y=1) != P(x=0)*P(y=1)
                check_coop_frequencies(dictionary, (0, 0))[0] != check_frequencies(dictionary, (0, 0, 1))[0] *
                check_frequencies(dictionary, (1, 0, 1))[1]):  # if P(x=0 & y=0) != P(x=0)*P(y=0)
            depd["x & y"] = "are DEPENDED"
        if (check_coop_frequencies(dictionary)[1] != check_frequencies(dictionary)[0] * check_frequencies(dictionary)[
            2]  # if P(x=1 & z=1) != P(x=1)*P(z=1)
                or
                check_coop_frequencies(dictionary, (1, 0))[1] != check_frequencies(dictionary, (1, 1, 0))[0] *
                check_frequencies(dictionary, (1, 1, 0))[2] or  # if P(x=1 & z=0) != P(x=1)*P(z=0)
                check_coop_frequencies(dictionary, (0, 1))[1] != check_frequencies(dictionary, (0, 1, 1))[0] *
                check_frequencies(dictionary, (0, 1, 1))[2] or  # if P(x=0 & z=1) != P(x=0)*P(z=1)
                check_coop_frequencies(dictionary, (0, 0))[1] != check_frequencies(dictionary, (0, 1, 0))[0] *
                check_frequencies(dictionary, (0, 1, 0))[2]):  # if P(x=0 & z=0) != P(x=0)*P(z=0)
            depd["x & z"] = "are DEPENDED"
        if (check_coop_frequencies(dictionary)[2] != check_frequencies(dictionary)[0] * check_frequencies(dictionary)[
            1]  # if P(y=1 & z=1) != P(y=1)*P(z=1)
                or
                check_coop_frequencies(dictionary, (1, 0))[2] != check_frequencies(dictionary, (1, 1, 0))[2] *
                check_frequencies(dictionary, (1, 1, 0))[1] or  # if P(y=1 & z=0) != P(y=1)*P(z=0)
                check_coop_frequencies(dictionary, (0, 1))[2] != check_frequencies(dictionary, (1, 0, 1))[2] *
                check_frequencies(dictionary, (1, 0, 1))[1] or  # if P(y=0 & z=1) != P(y=0)*P(z=1)
                check_coop_frequencies(dictionary, (0, 0))[2] != check_frequencies(dictionary, (1, 0, 0))[2] *
                check_frequencies(dictionary, (1, 0, 0))[1]):  # if P(y=0 & z=0) != P(y=0)*P(z=0)
            depd["y & z"] = "are DEPENDED"
        return [depd["x & y"], depd["x & z"], depd["y & z"]]
    except:
        return "check_dependencies doesnt work"


def reshuffle(dictionary: dict):
    new_dict = dictionary.copy()
    keys = list(dictionary.keys())
    for key in keys:
        shuffle_coloumns(new_dict[key])
    return new_dict


def shuffle_coloumns(dictionary: dict):
    '''influence on dictionary(tabs) and shuffle coloumn(strings)
       returns the shuffled dictionary'''
    shufflelist = [i for i in range(len(dictionary[list(dictionary.keys())[0]]))]  # list(dictionary.keys())[0] = 'x'
    rm.shuffle(shufflelist)
    tempx, tempy, tempz = [dictionary[list(dictionary.keys())[i]].copy() for i in range(3)]
    for i in range(len(shufflelist)):
        dictionary[list(dictionary.keys())[0]][shufflelist[i]] = tempx[i]  # list(dictionary.keys())[0] = 'x'
        dictionary[list(dictionary.keys())[1]][shufflelist[i]] = tempy[i]  # list(dictionary.keys())[1] = 'y'
        dictionary[list(dictionary.keys())[2]][shufflelist[i]] = tempz[i]  # list(dictionary.keys())[2] = 'z'
    return dictionary


def check_coop_frequencies(dictionary: dict, t=(1, 1)):  # [P(x=1 & y=1), P(x=1 & z=1), P(y=1 & z=1)]
    if t == (1, 1):
        iwx = {i for i, x in enumerate(dictionary[list(dictionary.keys())[0]]) if x == 1}
        iwy1 = iwy2 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 1}
        iwz = {i for i, x in enumerate(dictionary[list(dictionary.keys())[2]]) if x == 1}
    if t == (0, 0):
        iwx = {i for i, x in enumerate(dictionary[list(dictionary.keys())[0]]) if x == 0}
        iwy1 = iwy2 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 0}
        iwz = {i for i, x in enumerate(dictionary[list(dictionary.keys())[2]]) if x == 0}
    if t == (1, 0):
        iwx = {i for i, x in enumerate(dictionary[list(dictionary.keys())[0]]) if x == 1}
        iwy1 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 0}
        iwy2 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 1}
        iwz = {i for i, x in enumerate(dictionary[list(dictionary.keys())[2]]) if x == 0}
    if t == (0, 1):
        iwx = {i for i, x in enumerate(dictionary[list(dictionary.keys())[0]]) if x == 0}
        iwy1 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 1}
        iwy2 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 0}
        iwz = {i for i, x in enumerate(dictionary[list(dictionary.keys())[2]]) if x == 1}

    freqxy, freqxz, freqyz = [len(iwx & iwy1) / len(dictionary[list(dictionary.keys())[0]]),
                              len(iwx & iwz) / len(dictionary[list(dictionary.keys())[0]]),
                              len(iwy2 & iwz) / len(dictionary[list(dictionary.keys())[0]])]

    return [freqxy, freqxz, freqyz]


def check_frequencies(dictionary: dict, t=(1, 1, 1)):  # [P(x=1), P(y=1), P(z=1)]
    '''shows how often "1" occurs
       returns triplet(list) of frquencies'''
    for i in range(len(dictionary[list(dictionary.keys())[0]])):
        freqx, freqy, freqz = [
            dictionary[list(dictionary.keys())[i]].count(t[i]) / len(dictionary[list(dictionary.keys())[i]]) for i in
            range(3)]
    return [freqx, freqy, freqz]


def intervente(dictionary: dict, name='y', fixed=1):
    '''does an intervention in variable "name" and equal it to "fixed"
       reutrns the dictionary with new distribution
       '''
    st = ['x', 'y', 'z']
    st.remove(name)  # to have a deal with other 2 variables

    indexes_where_name_is_0 = [i for i, x in enumerate(dictionary[name]) if x == 0]  # индексы, где Y = 0
    indexes_where_name_is_1 = [i for i, x in enumerate(dictionary[name]) if x == 1]  # индексы, где Y = 1

    x_when_name = [dictionary[st[0]][i] for i in indexes_where_name_is_1]  # Xs where y=1
    x_when_not_name = [dictionary[st[0]][i] for i in indexes_where_name_is_0]  # Xs where y=0
    z_when_name = [dictionary[st[1]][i] for i in indexes_where_name_is_1]  # Zs where y=1
    z_when_not_name = [dictionary[st[1]][i] for i in indexes_where_name_is_0]  # Zs where y=0

    freq_x_when_name = len([i for i in x_when_name if i == 1]) / len(x_when_name)
    freq_x_when_not_name = len([i for i in x_when_not_name if i == 1]) / len(x_when_not_name)
    freq_z_when_name = len([i for i in z_when_name if i == 1]) / len(z_when_name)
    freq_z_when_not_name = len([i for i in z_when_not_name if i == 1]) / len(z_when_not_name)

    indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]
    indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]

    indexes_when_y1_and_z0 = list(set(indexes_where_name_is_1) & set(indexes_where_z0))  # индексы где Y = 1 и Z = 0
    indexes_when_y1_and_z1 = list(set(indexes_where_name_is_1) & set(indexes_where_z1))  # индексы где Y = 1 и Z = 1
    indexes_when_y0_and_z0 = list(set(indexes_where_name_is_0) & set(indexes_where_z0))  # индексы где Y = 0 и Z = 0
    indexes_when_y0_and_z1 = list(set(indexes_where_name_is_0) & set(indexes_where_z1))  # индексы где Y = 0 и Z = 1
    # проверил, что они не пересекаются
    x_when_y1_and_z0 = [dictionary[st[0]][i] for i in
                        indexes_when_y1_and_z0]  # соответственно значения X в этих индексах
    x_when_y1_and_z1 = [dictionary[st[0]][i] for i in indexes_when_y1_and_z1]
    x_when_y0_and_z0 = [dictionary[st[0]][i] for i in indexes_when_y0_and_z0]
    x_when_y0_and_z1 = [dictionary[st[0]][i] for i in indexes_when_y0_and_z1]

    try:

        freqx_when_y1_and_z0 = len([i for i in x_when_y1_and_z0 if i == 1]) / len(x_when_y1_and_z0)
        freqx_when_y1_and_z1 = len([i for i in x_when_y1_and_z1 if i == 1]) / len(x_when_y1_and_z1)
        freqx_when_y0_and_z0 = len([i for i in x_when_y0_and_z0 if i == 1]) / len(x_when_y0_and_z0)
        freqx_when_y0_and_z1 = len([i for i in x_when_y0_and_z1 if i == 1]) / len(x_when_y0_and_z1)

        dictionary[name] = [fixed] * len(dictionary[name])  # заполняем весь Y значением fixed

        if fixed == 1:
            dictionary[st[1]] = create_list_from_freq(freq_z_when_name, len(dictionary[name]))  # заполняем Z значениями
            indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]  # новые индексы где Z = 0
            indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]  # новые индексы где Z = 1
            corresponding_list_x_y1_z0 = create_list_from_freq(freqx_when_y1_and_z0, len(indexes_where_z0))
            corresponding_list_x_y1_z1 = create_list_from_freq(freqx_when_y1_and_z1, len(indexes_where_z1))

            for i in range(len(indexes_where_z0)):
                dictionary[st[0]][indexes_where_z0[i]] = corresponding_list_x_y1_z0[i]

            for i in range(len(indexes_where_z1)):
                dictionary[st[0]][indexes_where_z1[i]] = corresponding_list_x_y1_z1[i]

        if fixed == 0:
            dictionary[st[1]] = create_list_from_freq(freq_z_when_not_name,
                                                      len(dictionary[name]))  # заполняем Z значениями
            indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]
            indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]
            corresponding_list_x_y0_z0 = create_list_from_freq(freqx_when_y0_and_z0, len(indexes_where_z0))
            corresponding_list_x_y0_z1 = create_list_from_freq(freqx_when_y0_and_z1, len(indexes_where_z1))
            for i in range(len(indexes_where_z0)):
                dictionary[st[0]][indexes_where_z0[i]] = corresponding_list_x_y0_z0[i]

            for i in range(len(indexes_where_z1)):
                dictionary[st[0]][indexes_where_z1[i]] = corresponding_list_x_y0_z1[i]

    except ZeroDivisionError:
        return "WRONG 0"

    except IndexError:
        return "WRONG indexes"

    return dictionary


def intervente2(dictionary: dict, name='y', fixed=1):
    '''does an intervention in variable "name" and equal it to "fixed"
       reutrns the dictionary with new distribution'''
    st = ['x', 'y', 'z']
    st.remove(name)  # to have a deal with other 2 variables

    indexes_where_name_is_0 = [i for i, x in enumerate(dictionary[name]) if x == 0]  # индексы, где Y = 0
    indexes_where_name_is_1 = [i for i, x in enumerate(dictionary[name]) if x == 1]  # индексы, где Y = 1

    x_when_name = [dictionary[st[0]][i] for i in indexes_where_name_is_1]  # Xs where y=1
    x_when_not_name = [dictionary[st[0]][i] for i in indexes_where_name_is_0]  # Xs where y=0
    z_when_name = [dictionary[st[1]][i] for i in indexes_where_name_is_1]  # Zs where y=1
    z_when_not_name = [dictionary[st[1]][i] for i in indexes_where_name_is_0]  # Zs where y=0

    #print(z_when_name)
    #print([i for i in z_when_name if i == 1])

    freq_x_when_name = len([i for i in x_when_name if i == 1]) / len(x_when_name)
    freq_x_when_not_name = len([i for i in x_when_not_name if i == 1]) / len(x_when_not_name)
    freq_z_when_name = len([i for i in z_when_name if i == 1]) / len(z_when_name)
    freq_z_when_not_name = len([i for i in z_when_not_name if i == 1]) / len(z_when_not_name)

    indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]
    indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]

    indexes_when_y1_and_z0 = list(set(indexes_where_name_is_1) & set(indexes_where_z0))
    indexes_when_y1_and_z1 = list(set(indexes_where_name_is_1) & set(indexes_where_z1))
    indexes_when_y0_and_z0 = list(set(indexes_where_name_is_0) & set(indexes_where_z0))
    indexes_when_y0_and_z1 = list(set(indexes_where_name_is_0) & set(indexes_where_z1))

    x_when_y1_and_z0 = [dictionary[st[0]][i] for i in indexes_when_y1_and_z0]
    x_when_y1_and_z1 = [dictionary[st[0]][i] for i in indexes_when_y1_and_z1]
    x_when_y0_and_z0 = [dictionary[st[0]][i] for i in indexes_when_y0_and_z0]
    x_when_y0_and_z1 = [dictionary[st[0]][i] for i in indexes_when_y0_and_z1]

    try:

        freqx_when_y1_and_z0 = len([i for i in x_when_y1_and_z0 if i == 1]) / len(x_when_y1_and_z0)
        freqx_when_y1_and_z1 = len([i for i in x_when_y1_and_z1 if i == 1]) / len(x_when_y1_and_z1)
        freqx_when_y0_and_z0 = len([i for i in x_when_y0_and_z0 if i == 1]) / len(x_when_y0_and_z0)
        freqx_when_y0_and_z1 = len([i for i in x_when_y0_and_z1 if i == 1]) / len(x_when_y0_and_z1)

        dictionary[name] = [fixed] * len(dictionary[name])  # заполняем весь Y значением fixed

        if fixed == 1:
            dictionary[st[1]] = create_list_from_freq(freq_z_when_name, len(dictionary[name]))  # заполняем Z значениями
            indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]
            indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]
            list_for_x_1 = create_list_from_freq(freq_x_when_name, len(indexes_where_z0))
            list_for_x_2 = create_list_from_freq(freq_x_when_name, len(indexes_where_z1))

            for i in range(len(indexes_where_z0)):
                dictionary[st[0]][indexes_where_z0[i]] = list_for_x_1[i]

            for i in range(len(indexes_where_z1)):
                dictionary[st[0]][indexes_where_z1[i]] = list_for_x_2[i]

        if fixed == 0:
            dictionary[st[1]] = create_list_from_freq(freq_z_when_not_name,
                                                      len(dictionary[name]))  # заполняем Z значениями
            indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]
            indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]
            list_for_x_1 = create_list_from_freq(freq_x_when_not_name, len(indexes_where_z0))
            list_for_x_2 = create_list_from_freq(freq_x_when_not_name, len(indexes_where_z1))
            for i in range(len(indexes_where_z0)):
                dictionary[st[0]][indexes_where_z0[i]] = list_for_x_1[i]

            for i in range(len(indexes_where_z1)):
                dictionary[st[0]][indexes_where_z1[i]] = list_for_x_2[i]

    except ZeroDivisionError:
        return "WRONG 0"

    except IndexError:
        return "WRONG indexes"

    return dictionary

def intervente3(dictionary: dict, name='y', fixed=1):
    '''does an intervention in variable "name" and equal it to "fixed"
       reutrns the dictionary with new distribution
       '''
    st = ['x', 'y', 'z']
    st.remove(name)  # to have a deal with other 2 variables

    indexes_where_name_is_0 = [i for i, x in enumerate(dictionary[name]) if x == 0]  # индексы, где Y = 0
    indexes_where_name_is_1 = [i for i, x in enumerate(dictionary[name]) if x == 1]  # индексы, где Y = 1

    x_when_name = [dictionary[st[0]][i] for i in indexes_where_name_is_1]  # Xs where y=1
    x_when_not_name = [dictionary[st[0]][i] for i in indexes_where_name_is_0]  # Xs where y=0
    z_when_name = [dictionary[st[1]][i] for i in indexes_where_name_is_1]  # Zs where y=1
    z_when_not_name = [dictionary[st[1]][i] for i in indexes_where_name_is_0]  # Zs where y=0

    freq_x_when_name = len([i for i in x_when_name if i == 1]) / len(x_when_name)
    freq_x_when_not_name = len([i for i in x_when_not_name if i == 1]) / len(x_when_not_name)
    freq_z_when_name = len([i for i in z_when_name if i == 1]) / len(z_when_name)
    freq_z_when_not_name = len([i for i in z_when_not_name if i == 1]) / len(z_when_not_name)

    indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]
    indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]

    indexes_when_y1_and_z0 = list(set(indexes_where_name_is_1) & set(indexes_where_z0))  # индексы где Y = 1 и Z = 0
    indexes_when_y1_and_z1 = list(set(indexes_where_name_is_1) & set(indexes_where_z1))  # индексы где Y = 1 и Z = 1
    indexes_when_y0_and_z0 = list(set(indexes_where_name_is_0) & set(indexes_where_z0))  # индексы где Y = 0 и Z = 0
    indexes_when_y0_and_z1 = list(set(indexes_where_name_is_0) & set(indexes_where_z1))  # индексы где Y = 0 и Z = 1
    # проверил, что они не пересекаются
    x_when_y1_and_z0 = [dictionary[st[0]][i] for i in
                        indexes_when_y1_and_z0]  # соответственно значения X в этих индексах
    x_when_y1_and_z1 = [dictionary[st[0]][i] for i in indexes_when_y1_and_z1]
    x_when_y0_and_z0 = [dictionary[st[0]][i] for i in indexes_when_y0_and_z0]
    x_when_y0_and_z1 = [dictionary[st[0]][i] for i in indexes_when_y0_and_z1]

    try:

        freqx_when_y1_and_z0 = len([i for i in x_when_y1_and_z0 if i == 1]) / len(x_when_y1_and_z0)
        freqx_when_y1_and_z1 = len([i for i in x_when_y1_and_z1 if i == 1]) / len(x_when_y1_and_z1)
        freqx_when_y0_and_z0 = len([i for i in x_when_y0_and_z0 if i == 1]) / len(x_when_y0_and_z0)
        freqx_when_y0_and_z1 = len([i for i in x_when_y0_and_z1 if i == 1]) / len(x_when_y0_and_z1)

        dictionary[name] = [fixed] * len(dictionary[name])  # заполняем весь Y значением fixed

        if fixed == 1:
            dictionary[st[1]] = create_list_from_freq(freq_z_when_name, len(dictionary[name]))  # заполняем Z значениями
            indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]  # новые индексы где Z = 0
            indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]  # новые индексы где Z = 1
            corresponding_list_x_y1_z0 = create_list_from_freq(freqx_when_y1_and_z0, len(indexes_where_z0))
            corresponding_list_x_y1_z1 = create_list_from_freq(freqx_when_y1_and_z1, len(indexes_where_z1))

            for i in range(len(indexes_where_z0)):
                dictionary[st[0]][indexes_where_z0[i]] = corresponding_list_x_y1_z0[i]

            for i in range(len(indexes_where_z1)):
                dictionary[st[0]][indexes_where_z1[i]] = corresponding_list_x_y1_z1[i]

        if fixed == 0:
            dictionary[st[1]] = create_list_from_freq(freq_z_when_not_name,
                                                      len(dictionary[name]))  # заполняем Z значениями
            indexes_where_z0 = [i for i, x in enumerate(dictionary[st[1]]) if x == 0]
            indexes_where_z1 = [i for i, x in enumerate(dictionary[st[1]]) if x == 1]
            corresponding_list_x_y0_z0 = create_list_from_freq(freqx_when_y0_and_z0, len(indexes_where_z0))
            corresponding_list_x_y0_z1 = create_list_from_freq(freqx_when_y0_and_z1, len(indexes_where_z1))
            for i in range(len(indexes_where_z0)):
                dictionary[st[0]][indexes_where_z0[i]] = corresponding_list_x_y0_z0[i]

            for i in range(len(indexes_where_z1)):
                dictionary[st[0]][indexes_where_z1[i]] = corresponding_list_x_y0_z1[i]

    except ZeroDivisionError:
        return "WRONG 0"

    except IndexError:
        return "WRONG indexes"

    return dictionary


'''
print(d['collider'], "- collider")

print(shuffle_coloumns(d['collider']), "- shuffled")
print(check_dependencies(d['collider']), "- dependencies")
print(check_frequencies(d['collider']), "- frequencies")
print(intervente2(d['collider'], 'z', 0), "- orange distribution (Z fixed")
print(check_dependencies(d['collider']), "- dependencies again")
print(check_frequencies(d['collider']), "- frequencies again")
temp = {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  'y': [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                  'z': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
print(intervente2(temp, 'z', 0), "- orange distribution (Z fixed)")
print(check_dependencies(temp), "- dependencies again x2")
print(check_frequencies(temp), "- frequencies again x2")
'''
