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
class News:
    text: str = field(
        default=None,
        validator=validators.optional(validators.instance_of(str)),
    )


@define()
class StockData:
    daily_price_data = field(
        default=DailyPriceData(),
        validator=validators.optional(validators.instance_of(DailyPriceData))
    )
    news = field(
        default=News(),
        validator=validators.optional(validators.instance_of(News))
    )