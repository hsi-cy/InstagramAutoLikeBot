# this file used for running the program. just key "python3 run.py" in the terminal
# (in this directory)
from instagramBot import InstagramBot
h_list = ['arts','picoftheday','photography','russia','moneyheist','pictureofinstagram','forest']
# set a list of hashtags
insta = InstagramBot('xxxx', 'xxxx')
# create a bot object with your account
insta.login()
sleep(5)

for hashtag in h_list:
    try:
        start = timeit.default_timer()
        insta.likePhotos(hashtag,100)
        stop = timeit.default_timer()
        print('Time: ', stop - start)  
        print(hashtag)
    except Exception as e:
        print(e)
        print("You got actioin block by Instagram!")
