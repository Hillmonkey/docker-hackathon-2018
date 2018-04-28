#! /bin/bash
docker container run --env TWILIO_ID --env TWILIO_SECRET \
	--env TWILIO_FROM --env TWILIO_TO larry_sms
