from django import template

register = template.Library()

@register.filter
def get_profile_picture(user):
    # use this in development for static files
    blank_profile_picture = '../static/img/blank-profile-picture.png'


    if user.profile_photo:
        return user.profile_photo.url 
    else:
        user.profile_photo = blank_profile_picture
        user.save()
        get_profile_picture(user)


@register.filter
def get_cover_photo(user):
    # use this in development for static files
    blank_cover_photo = '../static/img/blank-cover-photo.jpg'

    if user.cover_photo:
        return user.cover_photo.url
    else:
        user.cover_photo = blank_cover_photo
        user.save()
        get_cover_photo(user)

