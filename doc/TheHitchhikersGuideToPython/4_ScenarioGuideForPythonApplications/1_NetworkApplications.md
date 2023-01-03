# [Network Applications](https://docs.python-guide.org/scenarios/client/)

## [HTTP](https://docs.python-guide.org/scenarios/client/)

Python’s standard urllib2 module is broken, don't use it.

The external requests library is what is usually used for this. In saying that, requests is synchronous.

[Collection of HTTP clients](https://www.scrapingbee.com/blog/best-python-http-clients/) with their attributes.

* [aiohttp](https://docs.aiohttp.org/en/stable/) is an external library
* [HTTPX](https://www.python-httpx.org/) is an external library (most promising)

### `async`/`await`:

**asyncio** (is a standard library)

* [Official doc](https://docs.python.org/3/library/asyncio.html)
* [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)

**asyncio** and **aiohttp**

[Asynchronous HTTP Requests in Python with aiohttp and asyncio](https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp)  
[Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)

## [Distributed Systems](https://docs.python-guide.org/scenarios/client/#distributed-systems)

### [ZeroMQ](https://docs.python-guide.org/scenarios/client/#zeromq)

### [RabbitMQ](https://docs.python-guide.org/scenarios/client/#rabbitmq)
