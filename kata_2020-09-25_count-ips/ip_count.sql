WITH prepared_ip_adresses AS (
  SELECT
    id,
    (SELECT regexp_matches(first, '([0-9]*).([0-9]*).([0-9]*).([0-9]*)')) AS first,
    (SELECT regexp_matches(last, '([0-9]*).([0-9]*).([0-9]*).([0-9]*)')) AS last
  FROM ip_addresses
)


SELECT id,
      (last[1]::BIGINT - first[1]::BIGINT) * 256 * 256 * 256 +
      (last[2]::BIGINT - first[2]::BIGINT) * 256 * 256 +
      (last[3]::BIGINT - first[3]::BIGINT) * 256 +
      (last[4]::BIGINT - first[4]::BIGINT) AS ips_between
FROM prepared_ip_adresses;
