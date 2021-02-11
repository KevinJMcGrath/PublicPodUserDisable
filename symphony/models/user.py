import symphony.utility as util

class User:
    def __init__(self, user_json):
        self.type = user_json['userAttributes']['accountType']
        self.user_attributes = UserAttributes(user_json['userAttributes'])
        self.user_system_info = UserSystemInfo(user_json['userSystemInfo'])
        self.user_roles = user_json['roles']

        self.id = self.user_system_info.id
        self.firstname = self.user_attributes.firstName
        self.lastname = self.user_attributes.lastName
        self.email = self.user_attributes.emailAddress
        self.displayname = self.user_attributes.displayName
        self.domain = self.email.split('@')[1] if self.email and '@' in self.email else self.email

class UserAttributes:
    def __init__(self, user_attrib_json):
        self.emailAddress = user_attrib_json.get('emailAddress')
        self.firstName = user_attrib_json.get('firstName')
        self.lastName = user_attrib_json.get('lastName')
        self.userName = user_attrib_json.get('userName')
        self.displayName = user_attrib_json.get('displayName')
        self.companyName = user_attrib_json.get('companyName')
        self.department = user_attrib_json.get('department')
        self.division = user_attrib_json.get('division')
        self.title = user_attrib_json.get('title')
        self.twoFactorAuthPhone = user_attrib_json.get('twoFactorAuthPhone')
        self.workPhoneNumber = user_attrib_json.get('workPhoneNumber')
        self.mobilePhoneNumber = user_attrib_json.get('mobilePhoneNumber')
        self.accountType = user_attrib_json.get('accountType')
        self.location = user_attrib_json.get('location')
        self.jobFunction = user_attrib_json.get('jobFunction')
        self.assetClasses = user_attrib_json.get('assetClasses', [])
        self.industries = user_attrib_json.get('industries', [])
        self.marketCoverage = user_attrib_json.get('marketCoverage', [])
        self.responsibility = user_attrib_json.get('responsibility', [])
        self.function = user_attrib_json.get('function', [])
        self.instrument = user_attrib_json.get('instrument', [])

class UserSystemInfo:
    def __init__(self, user_sys_info_json):
        self.id = user_sys_info_json['id']
        self.status = user_sys_info_json.get('status', 'UNKOWN')
        self.createdDate = util.ms_to_datetime(user_sys_info_json.get('createdDate'))
        self.createdBy = user_sys_info_json.get('createdBy')
        self.lastUpdatedDate = util.ms_to_datetime(user_sys_info_json.get('lastUpdatedDate'))
        self.lastLoginDate = util.ms_to_datetime(user_sys_info_json.get('lastLoginDate'))
        self.deactivatedDate = util.ms_to_datetime(user_sys_info_json.get('deactivatedDate'))

