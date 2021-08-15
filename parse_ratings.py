#!/bin/python
import pandas as pd

my_profile_id="3238633"
my_steam_id="76561198202213716"
def parse_games_file(filename):
    with open(filename, 'r') as f:
        game_list=f.readline().split('{"rating":')

        #clean list
        game_list=game_list[1:]
        #drop comma/ ] from each game
        for i in range(len(game_list)):
            game_list[i] = '"rating":%s'%game_list[i][:-2]
            #print(game_list[i])
            #print(' ')
        return game_list


def get_panda(game_list, nvar, ngames):


    data_list= [['' for _ in range(nvar)] for _ in range(ngames)]
    category_list = ['' for _ in range(nvar)]
    for i in range(ngames):
        gdata=game_list[i]
        gdata= gdata[:-1].split(',')
        gvar=len(gdata)


        #import pdb; pdb.set_trace()
        #on first pass extract list of variables, stripping quotes
        if i==0:
            for k in range(gvar):
                category_list[k] = gdata[k].split(':')[0].strip('"')

        
        for j, dat in enumerate(gdata):
            category, val = dat.split(':')
            data_list[i][j]=val

    df = pd.DataFrame(data=data_list, columns=category_list)

    return df
if __name__ == '__main__':
    game_file=parse_games_file("rating.txt")
    ngames = len(game_file)
    print("games: ", ngames)
    nvar=7 #should be fixed
    df= get_panda(game_file,nvar, ngames)

    df.to_csv("rating_frame.csv")
