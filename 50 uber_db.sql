-- =====================================
-- CREATE DATABASE
-- =====================================

CREATE DATABASE uber_db;
USE uber_db;

-- =====================================
-- RIDERS TABLE
-- =====================================

CREATE TABLE riders (
    rider_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    
    full_name VARCHAR(255) NOT NULL,
    
    age INT,
    
    phone VARCHAR(20) NOT NULL UNIQUE,
    
    email VARCHAR(255) NOT NULL UNIQUE,
    
    profile_image_url TEXT,
    
    is_active BOOLEAN DEFAULT TRUE,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- DRIVERS TABLE
-- =====================================

CREATE TABLE drivers (
    driver_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    
    full_name VARCHAR(255) NOT NULL,
    
    email VARCHAR(255) NOT NULL UNIQUE,
    
    phone VARCHAR(20) NOT NULL UNIQUE,
    
    license_number VARCHAR(100) NOT NULL UNIQUE,
    
    profile_image_url TEXT,
    
    rating DECIMAL(2,1) DEFAULT 5.0,
    
    total_rides INT DEFAULT 0,
    
    is_active BOOLEAN DEFAULT TRUE,
    
    is_online BOOLEAN DEFAULT FALSE,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- VEHICLES TABLE
-- =====================================

CREATE TABLE vehicles (
    vehicle_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    
    driver_id BIGINT NOT NULL,
    
    license_plate VARCHAR(20) NOT NULL UNIQUE,
    
    company VARCHAR(100) NOT NULL,
    
    model VARCHAR(100) NOT NULL,
    
    manufacture_year INT NOT NULL,
    
    color VARCHAR(50),
    
    vehicle_type VARCHAR(50) NOT NULL,
    
    seats INT NOT NULL,
    
    is_active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_vehicle_driver
        FOREIGN KEY (driver_id)
        REFERENCES drivers(driver_id)
        ON DELETE CASCADE
);

-- =====================================
-- DRIVER LOCATIONS TABLE
-- =====================================

CREATE TABLE driver_locations (
    driver_id BIGINT PRIMARY KEY,
    
    latitude DECIMAL(9,6) NOT NULL,
    
    longitude DECIMAL(9,6) NOT NULL,
    
    heading INT,
    
    speed_kmh DECIMAL(5,2),
    
    accuracy_meters INT,
    
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_driver_location
        FOREIGN KEY (driver_id)
        REFERENCES drivers(driver_id)
        ON DELETE CASCADE
);

-- =====================================
-- PRICING ZONES TABLE
-- =====================================

CREATE TABLE pricing_zones (
    zone_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    
    zone_name VARCHAR(255) NOT NULL,
    
    boundary_polygon TEXT,
    
    base_rate_per_km DECIMAL(10,2) NOT NULL,
    
    base_rate_per_minute DECIMAL(10,2) NOT NULL,
    
    minimum_fare DECIMAL(10,2) NOT NULL,
    
    is_active BOOLEAN DEFAULT TRUE
);

-- =====================================
-- SURGE PRICING TABLE
-- =====================================

CREATE TABLE surge_pricing (
    surge_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    
    zone_id BIGINT NOT NULL,
    
    multiplier DECIMAL(3,2) NOT NULL,
    
    start_time TIMESTAMP NOT NULL,
    
    end_time TIMESTAMP NOT NULL,

    CONSTRAINT fk_surge_zone
        FOREIGN KEY (zone_id)
        REFERENCES pricing_zones(zone_id)
        ON DELETE CASCADE
);

-- =====================================
-- RIDES TABLE
-- =====================================

CREATE TABLE rides (
    ride_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    
    rider_id BIGINT NOT NULL,
    
    driver_id BIGINT,
    
    vehicle_id BIGINT,
    
    zone_id BIGINT,
    
    pickup_latitude DECIMAL(9,6) NOT NULL,
    
    pickup_longitude DECIMAL(9,6) NOT NULL,
    
    pickup_address TEXT NOT NULL,
    
    destination_latitude DECIMAL(9,6) NOT NULL,
    
    destination_longitude DECIMAL(9,6) NOT NULL,
    
    destination_address TEXT NOT NULL,
    
    requested_vehicle_type VARCHAR(50),
    
    status VARCHAR(50) NOT NULL,
    
    estimated_fare DECIMAL(10,2),
    
    final_fare DECIMAL(10,2),
    
    distance_km DECIMAL(10,2),
    
    duration_minutes INT,
    
    requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    matched_at TIMESTAMP NULL,
    
    pickup_at TIMESTAMP NULL,
    
    completed_at TIMESTAMP NULL,
    
    canceled_at TIMESTAMP NULL,

    CONSTRAINT fk_ride_rider
        FOREIGN KEY (rider_id)
        REFERENCES riders(rider_id),

    CONSTRAINT fk_ride_driver
        FOREIGN KEY (driver_id)
        REFERENCES drivers(driver_id),

    CONSTRAINT fk_ride_vehicle
        FOREIGN KEY (vehicle_id)
        REFERENCES vehicles(vehicle_id),

    CONSTRAINT fk_ride_zone
        FOREIGN KEY (zone_id)
        REFERENCES pricing_zones(zone_id)
);

-- =====================================
-- PAYMENTS TABLE
-- =====================================

CREATE TABLE payments (
    payment_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    
    ride_id BIGINT NOT NULL,
    
    amount DECIMAL(10,2) NOT NULL,
    
    payment_method VARCHAR(50) NOT NULL,
    
    status VARCHAR(50) NOT NULL,
    
    gateway_transaction_id VARCHAR(255) UNIQUE,
    
    failure_reason TEXT,
    
    processed_at TIMESTAMP NULL,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_payment_ride
        FOREIGN KEY (ride_id)
        REFERENCES rides(ride_id)
        ON DELETE CASCADE
);

-- =====================================
-- RATINGS TABLE
-- =====================================

CREATE TABLE ratings (
    rating_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    
    ride_id BIGINT NOT NULL,
    
    rater_type VARCHAR(20) NOT NULL,
    
    rater_id BIGINT NOT NULL,
    
    ratee_type VARCHAR(20) NOT NULL,
    
    ratee_id BIGINT NOT NULL,
    
    stars INT NOT NULL,
    
    review TEXT,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_rating_ride
        FOREIGN KEY (ride_id)
        REFERENCES rides(ride_id)
        ON DELETE CASCADE
);

-- =====================================
-- INDEXES
-- =====================================

CREATE INDEX idx_rides_rider_id
ON rides(rider_id);

CREATE INDEX idx_rides_driver_id
ON rides(driver_id);

CREATE INDEX idx_rides_vehicle_id
ON rides(vehicle_id);

CREATE INDEX idx_rides_zone_id
ON rides(zone_id);

CREATE INDEX idx_rides_status
ON rides(status);

CREATE INDEX idx_driver_locations_updated_at
ON driver_locations(updated_at);

CREATE INDEX idx_payments_ride_id
ON payments(ride_id);

CREATE INDEX idx_surge_zone_id
ON surge_pricing(zone_id);