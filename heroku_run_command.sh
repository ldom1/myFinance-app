heroku run python manage.py migrate --app myfinance-appli
heroku run python manage.py FundsCAGLobalManagement --app myfinance-appli
heroku run python manage.py AssetsGlobalManagement --app myfinance-appli
heroku run python manage.py getAndCheckAssetsLimits --app myfinance-appli