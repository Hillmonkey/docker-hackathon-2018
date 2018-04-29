#! /bin/bash
docker container run -p 80:5000 --env TWILIO_ID --env TWILIO_SECRET --env TWILIO_FROM --env TWILIO_TO larry_sms:debstretch
