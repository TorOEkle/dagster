from dagster import Definitions, load_assets_from_modules

from . import assets
from . import column_assets
playground_group = load_assets_from_modules([assets], group_name="Playground")
column_asset_group = load_assets_from_modules([column_assets], group_name="Column_Assets")
all_assets = playground_group + column_asset_group

defs = Definitions(
    assets=all_assets,
)
