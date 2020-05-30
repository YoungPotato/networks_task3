import argparse
from vk_inf import Information


def main():
    parser = argparse.ArgumentParser(description='Программа, которая выводит '
                                                 'информация в удобном '
                                                 'виде из ВК')
    parser.add_argument('-m', help='Названия методов, котрые нужны выполнять')
    parser.add_argument('-id', help='ID пользователя, о котором '
                                    'хотите получить информацию')
    args = parser.parse_args()
    inf = Information(args.id, args.m)
    inf.run()


if __name__ == '__main__':
    main()
