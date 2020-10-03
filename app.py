import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
from time import time
from datetime import datetime
import time
import datetime

def getCurrentTimeStamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def isNonEmptyQuery(query):
    cur.execute(query)
    con.commit()
    if cur.rowcount == 0:
        return False
    return True

def viewTable(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return


def viewOptions():
    print("\nChoose the data that you want to see.\n\n")
    print("1.  USERS")
    print("2.  POST")
    print("3.  STORIES")
    print("4.  MESSAGES")
    print("5.  PROFILES")
    print("6.  EDUCATION OF USERS")
    #Pages
    print("7.  PAGES")
    print("8.  PAGES OF BUSINESS_PLACE")
    print("9. PRODUCTS OF BRANDS AND DETAILS")
    print("10. PAGES OF COMPANIES")
    print("11. BRANCHES OF COMPANIES")
    print("12. PAGES OF BRAND PRODUCTS")
    print("13. PAGES OF PUBLIC FIGURES")
    print("14. NEWS ABOUT PUBLIC FIGURES")
    print("15. PAGES OF ENTERTAINMENT INDUSTRY ENTITIES")
    print("16. PAGES OF CAUSE COMMUNITIES")
    #Groups
    print("17. GROUPS")
    #RelatioNships
    print("18. COMMENTS RELATIONSHIPS")
    print("19. FOLLOWS RELATIONSHIPS")
    print("20. GENERAL REACTS TO POSTS")
    print("21. LIKES TO PAGES")
    print("22. BELONGS TO GROUP RELATIONSHIP WITH USERS")
    print("23. ADMINS OF GROUPS")
    print("24. MODERATORS OF GROUPS")
    print("25. REACTS TO COMMENTS")
    print("26. MENTIONS OF USERS IN COMMENTS")
    print("27. SPECIFIC MESSAGES BETWEEN USERS - META DETAILS")
    print("28. GENERAL MESSAGES TO GROUPS - META DETAILS")
    print("29. RESPONDS TO STORIES")
    print("30. SHARES A POST IN A GROUP") # Basically posts in a group - comment to avoid semantical confusion
    print("31. USERS TAGGED IN POSTS")
    print("\n")
    choice = input("Enter: ")

    if choice == '1':
        query = "SELECT * FROM USER;"
    elif choice == '2':
        query = "SELECT * FROM POST;"
    elif choice == '3':
        query = "SELECT * FROM STORIES;"
    elif choice == '4':
        query = "SELECT * FROM MESSAGE;"
    elif choice == '5':
        query = "SELECT * FROM PROFILE;"
    elif choice == '6':
        query = "SELECT * FROM EDUCATION;"
    # Pages and subclasses
    elif choice == '7':
        query = "SELECT * FROM PAGE;"
    elif choice == '8':
        query = "SELECT * FROM BUSINESS_PLACE;"
    elif choice == '9':
        query = "SELECT * FROM PROD_BP;"
    elif choice == '10':
        query = "SELECT * FROM COMPANY;"
    elif choice == '11':
        query = "SELECT * FROM BRANCH_COMPANY;"
    elif choice == '12':
        query = "SELECT * FROM BRAND_PRODUCT;"
    elif choice == '13':
        query = "SELECT * FROM PUBLIC_FIGURE;"
    elif choice == '14':
        query = "SELECT * FROM NEWS_PUB_FIG;"
    elif choice == '15':
        query = "SELECT * FROM ENTERTAINMENT"
    elif choice == '16':    
        query = "SELECT * FROM CAUSE_COMMUNITY"
    # Pages over
    elif choice == '17':
        query = "SELECT * FROM social_media.GROUP"
    # Relationships
    elif choice == '18':
        query = "SELECT * FROM COMMENTS;"
    elif choice == '19':
        query = "SELECT * FROM FOLLOWS;"
    elif choice == '20':
        query = "SELECT * FROM MAKES_GENERAL_REACT;"
    elif choice == '21':
        query = "SELECT * FROM LIKES"
    elif choice == '22':
        query = "SELECT * FROM BELONGS_TO"
    elif choice == '23':
        query = "SELECT * FROM IS_ADMIN"
    elif choice == '24':
        query = "SELECT * FROM IS_MODERATOR"
    elif choice == '25':
        query = "SELECT * FROM MAKES_A_REACT;"
    elif choice == '26':
        query = "SELECT * FROM MENTIONS;"
    elif choice == '27':
        query = "SELECT * FROM SENDS_SPECIFIC;"
    elif choice == '28':
        query = "SELECT * FROM SENDS_GENERAL"
    elif choice == '29':
        query = "SELECT * FROM RESPONDS"
    elif choice == '30':
        query = "SELECT * FROM SHARES"
    elif choice == '31':
        query = "SELECT * FROM IS_TAGGED;"
    else:
        print("You have entered an invalid option.")

    try:
        no_of_rows = cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError!\n")
        return
    
    rows = cur.fetchall()
    viewTable(rows)
    con.commit()



def addUser():
    global cur
    user = {}
    print("Enter the details of the user:")

    user["name"] = input("Please provide name of the user:")
    user["email"] = input("Please provide the email id of the user:")
    user["password"] = input("Please provide the password:")
    user["address"] = input("Please provide the address:")
    user["phone"] = input("Please enter the phone number [without space or hyphen]")

    try:
        query = "INSERT INTO USER VALUES(NULL, '%s','%s','%s','%s',%s, '00:00:00')" %(user["password"],user["name"],user["email"],user["address"],user["phone"])   
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print(e)
        print("Invalid data! :( \n") 
   

def addProfile():
    print("Enter the profile details of the user:")
    profile = {}
    # try:
    #     query = "SELECT user_id FROM USER WHERE password='%s' AND name='%s' AND email='%s'" %(user['password'],user['name'],user['email'])
    #     cur.execute(query)
    #     profile["user_id"] = cur.fetchone()[0]
    # except Exception as e:
    #     cur.rollback()
    #     print(e)
    #     print("Something went wrong")
    profile['user_id'] = input("Enter user id of the user: ")
    profile['dob'] = input("Enter Date-of-Birth in YYYY-MM-DD format: ")
    profile['sex'] = input("Enter sex of the use [Male, Female, Others, PreferNotToSay]: ")

    try:
        query = "INSERT INTO PROFILE VALUES (%s,'%s','%s')" %(profile["user_id"],profile["dob"],profile["sex"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print(e)
        print("Invalid data! :( \n")

def addPost():
    global cur
    post = {}

    post['user_id'] = input("Enter the user ID:")
    # ts = time.time()
    post['time'] = getCurrentTimeStamp()
    post['text'] = input("Enter the post text:")
    post['media'] = input("Enter media associated with the post")
    
    try:
        query = "INSERT INTO POST VALUES (NULL, '%s', '%s', '%s', %s)" %(post["time"], post["text"], post["media"], post["user_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print(e)
        print("Invalid data! :( \n")


def addComment():
    global cur
    row = {}
    row["time"] = getCurrentTimeStamp()
    row["text"] = input("Enter the comment: ")
    row["media"] = input("Enter the link to the media: ")

    # Reminder: Do the following check in all valid places.
    if len(row["text"]) == 0 and len (row["media"]) == 0:
        print("You can't make an empty comment!")
        return

    try:
        query = "INSERT INTO COMMENT VALUES(NULL, '%s', '%s', '%s');" %(row["time"], row["text"], row["media"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print(e)
        print("Error: Check your inputs.")
    return


def addStory():
    global cur
    row = {}
    row["time"] = getCurrentTimeStamp()
    row["text"] = input("Enter what's shared in the story: ")
    row["media"] = input("Enter the link to media shared in the story: ")
    row["user_id"] = input("Enter the ID of the user who made this story: ")

    if len(row["text"]) == 0 and len (row["media"]) == 0:
        print("You can't make an empty story with no text and no media!")
        return

    try:
        query = "INSERT INTO STORIES VALUES(NULL, '%s', '%s', '%s', %s);" % (row["time"], row["text"], row["media"], row["user_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print(e)
        pritn("Error: Check you inputs.")
    return



# def isValidUserID(user_id):
#     cur.execute("SELECT user_id from USER where user_id=%s;" % (user_id))
#     con.commit()
#     if cur.rowcount == 0:
#         return False
#     return True

def addFollows():
    global cur

    row = {}
    row["follower_id"] = input("Enter user ID of the person that wants to follow someone: ")
    # if isValidUserID(row["follower_id"]) == False:
    #     print("Invalid user_id")
    #     return
    row["following_id"] = input("Enter the user ID of the person that will be followed by the former person: ")
    # if isValidUserID(row["follower_id"]) == False:
    #     print("Invalid user_id")
    #     return
    try:
        query = "INSERT INTO FOLLOWS(follower_id, following_id) VALUES(%s, %s);" % (row["follower_id"], row["following_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print("Error: This is not a valid query! \n")
        return
    return


def addMakesGeneralReact():
    global cur
    row = {}

    # try:
    row["post_id"] = input("Enter the POST ID: ")
    # except Exception as e:
    #     print("Invalid POST ID")
    # try:
    row["user_id"] = input("Enter your USER ID: ")
    # except Exception as e:
    #     print("Invalid USER ID")

    print("Choose the react type by pressing the corresponding number")
    print("1 . Like")
    print("2 . Dislike")
    print("3 . Wow")
    print("4 . Heart")
    print("5 . Angry")
    print("6 . Haha")
    reactNum = 123
    try:
        reactNum = int(input())
    except:
        print("Invalid react Type")

    if reactNum == 1:
        row["reactedType"]="Like"
    elif reactNum == 2:
        row["reactedType"]="Dislike"
    elif reactNum == 3:
        row["reactedType"]="Wow"
    elif reactNum == 4:
        row["reactedType"]="Heart"
    elif reactNum == 5:
        row["reactedType"]="Angry"
    elif reactNum == 6:
        row["reactedType"]="Haha"
    else :
        print("Invalid react Type")
        return
    try:
        query = "INSERT INTO MAKES_GENERAL_REACT(post_id, user_id, reacted_type) VALUES(%s, %s, '%s');" % (
            row["post_id"], row["user_id"],row["reactedType"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print("Error: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return

def addLikes():
    global cur
    row = {}
    # try:
    row["page_id"] = input("Enter the user ID: ")
    row["user_id"] = input("Enter the page ID of the page to like: ")
    # except Exception as e:
    #     print("Invalid USER ID")
    try:
        query = "INSERT INTO LIKES(page_id, user_id) VALUES(%s, %s);" % (
            row["page_id"], row["user_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print("Error: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return

def addUserToGroup():
    global cur
    row = {}
    row["user_id"] = input("Enter the ID of the user who wants to join a group: ")
    row["group_id"] = input("Enter the ID of the group that the user wants to join: ")
    try:
        query = "INSERT INTO BELONGS_TO VALUES(%s, %s);" % (row["user_id"], row["group_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print("Error: Check your inputs.")
        return
    return

def makeUserAdmin():
    global cur
    row = {}
    row["user_id"] = input("Enter the name of the user to make him an admin of a group: ")
    row["group_id"] = input("Enter the name of the group for which user should be made an admin of: ")
    # Don't we have to check if the user is a member of the group?
    query = "SELECT * FROM BELONGS_TO where group_id=%s and user_id=%s;" % (row["group_id"], row["user_id"])
    if isNonEmptyQuery(query) == False:
        print("User doesn't belong to the group")
        return
    try:
        query = "INSERT INTO IS_ADMIN VALUES(%s, %s);" (row["user_id"], row["group_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print("Error: Check your inputs.")
        return
    return

def makeUserModerator():
    global cur
    row = {}
    row["user_id"] = input("Enter the ID of the user to make him an moderator of a group: ")
    row["group_id"] = input("Enter the ID of the group for which user should be made an moderator of: ")
    # Don't we have to check if the user is a member of the group?
    query = "SELECT * FROM BELONGS_TO where group_id=%s and user_id=%s;" % (row["group_id"], row["user_id"])
    if isNonEmptyQuery(query) == False:
        print("User doesn't belong to the group")
        return
    try:
        query = "INSERT INTO IS_MODERATOR VALUES(%s, %s);" (row["user_id"], row["group_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print("Error: Check your inputs.")
        return
    return

def makeReactionToAComment():
    global cur
    row = {}
    row["user_id"] = input("Enter the ID of the user who made the reaction: ")
    row["comment_id"] = input("Enter the ID of the comment in which the reaction was made: ")
    print("Choose the react type by pressing the corresponding number")
    print("1 . Like")
    print("2 . Dislike")
    print("3 . Wow")
    print("4 . Heart")
    print("5 . Angry")
    print("6 . Haha")
    reactNum = 123
    try:
        reactNum = int(input())
    except:
        print("Invalid react Type")

    if reactNum == 1:
        row["reactedType"]="Like"
    elif reactNum == 2:
        row["reactedType"]="Dislike"
    elif reactNum == 3:
        row["reactedType"]="Wow"
    elif reactNum == 4:
        row["reactedType"]="Heart"
    elif reactNum == 5:
        row["reactedType"]="Angry"
    elif reactNum == 6:
        row["reactedType"]="Haha"
    else :
        print("Invalid react Type")
        return
    
    try:
        query = "INSERT INTO MAKES_A_REACT(comment_id, user_id, reacted_type) VALUES(%s, %s, '%s');" % (
            row["comment_id"], row["user_id"],row["reactedType"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print("Error: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return

def mentionInComment():
    global cur
    row = {}
    row["comment_id"] = input("Enter the ID of the comment: ")
    row["mentioner_id"] = input("Enter the ID of the user who mentioned someone: ")
    row["mentionee_id"] = input("Enter the ID of the user who got mentioned: ")
    try:
        query = "INSERT INTO MENTIONS VALUES(%s, %s, %s);" (row["mentioner_id"], row["mentionee_id"], row["comment_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        cur.rollback()
        print("Error: Check your inputs.")
        return
    return



def insertionOptions():
    print("Enter what you want to insert\n")







def refreshDatabase():
    global cur

    # Deleting incorrectly entered data in insert function
    # Have to write this function.
    print("Hello: Refreshing database") #Test printline.

while(1):
    tmp = sp.call('clear', shell=True)
    # The two lines below should be uncommented 
    # username = input("Username: ")
    # password = input("Password: ")

    username = 'root'
    password = 'blahblah'

    try:
        con = pymysql.connect(host='127.0.0.1',
                              user=username,
                              password=password,
                              db='social_media',
                              cursorclass=pymysql.cursors.DictCursor,
                              port=5005)
    except Exception as excep:
        print(excep)
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        continue

    # print("hi\n")
    # ts = time.time()
    # asdf = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # print("HI: %s\n" %(asdf))
    # input("hisd")
    # # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    with con.cursor() as cur:
        exitflag = 0
        while(1):
            tmp = sp.call('clear', shell=True)
            refreshDatabase()
            print("CHOOSE AN OPTION\n")
            print("1.View Options")
            print("2.Insertion Options")
            print("3.Deletion Options")
            print("4.Modify Options")
            print("5.Quit")
            inp = input("\nENTER: ")
            if(inp == '1'):
                # addUser()
                # addProfile()
                # addPost()
                # addFollows()

                # addMakesGe    neralReact()
                # addComment()
                addStory()
                # addLikes()
                viewOptions()
            elif(inp == '2'):
                insertionOptions()
            elif(inp == '5'):
                exitflag = 1
                print("Exiting.")
                break
            
            input("Press enter to continue: ")

    if exitflag == 1:
        break
