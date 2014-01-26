#!/usr/bin/env python3
# pLotek 1.0
# -*- coding: utf-8 -*-
# author: Bart Grzybicki <bgrzybicki@gmail.com>
# *** CHANGELOG ***
# 2014.01.26
# - first initial version

import random, os, platform

def drawnumbers(gametype, number_of_draws):
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
                nums_to_draw = 10
        num_range = range(num_start,num_end)
        nums_all = ''
        draw = number_of_draws
        for draw in range(1, draw+1):
                nums_drawed = random.sample(num_range, nums_to_draw)
                for num in nums_drawed:
                        nums_all = nums_all + str(num) + ','

                nums_all = nums_all[:-1]

                print('Zakład nr ' + str(draw) + ' dla ' + game_name + ': ' + nums_all)
                nums_all = ''

def main():
        os_platform = platform.system()
        if os_platform == 'Windows':
                os.system('cls')
        else:
                os.system('clear')

        print('************************')
        print('* LOTTO 1.0 by bartgee *')
        print('************************')
        print('1. Lotto')
        print('2. Mini Lotto')
        print('3. Multi Multi')
        print('------------------------')
        running = True
        while running:
                try:
                        gametype = int(input('Wybierz grę LOTTO (1,2 lub 3): '))
                        if gametype == 1 or gametype == 2 or gametype == 3:
                                running = False
                except:        
                        print('Wprowadzono błędne dane!')
        running = True
        while running:
                try:
                        number_of_draws = int(input('Podaj ilość zakładów (od 1 do 20): '))
                        if number_of_draws in range(1, 21):
                                running = False
                                print('------------------------')
                except:
                        print('Wprowadzono błędne dane!')

        drawnumbers(gametype, number_of_draws)
        restart = input('Nowe losowanie? UWAGA - wyniki ostatniego losowania zostaną utracone! (t/n): ')
        if restart == 't':
                if __name__ == '__main__':
                        main()

if __name__ == '__main__':
        main()
