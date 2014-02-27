#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pLotek 2.1 beta
# author: Bart Grzybicki <bgrzybicki@gmail.com>
#
# CHANGELOG moved to external file

import random, os, platform, sys, csv
# importing local modules:
import combinations

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def chances():
    ''' How many combinations are there?
    '''
    cb = combinations.combinations(49,6)
    cb = str(cb)
    print('Ilość kombinacji w Lotto: ' + combinations.splitthousands(cb,'.'))
    cb = combinations.combinations(42,5)
    cb = str(cb)
    print('Ilość kombinacji w Mini Lotto: ' + combinations.splitthousands(cb,'.'))
    cb = int(combinations.combinations(80,10) / combinations.combinations(20,10))
    cb = str(cb)
    print('Ilość kombinacji w Multi Multi: ' + combinations.splitthousands(cb,'.'))
    input('Wciśnij ENTER: ')
    running2 = True
    while running2:
        try:
            clearscreen()
            print('Obliczanie prawdopodobieństwa wygranej.')
            print('1. Lotto')
            print('2. Mini Lotto')
            print('3. Multi Multi')
            game = input('Wybierz grę: ')
            if game != '' and int(game) in range(1,4):
                game = int(game)
                if game == 1: # Lotto
                    gamename = 'Lotto'
                    nums = 49
                    start = 3
                    stop = 7
                    numsdrawed = 6
                    running2 = False
                if game == 2: # Mini Lotto
                    gamename = 'Mini Lotto'
                    nums = 42
                    start = 3
                    stop = 6
                    numsdrawed = 5
                    running2 = False
                if game == 3: # Multi Multi
                    gamename = 'Multi Multi'
                    nums = 80
                    running2 = False
                    numsdrawed = input('Podaj ilość typowanych liczb: ')
                    numsdrawed = int(numsdrawed)
                    if numsdrawed >= 5 and numsdrawed <= 7:
                        start = 3
                    elif numsdrawed >= 2 and numsdrawed <= 4:
                        start = 2
                    elif numsdrawed == 1:
                        start = 1
                    else:
                        start = 4
                    stop = numsdrawed + 1
                    machinedrawed = 20
            if game != 3:
                machinedrawed = numsdrawed
        except:
            print('Wprowadzono błędne dane!')
    clearscreen()
    print('Prawdopodobieństwo trafienia w '+ gamename)
    print('Typowano ' + str(numsdrawed) + ' z ' +str(nums))
    print('-------------------------------')
    running = True
    numsmatched = numsdrawed
    while running:
        try:
            if numsdrawed is not None and numsdrawed in range(start, stop):
                cb = combinations.matched(nums,numsdrawed,numsmatched,machinedrawed)
                cb = str(cb)
                print('Trafiono ' + str(numsmatched) + ': ' + '1:' + combinations.splitthousands(cb,'.'))
                numsmatched = numsmatched - 1
                if numsmatched == start - 1:
                    running = False
        except:
            print('Wprowadzono błędne dane!')
    input('Wciśnij ENTER: ')
    return


