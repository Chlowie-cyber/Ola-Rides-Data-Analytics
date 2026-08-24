USE ola_bookings;

-- Metric 1: Overall Trip Summary & Completion Rate
SELECT
	COUNT(*) AS total_bookings,
    SUM(CASE WHEN Booking_Status = 'Success' THEN 1 ELSE 0 END) AS successful_trips,
    ROUND (SUM(CASE WHEN Booking_Status = 'Success' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS completion_rate_pct
FROM ola_ride_data;

-- Metric 2: Top Pickup Locations by Demand
SELECT
	Pickup_Location,
    COUNT(*) AS total_trips
FROM ola_ride_data
GROUP BY Pickup_Location
ORDER BY total_trips DESC
LIMIT 10;

-- Metric 3: Macro Cancellation Breakdown
SELECT
	Booking_Status,
    COUNT(*) AS total_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ola_ride_data), 2) AS pct_of_total
FROM ola_ride_data
WHERE Booking_Status LIKE '%Canceled%' OR Booking_Status LIKE '%Cancelled'
GROUP BY Booking_Status;

-- Metric 4: Revenue & Fare Analysis by Vehicle Type
SELECT
	Vehicle_Type,
    COUNT(*) AS total_rides,
    ROUND(SUM(CAST(Booking_Value AS DECIMAL(10,2))), 2) AS total_revenue_zar,
    ROUND(AVG(CAST(Booking_Value AS DECIMAL(10,2))), 2) AS avg_fare_zar
FROM ola_ride_data
WHERE Booking_status= 'Success'
GROUP BY Vehicle_Type
ORDER BY total_revenue_zar DESC;

-- Metric 5: Top Reasons for Driver Cancellations
SELECT
    Canceled_Rides_by_Driver AS cancellation_reason,
    COUNT(*) AS cancellation_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS pct_share
FROM ola_ride_data
WHERE Canceled_Rides_by_Driver IS NOT NULL
AND Canceled_Rides_by_Driver != 'N/A'
GROUP BY Canceled_Rides_by_Driver
ORDER BY cancellation_count DESC;

-- Metric 6: Customer &  Driver Rating Distribution
SELECT
    ROUND(AVG(Customer_Rating), 2) AS avg_customer_rating,
    ROUND(AVG(Driver_Ratings), 2) AS avg_driver_rating
FROM ola_ride_data
WHERE Booking_Status = 'Success';