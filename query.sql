SELECT
    house_id,
    area_z,
    age_z,
    distance_center_z,
    quality_z,
    price_index

FROM
    housing_regression

WHERE
    price_index IS NOT NULL
    AND price_index > 0;