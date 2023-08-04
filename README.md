# mean-season
Python program using Selenium and BeautifulSoup4 to generate the average of listed seasons of a TV Show from IMDb. It is a straightforward process to see the ratings of individual ratings of the season in metacritic, but most often they lack the ratings and show a blank image evem for decades old emmy winning TV shows. IMDb does not have this feature, atleast not in a easily discernible way. This programs scrapes and displays the average ratings of each season.

| IMDb data  | Metacritic data  |
| :------------: | :------------: |
|  ![](https://github.com/hariprasath112/mean-season/assets/96934076/03a0f578-b0df-4ff2-804e-04d41f3f20a0) | ![](https://github.com/hariprasath112/mean-season/assets/96934076/6bb92f6d-09a4-4c27-9e8e-6dcc67c79243)  |


Before you run the script install,

    pip install selenium
	pip install beautifulsoup4

Additionally, you also need to install a web driver for Selenium to access. You can install chrome driver from below link.

`https://chromedriver.chromium.org/downloads`

Note: Chrome driver must me added to PATH [or include the path in the code like this.](https://stackoverflow.com/questions/40555930/selenium-chromedriver-executable-needs-to-be-in-path)

Make sure you install the same release of chrome driver as your chrome web browser. You can check your version through the below link.

`chrome://version/`

If you wish to use other drivers (Edge for Microsoft Edge and Gecko for Firefox). Change `Chrome()` to your desired driver. For example, `Edge()` in Line 9 in the code.

            driver= webdriver.Chrome()


### Sample Output:
![](https://github.com/hariprasath112/mean-season/assets/96934076/ecfa4568-9cdd-4cfa-a893-9e641d299fe3)
### Sample Error Handling:
![](https://github.com/hariprasath112/mean-season/assets/96934076/04070a1b-426b-4f29-abe6-b1ea1fb56ec1)


### Releases
A executable file (.exe) for Windows operating system has been made using `pyintstaller` that lets you use the program without the hassles of installing libraries you're not familiar with. This also requires you to install a web driver. This will not function without a web driver. [Click here to download the release.](https://github.com/hariprasath112/mean-season/releases/tag/v1.0)
