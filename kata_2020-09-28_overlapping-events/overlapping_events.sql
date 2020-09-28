SELECT v.entry_time when_happened, COUNT(*) visits_count
FROM visits v
JOIN visits v2 ON
  (v.entry_time >= v2.entry_time AND
   v.entry_time < v2.exit_time)
GROUP BY v.id, v.entry_time
ORDER BY visits_count DESC, when_happened ASC
LIMIT 1
