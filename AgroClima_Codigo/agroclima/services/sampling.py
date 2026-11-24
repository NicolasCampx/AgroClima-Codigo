def sample_rows(rows, limit):
    limit = max(2, int(limit))
    if len(rows) <= limit:
        return rows

    return [rows[i * (len(rows) - 1) // (limit - 1)] for i in range(limit)]
