#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pLotek 1.1
# author: Bart Grzybicki <bgrzybicki@gmail.com>
#
# *** CHANGELOG ***
#
# 2014.01.31 - ver. 1.2
# - code cleanup
#
# 2014.01.30 - ver. 1.2 testing
# - code cleanup
#
# 2014.01.26 - ver. 1.1
# - added Multi Multi drawing options
# - drawed numbers are now stored in a list
# - changed indents to Python standard coding standard (4 chars)
# - added ENTER key as input for default options
#
# 2014.01.26 - ver. 1.0
# - first initial version

import random, os, platform

def clearscreen():
    ''' Clears the screen.

    usage: clearscreen()
    '''
    os_platform = platform.system()
    if os_platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def drawnumbers(gametype, nums_to_draw, number_of_draws):
    ''' Draws the numbers in chosen Lotto - a Polish lottery games. At the moment
    threee of them - Lotto, Mini Lotto and Multi Multi

    The two values must be integers.
    '''

    num_start = 1
    if gametype == 1:
        game_name = 'Lotto'
        num_end = 49
        nums_to_draw = 6
    if gametype == 2:
        game_name = 'Mini Lotto'
        num_end = 42
        nums_to_draw = 5
    if gametype == 3:
        game_name = 'Multi Multi'
        num_end = 80
    num_range = range(num_start,num_end)
    nums_all = ''
    draw = number_of_draws
    for draw in range(1, draw+1):
        nums_drawed = random.sample(num_range, nums_to_draw)
        nums_list = []
        for num in nums_drawed:
                nums_list.append(num)

        nums_list.sort()
        nums_all = ''
        for item in nums_list:
                nums_all = nums_all + str(item) + ','

        nums_all = nums_all[:-1]
        print('Zakład nr ' + str(draw) + ' dla ' + game_name + ': ' + nums_all)

def main():

    clearscreen()

    print('*************************')
    print('* pLotek 1.2 by bartgee *')
    print('*************************')
    print('1. Lotto')
    print('2. Mini Lotto')
    print('3. Multi Multi')
    print('-------------------------')
    running = True
    while running:
        try:
            gametype = input('Wybierz grę LOTTO (1,2,3 lub ENTER dla LOTTO): ')
            if gametype != '' and int(gametype) in range(1,4):
                gametype = int(gametype)
            if gametype == '':
                gametype = 1
                nums_to_draw = 6
                running = False
            elif gametype == 1 or gametype == 2:
                      nums_to_draw = ''
                      running = False
            elif gametype == 3:
                running = False
                running2 = True
                while running2:
                    try:
                        nums_to_draw = input('Podaj ilość typowanych liczb (1-10 lub ENTER dla 10): ')
                        if nums_to_draw != '' and int(nums_to_draw) in range(1,11):
                            nums_to_draw = int(nums_to_draw)
                        if nums_to_draw == '':
                            nums_to_draw = 10
                            print('Wybrano 10 liczb.')
                            running2 = False
                        elif nums_to_draw in range(1,11):
                            running2 = False
                    except:
                        print('Wprowadzono błędne dane!')
                    running = False
        except:
            print('Wprowadzono błędne dane!')
    running = True
    while running:
        try:
            number_of_draws = input('Podaj ilość zakładów (od 1 do 20 lub ENTER dla 1): ')
            if number_of_draws != '' and int(number_of_draws) in range(1,21):
                number_of_draws = int(number_of_draws)
            if number_of_draws == '':
                number_of_draws = 1
                print('Wybrano 1 zakład.')
                running = False
            elif number_of_draws in range(1, 21):
                running = False
            print('-------------------------')
        except:
                print('Wprowadzono błędne dane!')

    drawnumbers(gametype, nums_to_draw, number_of_draws)

    restart = input('Nowe losowanie? UWAGA - wyniki ostatniego losowania zostaną utracone! (t/n): ')
    if restart == 't' or restart == '':
            if __name__ == '__main__':
                main()

if __name__ == '__main__':
    main()
