import os
from collections import namedtuple
from logg import logger
import argparse

FObj = namedtuple('FObj', ['name', 'ext', 'fold', 'p_name'])


def f_path(my_path):
    if not os.path.exists(my_path):
        logger.warning(msg='Задан не существующий путь')
        return None

    list_ntup = []

    for f_info in os.walk(my_path):
        if f_info[1]:
            for f in f_info[1]:
                new_fo = FObj(f, None, True, f_info[0].replace('\\', '/'))
                list_ntup.append(new_fo)
                logger.info(msg=str(new_fo))

        if f_info[2]:
            for f in f_info[2]:
                name_exp = f.rsplit('.', 1)
                new_fo = FObj(name_exp[0], name_exp[1], False, f_info[0].replace('\\', '/'))
                list_ntup.append(new_fo)
                logger.info(msg=str(new_fo))

    return list_ntup


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('my_path', metavar='p', type=str, nargs='?')
    args = parser.parse_args()
    f_path(args.my_path)



    # for i in f_path('C:/teach/test'):
    #     print(i)