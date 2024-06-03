# Coder's Cafe 
This is a fullstack project written in Python using the Django framework on the backend, connecting to a PostgreSQL database. Using the bootstrap framework on the frontend within HTML and CSS.

## Plan 
I have detailed my planned features within User Stories, which can be found at: https://github.com/users/Nicolemann98/projects/1/views/1

## Important notes 
The staff user that can view all of the bookings on the booking screen is as follows, username: `staff.member` & password is: `Password11*`.

In order to test the functions of the bookings page and all its features, new users can be created in the account page.

## Testing
Initally I tested to ensure that the homepage would be responsive over desktop, tablet and mobile screens
Responsive home screen on mobile:

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/384ffaa3-721a-4104-b30e-7fe7d9bfc96c)

Responsive homescreen on tablet: 

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/bcc60b0f-dcb3-4cd0-b1b5-34c85b6a1c77)

This is the booking screen from the staff member's perspective:

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/cab76240-db4b-4a14-8019-cc8108eda2d5)

This is the account page: 

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/a29c9a00-804c-4b65-8172-b6840cb4f2b6)

This is the menu page:

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/3dcfaa3c-8e05-496e-ab07-3860b32ff5fe)

Upon clicking the download button on the menu page, users will have the option to download a pdf version of the menu

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/e3207977-0aaf-4725-85a3-09f84d018f52)


Now we will start testing the booking functionality. Logging in as JohnDoe, we can see that he has no bookings

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/e3516df0-a2b6-414a-b930-d041a36044d4)

We will click create booking and fill in the form

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/9f99628c-3fec-47e7-a5ca-3a7a5e0bcd8d)

Upon clicking submit, we can see that this booking has been added, along with a confirmation message

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/edf28df4-73ff-464b-a768-675c900f1f03)

The cafe has a total of 20 seats, now we will try to create the following booking that will exceed the cafe's capacity

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/b4a9ac5e-c28a-4b5e-8db9-f298f7f75601)

Clicking submit, we are given an error message telling us there aren't enough seats

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/1028da96-0159-4123-98bc-2e5a8c1d2234)

And the booking has not been saved

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/e182766f-0318-4a7d-b215-9ae3076b4b1d)

Similarly if we try to create a booking in the past

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/7c17e097-be30-4282-8187-ff10fdca3239)

Finally if we click delete on the booking, we get a warning message

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/0ee45471-a26f-4459-8661-87aedd60b8ff)

And we see that if we click delete on the pop-up to confirm, the booking is deleted

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/700a419a-b00a-474c-afa8-174bda604db8)



## Bugs 

There was a bug, that when editing a booking, the validation for number of seats failed because the validator got all the bookings with the same start time,
summed their number of seats and added the number of seats of the new booking, however this failed because if you didn't change the start time of the booking you are editing,
then that booking got counted twice. I fixed this by adding a filter to the bookings we received to not include the previous booking which was amended.

### Python Validator

The code passes the Code Institure Linter Python Validation with zero errors.

forms.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/8fb0594c-a0d1-4ed4-95f4-121383d3775c)

models.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/0757cb68-5fe3-400e-8a9e-6b4e90f12d53)

test_forms.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/b216e4c2-e08b-4757-bb32-63aee0f5f6dc)

test_views.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/b5ca207b-34be-4e66-9a07-b5ab58365489)

urls.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/e934a848-1d71-46ca-9327-13b3b2286a55)

views.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/f7c2bc0f-6a94-4c9b-9492-910c34e23b3c)


### HTML W3C Validator

Index Page

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/5e189f2a-8c12-40aa-a08b-0987f0def4e0)

Menu Page

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/7782b4f2-7a30-4554-91eb-8926ab2f3dcc)

Account Page

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/45fd9387-1328-4183-96a3-5bf979b60b97)

Bookings Page

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/17d11e11-6abc-4658-adde-b318d5a702e8)


## Deployment 

This project was deployed onto Heroku, the link for which is: https://nicole-full-stack-project-7589e5b487d3.herokuapp.com/

## Credits 

- Code institute course materials
- Django documentation: https://docs.djangoproject.com/en/5.0/
- Font Awesome for icons
- Favicon created from https://favicon.io/favicon-converter/
- Photos used on main page are from:
    https://blog.hyperiondev.com/index.php/2018/08/06/what-kind-of-companies-do-coders-work-for/  (coder's photo)
    https://www.chinadaily.com.cn/bizchina/tech/2016-03/09/content_23789709.htm (mock cafe photo)
- Photo of scone on menu page from Pexels

## Struggles

This project was very challenging in a number of ways, not only as it was my first ever fullstack project, but also because there was
a large number of new materials to also learn in addition to changing my existing skills to adapt to the additon of Bootstrap and Django.

There were a numnber of issues with deployment which needed to be amended to fix the functionality of the bookings and account pages, and also a number of differences in the styling upon deployment.

I received terminal errors when trying to run unit tests, regarding not being able to connect to the database, after searching online forums for help, I found that adding the following line under the databases section of the setttings.py file 

```del DATABASES['default']['OPTIONS']['sslmode']```








