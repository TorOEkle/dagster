from dagster import asset, AssetIn, AssetOut, Output


@asset()
def asset_one(kinds={"python", "graphql"}):
    return 1

@asset(ins={"asset_one": AssetIn()})
def asset_two(asset_one):
    return asset_one + 1

@asset(ins={"asset_two": AssetIn()})
def asset_three(asset_two):
    return asset_two + 1

@asset(owners=["toro@cap.com", "team:data-eng"])
def asset_four():
    return 4

