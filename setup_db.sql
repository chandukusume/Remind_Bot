-- Create database for Remind Bot
CREATE DATABASE remindbot;

-- Connect to the new database and create tables
\c remindbot;

-- Table to store bot configuration
CREATE TABLE bot_config (
    id SERIAL PRIMARY KEY,
    master_sheet_id VARCHAR(255),
    active_sheet_id VARCHAR(255),
    schedule_time VARCHAR(100),
    reminders_active BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store reminder logs
CREATE TABLE reminder_logs (
    id SERIAL PRIMARY KEY,
    sheet_id VARCHAR(255),
    recipient_group VARCHAR(50),
    message_sent TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store submission counts
CREATE TABLE submission_counts (
    id SERIAL PRIMARY KEY,
    sheet_id VARCHAR(255),
    count INTEGER,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial config row
INSERT INTO bot_config (master_sheet_id, active_sheet_id, reminders_active) 
VALUES (NULL, NULL, false);