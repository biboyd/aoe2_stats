#!/bin/bash


#pull data from site
mv data.txt old.data.txt
mv ratings.txt old.ratings.txt

curl "https://aoe2.net/api/player/matches?game=aoe2de&steam_id=76561198202213716&leaderboard_id=3&count=500" -o data.txt
curl "https://aoe2.net/api/player/ratinghistory?game=aoe2de&steam_id=76561198202213716&leaderboard_id=3&count=500" -o rating.txt
