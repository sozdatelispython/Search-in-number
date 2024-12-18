# OSearch

Hello, dear people, osearch is an osint tool for searching for any information

In the main menu we can see 4 items: Search by number, search by IP, search by passport and exit

The first item searches for information by number, it displays the country, mobile operator, and coordinates NOTE: COORDINATES POINT TO CITY CENTER

The second and third points are in development but I will try to do them as soon as possible

Well, I don’t think it’s worth explaining about the fourth point

Unfortunately, the program only supports Russian, but in the future I will try to add new languages

# Install in termux
~1.pkg update && pkg upgrade -y~
*2.pkg install python*
*3.pkg install python-pip*
*4.pkg install git*
*5.git clone https://github.com/sozdatelispython/Search-in-number*
*6.cd Search-in-number*
*7.pip install -r requirements.txt*
*8.python OSearch.py*