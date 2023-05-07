import logging
from typing import List
from concurrent.futures import ThreadPoolExecutor

from confluent_kafka import Producer

from stock_builder import StockBuilder, Stock
from stock_utils import on_schedule
from config import stock_config


@on_schedule
def publish_stocks():
    stocks: List[Stock] = []
    with ThreadPoolExecutor(max_workers=16) as executor:
        for result in executor.map(build_stock, stock_config["tickers"]["list"]):
            stocks.append(result)
            produce_stock_to_stream(result)


def build_stock(stock):
    built = StockBuilder(stock)
    built.collate_daily_price_data()
    built.collate_news_data()
    return built.stock


def on_delivery(err, msg):
    if err:
            logging.error('ERROR: Message failed delivery: {}'.format(err))
    else:
        logging.info("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))


def produce_stock_to_stream(stock: Stock):
    kafka_config = stock_config["kafka"]
    producer = Producer(kafka_config)

    producer.produce(
        topic=stock_config["topics"]["stock_producer_topic"],
        value=str(stock.daily_price_data.current_price),
        key=stock.ticker,
        on_delivery=on_delivery,
    )
    producer.flush()


def main():
    logging.info("Stock Watcher Started!")
    publish_stocks()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="[%(asctime)s] %(levelname)s - %(message)s"
    )
    main()


# TO SEE STUFF
# logging.info(f"*** Info for {built_stock.ticker}! ***")
# logging.info("Daily Price Data:")
# pprint(built_stock.daily_price_data)
# pcnt = percentage_change(built_stock.daily_price_data.current_price, built_stock.daily_price_data.open_price)
# logging.info(f"PERCENTAGE CHANGE: {pcnt:.2f}%")
# logging.info("-----------------")
# logging.info("Stories:")
# for story in built_stock.news:
#    logging.info(story.title)
#    logging.info(story.publisher)
#    logging.info(datetime.fromtimestamp(story.published_timestamp))
#    logging.info(story.link)
#    logging.info("-----------------")
# logging.info("")
# logging.info("")
