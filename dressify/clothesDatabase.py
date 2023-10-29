# from stream_sqlite import stream_sqlite
# import httpx

# # Iterable that yields the bytes of a sqlite file
# def sqlite_bytes():
#     with httpx.stream('GET', 'http://www.parlgov.org/static/stable/2020/parlgov-stable.db') as r:
#         yield from r.iter_bytes(chunk_size=65_536)

# # If there is a single table in the file, there will be exactly one iteration of the outer loop.
# # If there are multiple tables, each can appear multiple times.
# for table_name, pragma_table_info, rows in stream_sqlite(sqlite_bytes(), max_buffer_size=1_048_576):
#     for row in rows:
#         print(row)