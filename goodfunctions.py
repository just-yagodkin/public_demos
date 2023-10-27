import random as rm
import ast
import copy


def create_list_from_freq(freq, size=16):
    num = round(freq * size)
    ones = [1 if i < num else 0 for i in range(size)]
    rm.shuffle(ones)
    return ones


pre_data_edges = {'nolinks': [False],
                  'onelink': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}}],
                  'twolinks': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}],
                  'collider1': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'ZY', 'source': 'Z', 'target': 'Y', 'label': ""}}],
                  'fork': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YX', 'source': 'Y', 'target': 'X', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}],
                  'threelinks': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XZ', 'source': 'X', 'target': 'Z', 'label': ""}}],
                  }

original_data = {'nolinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                             'y': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                             'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
                 'onelink': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                             'y': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                             'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]},
                 'twolinks': {'x': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                              'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]},
                 'collider1': {'x': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                               'y': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                               'z': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]},
                 'fork': {'x': [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          'z': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                 'threelinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                'y': [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                                'z': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
                 }

# gf.smartdatainterv(
pre_preobservational_data = copy.deepcopy(original_data)

d = {'nolinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 'y': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                 'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
     'onelink': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 'y': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]},
     'twolinks': {'x': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]},
     'collider1': {'x': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                   'y': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                   'z': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]},
     'fork': {'x': [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              'z': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
     'collider2': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                   'y': [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                   'z': [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1]},
     'threelinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    'y': [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                    'z': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
     }  # collider2 is optional


def check_dependencies(dictionary: dict):
    """The idea is if [(z=1xn/z=0xn)|y=1]==[(z=1xn/z=0xn)|y=0] => z_||_y (z & y  are independed)
       returns list of 'answers'"""
    depd = {"x & y": "are INDEPENDED",
            "x & z": "are INDEPENDED",
            "y & z": "are INDEPENDED", }

    iwx0 = indexes_where_x_is_0 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[0]]) if x == 0}
    iwx1 = indexes_where_x_is_1 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[0]]) if x == 1}
    iwy0 = indexes_where_y_is_0 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 0}
    iwy1 = indexes_where_y_is_1 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[1]]) if x == 1}
    iwz0 = indexes_where_z_is_0 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[2]]) if x == 0}
    iwz1 = indexes_where_z_is_1 = {i for i, x in enumerate(dictionary[list(dictionary.keys())[2]]) if x == 1}

    number_of_x1_when_y1 = len(iwx1 & iwy1)
    number_of_x0_when_y1 = len(iwx0 & iwy1)
    number_of_x0_when_y0 = len(iwx0 & iwy0)
    number_of_x1_when_y0 = len(iwx1 & iwy0)

    number_of_x1_when_z1 = len(iwx1 & iwz1)
    number_of_x0_when_z1 = len(iwx0 & iwz1)
    number_of_x0_when_z0 = len(iwx0 & iwz0)
    number_of_x1_when_z0 = len(iwx1 & iwz0)

    number_of_y1_when_z1 = len(iwy1 & iwz1)
    number_of_y0_when_z1 = len(iwy0 & iwz1)
    number_of_y0_when_z0 = len(iwy0 & iwz0)
    number_of_y1_when_z0 = len(iwy1 & iwz0)

    #   checking X and Y independencies

    if number_of_x0_when_y1 != 0 and number_of_x0_when_y0 != 0:
        if number_of_x1_when_y1 / number_of_x0_when_y1 != number_of_x1_when_y0 / number_of_x0_when_y0:
            depd['x & y'] = 'are DEPENDED'
    elif number_of_x1_when_y1 != 0 and number_of_x1_when_y0 != 0:
        if number_of_x0_when_y1 / number_of_x1_when_y1 != number_of_x0_when_y0 / number_of_x1_when_y0:
            depd['x & y'] = 'are DEPENDED'
    elif number_of_x1_when_y0 != 0 and number_of_x0_when_y0 != 0:
        if number_of_x1_when_y1 / number_of_x1_when_y0 != number_of_x0_when_y1 / number_of_x0_when_y0:
            depd['x & y'] = 'are DEPENDED'
    elif number_of_x1_when_y1 != 0 and number_of_x0_when_y1 != 0:
        if number_of_x1_when_y0 / number_of_x1_when_y1 != number_of_x0_when_y0 / number_of_x0_when_y1:
            depd['x & y'] = 'are DEPENDED'
    elif len(iwx0) != len(iwx1) and len(iwy0) != len(iwy1):  # not sure
        depd['x & y'] = 'are DEPENDED'  # not sure
    else:
        print('беда')

    #   checking X and Z independencies

    if number_of_x0_when_z1 != 0 and number_of_x0_when_z0 != 0:
        if number_of_x1_when_z1 / number_of_x0_when_z1 != number_of_x1_when_z0 / number_of_x0_when_z0:
            depd['x & z'] = 'are DEPENDED'
    elif number_of_x1_when_z1 != 0 and number_of_x1_when_z0 != 0:
        if number_of_x0_when_z1 / number_of_x1_when_z1 != number_of_x0_when_z0 / number_of_x1_when_z0:
            depd['x & z'] = 'are DEPENDED'
    elif number_of_x1_when_z0 != 0 and number_of_x0_when_z0 != 0:
        if number_of_x1_when_z1 / number_of_x1_when_z0 != number_of_x0_when_z1 / number_of_x0_when_z0:
            depd['x & z'] = 'are DEPENDED'
    elif number_of_x1_when_z1 != 0 and number_of_x0_when_z1 != 0:
        if number_of_x1_when_z0 / number_of_x1_when_z1 != number_of_x0_when_z0 / number_of_x0_when_z1:
            depd['x & z'] = 'are DEPENDED'
    elif len(iwx0) != len(iwx1) and len(iwz0) != len(iwz1):  # not sure
        depd['x & z'] = 'are DEPENDED'  # not sure
    else:
        print('беда')

    #   checking Y and Z independencies

    if number_of_y0_when_z1 != 0 and number_of_y0_when_z0 != 0:
        if number_of_y1_when_z1 / number_of_y0_when_z1 != number_of_y1_when_z0 / number_of_y0_when_z0:
            depd['y & z'] = 'are DEPENDED'
    elif number_of_y1_when_z1 != 0 and number_of_y1_when_z0 != 0:
        if number_of_y0_when_z1 / number_of_y1_when_z1 != number_of_y0_when_z0 / number_of_y1_when_z0:
            depd['y & z'] = 'are DEPENDED'
    elif number_of_y1_when_z0 != 0 and number_of_y0_when_z0 != 0:
        if number_of_y1_when_z1 / number_of_y1_when_z0 != number_of_y0_when_z1 / number_of_y0_when_z0:
            depd['y & z'] = 'are DEPENDED'
    elif number_of_y1_when_z1 != 0 and number_of_y0_when_z1 != 0:
        if number_of_y1_when_z0 / number_of_y1_when_z1 != number_of_y0_when_z0 / number_of_y0_when_z1:
            depd['y & z'] = 'are DEPENDED'
    elif len(iwy0) != len(iwy1) and len(iwz0) != len(iwz1):  # not sure
        depd['y & z'] = 'are DEPENDED'  # not sure
    else:
        print('беда')
    return [depd["x & y"], depd["x & z"], depd["y & z"]]


