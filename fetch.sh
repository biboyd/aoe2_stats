#!/bin/bash

#pull data from site
curl "https://aoe2.net/api/player/matches?game=aoe2de&steam_id=76561198202213716&count=500" -o data.txt
