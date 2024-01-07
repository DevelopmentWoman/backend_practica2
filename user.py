import json
import math
class User():

    def __init__(self, user={}) -> None:
        self.user = user
        self.profile = {}
        # pass


    def fn_msg_except(self,msg):
        return {
            "payload": None,
            "error": msg
        }   
    
    def fn_open_file(self,path_file):
        with open(path_file,"r") as f:
            data_user = json.load(f)
        return data_user
    
    def fn_write_file(self,path_file, data_user, profile):
        with open(path_file, "w") as f_w:
            json.dump(data_user, f_w)

        return {
            "payload": profile,
            "status": 200,
            "error":{
                    "active": None,
                    "msg": None
            }}
    def set_profile(self):
        self.profile= {
            "name": self.user["name"].strip(),
            "email": self.user["email"].strip(),
            "age": self.user["age"],
            "role": self.user["role"].strip()
            }


    def get_profile(self):
        return self.profile




    def fn_create_user(self):

        if self.user:    
            file_json = "mock.json" 
            self.set_profile()  
            profile=self.get_profile()

            try:
                data_user = self.fn_open_file(file_json)
                if data_user:
                    for elem in data_user:       
                        if profile["email"] in elem["email"]: raise ValueError("User already exists")
                    data_user.append(profile)
                write_user = self.fn_write_file(file_json,data_user, profile)
                return write_user
                   
            except ValueError as e:
                return self.fn_msg_except(str(e))          

            except:
                return self.fn_msg_except("A error ocurred while trying to register the user")
 




    def fn_update_user(self):
        if self.user: 
            err = 1
            file_json = "mock.json"   
            self.set_profile()  
            profile=self.get_profile()
            try:
                data_user = self.fn_open_file(file_json)

                for elem in data_user:
                    if elem["email"]==profile["email"]:
                        elem["name"]=profile["name"]
                        elem["age"]=profile["age"]
                        elem["role"]=profile["role"]
                        err=0                               
                if err==1: raise ValueError("Email does not exist")
                write_user = self.fn_write_file(file_json,data_user, profile)
                return write_user
            
            except ValueError as e:
                return self.fn_msg_except(str(e))
                           
            except NameError as e:
                return self.fn_msg_except("A error ocurred while trying to update the user")

    def fn_delete_user(self,email):
        if email: 
            err = 1   
            file_json = "mock.json" 

            try:
                data_user = self.fn_open_file(file_json)
                if data_user:
                    for elem in data_user:       
                        if email in elem["email"]: 
                            data_user.remove(elem)
                            err=0
                    if err==1: raise ValueError("Invalid Email")
                write_user = self.fn_write_file(file_json,data_user, email)
                return write_user
                   
            except ValueError as e:
                return self.fn_msg_except(str(e))          

            except:
                return self.fn_msg_except("A error ocurred while trying to register the user")
 

    def fn_get_users(self):
        json_file = "mock.json"   
        data_user = self.fn_open_file(json_file)
        return(sorted(data_user,key= lambda user: user["age"]))
    

    def fn_pagination(self, page,count_show, lenght_list_user, data_user): 
        if int(page)<=0: page=1
        long_user= math.ceil(lenght_list_user/count_show)
        dic_page={}
        last_page=0
        i = 0
        j=0

        while i<long_user:
            tmp_list =[]
            for x in range(j,j+count_show,1):
                if x<lenght_list_user: 
                    tmp_list.append(data_user[x])
                j+=1
            dic_page.update({i: tmp_list})
            last_page=i
            i+=1

        if int(page)-1 >= long_user:
            dic_page_return = dic_page[last_page]
        else:
            dic_page_return = dic_page[int(page)-1]

        return(dic_page_return)

       



    def fn_get_mobile_user(self, page):
        i=0
        result_user = {}
        json_file = "mock.json"
        data_user = self.fn_open_file(json_file)
        dic_page = self.fn_pagination(page,2, len(data_user), data_user)
        for elem in dic_page:
            result_user.update({i:elem})
            i+=1
        return {
            "payload": result_user,
            "status": 200,
            "error":{
                    "active": None,
                    "msg": None
            }}
    
    def fn_get_desktop_user(self, page):
        i=0
        result_user = {}
        json_file = "mock.json"
        data_user = self.fn_open_file(json_file)
        dic_page = self.fn_pagination(page,4, len(data_user), data_user)
        for elem in dic_page:
            result_user.update({i:elem})
            i+=1
        return {
            "payload": result_user,
            "status": 200,
            "error":{
                    "active": None,
                    "msg": None
            }}