# def reshuffle(dictionary: dict):
#     new_dict = dictionary.copy()
#     keys = list(dictionary.keys())
#     for key in keys:
#         shuffle_coloumns(new_dict[key])
#     return new_dict

def reshuffle(lst):
    new_list = lst.copy()
    return [[x[0], shuffle_coloumns(x[1])] for x in new_list]


def reshuffleold(dictionary: dict):
    new_dict = dictionary.copy()
    keys = list(dictionary.keys())
    for key in keys:
        shuffle_coloumns(new_dict[key])
    return new_dict


def shuffle_coloumns(dictionary: dict):
    """influence on dictionary(tabs) and shuffle coloumn(strings)
       returns the shuffled dictionary"""

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
    if freqxy == 0:
        freqxy = 1 / 2
    if freqxz == 0:
        freqxz = 1 / 2
    if freqyz == 0:
        freqyz = 1 / 2

    return [freqxy, freqxz, freqyz]


def check_frequencies(dictionary: dict, t=(1, 1, 1)):  # [P(x=1), P(y=1), P(z=1)]
    """shows how often "1" occurs
       returns triplet(list) of frquencies
       """
    length = 16
    freqx = 0
    freqy = 0
    freqz = 0
    for i in dictionary['x']:
        if i == 1:
            freqx += 1
    for i in dictionary['y']:
        if i == 1:
            freqy += 1
    for i in dictionary['z']:
        if i == 1:
            freqz += 1

    return [freqx / length, freqy / length, freqz / length]


