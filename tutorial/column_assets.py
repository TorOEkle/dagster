from dagster import (
    AssetKey,
    MaterializeResult,
    TableColumnDep,
    TableColumnLineage,
    asset,
    MetadataValue,
)
import pandas as pd


@asset(kinds={"oracle"})
def source_bar():
    df = pd.DataFrame({
        "column_bar": [1, 2, 3],
        "other_column_bar": ["A", "B", "C"]
    })
    
    yield MaterializeResult(
        metadata={
            "dagster/column_lineage": TableColumnLineage(
                deps_by_column={
                    "column_bar": [
                        TableColumnDep(
                            asset_key=AssetKey("source_bar"),
                            column_name="column_bar",
                        ),
                    ],
                }
            ),
            "preview": MetadataValue.md(df.head().to_markdown()), 
        }
    )

@asset
def source_baz(kinds={"excel"}):
    df = pd.DataFrame({
        "column_baz": [4, 5, 6],
        "other_column_baz": ["D", "E", "F"]
    })
    
    yield MaterializeResult(
        metadata={
            "dagster/column_lineage": TableColumnLineage(
                deps_by_column={
                    "column_baz": [
                        TableColumnDep(
                            asset_key=AssetKey("source_baz"),
                            column_name="column_baz",
                        ),
                    ],
                }
            ),
            "preview": MetadataValue.md(df.head().to_markdown()),  
        }
    )

# Third asset: combined_asset
@asset(deps=[AssetKey("source_bar"), AssetKey("source_baz")])
def combined_asset():
    df_source_bar = pd.DataFrame({
        "column_bar": [1, 2, 3],
        "other_column_bar": ["A", "B", "C"]
    })
    df_source_baz = pd.DataFrame({
        "column_baz": [4, 5, 6],
        "other_column_baz": ["D", "E", "F"]
    })
    
    combined_df = pd.DataFrame({
        "combined_column": df_source_bar["column_bar"] + df_source_baz["column_baz"]
    })
    
    yield MaterializeResult(
        metadata={
            "dagster/column_lineage": TableColumnLineage(
                deps_by_column={
                    "combined_column": [
                        TableColumnDep(
                            asset_key=AssetKey("source_bar"),
                            column_name="column_bar",
                        ),
                        TableColumnDep(
                            asset_key=AssetKey("source_baz"),
                            column_name="column_baz",
                        ),
                    ],
                }
            ),
            "preview": MetadataValue.md(combined_df.head().to_markdown()),  
        }
    )
