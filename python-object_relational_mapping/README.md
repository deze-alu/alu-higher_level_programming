# Python - Object-relational mapping

Talking to a MySQL database from Python, first with raw queries through
`MySQLdb` and then through the `SQLAlchemy` object-relational mapper.

## Raw queries with MySQLdb

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all the states of a database |
| `1-filter_states.py` | Lists the states whose name starts with an upper N |
| `2-my_filter_states.py` | Lists the states matching an argument |
| `3-my_safe_filter_states.py` | The same query, safe from SQL injection |
| `4-cities_by_state.py` | Lists the cities with the name of their state |
| `5-filter_cities.py` | Lists the cities of a given state |

## Object-relational mapping with SQLAlchemy

| File | Description |
|------|-------------|
| `model_state.py` | The State class linked to the states table |
| `model_city.py` | The City class linked to the cities table |
| `6-model_state.py` | Creates the states table |
| `7-model_state_fetch_all.py` | Lists all the states |
| `8-model_state_fetch_first.py` | Prints the first state |
| `9-model_state_filter_a.py` | Lists the states holding the letter a |
| `10-model_state_my_get.py` | Prints the id of a state given by name |
| `11-model_state_insert.py` | Adds the state Louisiana |
| `12-model_state_update_id_2.py` | Renames the state whose id is 2 |
| `13-model_state_delete_a.py` | Deletes the states holding the letter a |
| `14-model_city_fetch_by_state.py` | Lists the cities with the name of their state |
