-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT *
FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28;
-- See all crimes committed on the given day and see crime report for this crime
    -- This crime was 10:15 am
SELECT *
FROM interviews
WHERE month = 7 AND year = 2021 AND day = 28;
-- Look at all the interviews from this day
    -- look for cars that left the parking lot ten +/- ten minutes of 10:15am
    -- Eugene recognized theif at emmas bakery walking by atm on leggett
    -- thief withdrew money on legett
    -- the thief made a -1:00 call
    -- theif is taking an early flight
    -- asked person on the phone to purchase phone tickets
SELECT account_number
FROM atm_transactions
WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';
-- Find all the accounts that made a withdraw on leggett on that day
SELECT name
FROM people
WHERE id IN (
    SELECT person_id FROM bank_accounts WHERE account_number IN (
        SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' and transaction_type = 'withdraw'));
-- Find out who made transactions on this day
    -- Kenny, Iman, Benista, Taylor, Brook, Luca, Diana, Bruce
SELECT name
FROM people
WHERE phone_number IN (
    SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);
-- Find all the people that made calls undera minute at that time
    -- the ones who also made a transaction were...
    -- Kenny - Doris, Benista, Taylor, Diana, Bruce
SELECT name
FROM people
WHERE phone_number IN (
    SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller IN (
            SELECT phone_number FROM people WHERE name IN (
                SELECT name FROM people WHERE id IN (
                    SELECT person_id FROM bank_accounts WHERE account_number IN (
                        SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' and transaction_type = 'withdraw')))));
-- Find all the recievers
    -- James Anna Philip Robin and Doris
SELECT name
FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = (
        SELECT phone_number FROM people where name = 'Kenny'
    ));
-- Kenny to Doris
SELECT name
FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = (
        SELECT phone_number FROM people where name = 'Benista'
    ));
-- Benista to Anna
SELECT name
FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = (
        SELECT phone_number FROM people where name = 'Taylor'
    ));
-- Taylor to James
SELECT name
FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = (
        SELECT phone_number FROM people where name = 'Diana'
    ));
-- Diana to Philip
-- Bruce to Robin
SELECT *
FROM flights
WHERE year = 2021 AND month = 7 AND day = 29;
-- Look at all flights the next day
    -- Earliest flight is at 8:20 (ID 36)
    -- ORIGIN: 8, DEST: 4
SELECT *
FROM airports
WHERE id = 4;
-- 4 is LaGuardia in NYC
SELECT name
FROM people
WHERE passport_number IN (
    SELECT passport_number FROM passengers WHERE flight_id = 36
);
-- Kenny and Dorris are on
-- Taylor is on (no james)
-- Bruce is on (no robin)
SELECT *
FROM bakery_security_logs
WHERE year = 2021 AND day = 28 AND month = 7 AND hour = 10 AND minute < 25 AND minute > 5 AND activity = 'exit';
-- Find everyone who left at the time given
SELECT name
FROM people
WHERE license_plate IN (
    SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND day = 28 AND month = 7 AND hour = 10 AND minute < 25 AND minute > 5 AND activity = 'exit'
);
-- Find the names of the people who left
    -- Bruce left

-- Bruce was at the ATM, on the phone, leaving the bakery, on the plane going to nyc

