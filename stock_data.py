from typing import List
from attr import define, field, validators


@define()
class DailyPriceData:
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
    daily_price_data = field(
        default=DailyPriceData(),
        validator=validators.optional(validators.instance_of(DailyPriceData)),
    )
    news_stories: List[NewsStory] = field(
        default=[], validator=validators.instance_of(list)
    )
