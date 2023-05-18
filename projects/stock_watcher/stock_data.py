from typing import List
from attr import define, field, validators


@define()
class DailyPriceData:
    currency: str = field(
        default=None,
        validator=validators.optional(validators.instance_of(str)),
    )
    daily_high: float = field(
        default=None,
        validator=validators.optional(validators.instance_of(float))
    )
    daily_low: float = field(
        default=None,
        validator=validators.optional(validators.instance_of(float))
    )
    current_price: float = field(
        default=None,
        validator=validators.optional(validators.instance_of(float)),
    )
    open_price: float = field(
        default=None,
        validator=validators.optional(validators.instance_of(float)),
    )
    previous_close_price: float = field(
        default=None,
        validator=validators.optional(validators.instance_of(float)),
    )

@define()
class NewsStory:
    title: str = field(validator=validators.instance_of(str)) # title
    published_timestamp: int = field(validator=validators.instance_of(int)) # providerPublishTime
    publisher: str = field(validator=validators.instance_of(str)) # publisher
    link: str = field(validator=validators.instance_of(str)) # link

@define()
class StockData:
    symbol = field(
        default="",
        validator=validators.instance_of(str),
    )
    long_name = field(
        default="",
        validator=validators.optional(validators.instance_of(str))
    )
    daily_price_data = field(
        default=DailyPriceData(),
        validator=validators.optional(validators.instance_of(DailyPriceData)),
    )
    news_stories: List[NewsStory] = field(
        default=[], validator=validators.instance_of(list)
    )
