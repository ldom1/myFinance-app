#!/bin/bash
heroku run python3 manage.py cleanAssetsDB
heroku run python3 manage.py getAssetsInfos
heroku run python3 manage.py getOptimalAssets
heroku run python3 manage.py getAndCheckAssetsLimits

# python3 manage.py cleanAssetsDB
# python3 manage.py getAssetsInfos
# python3 manage.py getOptimalAssets
# python3 manage.py getAndCheckAssetsLimits