class guildInfo:
    def __init__(self):
        self.roles=[]
        self.guildObj=None
        self.moderatorRole=""
        self.flipRole=""
    def __repr__(self):
        returned = f"{self.guildObj.name}, {self.guildObj.id}, moderatorRole = {self.moderatorRole}, roleList = {self.roles}"
        return returned
    def roleList(self):
        return self.roles
    def flip(self):
        return self.flipRole
    def guild(self):
        return self.guildObj
    def modRole(self):
        return self.moderatorRole
    def addRoleList(self, role):
        self.roles.append(role)
    def removeRoleList(self, role):
        self.roles.remove(role)
    def setModRole(self, role):
        self.moderatorRole = role
    def setFlipRole(self, role):
        self.flipRole= role
    def setGuild(self, obj):
        self.guildObj = obj
    