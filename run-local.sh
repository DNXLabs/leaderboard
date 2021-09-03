#!/bin/bash
docker build --target main -t leaderboard .
docker run --env-file .env -v $(pwd):/app leaderboard