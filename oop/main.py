
class Registration:

    @staticmethod
    def register_user(email, password, first_name, last_name):
        if ("@" in email) and (len(password) > 6):
            return Profile(first_name, last_name)


class FbModel:
    def __init__(self, profile_picture, cover_picture):
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture
    
    def get_profile_pictrue_url(self):
        return "wwww.fb.com/profile/"+self.profile_picture
    
    def get_cover_pictrue_url(self):
        return "wwww.fb.com/cover/"+self.cover_picture

class Profile(FbModel):
    
    def __init__(self,first_name, last_name, profile_picture=None, cover_picture=None):
        super().__init__(profile_picture, cover_picture)
        self.first_name = first_name
        self.last_name = last_name
    @property
    def get_full_name(self):
        return self.first_name+" - "+self.last_name

    def __str__(self):
        return self.first_name+" - "+self.last_name+" - "+self.get_profile_pictrue_url()+" - "+self.get_cover_pictrue_url()

class Page(FbModel):
    def __init__(self, name, profile_picture, cover_picture, followers=0):
        super().__init__(profile_picture, cover_picture)
        self.name = name
        self.followers = followers
    
    def get_info(self):
        return {
            'name':self.name,
            'followers':self.followers
        }

    def __add__(self,other):
        return self.name+" - "+other.name+" - "+" Total Followers: "+str(self.followers+other.followers)
    
    def __sub__(self,other):
        return self.name+" - "+other.name+" - "+" Total Followers: "+str(self.followers-other.followers)



#user1 = Profile(first_name="Arman", last_name="Avetisyan", profile_picture="arman.jpeg", cover_picture="arman_cover.jpeg")
#user1 = Profile(first_name="John", last_name="Smith", profile_picture="john.jpeg", cover_picture="smith.jpeg")

#codeTubesPage = Page("Code Tubes", 'code_tubes.jpeg','code_tubes_cover.jpeg',1500)
#ArmGovPage = Page("Arm Gov", 'armgov.jpeg','armgov_cover.jpeg',4500)

#print(ArmGovPage-codeTubesPage)

myProfile = Registration.register_user("arman@gmail.com", "Passwrod123!", "Arman", "Avetisyan")
print(myProfile.get_full_name)
#print(user1.get_full_name())
