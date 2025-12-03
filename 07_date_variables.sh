#!/bin/bash
Date=$(date)
START_TIME=$(date +%s)
slee 20
END_TIME=$(date +%s)

TOTAL_TIME=$(($END_TIME-$START_TIME))

echo "Script excuted in: $TOTAL_TIME Seconds"