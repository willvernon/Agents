# %%
!uv add nlfreadpy pandas

# %%

import asyncio
import pandas as pd 

from agents import Agent, Runner, function_tool
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI

import nflreadpy as nfl


# %%
#### Setup
player_stats = nfl.load_player_stats([2022, 2023])
player_stats = player_stats.to_pandas()
player_stats.head()

# %%
player_stats[player_stats['player_name'] == 'T.Brady']

# %%