def comparedbfile(filename):
    ''' Reads the CSV file with space as a delimiter
        and then compares actual draw with historical draws database.
        It also prints matches and counts them.
    '''
    global nums_list, database, matchcount, dbrowcount, dayzero, daylast
    data = []
    database = []
    #matchcount = 0
    with open(filename, newline = '\n', encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        data = [tuple(row) for row in reader]
        index = 0
        for i in data:
            database = data[index][2]
            day = data[index][1]
            dayzero = data[0][1]
            dbrowcount = len(data)
            if index < len(data)-1:
                index = index + 1
                daylast = data[index][1]
            database = database.split(',')
            list(database)
            database = [int(item) for item in database]
            common_nums = []
            common_nums = frozenset(nums_list).intersection(database) # compare drawed numbers with database
            common_nums = list(common_nums)
            common_nums.sort()
            match = len(common_nums) == len(nums_list)
            if match == True:
                matchcount = matchcount + 1
                #print('Ilość dopasowań: ' + str(len(common_nums)))
                #if matchcount <= 3:
                    #print('Liczby: ', common_nums)
                    #print('Padły już w ' + game_name + ' w dniu ' + day + ' r.!')
                    #print('Wynik losowania: ' + str(database))
                #input('ENTER')
    return matchcount, dbrowcount, dayzero, daylast


def geturl(url):
    ''' Gets the URL and saves it to file.

    Full URL must be given as an argument.
    '''
    full_path = os.path.realpath(__file__)
    workingdir = os.path.dirname(full_path)
    f = open(workingdir + '/' + filename, 'w')
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
    global gamealiases, gamealias, filename
    gamealiases = {'dl': 'dl_razem.txt', 'ml': 'el.txt', 'mm': 'ml.txt'}
    for gamealias, filename in gamealiases.items():
        dbdownload(gamealias)
    input('Wciśnij ENTER: ')
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
    print('* pLotek 2.1 BETA! by bartgee *')
    print('*******************************')
    print('u - aktualizacja baz losowań')
    print('p - prawdopodobieństwo wygranej')
    print('1. Lotto')
    print('2. Mini Lotto')
    print('3. Multi Multi')
    print('q - wyjście')
    print('-------------------------------')


def gameselect():
    ''' returns a game name, numbers to draw and number of draws selected by user
    '''
    global gametype, nums_to_draw, number_of_draws, matchcount
    matchcount = 0
    running = True
    while running:
        try:
            gametype = input('Wybierz grę LOTTO (1,2,3 lub ENTER dla LOTTO): ')
            if gametype == 'u':
                running = False
                return gametype
            if gametype == 'p':
                running = False
                return gametype
            if gametype == 'q':
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
    if gametype == 'u' or gametype == 'p' or gametype == 'q':
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
            #print('-------------------------------')
        except:
                print('Wprowadzono błędne dane!')
    return gametype, nums_to_draw, number_of_draws


def drawnumbers(gametype, nums_to_draw, number_of_draws):
    ''' Draws the numbers in chosen Lotto - a Polish lottery games. At the moment
    threee of them - Lotto, Mini Lotto and Multi Multi

    The two values must be integers.
    '''
    global game_name, gamefile, nums_all, nums_list
    num_start = 1
    if gametype == 1:
        game_name = 'Lotto'
        gamefile = 'dl_razem.txt'
        num_end = 49
        nums_to_draw = 6
    if gametype == 2:
        game_name = 'Mini Lotto'
        gamefile = 'el.txt'
        num_end = 42
        nums_to_draw = 5
    if gametype == 3:
        game_name = 'Multi Multi'
        gamefile = 'ml.txt'
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
        print('-------------------------------')
        print('Zakład nr ' + str(draw) + ' dla ' + game_name + ': ' + nums_all)
        #workingdir = os.getcwd()
        full_path = os.path.realpath(__file__)
        workingdir = os.path.dirname(full_path)
        comparedbfile(workingdir + '/' + gamefile)
        printmatches()
    return nums_all, nums_list


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
    elif gametype == 'p':
        clearscreen()
        chances()
        main()
    elif gametype == 'q':
        sys.exit(0)

#    else:
#        drawnumbers(gametype, nums_to_draw, number_of_draws)
#        readdbfile('dl_razem.txt')
#        restartgame()


def comparetest():
    ''' This function is just for manual comparing drawed numbers
        with historical from database
    '''
    global nums_all, nums_list, nums_drawed
    nums_all = input('wygraj sam 6 z 49 - podaj ręcznie: ')
    nums_drawed = nums_all.split(',')
    nums_drawed = [ int(item) for item in nums_drawed ]
    print('po konwersji do int:')
    for item in nums_drawed:
        print(item)
    nums_list = []
    for num in nums_drawed:
        nums_list.append(num)
    nums_list.sort()
    #print('nums_list:', nums_list)
    comparedbfile(gamefile) # we're only using this in the rest of the code!
    #drawnumbers(gametype, nums_to_draw, number_of_draws)
    #comparedbfile('ml.txt')
    #comparedbfile('dl_razem.txt')
    print('koniec fukcji comparedbtest()')
    #sys.exit(0)
    #return nums_list


def printmatches():
    ''' Prints matches if they occured in draws.
    '''
    if matchcount > 1:
        print('Liczby te wylosowano już ' + str(matchcount) + ' razy!')
    elif matchcount == 1:
        print('Liczby te wylosowano już ' + str(matchcount) + ' raz!')
    elif matchcount == 0:
        print('Nigdy nie wylosowano takich liczb!')

def printfooter():
    ''' Prints the footer after drawing
    '''
    print('###############################')
    print('Baza ' + game_name + ' zawiera ' + str(dbrowcount) + ' losowań od dnia ' + str(dayzero) + ' r.')
    print('Ostatnie losowanie w bazie jest z dnia ' + str(daylast) + ' r.')


def main():
    clearscreen()
    printheader()
    gameselect()
    draworupdate()
    drawnumbers(gametype, nums_to_draw, number_of_draws)
    printfooter()
    #printmatches()
    #comparetest()
    restartgame()

if __name__ == '__main__':
    main()
