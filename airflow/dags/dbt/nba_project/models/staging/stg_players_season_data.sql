with source as (

    select *
    from {{ source('raw', 'PLAYERS_SEASON_DATA') }}

),

renamed as (

    select 
        PLAYERID                as player_id,
        PLAYERNAME              as player_name,
        POSITION                as position,
        TEAM                    as team,
        SEASON                  as season,
        ISPLAYOFF               as is_playoff,

       
        GAMES                   as games,
        GAMESSTARTED            as games_started,
        MINUTESPG               as minutes_per_game,

        FIELDGOALS              as field_goals,
        FIELDATTEMPTS           as field_attempts,
        FIELDPERCENT            as field_goal_pct,
        AGE                    as age,
        THREEFG                 as three_fg,
        THREEATTEMPTS           as three_attempts,
        THREEPERCENT            as three_point_pct,

        TWOFG                   as two_fg,
        TWOATTEMPTS             as two_attempts,
        TWOPERCENT              as two_point_pct,

        FT                      as free_throws,
        FTATTEMPTS              as free_throw_attempts,
        FTPERCENT               as free_throw_pct,
        EFFECTFGPERCENT         as effective_fg_pct,
        OFFENSIVERB             as offensive_rebounds,
        DEFENSIVERB             as defensive_rebounds,
        TOTALRB                 as total_rebounds,
        ASSISTS                 as assists,
        STEALS                  as steals,
        BLOCKS                  as blocks,
        TURNOVERS               as turnovers,
        PERSONALFOULS           as personal_fouls,
        POINTS                  as points

    from source

)

select *
from renamed