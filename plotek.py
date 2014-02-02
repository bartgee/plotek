#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pLotek 2.0 beta
# author: Bart Grzybicki <bgrzybicki@gmail.com>
#
# CHANGELOG moved to external file

import random, os, platform, sys, csv
#from array import array

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

#class draw:

    #def __init__(self):


def readdbfile(filename):
    ''' Reads the CSV file with space as a delimiter
    '''
    global drawedbefore
    with open(filename, newline = '\n', encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        input('nadus enter!')

        data = [tuple(row) for row in reader]
        index = 0
        for i in data:
            #drawed = print('liczby: ' + data[index][2])
            drawed = data[index][2]
            day = data[index][1]
            if index < len(data)-1:
                index = index + 1
            #print(data)
            #return

            #print('z funkcji readdbfile: nums_all: ' + nums_all + '; losowania historyczne: ' + data[index][2])
            if nums_all == drawed:
                print('wylosowano juz wygrany zestaw!: ')
                print('z funkcji readdbfile: wybrałeś: ' + nums_all + '; losowania historyczne: ' + drawed + ' z dnia '+ day )
                return
            #else:
                #print('wylosowano nowy zestaw')


def geturl(url):
    ''' Gets the URL and saves it to file.

    Full URL must be given as an argument.
    '''
    f = open(filename, 'w')
    for line in urlopen(url):
        line = line.decode('utf-8')
        f.write(line)
    f.close()


def dbdownload(gamealias):
    ''' Downloads LOTTO database in text format from mbnet.com.pl

    The argument is gamealias:
    - dl: for Lotto
    - ml: for Mini Lotto
    - mm: for Multi Multi
    '''
    if gamealias == 'dl':
        gamename = 'Lotto'
    elif gamealias == 'ml':
        gamename = 'Mini Lotto'
    else:
        gamename =  'Multi Multi'
    filename = gamealiases[gamealias]
    try:
        print('Pobieranie bazy losowań LOTTO...')
        url = ('http://www.mbnet.com.pl/' + filename)
        geturl(url)
        print('Pobrano bazę losowań ' + gamename + ' :).')
    except:
        print('Błąd pobierania bazy losowań ' + gamename + '!')


def alldbdownload():
    ''' Download all LOTTO databases
    '''
    global gamealiases
    global gamealias
    global filename
    gamealiases = {'dl': 'dl_razem.txt', 'ml': 'el.txt', 'mm': 'ml.txt'}
    for gamealias, filename in gamealiases.items():
        dbdownload(gamealias)
    continuegame = input('Wciśnij ENTER: ')
    return


def clearscreen():
    ''' Clears the screen.

    usage: clearscreen()
    '''
    os_platform = platform.system()
    if os_platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def printheader():
    ''' Prints the app header
    '''
    print('*******************************')
    print('* pLotek 2.0 BETA! by bartgee *')
    print('*******************************')
    print('u - aktualizacja baz losowań')
    print('1. Lotto')
    print('2. Mini Lotto')
    print('3. Multi Multi')
    print('-------------------------------')


def gameselect():
    ''' returns a game name, numbers to draw and number of draws selected by user
    '''
    global gametype
    global nums_to_draw
    global number_of_draws
    running = True
    while running:
        try:
            gametype = input('Wybierz grę LOTTO (1,2,3 lub ENTER dla LOTTO): ')
            if gametype == 'u':
                running = False
                return gametype
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
    if gametype == 'u':
        return
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
            print('-------------------------------')
        except:
                print('Wprowadzono błędne dane!')
    return gametype, nums_to_draw, number_of_draws


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
    global nums_all
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
    return nums_all

def restartgame():
    restart = ''
    restart = input('Nowe losowanie? UWAGA - wyniki ostatniego losowania zostaną utracone! (t/n): ')
    if restart == 't' or restart == '':
        main()
    else:
        sys.exit(0)


def draworupdate():
    ''' Checks whether the user chose to update drawing databases
    '''
    if gametype == 'u':
        clearscreen()
        alldbdownload()
        main()
#    else:
#        drawnumbers(gametype, nums_to_draw, number_of_draws)
#        readdbfile('dl_razem.txt')
#        restartgame()


def main():
    clearscreen()
    printheader()
    # code for parsing csv files
    #readdbfile('dl_razem.txt')
    #sys.exit()
    # /code for parsing csv files
    gameselect()
    draworupdate()
    drawnumbers(gametype, nums_to_draw, number_of_draws)
    global nums_all
    nums_all = input('losuj sam 6 z 49 podaj typie!: ')
    readdbfile('dl_razem.txt')
    restartgame()

if __name__ == '__main__':
    main()
