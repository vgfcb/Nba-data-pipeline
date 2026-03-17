select
    season,
    player_id,
    max(is_playoff) as is_playoff,
    sum(points) / sum(games) as avg_points,
    sum(assists) / sum(games) as avg_assists,
    sum(total_rebounds) / sum(games) as avg_rebounds
from {{ ref('stg_players_season_data') }}
group by
    season,
    player_id
