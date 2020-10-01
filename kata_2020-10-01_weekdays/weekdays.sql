CREATE FUNCTION weekdays(DATE, DATE) RETURNS INTEGER
    AS $$
    SELECT
      SUM(CASE
            WHEN (EXTRACT(DOW FROM dd) IN (0,6))
              THEN 0
            ELSE 1
        END)::INTEGER

    FROM generate_series(
          LEAST($1, $2)::date,
          GREATEST($1, $2)::date,
          '1 day'::interval) dd
    $$
    LANGUAGE SQL;
