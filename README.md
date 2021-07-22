# Bitly url shortener

The script allows you to reduce links using the [bit.ly](https://bitly.com/) service, as well as receive the number of clicks on the abbreviated link.

### How to install

To authorize, you must obtain a TOKEN, you can obtain it from this site [dev.bitly.com](https://dev.bitly.com/api-reference). Token must be saved to `.env` file

Add your token to the `.env` file just as shown in the example below
```
BITLY_API_KEY=your token
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Enter a long link to get a short

```
Input:
$ python3 main.py https://dvmn.org/modules/web-api/lesson/migration-from-website/
Output:
https://bit.ly/2VNYLdL
```
### Enter a short link to get the number of clicks on it

```
Input:
$ python3 main.py https://bit.ly/2VNYLdL
Output:
Number of clicks on the link: 10
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).