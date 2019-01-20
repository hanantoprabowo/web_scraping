# Web Scraping
Demo project to do a web scraping

## About
This project is a demo, and uses beautifulsoup to do a web scraping.

## Prerequisite
* Clone this repository
  ```
  $ git clone https://github.com/hanantoprabowo/web_scraping.git
  ```
* Download and install [Anaconda](https://www.anaconda.com/download/)
* Start Anaconda Prompt
  * Install the required packages
    ```
    $ conda install -c anaconda beautifulsoup4
    ```

## Running
```
$ python weather_hannover.py
```

Example
```
$ python weather_hannover.py
So, 20.01. -- min: -6°, max: -1°
Mo, 21.01. -- min: -6°, max:  3°
Di, 22.01. -- min: -4°, max:  2°
Mi, 23.01. -- min: -5°, max:  1°
Do, 24.01. -- min: -4°, max:  0°
Fr, 25.01. -- min: -4°, max:  0°
Sa, 26.01. -- min: -2°, max:  2°
So, 27.01. -- min:  0°, max:  3°
```

## References
* [Weather Forecast Website](https://www.wetter.de/)
* [How to scrape websites with Python and BeautifulSoup](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe)