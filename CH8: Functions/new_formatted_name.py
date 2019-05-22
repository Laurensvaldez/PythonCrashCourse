def get_formatted_name(first_name, last_name, middle_name= ''):
    """Return a full name, neatly formatted."""
    # if-statement in case the user provides a middle name
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    # if there's no middle name given, then 'else'
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)