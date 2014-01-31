#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# pLotek 2.0 beta
# author: Bart Grzybicki <bgrzybicki@gmail.com>
# *** CHANGELOG ***
#
#  2014.01.31 - DEVEL VERSIOB 2.0.1 alpha
# - integrated clearsreen() from master branch
# - integrated geturl() from devel branch
#
# 2014.01.31 - ver. 1.2
# - changed to Python2
#
# 2014.01.30 - ver. 1.2 testing
# - code cleanup
#
# 2014.01.27 - DEVEL VERSION 2.0 alpha !!!
# - new functions are in my mind at the moment ;)
# - working on historical LOTTO drawings usage:
#   * download historical drawings data file from the Internet (done)
#   * putting the data into some parse'able file - probably it will be CSV format (under construction)
#   * choosing the ideas of usage (in the near future)
#
# 2014.01.26 - ver. 1.1
# - added Multi Multi drawing options
# - drawed numbers are now stored in a list
# - changed indents to Python standard coding standard (4 chars)
# - added ENTER key as input for default options
#
# 2014.01.26 - ver. 1.0
# - first initial version

import random, os, platform, sys
from urllib import urlopen

reload(sys)
sys.setdefaultencoding('UTF-8')

def clearscreen():
    ''' Clears the screen.

    usage: clearscreen()
    '''
    os_platform = platform.system()
    if os_platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def geturl(url):
    ''' Gets the URL and saves it to file.

    Full URL must be given as an argument.
    '''
    f = open('dl.txt', 'w')
    for line in urlopen(url):
        line = line.decode('utf-8')
        f.write(line)
    f.close()

def drawnumbers(gametype, nums_to_draw, number_of_draws):
    u''' Draws the numbers in chosen Lotto - a Polish lottery games. At the moment
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
    num_range = xrange(num_start,num_end)
    nums_all = ''
    draw = number_of_draws
    for draw in xrange(1, draw+1):
        nums_drawed = random.sample(num_range, nums_to_draw)
        nums_list = []
        for num in nums_drawed:
                nums_list.append(num)

        nums_list.sort()
        nums_all = ''
        for item in nums_list:
                nums_all = str(nums_all) + str(item) + ','

        nums_all = nums_all[:-1]
        print 'Zakład nr ' + str(draw) + ' dla ' + game_name + ': ' + str(nums_all)

def main():

    clearscreen()

    print '*********************************'
    print '* pLotek 2.0.1 BETA! by bartgee *'
    print '*      Python 2 version *'
    print '*********************************'
    print '1. Lotto'
    print '2. Mini Lotto'
    print '3. Multi Multi'
    print '---------------------------------'

    # testing code for lottery historical drawings
    try:
        print('Pobieranie bazy losowań LOTTO...')
        geturl('http://www.mbnet.com.pl/dl.txt')
        print('Pobrano bazę losowań :).')
    except:
        print('Błąd pobierania bazy losowań LOTTO!')
#    sys.exit(0)
    # testing code for lottery historical drawings

    running = True
    while running:
        try:
            gametype = raw_input('Wybierz grę LOTTO (1,2,3 lub ENTER dla LOTTO): ')
            if gametype != '' and int(gametype) in xrange(1,4):
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
                        nums_to_draw = raw_input('Podaj ilość typowanych liczb (1-10 lub ENTER dla 10): ')
                        if nums_to_draw != '' and int(nums_to_draw) in xrange(1,11):
                            nums_to_draw = int(nums_to_draw)
                        if nums_to_draw == '':
                            nums_to_draw = 10
                            print 'Wybrano 10 liczb.'
                            running2 = False
                        elif nums_to_draw in xrange(1,11):
                            running2 = False
                    except:
                        print 'Wprowadzono błędne dane! 1'
                    running = False
        except:
            print 'Wprowadzono błędne dane! 2'
    running = True
    while running:
        try:
            number_of_draws = raw_input('Podaj ilość zakładów (od 1 do 20 lub ENTER dla 1): ')
            if number_of_draws != '' and int(number_of_draws) in xrange(1,21):
                number_of_draws = int(number_of_draws)
            if number_of_draws == '':
                number_of_draws = 1
                print 'Wybrano 1 zakład.'
                running = False
            elif number_of_draws in xrange(1, 21):
                running = False
            print '---------------------------------'
        except:
                print 'Wprowadzono błędne dane!'

    drawnumbers(gametype, nums_to_draw, number_of_draws)

    restart = raw_input('Nowe losowanie? UWAGA - wyniki ostatniego losowania zostaną utracone! (t/n): ')
    if restart == 't' or restart == '':
            if __name__ == '__main__':
                main()

if __name__ == '__main__':
    main()
