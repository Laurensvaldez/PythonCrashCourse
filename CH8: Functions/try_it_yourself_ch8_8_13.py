# Start with a copy of user_profile from page 153. Build a profile of yourself by calling build_profile, using your
# first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
        return profile


user_profile = build_profile('laurens', 'salcedo valdez',
                             favorite_sport='baseball',
                             birth_place='rotterdam',
                             favorite_vacation_spot='norway')

print(user_profile)