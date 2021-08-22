# CookieLandV2

Hi cookieland, This is my try to make my AAC, To automate the tasks of creating the accounts.

## ***How to Setup***
Make sure you have downloaded python  

1. Download the files go to your command promt and type these commands:  
`cd (yourfilepath)` press enter  
 `pip install -r requirements.txt` wait until it finishes  
 Close that command promt    
 
Now your gotta setup gmail    
### Setup your gmail for this.
1. Go to Gmail (https://mail.google.com/mail/u/#settings/fwdandpop)
2. Allow access to IMAP, Click save.
3. Go to https://myaccount.google.com/security
4. Allow access to "less secure apps"

    
## Using settings.txt


You'll see settings.txt  
-emailamazon=   
-emailgmail=   
-passwordgmail=   
-name=   
-phone=   
You gotta add your information in the (email) parts without any @gmail information ***Yes, you have to use gmail*** (Make sure you don't add any extra information to this file, Don't press enter at the end of it or something like that)

## Now that you have set it up, How to use it.
1. Open Sms receiver.py
2. Wait for the .ngrok link to show up
3. Copy the .ngrok link and paste it on twilio under "configure your number here:  
![Twilio](https://i.imgur.com/1iZIUzz.png)  
4. Click "Save" On twilio
5. **Now Run Main.py** And when it asks for gmail+? Put a gmail+ you haven't used, It will try to continue by adding 1 number each time it loops to that.

