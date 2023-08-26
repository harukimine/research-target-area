import geopandas as gpd
from pathlib import Path


base_dir = "base_file/WatershedBoundary"


def main():
    files = Path().glob(f"{base_dir}/*/*.shp")
    for file in files:
        print(f"load {file}")
        df = gpd.read_file(file)
        df = transform_to_JGD2011(df)
        save_shp_to_geojson(df, filepath=file)


def transform_to_JGD2000(df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    return transform_coordinate_system(df, epsg=4612)


def transform_to_JGD2011(df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    return transform_coordinate_system(df, epsg=6668)


def transform_to_WGS84(df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    return transform_coordinate_system(df, epsg=4326)


def transform_to_TokyoGD(df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    return transform_coordinate_system(df, epsg=4301)


def transform_coordinate_system(df: gpd.GeoDataFrame, epsg: int) -> gpd.GeoDataFrame:
    """
    epsg (int) -> gpd.GeoDataFrame: EPSG (European Petroleum Survey Group) code
    """
    print("Coordinate system before: ", df.crs)
    if df.crs is None:
        df.crs = f"epsg:{epsg}"
    else:
        df = df.to_crs(epsg=epsg)
    print("Coordinate system After: ", df.crs)
    return df


def save_shp_to_geojson(df: gpd.GeoDataFrame, filepath: str) -> None:
    dest = filepath
    df.to_file(dest.with_suffix(".geojson"), driver="GeoJSON", encoding="utf-8")


if __name__ == "__main__":
    main()
