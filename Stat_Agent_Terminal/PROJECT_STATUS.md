# NFL Stats Agent - Project Status

## 🎯 Project Goal

Build an agent that answers NFL stats questions using local LLM (Qwen3-4B via LM Studio)

## ✅ Completed

- [x] Set up basic agent structure (learned from weather agent)
- [x] Installed dependencies (openai, agents, nfl_data_py, polars)
- [x] Explored nfl_data_py - loads player stats as Polars DataFrames
- [x] Decided to use Polars directly (instead of converting to pandas)

## 📍 Where I Left Off

Working in `stat_agent.ipynb` - exploring NFL data structure

## 🔜 Next Steps

1. Write a simple function to query player stats
2. Format the stats into a readable string for agent
3. Wrap function with @function_tool decorator
4. Set up agent with local LM Studio model
5. Test basic query: "What are Patrick Mahomes' 2023 stats?"

## 📝 Notes

- nflreadpy returns Polars DataFrames (not pandas)
- Polars syntax: `df.filter(pl.col('column') == 'value')`
- LM Studio running at: http://localhost:1234/v1
- Model: qwen/qwen3-4b-2507

## 🤔 Questions to Explore Later

- How to handle player name variations (T.Brady vs Tom Brady)?
- Should I add multiple tools (player stats, team stats, comparisons)?
- How to format stats nicely for the LLM?
