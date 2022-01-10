#!/usr/bin/env python3

import requests
import pandas as pd

def main():

    season_id = '2020-21'
    per_mode = 'Totals'

    nba_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode='+per_mode+'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+season_id+'&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

    headers  = {
     'Connection': 'keep-alive',
     'Accept': 'application/json, text/plain, */*',
     'x-nba-stats-token': 'true',
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
     'x-nba-stats-origin': 'stats',
     'Sec-Fetch-Site': 'same-origin',
     'Sec-Fetch-Mode': 'cors',
     'Referer': 'https://stats.nba.com/',
     'Accept-Encoding': 'gzip, deflate, br',
     'Accept-Language': 'en-US,en;q=0.9',
 }

    response = requests.get(url=nba_info_url, headers=headers).json()

    player_info = response['resultSets'][0]['rowSet']

    columns_list = [
                "PLAYER_ID",
                "PLAYER_NAME",
                "NICKNAME",
                "TEAM_ID",
                "TEAM_ABBREVIATION",
                "AGE",
                "GP",
                "W",
                "L",
                "W_PCT",
                "MIN",
                "FGM",
                "FGA",
                "FG_PCT",
                "FG3M",
                "FG3A",
                "FG3_PCT",
                "FTM",
                "FTA",
                "FT_PCT",
                "OREB",
                "DREB",
                "REB",
                "AST",
                "TOV",
                "STL",
                "BLK",
                "BLKA",
                "PF",
                "PFD",
                "PTS",
                "PLUS_MINUS",
                "NBA_FANTASY_PTS",
                "DD2",
                "TD3",
                "GP_RANK",
                "W_RANK",
                "L_RANK",
                "W_PCT_RANK",
                "MIN_RANK",
                "FGM_RANK",
                "FGA_RANK",
                "FG_PCT_RANK",
                "FG3M_RANK",
                "FG3A_RANK",
                "FG3_PCT_RANK",
                "FTM_RANK",
                "FTA_RANK",
                "FT_PCT_RANK",
                "OREB_RANK",
                "DREB_RANK",
                "REB_RANK",
                "AST_RANK",
                "TOV_RANK",
                "STL_RANK",
                "BLK_RANK",
                "BLKA_RANK",
                "PF_RANK",
                "PFD_RANK",
                "PTS_RANK",
                "PLUS_MINUS_RANK",
                "NBA_FANTASY_PTS_RANK",
                "DD2_RANK",
                "TD3_RANK",
                "CFID",
                "CFPARAMS"
            ]

    nba_df = pd.DataFrame(player_info, columns = columns_list)

    sorted_by_age = nba_df.sort_values(["AGE"], ascending=True)

    nba_df.head(20).to_excel("nba_age.xlsx")




    print(sorted_by_age.head(20))


if __name__ == "__main__":
    main()



