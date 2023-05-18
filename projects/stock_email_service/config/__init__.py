import yaml
import pathlib


path = pathlib.Path(__file__).parent / "config.yaml"
with path.open(mode="rb") as fp:
    stock_config = yaml.safe_load(fp)