def intervente(key: str, dictionary: dict, name='y', fixed=1):
    """does an intervention in variable "name" and equal it to "fixed"
       reutrns the copy of new dictionary with new distribution
       """

    interv_dict = dictionary.copy()

    length = 16
    st = ['x', 'y', 'z']
    st.remove(name)  # to have a deal with other 2 variables

    indexes_where_name_is_0 = [i for i, x in enumerate(dictionary[name]) if x == 0]  # indexes where Y = 0
    indexes_where_name_is_1 = [i for i, x in enumerate(dictionary[name]) if x == 1]  # indexes where Y = 1

    x_when_name = [dictionary[st[0]][i] for i in indexes_where_name_is_1]  # Xs where y=1
    x_when_not_name = [dictionary[st[0]][i] for i in indexes_where_name_is_0]  # Xs where y=0
    z_when_name = [dictionary[st[1]][i] for i in indexes_where_name_is_1]  # Zs where y=1
    z_when_not_name = [dictionary[st[1]][i] for i in indexes_where_name_is_0]  # Zs where y=0

    freq_z_when_name = len([i for i in z_when_name if i == 1]) / len(z_when_name)  # freq z if y = 1
    freq_z_when_not_name = len([i for i in z_when_not_name if i == 1]) / len(z_when_not_name)  # freq z if y = 0
    freq_x_when_name = len([i for i in x_when_name if i == 1]) / len(x_when_name)  # freq x if y = 1
    freq_x_when_not_name = len([i for i in x_when_not_name if i == 1]) / len(x_when_not_name)  # freq x if y = 0

    freq_z_when_y = len(set([i for i, x in enumerate(dictionary[st[0]]) if x == 1]) & set(
        [i for i, x in enumerate(dictionary[st[1]]) if x == 1])) / len(
        [i for i, x in enumerate(dictionary[st[0]]) if x == 1])
    freq_z_when_not_y = len(set([i for i, x in enumerate(dictionary[st[0]]) if x == 1]) & set(
        [i for i, x in enumerate(dictionary[st[1]]) if x == 0])) / len(
        [i for i, x in enumerate(dictionary[st[0]]) if x == 0])

    freq_x_when_y = len(set([i for i, x in enumerate(dictionary[st[1]]) if x == 1]) & set(
        [i for i, x in enumerate(dictionary[st[0]]) if x == 1])) / len(
        [i for i, x in enumerate(dictionary[st[1]]) if x == 1])
    freq_x_when_not_y = len(set([i for i, x in enumerate(dictionary[st[1]]) if x == 1]) & set(
        [i for i, x in enumerate(dictionary[st[0]]) if x == 0])) / len(
        [i for i, x in enumerate(dictionary[st[1]]) if x == 0])

    interv_dict[name] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # fill Y with fixed value

    ###----- Y BLOCK -----###

    if name == 'y':
        if key == 'twolinks':
            if fixed == 1:
                z = [1 if i < round(freq_z_when_name * length) else 0 for i in range(length)]
                x = [1 if i < round(check_frequencies(dictionary)[0] * freq_z_when_name * length) else 0 for i in
                     range(round(freq_z_when_name * length))]
                x += [1 if i < round(check_frequencies(dictionary)[0] * round(length * (1 - freq_z_when_name))) else 0
                      for i in
                      range(round(length * (1 - freq_z_when_name)))]
            else:
                z = [1 if i < round(freq_z_when_not_name * length) else 0 for i in range(length)]
                x = [1 if i < round(check_frequencies(dictionary)[0] * freq_z_when_not_name * length) else 0 for i in
                     range(round(freq_z_when_not_name * length))]
                x += [
                    1 if i < round(check_frequencies(dictionary)[0] * round(length * (1 - freq_z_when_not_name))) else 0
                    for i in
                    range(round(length * (1 - freq_z_when_not_name)))]
            interv_dict[st[1]] = z
            interv_dict[st[0]] = x
            return interv_dict

        elif key == 'threelinks':
            if fixed == 1:
                x = [1 if i < round(check_frequencies(dictionary)[0] * length) else 0 for i in range(length)]
                z = [1 if i < round(check_frequencies(dictionary)[0] * length) else 0 for i in range(length)]
            else:
                x = [1 if i < round(check_frequencies(dictionary)[0] * length) else 0 for i in range(length)]
                z = [0] * length
            interv_dict[st[1]] = z
            interv_dict[st[0]] = x
            return interv_dict
        # elif key == 'threelinks':
        #    if fixed == 1:
        #        x = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
        #        z = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
        #    else:
        #        x = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
        #        z = [0] * length

        elif key == 'fork':
            if fixed == 1:
                x = [1 if i < round(freq_x_when_name * length) else 0 for i in
                     range(length)]
                z = [1 if i < round(freq_z_when_name * freq_x_when_name * length) else 0 for i in
                     range(round(freq_x_when_name * length))]
                z += [1 if i < round(freq_z_when_name * round(length * (1 - freq_x_when_name))) else 0 for i in
                      range(round(length * (1 - freq_x_when_name)))]
            else:
                x = [1 if i < round(freq_x_when_not_name * length) else 0 for i in
                     range(length)]
                z = [1 if i < round(freq_z_when_not_name * freq_x_when_not_name * length) else 0 for i in
                     range(round(freq_x_when_not_name * length))]
                z += [1 if i < round(freq_z_when_not_name * round(length * (1 - freq_x_when_not_name))) else 0 for i in
                      range(round(length * (1 - freq_x_when_not_name)))]
            interv_dict[st[1]] = z
            interv_dict[st[0]] = x
            return interv_dict

        else:
            x = [1 if i < round(check_frequencies(dictionary)[0] * length) else 0 for i in range(length)]
            z = [1 if i < round(check_frequencies(dictionary)[2] * length // 2) else 0 for i in range(length // 2)] * 2
            interv_dict[st[1]] = z
            interv_dict[st[0]] = x
            return interv_dict

    ###----- X BLOCK -----###

    if name == 'x':
        if key == 'twolinks':
            if fixed == 1:
                x = [1 if i < round(freq_x_when_name * length) else 0 for i in range(length)]
                z = [1 if i < round(freq_z_when_y * freq_x_when_name * length) else 0 for i in
                     range(round(freq_x_when_name * length))]

                z += [1 if i < round((1 - freq_x_when_name) * freq_z_when_y * length - 1) else 0 for i in
                      # 1 is a crunch :(
                      range(length - round(freq_x_when_name * length))]

                interv_dict[st[1]] = z
                interv_dict[st[0]] = x
                return interv_dict

            else:
                print("Don't use zero!! PLS!")
                pass

        elif key == 'threelinks':  # NEED TO CHECK...
            if fixed == 1:
                x = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
                z = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
            else:
                x = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
                z = [0] * length

        elif key == 'fork':
            x = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
            z = dictionary[st[1]].copy()

        elif key == "nolinks":
            x = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
            z = [1 if i < round(check_frequencies(dictionary)[2] * length // 2) else 0 for i in range(length // 2)] * 2

        elif key == "onelink":
            if fixed == 1:
                x = [1 if i < round(freq_x_when_name * length) else 0 for i in range(length)]
                z = [1 if i < round(check_frequencies(dictionary)[2] * freq_x_when_name * length) else 0 for i in
                     range(round(freq_x_when_name * length))]
                z += [1 if i < round(check_frequencies(dictionary)[2] * round(length * (1 - freq_x_when_name))) else 0
                      for i in range(round(length * (1 - freq_x_when_name)))]
            else:
                x = [1 if i < round(freq_x_when_not_name * length) else 0 for i in range(length)]
                z = [1 if i < round(check_frequencies(dictionary)[2] * freq_x_when_not_name * length) else 0 for i in
                     range(round(freq_x_when_not_name * length))]
                z += [
                    1 if i < round(check_frequencies(dictionary)[2] * round(length * (1 - freq_x_when_not_name))) else 0
                    for i in range(round(length * (1 - freq_x_when_not_name)))]

            interv_dict[st[1]] = z
            interv_dict[st[0]] = x
            return interv_dict

        elif key == "collider1":
            if fixed == 1:
                z = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
                x = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
            else:
                print('doenst work!')
                z = [1 if i < round(check_frequencies(dictionary)[2] * length) else 0 for i in range(length)]
                x = [0] * length

            interv_dict[st[1]] = z
            interv_dict[st[0]] = x
            return interv_dict

    ###----- Z BLOCK -----###

    if name == 'z':
        if key == 'collider1':
            x = [1 if i < round(check_frequencies(dictionary)[0] * length) else 0 for i in range(length)]
            if fixed == 1:
                z = [1 if i < round(check_frequencies(dictionary)[0] * length) else 0 for i in range(length)]
            else:
                z = [0] * length

        if key == "nolinks":
            x = [1 if i < round(check_frequencies(dictionary)[0] * length) else 0 for i in range(length)]
            z = [1 if i < round(check_frequencies(dictionary)[1] * length // 2) else 0 for i in range(length // 2)] * 2

        if key == "onelink" or key == "twolinks":
            x = dictionary[st[0]].copy()
            z = dictionary[st[1]].copy()

        if key == 'fork' or key == "threelinks":  # NEED TO CHECK threelinks
            z = [1 if i < round(check_frequencies(dictionary)[1] * length) else 0 for i in range(length)]
            x = dictionary[st[0]].copy()

    # interv_dict[st[1]] = z
    # interv_dict[st[0]] = x

    return interv_dict


def revstring(string: str):
    temp = "%s" % string
    return temp[::-1]


def tancold(lst: list):
    temp = list()

    if lst == [{'data': {'counter': 0, 'id': 'X', 'name': 'X'}, 'style': {'background-color': '#c3cec0'}},
               {'data': {'counter': 0, 'id': 'Y', 'name': 'Y'}, 'style': {'background-color': '#c3cec0'}},
               {'data': {'counter': 0, 'id': 'Z', 'name': 'Z'}, 'style': {'background-color': '#c3cec0'}}]:
        return True  # That's for the case when there are no edges :(

    for dictionary in lst:
        if dictionary['counter'] == 1:
            temp.append(dictionary['source'] + dictionary['target'])

    for tpl in temp:
        if revstring(tpl) in temp:
            return False

    if (('XY' in temp) and ('YZ' in temp) and ('ZX' in temp)) or (('YX' in temp) and ('XZ' in temp) and ('ZY' in temp)):
        return False

    return True


def tanc(lst: str):
    lst = ast.literal_eval(lst)
    temp = list()

    if (lst == [{"counter": 0, "weight": 0, "id": "XY", "source": "X", "target": "Y", "label": ""},
                {"counter": 0, "weight": 0, "id": "YX", "source": "Y", "target": "X", "label": ""},
                {"counter": 0, "weight": 0, "id": "YZ", "source": "Y", "target": "Z", "label": ""},
                {"counter": 0, "weight": 0, "id": "XZ", "source": "X", "target": "Z", "label": ""},
                {"counter": 0, "weight": 0, "id": "ZY", "source": "Z", "target": "Y", "label": ""},
                {"counter": 0, "weight": 0, "id": "ZX", "source": "Z", "target": "X", "label": ""}]) or \
            (lst == [{'data': {'counter': 0, 'id': 'X', 'name': 'X'}, 'style': {'background-color': '#c3cec0'}},
                     {'data': {'counter': 0, 'id': 'Y', 'name': 'Y'}, 'style': {'background-color': '#c3cec0'}},
                     {'data': {'counter': 0, 'id': 'Z', 'name': 'Z'}, 'style': {'background-color': '#c3cec0'}}]):
        return True  # That's for the case when there are no edges :(

    for dictionary in lst:
        if dictionary['counter'] == 1:
            temp.append(dictionary['source'] + dictionary['target'])

    for tpl in temp:
        if revstring(tpl) in temp:
            return False

    if (('XY' in temp) and ('YZ' in temp) and ('ZX' in temp)) or (('YX' in temp) and ('XZ' in temp) and ('ZY' in temp)):
        return False

    return True


def supercrunchfunc(l1: list):
    for unit in l1:
        print(smartdatainterv(unit[0], unit[1]))
        # unit = smartdatainterv(unit[0], unit[1])


def smartdatainterv(d: dict, seed=0):
    """seed 1:  X Y Z   ->   X Z Y
       seed 2:  X Y Z   ->   Y X Z
       seed 3:  X Y Z   ->   Y Z X
       seed 4:  X Y Z   ->   Z X Y
       seed 5:  X Y Z   ->   Z Y X
    """

    tempd = copy.deepcopy(d)

    if seed == 0:
        return tempd
    if seed == 1:
        tempd['y'], tempd['z'] = d['z'], d['y']
    if seed == 2:
        tempd['x'], tempd['y'] = d['y'], d['x']
    if seed == 3:
        tempd['x'], tempd['y'], tempd['z'] = d['y'], d['z'], d['x']
    if seed == 4:
        tempd['x'], tempd['y'], tempd['z'] = d['z'], d['x'], d['y']
    if seed == 5:
        tempd['x'], tempd['z'] = d['z'], d['x']
    return tempd


def smartedgesinterv(l: list, seed):
    """seed 1:  X Y Z   ->   X Z Y
       seed 2:  X Y Z   ->   Y X Z
       seed 3:  X Y Z   ->   Y Z X
       seed 4:  X Y Z   ->   Z X Y
       seed 5:  X Y Z   ->   Z Y X
    """
    templ = copy.deepcopy(l)

    if seed == 0 or l == [False]:
        return templ

    if seed == 1:
        for d in templ:
            d['data']['id'] = d['data']['id'].replace("Y", "z").replace("Z", "y").upper()
            d['data']['source'] = d['data']['source'].replace("Y", "z").replace("Z", "y").upper()
            d['data']['target'] = d['data']['target'].replace("Y", "z").replace("Z", "y").upper()

    if seed == 2:
        for d in templ:
            d['data']['id'] = d['data']['id'].replace("Y", "x").replace("X", "y").upper()
            d['data']['source'] = d['data']['source'].replace("Y", "x").replace("X", "y").upper()
            d['data']['target'] = d['data']['target'].replace("Y", "x").replace("X", "y").upper()

    if seed == 4:
        for d in templ:
            d['data']['id'] = d['data']['id'].replace("X", "y").replace("Y", "z").replace("Z", "x").upper()
            d['data']['source'] = d['data']['source'].replace("X", "y").replace("Y", "z").replace("Z", "x").upper()
            d['data']['target'] = d['data']['target'].replace("X", "y").replace("Y", "z").replace("Z", "x").upper()

    if seed == 3:
        for d in templ:
            d['data']['id'] = d['data']['id'].replace("X", "z").replace("Y", "x").replace("Z", "y").upper()
            d['data']['source'] = d['data']['source'].replace("X", "z").replace("Y", "x").replace("Z", "y").upper()
            d['data']['target'] = d['data']['target'].replace("X", "z").replace("Y", "x").replace("Z", "y").upper()

    if seed == 5:
        for d in templ:
            d['data']['id'] = d['data']['id'].replace("Z", "x").replace("X", "z").upper()
            d['data']['source'] = d['data']['source'].replace("Z", "x").replace("X", "z").upper()
            d['data']['target'] = d['data']['target'].replace("Z", "x").replace("X", "z").upper()
    return templ


def minifunc(number):  # where Y will be.      Optional!
    if number == 1 or number == 4:
        return "Z"
    if number == 0 or number == 5:
        return "Y"
    if number == 2 or number == 3:
        return "X"


def userschoice(lst: str):  # lst is a user's form
    lst = ast.literal_eval(lst)
    temp = list()

    if lst == [{'data': {'counter': 0, 'id': 'X', 'name': 'X'}, 'style': {'background-color': '#c3cec0'}},
               {'data': {'counter': 0, 'id': 'Y', 'name': 'Y'}, 'style': {'background-color': '#c3cec0'}},
               {'data': {'counter': 0, 'id': 'Z', 'name': 'Z'}, 'style': {'background-color': '#c3cec0'}}]:
        return []  # That's for the case when there are no edges :(

    for dictionary in lst:
        if dictionary['counter'] == 1:
            temp.append(dictionary['source'] + dictionary['target'])

    return temp


def wherey(seed: int):
    if seed in [1, 4]:
        return "Z"
    if seed in [0, 5]:
        return "Y"
    if seed in [2, 3]:
        return "X"


def wherex(seed: int):
    if seed in [3, 5]:
        return "Z"
    if seed in [0, 1]:
        return "X"
    if seed in [2, 4]:
        return "Y"


def dgpchoice(lst: list):  # lst is an original form
    temp = list()

    if lst == [False]:
        return []  # That's for the case when there are no edges :(        (nolinks)

    for dictionary in lst:
        temp.append(dictionary['data']['source'] + dictionary['data']['target'])

    return temp


def fine(user: list, dgp: list):
    penalty = 0

    for str in user:
        if str not in dgp:
            if revstring(str) not in dgp:  # user set an edge which is not in original data
                penalty += 3.25
            else:  # user set an edge with wrong direction
                penalty += 1

    for str in dgp:
        if str not in user:
            if revstring(str) not in user:  # user missed an edge
                penalty += 2
            # else user has confounded a direction, but we have already counted this case

    return penalty


def accuracy(num):
    # accuracy is from 0 to 1
    return (10 - num) * 0.1


def directional_error(user: list, dgp: list):
    count = 0

    for str in user:
        if str not in dgp:
            if revstring(str) in dgp:  # user set an edge which is not in original data
                count += 1

    return count


def structure_error(user: list, dgp: list):
    count = 0

    for str in user:
        if str not in dgp:
            if revstring(str) not in dgp:  # user set an edge which is not in original data
                count += 1

    for str in dgp:
        if str not in user:
            if revstring(str) not in user:  # user missed an edge
                count += 1

    return count


###----- TESTS -----###


'''
print(d['onelink'], "- onelink")
print(check_frequencies(d['onelink']), "- frequencies")

print(intervente('onelink', d['onelink'], "x"), "- orange distribution (X fixed)")
print(check_frequencies(intervente('onelink', d['onelink'], "x")), "- frequencies again")
print(intervente('onelink', d['onelink'], "y"), "- orange distribution (Y fixed)")
print(check_frequencies(intervente('onelink', d['onelink'], "y")), "- frequencies again")
print(intervente('onelink', d['onelink'], "z"), "- orange distribution (Z fixed)")
print(check_frequencies(intervente('onelink', d['onelink'], "z")), "- frequencies again")



print()
print()

print(d['nolinks'], "- nolinks")
print(check_frequencies(d['nolinks']), "- frequencies")

print(intervente('nolinks', d['nolinks'], "x"), "- orange distribution (X fixed)")
print(check_frequencies(intervente('nolinks', d['onelink'], "x")), "- frequencies again")
print(intervente('nolinks', d['nolinks'], "y"), "- orange distribution (Y fixed)")
print(check_frequencies(intervente('nolinks', d['nolinks'], "y")), "- frequencies again")
print(intervente('nolinks', d['nolinks'], "z"), "- orange distribution (Z fixed)")
print(check_frequencies(intervente('nolinks', d['nolinks'], "z")), "- frequencies again")

print()
print()


print(d['twolinks'], "- twolinks")
print(check_frequencies(d['twolinks']), "- frequencies")

# print(intervente('twolinks', d['twolinks'], "x"), "- orange distribution (X fixed)")
# print(check_frequencies(intervente('twolinks', d['twolinks'], "x")), "- frequencies again")
print(intervente('twolinks', d['twolinks'], "y"), "- orange distribution (Y fixed)")
print(check_frequencies(intervente('twolinks', d['twolinks'], "y")), "- frequencies again")
# print(intervente('twolinks', d['twolinks'], "z"), "- orange distribution (Z fixed)")
# print(check_frequencies(intervente('twolinks', d['twolinks'], "z")), "- frequencies again")

print()
print()


print(d['collider1'], "- collider")
print(check_frequencies(d['collider1']), "- frequencies")

print(intervente('collider1', d['collider1'], "x"), "- orange distribution (X fixed)")
print(check_frequencies(intervente('collider1', d['collider1'], "x")), "- frequencies again")
print(intervente('collider1', d['collider1'], "y"), "- orange distribution (Y fixed)")
print(check_frequencies(intervente('collider1', d['collider1'], "y")), "- frequencies again")

# print(intervente('collider', d['collider1'], "z"), "- orange distribution (Z fixed)")
# print(check_frequencies(intervente('collider', d['collider1'], "z")), "- frequencies again")

print()
print()

print(d['fork'], "- fork")
print(check_frequencies(d['fork']), "- frequencies")

# print(intervente('fork', d['fork'], "x"), "- orange distribution (X fixed)")
# print(check_frequencies(intervente('fork', d['fork'], "x")), "- frequencies again")
print(intervente('fork', d['fork'], "y"), "- orange distribution (Y fixed)")
print(check_frequencies(intervente('fork', d['fork'], "y")), "- frequencies again")
# print(intervente('fork', d['fork'], "z"), "- orange distribution (Z fixed)")
# print(check_frequencies(intervente('fork', d['fork'], "z")), "- frequencies again")


print()
print()

print(d['threelinks'], "- threelinks")
print(check_frequencies(d['threelinks']), "- frequencies")

print(intervente('threelinks', d['threelinks']), "- orange distribution (Y fixed)")
print(check_frequencies(intervente('threelinks', d['threelinks'])), "- frequencies again")
# print(intervente('threelinks', d['threelinks'], "y"), "- orange distribution (Y fixed)")
# print(check_frequencies(intervente('threelinks', d['threelinks'], "y")), "- frequencies again")
# print(intervente('threelinks', d['threelinks'], "z"), "- orange distribution (Z fixed)")
# print(check_frequencies(intervente('threelinks', d['threelinks'], "z")), "- frequencies again")
'''
