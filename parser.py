#!/bin/python
import pandas as pd

my_profile_id="3238633"
my_steam_id="76561198202213716"
def parse_games_file(filename):
    with open(filename, 'r') as f:
        game_list=f.readline().split('{"match_id":')

        #clean list
        game_list=game_list[1:]
        #drop comma/ ] from each game
        for i in range(len(game_list)):
            game_list[i] = '"match_id":%s'%game_list[i][:-2]
            #print(game_list[i])
            #print(' ')
        return game_list


def get_panda(game_list, nvar, ngames):


    data_list= [['' for _ in range(nvar)] for _ in range(ngames)]
    category_list = ['' for _ in range(nvar)]
    for i in range(ngames):
        gdata, combined_pdata= game_list[i].split('"players"')

        gdata= gdata[:-1].split(',')
        gvar=len(gdata)
        p1string, p2string = combined_pdata[3:-2].split('},{')
        p1data= p1string.split(",")
        p2data= p2string.split(",")
        pvar=len(p1data)

        #import pdb; pdb.set_trace()
        #on first pass extract list of variables, stripping quotes
        if i==0:
            for k in range(gvar):
                category_list[k] = gdata[k].split(':')[0].strip('"')
            for k in range(pvar):
                new_k = k + gvar
                category_list[new_k]= "my "+p1data[k].split(':')[0].strip('"')
            for k in range(pvar):
                new_k = k + gvar+pvar
                category_list[new_k]= "opponent "+p1data[k].split(':')[0].strip('"')

        p1_id = p1data[0].split(':')[1]
        p2_id = p2data[0].split(':')[1]

        if p1_id == my_profile_id:
            tot_game_data = gdata+p1data+p2data
        elif p2_id == my_profile_id:
            tot_game_data = gdata+p2data+p1data
        else:
            raise RuntimeError(f"Something got messed up, neither {p1_id} or {p2_id}, t equal {my_profile_id}")

        for j, dat in enumerate(tot_game_data):
            category, val = dat.split(':')
            data_list[i][j]=val

    df = pd.DataFrame(data=data_list, columns=category_list)

    return df
if __name__ == '__main__':
    game_file=parse_games_file("data.txt")
    ngames = len(game_file)
    nvar=74 #should be fixed
    df= get_panda(game_file,nvar, ngames)

    df.to_csv("data_frame.csv")
