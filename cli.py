import click
import json
import pymysql
import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api
import pytest
#Config
try:
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="cv4u")
    mycr=conn.cursor()
    cloudinary.config(cloud_name="dy9so7yhs", api_key="543617755226786", api_secret="pawptsoBASgr1jWvD0lhZAvOZhU",
                      CLOUDINARY_URL="cloudinary://543617755226786:pawptsoBASgr1jWvD0lhZAvOZhU@dy9so7yhs")
except Exception:
    print("Cannot connect to Mysql//Cloudinary")
@click.group(chain=True)
def cli():
    pass
@cli.command('login')
@click.option('--username')
@click.option('--password')
def login(username,password):
    userold=username
    username=addslashes(username)
    try:
        mycr.execute("SELECT passwordval from users where username="+username)
        data=mycr.fetchall()
        data=str(data[0][0])
        if(data==password):
            print(userold+" Has logged successfully into the system!")
            tokenuser(userold)
            return True
        else:
            print("Wrong Password\\Username details!")
            return False
    except Exception:
        print("Wrong Password\\Username details!")
        return False
@cli.command('register')
@click.option('--username')
@click.option('--password')
@click.option('--email')
@click.option('--acctype')
def register(username,password,email,acctype):
    userold=username
    username = addslashes(username)
    try:
        tk=0
        mycr.execute("SELECT username from users where username=" + username)
        data = mycr.fetchall()
        data = str(data[0][0])
        if(data==userold):
            print("Username Already taken")
            tk=0
            return False
        else:
            tk=1
    except Exception:
        tk=1
    if(tk==1):
        acctype=int(acctype)
        password=addslashes(password)
        email=addslashes(email)
        try:
            s="""INSERT INTO users(`ID`, `username`, `passwordval`, `typeid`,`email`) VALUES (NULL ,%s,%s,%s,%s)"""%(username,password,acctype,email)
            sp=mycr.execute(s)
            conn.commit()
            if sp==1:
                print("Register Successfully!")
                conn.close()
                return True
            else:
                print("Register occur a problem")
        except Exception:
            print("Register occur a problem")
    else:
        return False
    return False
@cli.command('filter')
def filter():
    username=addslashes(tokenread())
    try:
        mycr.execute("SELECT typeid from users where username="+username)
        data=mycr.fetchall()
        data = str(data[0][0])
        if(data=="1"):
            readr="""SELECT * FROM `cvinfo`"""
            sp=mycr.execute(readr)
            dicti=mycr.fetchall()
            for i in dicti:
                print(i)
        else:
            print("Account type not suiteable for Filter!")
    except Exception as e:
        print(e)
@cli.command('add')
@click.option('--path')
def upload(path):
    username=addslashes(tokenread())#Username
    nowdate=datetime.datetime.now()
    currdate=addslashes(str(nowdate.year)+"-"+str(nowdate.month)+"-"+str(nowdate.day))
    with open(path) as fd:
        json_data = json.load(fd)
    #In the future add the opprituntiy to read in loop and add columns to the sql
    personal=addslashes(json_data['basics']['summary'])
    edu=addslashes(json_data['education']['edu'])
    skills=addslashes(json_data['skills']['desc'])
    carrhist=addslashes(json_data['history']['desc'])
    ref=addslashes(json_data['references']['reference'])
    image=addslashes(json_data['basics']['image'])
    img =json_data['basics']['image']
    s="""INSERT INTO `cvinfo` (`ID`, `username`, `datecol`, `personals`, `academich`, `skills`, `carrerhistory`, `refe` , `image`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s) """%(username,currdate,personal,edu,skills,carrhist,ref,image)
    sp=mycr.execute(s)
    conn.commit()
    cloudinary.uploader.upload(img,public_id=img)
    if sp==1:
        print("CV Uploaded Successfully!")
        conn.close()
        return True
    else:
        print("CV Uploading occur a problem")
        return False
def addslashes(name):
    return ("\'"+name+"\'")
def tokenuser(user):
    filet=None
    try:
        filet=open("token.dat","w")
        filet.write(user)
    except Exception:
        print("Cannot write token")
    finally:
        if filet:
            filet.close()
def tokenread():
    username=None
    try:
        filet=open("token.dat","r")
        username=filet.read()
        filet.close()
    except Exception:
        print("You are not logged in\\Token not found")
    return username
if __name__ == '__main__':
    cli()


