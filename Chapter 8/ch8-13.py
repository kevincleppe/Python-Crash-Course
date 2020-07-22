def build_profile(first, last, **user_info):
    user_info['first_name']= first
    user_info['last_name'] = last
    return user_info



user= build_profile('keervin', 'cleepr', location= 'hign')

print(user)