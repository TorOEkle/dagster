from dagster import asset, AssetIn, AssetOut, Output


@asset(kinds={"python", "graphql"})
def asset_one():
    return 1

@asset(ins={"asset_one": AssetIn()},
       kinds={"duckdb"})
def asset_two(asset_one):
    return asset_one + 1

@asset(ins={"asset_two": AssetIn()})
def asset_three(asset_two):
    return asset_two + 1

@asset(owners=["toro@cap.com", "team:data-eng"])
def asset_four():
    return 4

