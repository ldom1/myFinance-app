import numpy as np
from assets.models import Assets, AssetsInfo
from datetime import timedelta, datetime, date


def get_info_for_one_asset_for_one_date(asset, date_of_compute):
    a = asset.filter(date=date_of_compute)[0]
    value = a.value
    variation = a.variation
    dividende = a.dividende

    try:
        a_3_month = asset.filter(date=date_of_compute + timedelta(days=-90))[0]
        value_3_month = a_3_month.value
        var_3_month = round((value - value_3_month) / value_3_month * 100, 2)
    except Exception as e:
        print(e)
        value_3_month = None
        var_3_month = None

    try:
        a_1_month = asset.filter(date=date_of_compute + timedelta(days=-30))[0]
        value_1_month = a_1_month.value
        var_1_month = round((value - value_1_month) / value_1_month * 100, 2)
    except Exception as e:
        print(e)
        value_1_month = None
        var_1_month = None

    try:
        a_1_week = asset.filter(date=date_of_compute + timedelta(days=-7))[0]
        value_1_week = a_1_week.value
        var_1_week = round((value - value_1_week) / value_3_month * 100, 2)
    except Exception as e:
        print(e)
        value_1_week = None
        var_1_week = None

    date_over_3_months = [y.date for y in asset.filter(date__gte=date_of_compute + timedelta(days=-30))]
    value_over_3_months = [y.value for y in asset.filter(date__gte=date_of_compute + timedelta(days=-30))]

    return value, variation, dividende, value_3_month, var_3_month, value_1_month, var_1_month, value_1_week, var_1_week, value_over_3_months, date_over_3_months


def get_asset_info():
    today = datetime.today()
    date_today = date(today.year, today.month, today.day)

    assets = Assets.objects.all()

    for id_asset in np.unique([y.id_asset for y in assets]):

        asset = assets.filter(id_asset=id_asset)
        asset_info = AssetsInfo.objects.filter(id_asset=id_asset)

        (value, variation, dividende, value_3_month, var_3_month, value_1_month, var_1_month, value_1_week, var_1_week,
         value_over_3_months, date_over_3_months) = get_info_for_one_asset_for_one_date(asset, date_today)

        if asset_info.count() == 0:
            assetinfo, created = AssetsInfo.objects.get_or_create(
                date_update=date_today,
                id_asset=id_asset,
                name=asset[0].name,
                value=value,
                variation=variation,
                dividende=dividende,
                value_3_month=value_3_month,
                value_1_month=value_1_month,
                value_1_week=value_1_week,
                var_3_month=var_3_month,
                var_1_month=var_1_month,
                var_1_week=var_1_week,
                # date_over_3_months=date_over_3_months,
                # value_over_3_months=value_over_3_months
            )
        else:
            asset = asset[0]
            asset.value = value
            asset.variation = variation
            asset.dividende = dividende
            asset.value_3_month = value_3_month
            asset.value_1_month = value_1_month
            asset.value_1_week = value_1_week
            asset.var_3_month = var_3_month
            asset.var_1_month = var_1_month
            asset.var_1_week = var_1_week
            # asset.date_over_3_months = date_over_3_months
            # asset.value_over_3_months = value_over_3_months
            asset.save()
