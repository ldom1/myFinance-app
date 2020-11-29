#!/bin/bash
heroku run python3 manage.py cleanAssetsDB
heroku run python3 manage.py getAssetsInfos
heroku run python3 manage.py getOptimalAssets
heroku run python3 manage.py getAndCheckAssetsLimits