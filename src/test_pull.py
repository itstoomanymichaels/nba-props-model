from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players

# Find a player by name
def get_player_id(name):
    all_players = players.get_players()
    match = [p for p in all_players if p['full_name'].lower() == name.lower()]
    if not match:
        print(f"Player '{name}' not found.")
        return None
    return match[0]['id']

# Pull game logs for current eason
def get_game_logs(player_name, season='2024-25'):
    player_id = get_player_id(player_name)
    if not player_id:
        return None
    
    log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    df = log.get_data_frames()[0]
    return df

if __name__ == "__main__":
    df = get_game_logs("Trae Young")
    print(df.head())
    print(df.columns.tolist())