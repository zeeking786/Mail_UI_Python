# Mail_UI_Python

So here I have created a GUI for sending mails with the help of basic Python and Tkinter

Just install one module for mailing process:
```pip install secure-smtplib```

I have separated the function so everyone can unserstand properly of each working process

There are two main function in this mail UI :
1. ```def layout():```
2. ```def mail():```

1. Function Layout is gonna handle the GUI part of Label , Entry , Text , Button and Menu Bar.

2. Next Function is mail function that gonna handle your main mailing part . It's also has some basic conditions in it like :

```
try:
    if send_email.get() == "" or send_pass.get() == "" or recv_email.get() == "":
        messagebox.showerror("Error", "Please enter the complete details.")
    else:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        a = send_email.get()
        b = send_pass.get()
        c = msg_body.get("1.0", END)
        d = recv_email.get()
        server.login(a, b)
        server.sendmail(a, d, c)
        server.close()
        msg_box()
except Exception as e:
    print(e)
    a = messagebox.askokcancel("Error", "Read instructions")
```

_Here, we can see that i have used try block under try i have if condition, this condition
check that sender mail,password and receiver mail is empty than it will show error message._

```server = smtplib.SMTP("smtp.gmail.com", 587)```
_Otherwise , It will execute else block which contain the instance of SMTP to encapsulate an SMTP connection. 
In this, you need to pass the first parameter of the server location and the second parameter of the port to use. 
For Gmail, we use port number 587._

```server.starttls()```
Using s.starttls for security reasons, now put the SMTP connection in the TLS mode. TLS (Transport Layer Security) encrypts 
all the SMTP commands. After that, for security and authentication, you need to pass your Gmail account credentials in the login instance. 

```
 a = send_email.get()
 b = send_pass.get()
 c = msg_body.get("1.0", END)
 d = recv_email.get()
```
After this i have created variable a,b,c and d which will work of getting the user input like sender email,sender password,message 
and receiver mail by using get method it will take all input .

```server.login(a, b)```
Now comes to login and i have passed parameter as a and b that is sender mail and password for login credentials

```server.sendmail(a, d, c)```
For sending mail we need a,d and c i.e.:sender mail,receiver mail and message .

```server.close()```
Time to close the server of gmail by using close method of it .

```msg_box()```
Now you will see that i have call another function named as msg_box() this will help us to know that mail have send successfully or not by showing popup message.

Exception block contain the error which will make you to read instructions And now it's over.

# Few Important Steps you need to do -

This steps you need to do for sending mail without interruption :

1. Go to Google Account click on "Manage your Google Account".

2. Now go to the left side you will see the "Security" click on it.

3. After the security page opens scroll down you will get "Less Secure App Access" click on it from OFF to ON.

This is needed so your Python script can access and your account and send emails from it.

At last, we have finished our E-mail sending concept with attachment and basic setups.

If you have any doubt or any setup issue you can refer my blog which is based on [Sending Mail](https://medium.com/zeeshaan786/send-attachment-mails-from-python-cd5e3934b317) 
and for more just contact to me on [Instagram](https://www.instagram.com/zeeshaansiddique/) , [Github](https://github.com/zeeking786) or [Medium](https://medium.com/zeeshaan786).

## Good luck 😘👍 and feel free for anything you want to tell or suggest me 😉!!!
